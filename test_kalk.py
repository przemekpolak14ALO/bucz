import unittest
from test import dodaj, odejmij

tab = [1,2,3]

class TestKalkulator(unittest.TestCase):
    def test_dodaj(self):
        self.assertEqual(dodaj(2,3),5)

    def test_odejmij(self):
        self.assertEqual(odejmij(2,3), -1)

    def test_czyZawiera(self):
        self.assertIn(11, tab)

if __name__=="__main__":
    unittest.main(verbosity=2)