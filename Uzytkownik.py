from Gracz import Gracz


class Uzytkownik(Gracz):
    """
    Podklasa Gracza reprezentująca gracza będącego użytkownikiem.
    """
    def podaj_dostepne_pola_w_bazie(self):
        """
        Zwraca dostępne pola w domku przeciwnika, czyli bazie.

        :return: Dostępne pola w bazie.
        :rtype: dict(Słownik, którego kluczami są obiekty typu int, zaś wartości to obiekty klasy Pole.)
        """
        dostepne_pola_w_bazie = dict()
        for pole in self.plansza.podaj_domek(self.podaj_kolor_przeciwnika()).podaj_lst_pol():
            if not pole.czy_pole_jest_zablokowane(self.kolor):
                dostepne_pola_w_bazie[abs(self.nr_bandy - pole.podaj_nr_pola())] = pole
        return dostepne_pola_w_bazie

    def czy_mozna_zdjac_wszystko_z_bandy(self, wynik_rzutu):
        """
        Sprawdza, czy można zdjąć wszystkie pionki z bandy.

        :param wynik_rzutu: Wynik rzutu kostką.
        :type wynik_rzutu: list(Lista, której elementami są obiekty typu int.)
        :return: True, jeśli można zdjąć wszystkie pionki z bandy, False w przeciwnym razie.
        :rtype: bool
        """
        a1 = len(self.plansza.podaj_bande(self.kolor))
        a = len(self.plansza.podaj_bande(self.kolor))
        if a == 0:
            print("Żaden pionek nie jest na bandzie.")
            return True
        b = wynik_rzutu.copy()
        dostepne_pola = self.podaj_dostepne_pola_w_bazie()
        if dostepne_pola == dict():
            print("Brak możliwości ruchu w tej kolejce.")
            return False
        for rzut in wynik_rzutu:
            if rzut in dostepne_pola and a > 0:
                a -= 1
                b.remove(rzut)
        while a > 0 and len(b) > 0:
            if len(b) == 1:
                break
            elif len(b) == 2:
                d1, d2 = b[0], b[1]
                if d1 + d2 in dostepne_pola:
                    a -= 1
                    b.remove(d1)
                    b.remove(d2)
                else:
                    break
            elif len(b) == 3:
                d = b[0]
                if d * 2 in dostepne_pola:
                    a -= 1
                    b.pop()
                    b.pop()
                elif d * 3 in dostepne_pola:
                    a -= 1
                    b.pop()
                    b.pop()
                    b.pop()
                else:
                    break
            else:
                d = b[0]
                if d * 2 in dostepne_pola:
                    a -= 1
                    b.pop()
                    b.pop()
                elif d * 3 in dostepne_pola:
                    a -= 1
                    b.pop()
                    b.pop()
                    b.pop()
                elif d * 4 in dostepne_pola:
                    a -= 1
                    b.pop()
                    b.pop()
                    b.pop()
                    b.pop()

                else:
                    break

        if a > 0:
            print("Nie można zdjąć wszystkich pionków z bandy", "Ilość dostępnych do zdjęcia pionków to", a1-a,
                  ". Później brak dalszej możliwości ruchu w tej kolejce.")
            return False
        else:
            print("Można zdjąć wszystkie pionki z bandy w tej kolejce.")
            return True

    def wyjdz_z_bandy_na_pole(self, nr_nowego_pola):
        """
        Wychodzi z pionkiem z bandy na podane pole.

        :param nr_nowego_pola: Numer nowego pola.
        :type nr_nowego_pola: int
        """
        if nr_nowego_pola in self.pola_z_pionkami_do_zbicia:
            self.plansza.dod_pionka_do_bandy(nr_nowego_pola)
        self.plansza.wez_pionka_z_bandy(nr_nowego_pola, self.kolor)

    def przesun_pionka_z_pola_na_pole(self, nr_aktualnego_pola, nr_nowego_pola):
        """
        Przesuwa pionka z jednego pola na drugie.

        :param nr_aktualnego_pola: Numer aktualnego pola.
        :type nr_aktualnego_pola: int
        :param nr_nowego_pola: Numer nowego pola.
        :type nr_nowego_pola: int
        """
        if nr_nowego_pola in self.dostepne_pola:
            a = self.pola_z_pionkami[nr_aktualnego_pola].zdejmij_pionka()
            if nr_nowego_pola in self.pola_z_pionkami_do_zbicia:
                self.plansza.dod_pionka_do_bandy(nr_nowego_pola)
            self.dostepne_pola[nr_nowego_pola].dodaj_pionka(a)
        else:
            print("Nie można wykonać tego ruchu!")

    def wyjdz_pionkiem_z_pola_z_planszy(self, nr_pola):
        """
        Zdejmuje pionka z podanego pola z planszy.

        :param nr_pola: Numer pola.
        :type nr_pola: int
        """
        if nr_pola in self.pola_z_pionkami:
            self.plansza.zdejmij_pionka_z_planszy(nr_pola)
        else:
            print("Na tym polu nie ma pionków. Nie można wykonać tego ruchu.")

    def podaj_mozliwosci_ruchu_print(self):
        """
        Wyświetla numery dostępnych pól, pól z pionkami gracza, pól z pionkami do zbicia oraz stan bandy.
        """
        print("Dostępne pola:", list(self.dostepne_pola.keys()))
        print("Pola z pionkami gracza", self.podaj_nazwe(), ":", list(self.pola_z_pionkami.keys()))
        print("Pola z pionkami do zbicia:", list(self.pola_z_pionkami_do_zbicia.keys()))
        print("Stan bandy:", self.plansza.stan_bandy())
