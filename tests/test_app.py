from unittest.mock import patch
import unittest
from app import app

@patch('app.client', autospec=True)
class TestKvitkaBackend(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_chat_endpoint(self, mock_client):
        mock_client.chat.completions.create.return_value = {
            "choices": [{"message": {"content": "Mock response"}}]
        }
        response = self.app.post('/api/chat', json={"query": "Hello!"})
        self.assertEqual(response.status_code, 200)
        self.assertIn("Mock response", response.get_json()['response'])
