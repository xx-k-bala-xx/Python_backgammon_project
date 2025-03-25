class Pole:
    """
    Klasa reprezentująca pojedyncze pole na planszy.

    Atrybuty klasy:
        -numer_pola: parametr typu int, który wskazuje, jaki numer został przypisany do pola (identyfikuje jego pozycję na planszy)

        -pionki_na_polu: lista pionków znajdujących się na danym polu
    """
    def __init__(self, numer_pola):
        """
        Inicjalizuje obiekt klasy Pole.

        :param numer_pola: Numer pola.
        :type numer_pola: int
        """
        self.numer_pola = numer_pola
        self.pionki_na_polu = []

    def podaj_nr_pola(self):
        """
        Zwraca numer pola.

        :return: Numer pola.
        :rtype: int
        """
        return self.numer_pola

    def podaj_lst_pionkow(self):
        """
        Zwraca listę pionków na polu.

        :return: Lista pionków na polu.
        :rtype: list(Lista, której elementami są obiekty klasy Pionek)
        """
        return self.pionki_na_polu

    def ustaw_lst_pionkow(self, lst):
        """
        Ustawia listę pionków na polu i zmienia pozycję pionków na liście.

        :param lst: Lista pionków.
        :type lst: list(Lista, której elementami są obiekty klasy Pionek)
        """
        self.pionki_na_polu = lst
        for pionek in lst:
            pionek.zmien_pozycje(self)

    def dodaj_pionka(self, pionek):
        """ Funkcja dodaje nowy obiekt instancji Pionek do pola.

        :param pionek: Pionek, który ma być dodany do pola.
        :type pionek: Pionek
        """
        self.pionki_na_polu.append(pionek)
        pionek.zmien_pozycje(self)

    def czy_pole_jest_zablokowane(self, kolor):
        """
        Sprawdza, czy pole jest zablokowane przez pionki przeciwnika.

        :param kolor: Kolor gracza.
        :type kolor: str
        :return: True, jeśli pole jest zablokowane, False w przeciwnym razie.
        :rtype: bool
        """
        if len(self.pionki_na_polu) <= 1:
            return False
        else:
            if self.pionki_na_polu[0].podaj_kolor() == kolor:
                return False
            else:
                return True

    def zdejmij_pionka(self):
        """
        Zdejmuje pionka z pola.

        :return: Zdejmowany pionek.
        :rtype: Pionek
        """
        return self.pionki_na_polu.pop()

    def __str__(self):
        """
        Zwraca reprezentację napisową pola.

        :return: Reprezentacja napisowa obiektu Pole.
        :rtype: str
        """
        a = len(self.pionki_na_polu)
        if a > 0:
            b = self.pionki_na_polu[0].podaj_kolor()
            return f"Pole nr {self.numer_pola}: liczba pionków-{a}; kolor-{b}."
        else:
            return f"Pole nr {self.numer_pola}: brak pionków."
