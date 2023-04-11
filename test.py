import unittest
import requests


class MyTestCase(unittest.TestCase):
    def test_200(self):
        response = requests.request('GET', 'http://localhost:5000/')
        sample = response.content.decode()
        self.assertEqual(sample, 'Home page')  # add assertion here


if __name__ == '__main__':
    unittest.main()
