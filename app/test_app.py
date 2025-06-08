import unittest
from app import app

class BasicTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_status(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

    def test_home_content(self):
        result = self.app.get('/')
        self.assertIn(b'Shivansh', result.data)

    def test_sample(self):
        self.assertEqual(2 + 2, 4)

if __name__ == "__main__":
    unittest.main()
