from Kostka import Kostka
from Plansza import Plansza
from Uzytkownik import Uzytkownik
from Bot import Bot


class PrzebiegGry:
    """
    Klasa reprezentująca rozgrywkę gry w Backgammon.

    Atrybuty klasy:
        -gracze: parametr typu dict, przechowujący graczy, którzy wezmą udział w grze

        -plansza: parametr typu Plansza, przechowujący planszę, na której odbędzie się gra

        -kostki: parametr typu dict, przechowujący dwie kostki, które będą użyte podczas gry

        -aktualny_gracz: parametr typu Gracz or NoneType, przechowujący informacje o aktualnie poruszającym się graczu

    """
    def __init__(self):
        """
        Inicjalizuje obiekt PrzebiegGry.

        Pyta użytkownika o rodzaj gry i tworzy odpowiednie obiekty, by gra mogła się odbyć.
        """
        print("Wybierz rodzaj gry podając numer opcji:")
        print("1. Player vs Bot")
        print("2. Player vs Player")
        a = input()
        while a not in ["1", "2"]:
            print("Wpisałeś błędny komunikat. Wybierz poprawnie opcję.")
            a = input()
        if a == "1":
            print("Podaj swój nick:")
            b = input()
            while b == "":
                print("Nick gracza musi składać się z przynajmniej jednego znaku. Podaj poprawny nick.")
                b = input()
            print("Wybierz kolor podając numer opcji:")
            print("1. czarny")
            print("2. czerwony")
            c = input()
            while c not in ["1", "2"]:
                print("Wpisałeś błędny komunikat. Wybierz poprawnie opcję.")
                c = input()
            if c == "1":
                self.gracze = {"czarny": Uzytkownik(b, "czarny"), "czerwony": Bot("Bot", "czerwony")}
            else:
                self.gracze = {"czerwony": Uzytkownik(b, "czerwony"), "czarny": Bot("Bot", "czarny")}
        else:
            print("Podaj nick pierwszego gracza:")
            b1 = input()
            while b1 == "":
                print("Nick gracza musi składać się z przynajmniej jednego znaku. Podaj poprawny nick.")
                b1 = input()
            print("Podaj nick drugiego gracza:")
            b2 = input()
            while b2 == "":
                print("Nick gracza musi składać się z przynajmniej jednego znaku. Podaj poprawny nick.")
                b2 = input()
            print("Wybierz kolor pionków dla", b1, "podając numer opcji:")
            print("1. czarny")
            print("2. czerwony")
            c = input()
            while c not in ["1", "2"]:
                print("Wpisałeś błędny komunikat. Wybierz poprawnie opcję.")
                c = input()
            if c == "1":
                self.gracze = {"czarny": Uzytkownik(b1, "czarny"), "czerwony": Uzytkownik(b2, "czerwony")}
            else:
                self.gracze = {"czerwony": Uzytkownik(b1, "czerwony"), "czarny": Uzytkownik(b2, "czarny")}

        self.plansza = Plansza()
        self.kostki = {1: Kostka(), 2: Kostka()}
        self.aktualny_gracz = None
        for gracz in self.gracze.values():
            gracz.dodaj_plansze(self.plansza)

        self.plansza.podaj_domek("czarny").ustaw_wlasciciela(self.gracze["czarny"])
        self.plansza.podaj_domek("czerwony").ustaw_wlasciciela(self.gracze["czerwony"])

    def uloz_pionki_na_planszy(self):
        """
        Ustawia pionki na planszy na początkową pozycję.
        """
        self.plansza.podaj_pole(1).ustaw_lst_pionkow(self.gracze["czerwony"].podaj_lst_pionkow()[0:2])
        self.plansza.podaj_pole(24).ustaw_lst_pionkow(self.gracze["czarny"].podaj_lst_pionkow()[0:2])

        self.plansza.podaj_pole(19).ustaw_lst_pionkow(self.gracze["czerwony"].podaj_lst_pionkow()[2:7])
        self.plansza.podaj_pole(6).ustaw_lst_pionkow(self.gracze["czarny"].podaj_lst_pionkow()[2:7])

        self.plansza.podaj_pole(17).ustaw_lst_pionkow(self.gracze["czerwony"].podaj_lst_pionkow()[7:10])
        self.plansza.podaj_pole(8).ustaw_lst_pionkow(self.gracze["czarny"].podaj_lst_pionkow()[7:10])

        self.plansza.podaj_pole(12).ustaw_lst_pionkow(self.gracze["czerwony"].podaj_lst_pionkow()[10:15])
        self.plansza.podaj_pole(13).ustaw_lst_pionkow(self.gracze["czarny"].podaj_lst_pionkow()[10:15])

    def kto_zaczyna_gre(self):
        """
        Określa, który gracz zaczyna grę na podstawie wyników rzutu kostkami oraz wypisuje jego nazwę.

        :return: Podaje gracza, który rozpoczyna grę.
        :rtype: Gracz
        """
        wynik_czarnego = self.kostki[1].rzut()
        wynik_czerwonego = self.kostki[2].rzut()
        while wynik_czerwonego == wynik_czarnego:
            wynik_czarnego = self.kostki[1].rzut()
            wynik_czerwonego = self.kostki[2].rzut()
        if wynik_czarnego > wynik_czerwonego:
            self.aktualny_gracz = self.gracze["czarny"]
        else:
            self.aktualny_gracz = self.gracze["czerwony"]
        print("Grę rozpoczyna", self.aktualny_gracz.podaj_nazwe()+".")
        return self.aktualny_gracz

    def podaj_aktualnego_gracza(self):
        """
        Zwraca aktualnego gracza, który ma wykonać ruch.

        :return: Podaje aktualnego gracza, który ma wykonać ruch.
        :rtype: Gracz
        """
        return self.aktualny_gracz

    def zmien_aktualnego_gracza(self):
        """
        Zmienia aktualnego gracza na przeciwnego.
        """
        if self.aktualny_gracz == self.gracze["czarny"]:
            self.aktualny_gracz = self.gracze["czerwony"]
        else:
            self.aktualny_gracz = self.gracze["czarny"]

    def stan_gry(self):
        """
        Wyświetla aktualny stan planszy.
        """
        self.plansza.stan_planszy()

    def ruch_gracza(self, gracz):
        """
        Wykonuje ruch dla podanego gracza na podstawie wyników rzutu kostkami.

        :param gracz: Gracz, który ma wykonać ruch.
        :type gracz: Gracz
        :return: None, kiedy ruch został bez przeszkód wykonany, "exit", kiedy użytkownik chce zakończyć grę, True, kiedy następuje Pass przez gracza, False, w sytuacji, kiedy gracz, który jest użytkownikiem w trakcie ruchu, zdjął wszystkie pionki z planszy
        :rtype: NoneType, str lub bool
        """
        a = self.kostki[1].rzut()
        b = self.kostki[2].rzut()
        wynik = [a, b]
        str_a = str(a)
        str_b = str(b)
        mozliwe_wejscia_oczek = [str_a, str_b, str_a+"+"+str_b, str_b+"+"+str_a]
        czy_rzut_jest_podwojony = False
        if a == b:
            czy_rzut_jest_podwojony = True
            wynik = [a]*4
            mozliwe_wejscia_oczek = [str_a, str_a+"+"+str_a, str_a+"+"+str_a+"+"+str_a,
                                     str_a+"+"+str_a+"+"+str_a+"+"+str_a]

        gracz.podaj_mozliwosci_ruchu()

        if gracz.podaj_nazwe() == "Bot":
            print("\nWynik rzutu kostkami:", wynik, "\n")
            self.stan_gry()
            print("\n_________________________________________________\n\n")
            c, d = gracz.zdejmij_pionki_z_bandy(wynik)
            if not c:
                return True
            else:
                for wynik_rzutu in d:
                    gracz.podaj_mozliwosci_ruchu()
                    if self.plansza.podaj_domek(gracz.podaj_kolor()).czy_wszystkie_w_domku():
                        u = gracz.wychodzenie_z_planszy(wynik_rzutu)
                        if not u:
                            gracz.przesun_pionka_na_pole(wynik_rzutu)
                    else:
                        gracz.przesun_pionka_na_pole(wynik_rzutu)
        else:
            gracz.podaj_mozliwosci_ruchu_print()
            i = 0
            while len(wynik) > 0:
                if i != 0:
                    print("Ciąg dalszy ruchu gracza", self.aktualny_gracz.podaj_nazwe(), ".")
                print("\nWynik rzutu kostkami:", wynik, "\n")
                self.stan_gry()
                gracz.podaj_mozliwosci_ruchu()
                if gracz.podaj_pola_z_pionkami() == dict():
                    return False
                print("\n_________________________________________________\n")
                print("Wybierz co chcesz zrobić, podając numer opcji:")
                print("0. Pass")
                print("1. Wyjść z bandy.")
                print("2. Ruszyć pionkiem z pola.")
                print("3. Wyjść pionkiem z planszy.")
                print("4. Zakończ grę.")
                print("Uwaga: Jeśli podczas ruchu wpiszesz coś nie tak jak chciałeś to wpisz 'błąd',"
                      " wtedy będziesz mógł zacząć ruch od nowa. ")
                czy_byla_opcja_2 = False
                niedozwolony_ruch = True
                while niedozwolony_ruch:
                    e = input()
                    while e not in ["0", "1", "2", "3", "4"]:
                        print("Wybierz opcję ruchu jeszcze raz.")
                        e = input()
                    if e == "0":
                        return True
                    elif e == "1":
                        if self.plansza.stan_bandy()[gracz.podaj_kolor()] == 0:
                            print("Nie ma pionków na bandzie. Wykonaj inny ruch.")
                            continue
                        else:
                            e2 = gracz.czy_mozna_zdjac_wszystko_z_bandy(wynik)
                            if not e2:
                                return True
                            print("Podaj nr pola na jakie chcesz wyjść pionkiem z bandy:")
                            e1 = input()
                            if e1 == "błąd":
                                continue
                            while not e1.isdigit() or \
                                    abs(gracz.podaj_nr_bandy() - int(e1)) not in gracz.podaj_dostepne_pola_w_bazie():
                                print("Podałeś niepoprawny numer pola! Podaj dozwolony numer pola:")
                                e1 = input()
                            gracz.wyjdz_z_bandy_na_pole(int(e1))
                            niedozwolony_ruch = False
                    elif e == "2":
                        if len(self.plansza.podaj_bande(gracz.podaj_kolor())) == 0:
                            print("Podaj nr pola z którego chcesz ruszyć pionek:")
                            e1 = input()
                            if e1 == "błąd":
                                continue
                            while not e1.isdigit() or int(e1) not in gracz.podaj_pola_z_pionkami():
                                print("Podałeś niepoprawny numer pola! Podaj dozwolony numer pola:")
                                e1 = input()
                            print("Podaj ilość oczek, o jaką chcesz przesunąć pionka,"
                                  " w postaci pojedynczej liczby lub sumy oczek.\n"
                                  "Przykład: Wynik rzutu kostkami:[4,5] możliwe wejścia to 5, 4, 5+4 lub 4+5.")
                            f = input()
                            if f == "błąd":
                                continue
                            while f not in mozliwe_wejscia_oczek or \
                                    sum([int(k) for k in f.split("+")]) * gracz.podaj_wsp_chodzenia() + int(e1)\
                                    not in gracz.podaj_dostepne_pola():
                                if f not in mozliwe_wejscia_oczek:
                                    print("Niepoprawna ilość oczek. Podaj poprawną ilość oczek.")
                                else:
                                    print("Nie można przesunąć pionka o taką ilość oczek, ponieważ pole",
                                          sum([int(k) for k in f.split("+")]) * gracz.podaj_wsp_chodzenia() + int(e1),
                                          "jest zablokowane.\n Przesuń pionka o inną ilość oczek.")
                                f = input()
                            gracz.przesun_pionka_z_pola_na_pole(int(e1),
                                                                sum([int(k) for k in f.split("+")]) *
                                                                gracz.podaj_wsp_chodzenia()+int(e1))
                            czy_byla_opcja_2 = True
                            niedozwolony_ruch = False
                        else:
                            print("Niedozwolony ruch. Najpierw zdejmij wszystkie pionki z bandy.")
                            continue
                    elif e == "3":
                        if self.plansza.podaj_domek(gracz.podaj_kolor()).czy_wszystkie_w_domku():
                            print("Podaj nr pola z którego chesz zdjąć pionka:")
                            e1 = input()
                            if e1 == "błąd":
                                continue
                            while not e1.isdigit() or int(e1) not in gracz.podaj_pola_z_pionkami():
                                print("Podałeś niepoprawny numer pola! Podaj dozwolony numer pola:")
                                e1 = input()
                            gracz.wyjdz_pionkiem_z_pola_z_planszy(int(e1))
                            niedozwolony_ruch = False
                        else:
                            print("Nie można zdejmować pionków z planszy.")
                            continue
                    else:
                        return "exit"
                if not czy_byla_opcja_2:
                    print("Podaj ilość zużytych oczek w tym ruchu w postaci pojedynczej liczby lub sumy oczek.\n "
                          "Przykład: Wynik rzutu kostkami:[4,5] możliwe wejścia to 5, 4, 5+4 lub 4+5.")
                    f = input()
                    if f == "błąd":
                        if e == "1":
                            self.plansza.dod_pionka_do_bandy(int(e1))
                            if int(e1) in gracz.podaj_pola_z_pionkami_do_zbicia():
                                self.plansza.wez_pionka_z_bandy(int(e1), gracz.podaj_kolor_przeciwnika())
                        else:
                            pionek = self.plansza.podaj_zdjete_z_planszy(gracz.podaj_kolor()).pop()
                            self.plansza.podaj_pole(int(e1)).dodaj_pionka(pionek)
                        continue
                    while f not in mozliwe_wejscia_oczek:
                        print("Niepoprawna ilość oczek. Podaj poprawną ilość oczek.")
                        f = input()
                if f.isdigit():
                    if czy_rzut_jest_podwojony:
                        mozliwe_wejscia_oczek.pop()
                        wynik.pop()
                    else:
                        if len(wynik) == 2:
                            mozliwe_wejscia_oczek.pop()
                            mozliwe_wejscia_oczek.pop()
                            mozliwe_wejscia_oczek.remove(f)
                            wynik.remove(int(f))
                        else:
                            mozliwe_wejscia_oczek.pop()
                            wynik.pop()
                else:
                    g = f.split("+")
                    for _ in range(len(g)):
                        mozliwe_wejscia_oczek.pop()
                        wynik.pop()
                print("\n_________________________________________________\n\n")
                i += 1

    def koniec_gry(self):
        """
        Sprawdza, czy zostały spełnione warunki, by gra została zakończona.

        :return: Gracz, który wygrał, False, jeśli nie zostały spełnione warunki, by zakończyć grę.
        :rtype: Gracz lub bool
        """
        if len(self.plansza.podaj_zdjete_z_planszy("czarny")) == 15:
            return self.gracze["czarny"]
        elif len(self.plansza.podaj_zdjete_z_planszy("czerwony")) == 15:
            return self.gracze["czerwony"]
        return False

    def gra(self):
        """
        Symuluje grę.
        """
        self.uloz_pionki_na_planszy()
        a = self.kto_zaczyna_gre()
        czy_wywolano_koniec_gry = False
        while not self.koniec_gry():
            print("Ruch gracza", self.aktualny_gracz.podaj_nazwe()+".")
            self.aktualny_gracz.podaj_kierunek_ruchu()
            b = self.ruch_gracza(a)
            if b == "exit":
                czy_wywolano_koniec_gry = True
                break
            self.zmien_aktualnego_gracza()
            a = self.podaj_aktualnego_gracza()
        if czy_wywolano_koniec_gry:
            print("Zakończono grę na życzenie użytkownika.")
        else:
            print("Koniec gry. Wygrał gracz o nazwie:", self.koniec_gry().podaj_nazwe()+".")
