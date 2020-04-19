from random import randint
from operator import attrgetter

# import only system from os
from os import system, name

# import sleep to show output for some time period
from time import sleep


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
    czy_odkryta = True
    numer = 0

    def __init__(self, imie):
        self.imie = imie

    def __str__(self):
        if self.czy_odkryta:
            first_letter = self.imie[0]
            card = CARD_TEMPLATE.format(first_letter, self.imie, first_letter)
        else:
            card = CARD_TEMPLATE.format(self.numer, "???", self.numer)

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
                card_line_str = str(karty[numer_karty])
                card_lines = card_line_str.split('\n')
                line += card_lines[card_line]
            lines.append(line)
            print(line)
    return str(lines)


def mieszaj_karty(karty):
    # mieszanie
    for poz in range(len(karty)):
        rand_poz = randint(0, len(karty)-1)
        karty[rand_poz], karty[poz] = karty[poz], karty[rand_poz]
    for numer_karty, karta in enumerate(karty):
        karta.numer = numer_karty + 1  # aby odpowiednio się wyświetlało dla gracza - bardziej czytelne

    return karty


def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def zgaduj():
    """
    zadaj pytanie                                   #print - trzeba wylosować nieodkrytą kartę
    dopóki nie zgadnięta karta:                     #while - zapisywać strzał gracza
        jeśli odp dobra to odkryj karte             #if -
        jeśli odp zła wróć do początku              #else - print "spróbuj jeszcze raz" --> continue
    :return: 
    """
    pass



def gra():
    """Funkcja przeprowadzająca grę."""
    karty = mieszaj_karty(KARTY)
    wyswietl_karty(karty)

    sleep(5)

    clear()

    for karta in karty:
        karta.czy_odkryta = False

    wyswietl_karty(karty)

    sleep(5)




gra()
