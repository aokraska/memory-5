from random import randint
from operator import attrgetter

CARD_TEMPLATE = """"
         ┌─────────┐
         │{}        │
         │         │
         │         │
         │ {:8}│
         │         │
         │         │
         │        {}│
         └─────────┘"""[1:]


class Karta:
    """Jeden z dziewięciu elementów."""

    def __init__(self, imie):
        self.imie = imie

    def __str__(self):
        first_letter = self.imie[0]
        card = CARD_TEMPLATE.format(first_letter, self.imie, first_letter)
        return card

KARTY = [Karta("Dżaga"), Karta("Gandzia"), Karta("Zadra"),
         Karta("Ciri"), Karta("Bazia"), Karta("Florka"),
         Karta("Forest"), Karta("Tola"), Karta("Coco")]


def wyswietl_karty(karty):
    lines = []
    for card_row in range(3):
        for card_line in range(len(CARD_TEMPLATE.split('\n'))):
            line = ""
            for card in range(3):
                numer_karty = 3 * card_row + card
                card_line_str = str(KARTY[numer_karty])
                card_lines = card_line_str.split('\n')
                line += card_lines[card_line]
            lines.append(line)
            print(line)
    return str(lines)


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
