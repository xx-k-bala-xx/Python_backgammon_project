class Domek:
    """
    Klasa reprezentująca domek w grze Backgammon składający się z 6 odpowiednich pól.

    Atrybuty klasy:
        -wlasciciel: parametr typu NoneType lub Gracz, który mówi, do kogo należy domek

        -lst_pol: lista pól, które tworzą domek
    """
    def __init__(self, lst_pol, wlasciciel=None):
        """
        Inicjalizuje nowy obiekt Domek.

        :param lst_pol: Lista pól, które należą do domku.
        :type lst_pol: list
        :param wlasciciel: Właściciel domku (opcjonalny), domyślnie None.
        :type wlasciciel: Gracz lub NoneType
        """
        self.wlasciciel = wlasciciel
        self.lst_pol = lst_pol

    def podaj_wlasciciela(self):
        """
        Zwraca właściciela domku.

        :return: Właściciel domku.
        :rtype: Gracz lub NoneType
        """
        return self.wlasciciel

    def ustaw_wlasciciela(self, nowy_wlasciciel):
        """
        Ustawia nowego właściciela domku.

        :param nowy_wlasciciel: Nowy właściciel domku.
        :type nowy_wlasciciel: Gracz
        """
        self.wlasciciel = nowy_wlasciciel

    def podaj_lst_pol(self):
        """
        Zwraca listę pól domku.

        :return: Lista pól domku.
        :rtype: list
        """
        return self.lst_pol

    def czy_wszystkie_w_domku(self):
        """
        Sprawdza, czy wszystkie pionki właściciela znajdują się w domku.

        :return: True, jeśli wszystkie pionki są w domku, False w przeciwnym razie.
        :rtype: bool
        """
        if self.wlasciciel is None:
            print("nie przypisano domku do gracza")
            return False
        else:
            for pionek in self.wlasciciel.podaj_lst_pionkow():
                if pionek.gdzie() not in self.lst_pol and pionek.gdzie() != "zdjęty":
                    return False
            return True
