import unittest
from src.subproject.app import app

class TestSubproject(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Welcome to the Kvitka Subproject", response.data)

if __name__ == '__main__':
    unittest.main()
