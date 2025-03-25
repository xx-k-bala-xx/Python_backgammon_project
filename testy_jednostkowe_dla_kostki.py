import unittest
from sympy import sympify
from Kostka import Kostka


class TestKostka(unittest.TestCase):
    def setUp(self):
        self.kostka_uczciwa = Kostka()
        self.kostka_nieuczciwa = Kostka(prob=("1/7", "1/7", "1/7", "1/7", "1/7", "2/7"))

    def test_init(self):
        poprawne_prob = ("1/9", "1/9", "2/9", "1/9", "1/9", "1/3")
        niepoprawne_prob = ("1/9", "1/9", "2/9", "1/9", "1/9", "2/3")
        dict_poprawne_prob = {1: sympify(poprawne_prob[0]), 2: sympify(poprawne_prob[1]), 3: sympify(poprawne_prob[2]),
                              4: sympify(poprawne_prob[3]), 5: sympify(poprawne_prob[4]), 6: sympify(poprawne_prob[5])}
        kostka = Kostka(poprawne_prob)
        # Sprawdzanie, czy atrybut Kostki oczka_prob jest poprawny
        self.assertDictEqual(kostka.oczka_prob, dict_poprawne_prob)
        # Sprawdzanie, czy zostanie poprawnie rzucony wyjątek, dla niepoprawnie podanego prawdopodobieństwa
        with self.assertRaises(ValueError):
            kostka = Kostka(niepoprawne_prob)

    def test_rzut(self):
        # Sprawdzenie, czy rzut zwraca wartość z zakresu 1-6
        for _ in range(100):
            wynik = self.kostka_uczciwa.rzut()
            self.assertTrue(1 <= wynik <= 6)

    def test_czy_uczciwa(self):
        # Sprawdzenie, czy uczciwa kostka zwraca True
        self.assertTrue(self.kostka_uczciwa.czy_uczciwa())

        # Sprawdzenie, czy nieuczciwa kostka zwraca False
        self.assertFalse(self.kostka_nieuczciwa.czy_uczciwa())


if __name__ == '__main__':
    unittest.main()
