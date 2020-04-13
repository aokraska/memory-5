from random import randint

class Karta:
    """Jeden z dziewięciu elementów."""

    def __init__(self, imie):
        self.imie = imie

    def __str__(self):
        return self.imie


KARTY = [Karta("Dżaga"), Karta("Gandzia"), Karta("Zadra"),
         Karta("Ciri"), Karta("Bazia"), Karta("Florka"),
         Karta("Forest"), Karta("Tola"), Karta("Coco")]


def wyswietl_karty(karty):
    for row in range(3):
        for element in range(3):
            numer_karty = 3*row + element
            print(karty[numer_karty], end=" ")
        print("\n")


def czysc_ekran():
    # czyszczenie ekranu
    pass


def mieszaj_karty(karty):
    # mieszanie
    for poz in range(len(karty)):
        rand_poz = randint(0, len(karty)-1)
        karty[rand_poz], karty[poz] = karty[poz], karty[rand_poz]
    return karty



def gra():
    """Funkcja przeprowadzająca grę."""
    karty = mieszaj_karty(KARTY)
    wyswietl_karty(karty)




gra()