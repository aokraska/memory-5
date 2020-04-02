

karty = ["Dżaga", "Gandzia", "Zadra",
         "Ciri", "Bazia", "Florka",
         "Forest", "Tola", "Coco"]


def wyswietl_karty(karty):
    for row in range(3):
        for element in range(3):
            numer_karty = 3*row + element
            print(karty[numer_karty], end=" ")
        print("\n")




wyswietl_karty(karty)