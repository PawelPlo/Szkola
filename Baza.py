class Uczen:
    def __init__(self, nazwa_klasy):
        self.nazwa_klasy = nazwa_klasy

    def wpisywanie_imienia_i_nazwiska(self, imie, nazwisko):
        imie = input("Podaj imie:   ").strip()
        imie = imie.lower().capitalize()
        nazwisko = input("Podaj nazwisko:   ").strip()
        nazwisko = nazwisko.lower().capitalize()
        imie_i_nazwisko = imie + " " + nazwisko
        return imie_i_nazwisko
class Nauczyciel:
    def __init__(self, nazwa_klasy, przedmiot):
        self.nazwa_klasy = nazwa_klasy
        self.przedmiot = przedmiot
class Wychowawca:
    def __init__(self, nazwa_klasy):
        self.nazwa_klasy = nazwa_klasy

uczniowie = []
nauczyciele = []
wychowawcy = []


nazwa_klasy = input("Podaj nazwę klasy:  ")
nowy_uczen = Uczen(nazwa_klasy)
nowy_uczen.wpisywanie_imienia_i_nazwiska()
uczniowie.append(wpisywanie_imienia_i_nazwiska())
