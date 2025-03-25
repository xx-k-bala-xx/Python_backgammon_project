from Domek import Domek
from Pole import Pole


class Plansza:
    """
    Klasa reprezentująca planszę do gry.

    Atrybuty klasy:
        -pola: parametr typu dict przechowujący pola znajdujące sie na planszy

        -domki: parametr typu dict przechowujący domki każdego koloru pionków

        -banda: parametr typu dict przechowujący stan bandy dla poszczególnego koloru pionków

        -zdjete_z_planszy: parametr typu dict przechowujący zdjęte z planszy pionki dla każdego koloru
    """
    def __init__(self):
        """
        Inicjalizuje nowy obiekt Plansza.
        """
        self.pola = dict()
        for i in range(1, 25, 1):
            self.pola[i] = Pole(i)

        self.domki = {"czarny": Domek([self.pola[i] for i in range(1, 7, 1)]),
                      "czerwony": Domek([self.pola[i] for i in range(19, 25, 1)])}
        self.banda = {"czarny": list(), "czerwony": list()}
        self.zdjete_z_planszy = {"czarny": set(), "czerwony": set()}

    def podaj_pole(self, nr_pola):
        """
        Zwraca pole o podanym numerze.

        :param nr_pola: Numer pola.
        :type nr_pola: int
        :return: Pole o podanym numerze.
        :rtype: Pole
        """
        return self.pola[nr_pola]

    def dod_pionka_do_bandy(self, nr_pola):
        """
        Dodaje pionka do bandy.

        :param nr_pola: Numer pola, z którego ma być zdejmowany pionek.
        :type nr_pola: int
        """
        pionek = self.pola[nr_pola].zdejmij_pionka()
        self.banda[pionek.podaj_kolor()].append(pionek)
        pionek.zmien_pozycje("banda")

    def wez_pionka_z_bandy(self, nr_pola, kolor):
        """
        Zdejmuje pionka z bandy i umieszcza na polu o podanym numerze.

        :param nr_pola: Numer pola, na którym ma być umieszczony pionek.
        :type nr_pola: int
        :param kolor: Kolor pionka, który ma być zdjęty z bandy ("czarny" lub "czerwony").
        :type kolor: str
        """
        pionek = self.banda[kolor].pop()
        self.pola[nr_pola].dodaj_pionka(pionek)

    def zdejmij_pionka_z_planszy(self, nr_pola):
        """
        Zdejmuje pionka z planszy.

        :param nr_pola: Numer pola, z którego ma być zdejmowany pionek.
        :type nr_pola: int
        """
        pionek = self.pola[nr_pola].zdejmij_pionka()
        self.zdjete_z_planszy[pionek.podaj_kolor()].add(pionek)
        pionek.zmien_pozycje("zdjęty")

    def podaj_domek(self, kolor):
        """
        Zwraca domek o podanym kolorze.

        :param kolor: Kolor domku ("czarny" lub "czerwony").
        :type kolor: str
        :return: Domek o podanym kolorze.
        :rtype: Domek
        """
        return self.domki[kolor]

    def podaj_bande(self, kolor):
        """
        Zwraca bandę o podanym kolorze.

        :param kolor: Kolor bandy ("czarny" lub "czerwony").
        :type kolor: str
        :return: Banda o podanym kolorze.
        :rtype: list(Lista, której elementami są obiekty klasy Pionek.)
        """
        return self.banda[kolor]

    def podaj_zdjete_z_planszy(self, kolor):
        """
        Zwraca zdejmowane pionki z planszy o podanym kolorze.

        :param kolor: Kolor pionków ("czarny" lub "czerwony").
        :type kolor: str
        :return: Zdjęte pionki z planszy o podanym kolorze.
        :rtype: set(Zbiór, którego elementami są obiekty klasy Pionek.)
        """
        return self.zdjete_z_planszy[kolor]

    def podaj_pola(self):
        """
        Zwraca wszystkie pola planszy.

        :return: Pola planszy.
        :rtype: dict(Słownik, którego kluczami są obiekty typu int, zaś wartości to obiekty klasy Pole.)
        """
        return self.pola

    def stan_planszy(self):
        """
        Wyświetla stan planszy.
        """
        for nr_pola in self.pola:
            print(str(self.pola[nr_pola]))

    def stan_bandy(self):
        """
        Zwraca stan bandy.

        :return: Stan bandy.
        :rtype: dict(Słownik, którego kluczami są obiekty typu str("czarny" lub "czerwony"), zaś kluczami są obiekty typu int.)
        """
        stan_bandy = dict()
        for kolor, lst in self.banda.items():
            stan_bandy[kolor] = len(lst)
        return stan_bandy
