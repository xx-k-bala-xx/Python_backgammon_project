import unittest
from Pionek import Pionek


class TestPionek(unittest.TestCase):
    def setUp(self):
        self.pionek = Pionek("czerwony")
        self.pionek.pozycja = "banda"

    def test_init(self):
        kolor = "czarny"
        pionek = Pionek(kolor)
        # Sprawdzanie, czy atrybut Pionka kolor jest poprawny
        self.assertEqual(pionek.kolor, kolor)
        # Sprawdzanie, czy zostanie poprawnie rzucony wyjątek, dla niepoprawnie podanego koloru
        with self.assertRaises(ValueError):
            pionek = Pionek("biały")

    def test_gdzie(self):
        # Sprawdzenie, czy metoda gdzie zwraca poprawną pozycję pionka
        self.assertEqual(self.pionek.gdzie(), "banda")

        # Sprawdzenie, czy domyślna pozycja pionka to None
        pionek_domyslnie = Pionek("czerwony")
        self.assertIsNone(pionek_domyslnie.gdzie())

    def test_podaj_kolor(self):
        # Sprawdzenie, czy metoda podaj_kolor zwraca poprawny kolor pionka
        self.assertEqual(self.pionek.podaj_kolor(), "czerwony")

    def test_zmien_pozycje(self):
        # Sprawdzenie, czy metoda zmien_pozycje zmienia pozycję pionka
        self.pionek.zmien_pozycje("nowa_pozycja")
        self.assertEqual(self.pionek.gdzie(), "nowa_pozycja")

        # Sprawdzenie, czy zmiana pozycji na "zdjęty" działa poprawnie
        self.pionek.zmien_pozycje("zdjęty")
        self.assertEqual(self.pionek.gdzie(), "zdjęty")


if __name__ == '__main__':
    unittest.main()
