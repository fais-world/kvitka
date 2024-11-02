import functions_framework
from google.auth import default
from googleapiclient.discovery import build


# HTTP-triggered function
@functions_framework.http
def list_files(request):

    # Use default credentials with Workload Identity Federation (WIF)
    def get_drive_service():
        credentials, _ = default(scopes=["https://www.googleapis.com/auth/drive"])
        service = build('drive', 'v3', credentials=credentials)
        return service

    # Retrieve the Drive ID from the request
    drive_id = request.json.get('driveId') if request.json else None
    if not drive_id:
        return {"error": "Missing 'driveId' parameter in request."}, 400

    try:
        service = get_drive_service()
        # List files in the specified Shared Drive
        results = service.files().list(
            driveId=drive_id,
            includeItemsFromAllDrives=True,
            supportsAllDrives=True,
            corpora='drive'
        ).execute()

        files = results.get('files', [])
        file_list = [f"Name: {file['name']}, ID: {file['id']}" for file in files]

        return {"status": "success", "files": file_list}, 200
    except Exception as e:
        return {"status": "error", "message": str(e)}, 500
