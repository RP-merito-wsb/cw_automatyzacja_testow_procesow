import unittest
from unittest.mock import patch
from api_test import TestAPI

class TestAPITest(unittest.TestCase):
    def setUp(self):
        self.api_test = TestAPI("http://api.open-notify.org/iss-now.json", 200, ["timestamp", "iss_position"])

    @patch('subprocess.run')
    def test_uruchom_test_zdany(self, mock_run):
        mock_run.return_value.stdout = '{"timestamp": 1598065084, "iss_position": {"latitude": "47.0386", "longitude": "9.6878"}}200'
        result = self.api_test.uruchom_test()
        self.assertEqual(result, "Test http://api.open-notify.org/iss-now.json: ZDANY")

    @patch('subprocess.run')
    def test_uruchom_test_niepowodzenie_status(self, mock_run):
        mock_run.return_value.stdout = '{"timestamp": 1598065084, "iss_position": {"latitude": "47.0386", "longitude": "9.6878"}}404'
        result = self.api_test.uruchom_test()
        self.assertTrue("NIE POWIODŁO SIĘ" in result)

    @patch('subprocess.run')
    def test_uruchom_test_niepowodzenie_klucz(self, mock_run):
        mock_run.return_value.stdout = '{"timestamp": 1598065084}200'
        result = self.api_test.uruchom_test()
        self.assertTrue("NIE POWIODŁO SIĘ" in result)

if __name__ == "__main__":
    unittest.main()
