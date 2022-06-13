import unittest
from System.lære import lære

class TestLære(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setupClass")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    def setUp(self):
        self.lære_1 = lære("te42", 123456)

    def tearDown(self):
        print("tearDown\n")

    def test_get_loginid(self):
        self.assertEqual(self.lære_1.getloginid(), "te42")

    def test_get_kursusnr(self):
        self.assertEqual(self.lære_1.getpassword(), 123456)

if __name__ == "__main__":
    unittest.main()