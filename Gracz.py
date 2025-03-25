from Pionek import Pionek


class Gracz:
    """
    Klasa reprezentująca gracza.

    Atrybuty klasy:
        -nazwa: parametr typu str, przechowujący informacje, o nicku gracza

        -kolor: parametr typu str, przechowujący informacje, jakim kolorem będzie grał gracz

        -lst_pionkow: parametr typu list, przechowujący listę pionków przypisanych do gracza

        -plansza: parametr typu Plansza, przechowujący planszę, na której odbędzie się gra

        -nr_bandy: parametr typu int, który mówi, jako które pole możemy traktować bandę w zależności od koloru

        -wsp_chodzenia: parametr typu int, który mówi, w jakim kierunku gracz przemieszcza się po planszy pionkami

        -dostepne_pola: parametr typu dict, przechowujący pola, na które gracz może przemieścić pionka

        -pola_z_pionkami: parametr typu dict, przechowujący pola, na których są pionki gracza

        -pola_z_pionkami_do_zbicia: parametr typu dict, przechowujący pola, na których znajdują się pionki przeciwnego gracza, które można zbić
    """
    def __init__(self, nazwa_gracza, kolor):
        """
        Inicjalizuje nowy obiekt Gracz.

        :param nazwa_gracza: Nazwa gracza.
        :type nazwa_gracza: str
        :param kolor: Kolor gracza ("czarny" lub "czerwony).
        :type kolor: str
        """
        self.nazwa = nazwa_gracza
        self.kolor = kolor
        self.lst_pionkow = []
        for _ in range(15):
            self.lst_pionkow.append(Pionek(kolor))
        self.plansza = None

        if self.kolor == "czerwony":
            self.nr_bandy = 0
            self.wsp_chodzenia = 1
        else:
            self.nr_bandy = 25
            self.wsp_chodzenia = -1

        self.dostepne_pola = None
        self.pola_z_pionkami = None
        self.pola_z_pionkami_do_zbicia = None

    def podaj_nazwe(self):
        """
        Zwraca nazwę gracza.

        :return: Nazwa gracza.
        :rtype: str
        """
        return self.nazwa

    def podaj_kolor(self):
        """
        Zwraca kolor gracza.

        :return: Kolor gracza ("czarny" lub "czerwony).
        :rtype: str
        """
        return self.kolor

    def podaj_lst_pionkow(self):
        """
        Zwraca listę pionków gracza.

        :return: Lista pionków gracza.
        :rtype: list(Lista, której elementami są obiekty klasy Pionek)
        """
        return self.lst_pionkow

    def podaj_kolor_przeciwnika(self):
        """
        Zwraca kolor przeciwnika.

        :return: Kolor przeciwnika ("czarny" lub "czerwony).
        :rtype: str
        """
        if self.kolor == "czarny":
            return "czerwony"
        else:
            return "czarny"

    def dodaj_plansze(self, plansza):
        """
        Dodaje planszę do gracza.

        :param plansza: Plansza do dodania.
        :type plansza: Plansza
        """
        self.plansza = plansza

    def podaj_mozliwosci_ruchu(self):
        """
        Aktualizuje dostępne pola, pola z pionkami oraz pola z pionkami do zbicia dla gracza.
        """
        dostepne_pola = dict()
        pola_z_pionkami = dict()
        pola_z_pionkami_do_zbicia = dict()
        for nr_pola, pole in self.plansza.podaj_pola().items():
            a = pole.podaj_lst_pionkow()
            b = nr_pola
            if len(a) == 0:
                dostepne_pola[b] = pole
            elif a[0].podaj_kolor() == self.kolor:
                dostepne_pola[b] = pole
                pola_z_pionkami[b] = pole
            elif len(a) == 1 and a[0].podaj_kolor() == self.podaj_kolor_przeciwnika():
                pola_z_pionkami_do_zbicia[b] = pole
                dostepne_pola[b] = pole
            else:
                continue
        self.dostepne_pola = dostepne_pola
        self.pola_z_pionkami = pola_z_pionkami
        self.pola_z_pionkami_do_zbicia = pola_z_pionkami_do_zbicia

    def podaj_dostepne_pola(self):
        """
        Zwraca dostępne pola dla gracza.

        :return: Dostępne pola dla gracza.
        :rtype: dict(Słownik, którego kluczami są obiekty typu int, zaś wartości to obiekty klasy Pole.)
        """
        return self.dostepne_pola

    def podaj_pola_z_pionkami(self):
        """
        Zwraca pola z pionkami gracza.

        :return: Pola z pionkami gracza.
        :rtype: dict(Słownik, którego kluczami są obiekty typu int, zaś wartości to obiekty klasy Pole.)
        """
        return self.pola_z_pionkami

    def podaj_pola_z_pionkami_do_zbicia(self):
        """
        Zwraca pola z pionkami przeciwnika, które mogą być zbite.

        :return: Pola z pionkami gracza.
        :rtype: dict(Słownik, którego kluczami są obiekty typu int, zaś wartości to obiekty klasy Pole.)
        """
        return self.pola_z_pionkami_do_zbicia

    def podaj_kierunek_ruchu(self):
        """
        Wyświetla kierunek ruchu pionków gracza.
        """
        if self.wsp_chodzenia == -1:
            print("Kierunek ruchu pionkami: w górę.\n")
        else:
            print("Kierunek ruchu pionkami: w dół.\n")

    def podaj_wsp_chodzenia(self):
        """
        Zwraca współczynnik chodzenia pionków gracza.

        :return: Współczynnik chodzenia pionków gracza (1 lub -1).
        :rtype: int
        """
        return self.wsp_chodzenia

    def podaj_nr_bandy(self):
        """
        Zwraca numer pola, reprezentującego bandę gracza.

        :return: Numer pola bandy gracza (0 lub 25).
        :rtype: int
        """
        return self.nr_bandy
