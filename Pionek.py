class Pionek:
    """
    Klasa reprezentująca pionka do gry.

    Atrybuty klasy:
        -pozycja: parametr typu NoneType, Pole lub str("zdjęty", "banda"), który mówi, gdzie aktualnie znajduje się pionek

        -kolor: parametr typu str, który mówi, jakiego koloru jest pionek do gry (czarny lub czerwony)
    """
    def __init__(self, kolor):
        """
        Inicjalizuje obiekt klasy Pionek.

        :param kolor: Kolor pionka.
        :type kolor: str
        """
        if kolor not in ["czarny", "czerwony"]:
            raise ValueError("Podano niepoprawny kolor pionka!")
        self.pozycja = None
        self.kolor = kolor

    def gdzie(self):
        """
        Zwraca aktualną pozycję pionka.

        :return: Aktualna pozycja pionka (pole, None,"zdjęty" lub "banda").
        :rtype: Pole, NoneType lub str
        """
        return self.pozycja

    def podaj_kolor(self):
        """
        Zwraca kolor pionka.

        :return: Kolor pionka ("czarny" lub "czerwony").
        :rtype: str
        """
        return self.kolor

    def zmien_pozycje(self, nowa_poz):
        """
        Zmienia pozycję pionka na podane pole.

        :param nowa_poz: Nowa pozycja pionka (pole,"zdjęty" lub "banda").
        :type nowa_poz: Pole lub str
        :return: None
        :rtype: NoneType
        """
        self.pozycja = nowa_poz
