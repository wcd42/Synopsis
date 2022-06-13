import unittest
from System.kursus import kursus

class TestKursus(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setupClass")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    def setUp(self):
        self.kursus_1 = kursus("systemdev", 42)

    def tearDown(self):
        print("tearDown\n")

    def test_get_kursusnavn(self):
        self.assertEqual(self.kursus_1.getkursusnavn(), "systemdev")

    def test_get_kursusnr(self):
        self.assertEqual(self.kursus_1.getkursusnr(), 42)

if __name__ == "__main__":
    unittest.main()