from unittest.mock import patch
from app import app
import unittest


class TestKvitkaAPI(unittest.TestCase):

    def setUp(self):
        """
        Sets up the test client for the Flask app.
        """
        self.app = app.test_client()
        self.app.testing = True

    @patch('app.openai.Completion.create')
    def test_chat_endpoint_with_fine_tuned_model(self, mock_openai):
        """
        Test the /api/chat endpoint with a fine-tuned OpenAI model.
        """
        # Mocking the OpenAI API response
        mock_openai.return_value = {
            "choices": [{"message": {"content": "Fine-tuned response"}}]
        }

        # Sending a POST request to the endpoint
        response = self.app.post('/api/chat', json={'query': 'Hello!'})

        # Validating the response
        self.assertEqual(response.status_code, 200)
        self.assertIn('Fine-tuned response', response.get_json()['response'])

    def test_chat_endpoint_no_query(self):
        """
        Test the /api/chat endpoint when no query is provided.
        """
        # Sending a POST request without a query
        response = self.app.post('/api/chat', json={})

        # Validating the response
        self.assertEqual(response.status_code, 400)
        self.assertIn('Query is required', response.get_json()['error'])

    @patch('app.openai.Completion.create')
    def test_chat_endpoint_openai_error(self, mock_openai):
        """
        Test the /api/chat endpoint when the OpenAI API raises an error.
        """
        # Mocking an OpenAI API exception
        mock_openai.side_effect = Exception("OpenAI API error")

        # Sending a POST request
        response = self.app.post('/api/chat', json={'query': 'Hello!'})

        # Validating the response
        self.assertEqual(response.status_code, 500)
        self.assertIn('OpenAI API error', response.get_json()['error'])


if __name__ == '__main__':
    unittest.main()
