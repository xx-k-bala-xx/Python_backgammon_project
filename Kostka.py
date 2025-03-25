import random
from sympy import sympify


class Kostka:
    """
    Klasa reprezentująca sześcienną kostkę do gry.

    Atrybuty klasy:
        -oczka_prob: parametr typu dict, który pamięta prawdopodobieństwo wyrzucenia poszczególnej ilości oczek na kostce
    """
    def __init__(self, prob=("1/6", "1/6", "1/6", "1/6", "1/6", "1/6")):
        """
        Inicjalizuje obiekt klasy Kostka.

        :param prob: Prawdopodobieństwo wyrzucenia poszczególnej ilości oczek.
        :type prob: tuple
        """
        if sympify(prob[0])+sympify(prob[1])+sympify(prob[2])+sympify(prob[3])+sympify(prob[4])+sympify(prob[5]) != 1:
            raise ValueError("Suma prawdopodobieństw nie jest równa 1!")
        self.oczka_prob = {1: sympify(prob[0]), 2: sympify(prob[1]), 3: sympify(prob[2]),
                           4: sympify(prob[3]), 5: sympify(prob[4]), 6: sympify(prob[5])}

    def rzut(self):
        """
        Wykonuje rzut kostką i zwraca wyrzuconą ilość oczek.

        :return: Wyrzucona ilość oczek.
        :rtype: int
        """
        a = random.random()

        b = self.oczka_prob[1]
        c = b+self.oczka_prob[2]
        d = c+self.oczka_prob[3]
        e = d+self.oczka_prob[4]
        f = e+self.oczka_prob[5]

        if a < b:
            return 1
        elif b <= a < c:
            return 2
        elif c <= a < d:
            return 3
        elif d <= a < e:
            return 4
        elif e <= a < f:
            return 5
        else:
            return 6

    def czy_uczciwa(self):
        """
        Sprawdza, czy kostka jest uczciwa.

        :return: True, jeśli kostka jest uczciwa, False w przeciwnym razie.
        :rtype: bool
        """
        if self.oczka_prob == {1: sympify("1/6"), 2: sympify("1/6"), 3: sympify("1/6"),
                               4: sympify("1/6"), 5: sympify("1/6"), 6: sympify("1/6")}:
            return True
        else:
            return False
