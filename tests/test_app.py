import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from app import app


class TestKvitkaBackend(unittest.TestCase):

    def setUp(self):
        """
        Sets up the test client for the Flask app.
        """
        self.app = app.test_client()
        self.app.testing = True

    @patch('app.openai.ChatCompletion.create')
    def test_chat_endpoint_with_valid_query(self, mock_openai):
        """
        Test the /api/chat endpoint with a valid query.
        """
        # Mocking OpenAI API response
        mock_openai.return_value = {
            "choices": [{"message": {"content": "Mocked chatbot response"}}]
        }

        # Sending a POST request to the endpoint
        response = self.app.post('/api/chat', json={'query': 'Hello!'})

        # Validating the response
        self.assertEqual(response.status_code, 200)
        self.assertIn('Mocked chatbot response', response.get_json()['response'])

    def test_chat_endpoint_without_query(self):
        """
        Test the /api/chat endpoint when no query is provided.
        """
        response = self.app.post('/api/chat', json={})
        self.assertEqual(response.status_code, 400)
        self.assertIn('Query is required', response.get_json()['error'])

    @patch('app.openai.ChatCompletion.create')
    def test_chat_endpoint_with_openai_error(self, mock_openai):
        """
        Test the /api/chat endpoint when OpenAI API raises an error.
        """
        mock_openai.side_effect = Exception("OpenAI API error")
        response = self.app.post('/api/chat', json={'query': 'Hello!'})
        self.assertEqual(response.status_code, 500)
        self.assertIn('OpenAI API error', response.get_json()['error'])

if __name__ == '__main__':
    unittest.main()
