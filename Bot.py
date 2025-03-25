from Gracz import Gracz


class Bot(Gracz):
    """
    Podklasa Gracza reprezentująca gracza będącego komputerem(botem).
    """
    def zdejmij_pionki_z_bandy(self, wynik_rzutu):
        """
        Zdejmuje pionki z bandy i umieszcza na planszy w odpowiednich miejscach.

        :param wynik_rzutu: Lista wyników rzutów kostką.
        :type wynik_rzutu: list
        :return: Krotka zawierająca informację, czy udało się zdejmować pionki z bandy i zaktualizowaną listę wyników rzutów.
        :rtype: tuple
        """
        a = len(self.plansza.podaj_bande(self.kolor))
        if a == 0:
            return True, wynik_rzutu

        b = wynik_rzutu.copy()

        dostepne_pola = dict()
        for pole in self.plansza.podaj_domek(self.podaj_kolor_przeciwnika()).podaj_lst_pol():
            if not pole.czy_pole_jest_zablokowane(self.kolor):
                dostepne_pola[abs(self.nr_bandy - pole.podaj_nr_pola())] = pole

        if dostepne_pola == dict():
            return False, wynik_rzutu

        for rzut in wynik_rzutu:
            if rzut in dostepne_pola and a > 0:
                if abs(self.nr_bandy - rzut) in self.pola_z_pionkami_do_zbicia:
                    self.plansza.dod_pionka_do_bandy(abs(self.nr_bandy - rzut))
                self.plansza.wez_pionka_z_bandy(dostepne_pola[rzut].podaj_nr_pola(), self.kolor)
                a -= 1
                b.remove(rzut)
        while a > 0 and len(b) > 0:
            if len(b) == 1:
                break
            elif len(b) == 2:
                d1, d2 = b[0], b[1]
                if d1 + d2 in dostepne_pola:
                    if abs(self.nr_bandy - (d1 + d2)) in self.pola_z_pionkami_do_zbicia:
                        self.plansza.dod_pionka_do_bandy(abs(self.nr_bandy - (d1 + d2)))
                    self.plansza.wez_pionka_z_bandy(dostepne_pola[d1 + d2].podaj_nr_pola(), self.kolor)
                    a -= 1
                    b.remove(d1)
                    b.remove(d2)
                else:
                    break
            elif len(b) == 3:
                d = b[0]
                if d * 2 in dostepne_pola:
                    if abs(self.nr_bandy - (d * 2)) in self.pola_z_pionkami_do_zbicia:
                        self.plansza.dod_pionka_do_bandy(abs(self.nr_bandy - (d * 2)))
                    self.plansza.wez_pionka_z_bandy(dostepne_pola[d * 2].podaj_nr_pola(), self.kolor)
                    a -= 1
                    b.pop()
                    b.pop()
                elif d * 3 in dostepne_pola:
                    if abs(self.nr_bandy - (d * 3)) in self.pola_z_pionkami_do_zbicia:
                        self.plansza.dod_pionka_do_bandy(abs(self.nr_bandy - (d * 3)))
                    self.plansza.wez_pionka_z_bandy(dostepne_pola[d * 2].podaj_nr_pola(), self.kolor)
                    a -= 1
                    b.pop()
                    b.pop()
                    b.pop()
                else:
                    break
            else:
                d = b[0]
                if d * 2 in dostepne_pola:
                    if abs(self.nr_bandy - (d * 2)) in self.pola_z_pionkami_do_zbicia:
                        self.plansza.dod_pionka_do_bandy(abs(self.nr_bandy - (d * 2)))
                    self.plansza.wez_pionka_z_bandy(dostepne_pola[d * 2].podaj_nr_pola(), self.kolor)
                    a -= 1
                    b.pop()
                    b.pop()
                elif d * 3 in dostepne_pola:
                    if abs(self.nr_bandy - (d * 3)) in self.pola_z_pionkami_do_zbicia:
                        self.plansza.dod_pionka_do_bandy(abs(self.nr_bandy - (d * 3)))
                    self.plansza.wez_pionka_z_bandy(dostepne_pola[d * 2].podaj_nr_pola(), self.kolor)
                    a -= 1
                    b.pop()
                    b.pop()
                    b.pop()
                elif d * 4 in dostepne_pola:
                    if abs(self.nr_bandy - (d * 4)) in self.pola_z_pionkami_do_zbicia:
                        self.plansza.dod_pionka_do_bandy(abs(self.nr_bandy - (d * 4)))
                    self.plansza.wez_pionka_z_bandy(dostepne_pola[d * 2].podaj_nr_pola(), self.kolor)
                    a -= 1
                    b.pop()
                    b.pop()
                    b.pop()
                    b.pop()

                else:
                    break

        if a > 0:
            return False, b
        else:
            return True, b

    def przesun_pionka_na_pole(self, wynik):
        """
        Przesuwa pionek na planszy w zależności od wyniku rzutu kostką.

        :param wynik: Wynik rzutu kostką.
        :type wynik: int
        :return: Wartość logiczna informująca, czy przesunięcie pionka się powiodło (True) lub nie (False).
        :rtype: bool
        """
        if self.pola_z_pionkami_do_zbicia != dict():
            for nr_pola in self.pola_z_pionkami_do_zbicia:
                if nr_pola - self.wsp_chodzenia * wynik in self.pola_z_pionkami:
                    c = self.pola_z_pionkami[nr_pola - self.wsp_chodzenia * wynik].zdejmij_pionka()
                    self.plansza.dod_pionka_do_bandy(nr_pola)
                    self.pola_z_pionkami[nr_pola] = self.pola_z_pionkami_do_zbicia[nr_pola]
                    self.pola_z_pionkami[nr_pola].dodaj_pionka(c)
                    return True

        pola_z_poj_pionkami = dict()
        for nr_pola, pole in self.pola_z_pionkami.items():
            if len(pole.podaj_lst_pionkow()) == 1:
                pola_z_poj_pionkami[nr_pola] = pole

        for nr_pola in pola_z_poj_pionkami:
            if nr_pola + self.wsp_chodzenia * wynik in self.pola_z_pionkami:
                c = pola_z_poj_pionkami[nr_pola].zdejmij_pionka()
                self.pola_z_pionkami[nr_pola + self.wsp_chodzenia * wynik].dodaj_pionka(c)
                return True
            elif nr_pola - self.wsp_chodzenia * wynik in self.pola_z_pionkami:
                c = self.pola_z_pionkami[nr_pola - self.wsp_chodzenia * wynik].zdejmij_pionka()
                self.pola_z_pionkami[nr_pola].dodaj_pionka(c)
                return True

        e = sorted(list(self.pola_z_pionkami.keys()))
        f = list(reversed(e.copy()))
        for j in range(len(e)):
            if self.kolor == "czarny":
                if f[j] - wynik in self.dostepne_pola:
                    g = self.pola_z_pionkami[f[j]].zdejmij_pionka()
                    self.dostepne_pola[f[j] - wynik].dodaj_pionka(g)
                    # self.pola_z_pionkami[f[j] - wynik] = self.dostepne_pola[f[j] - wynik]
                    return True
            elif self.kolor == "czerwony":
                if e[j] + wynik in self.dostepne_pola:
                    g = self.pola_z_pionkami[e[j]].zdejmij_pionka()
                    self.dostepne_pola[e[j] + wynik].dodaj_pionka(g)
                    # self.pola_z_pionkami[e[j] + wynik] = self.dostepne_pola[e[j] + wynik]
                    return True

        return False

    def wychodzenie_z_planszy(self, wynik):
        """
        Zdejmuje pionek z planszy na podstawie wyniku rzutu.

        :param wynik: Wynik rzutu kostką.
        :type wynik: int
        :return: Wartość logiczna informująca, czy zdejmowanie pionka z planszy się powiodło (True) lub nie (False).
        :rtype: bool
        """
        if self.kolor == "czarny":
            if wynik in self.pola_z_pionkami:
                self.plansza.zdejmij_pionka_z_planszy(wynik)
                return True
            else:
                b = [k for k in self.pola_z_pionkami.keys() if k < wynik]
                if b:
                    self.plansza.zdejmij_pionka_z_planszy(b[-1])
                    return True
        else:
            c = 25 - wynik
            if c in self.pola_z_pionkami:
                self.plansza.zdejmij_pionka_z_planszy(c)
                return True
            else:
                b = [k for k in self.pola_z_pionkami.keys() if k > c]
                if b:
                    self.plansza.zdejmij_pionka_z_planszy(b[0])
                    return True
        return False
