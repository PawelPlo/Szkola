class Uczen:
    def __init__(self, nazwisko_ucznia, imie_ucznia, nazwa_klasy, lekcje):
        self.nazwisko_ucznia = nazwisko_ucznia
        self.imie_ucznia = imie_ucznia
        self.nazwa_klasy = nazwa_klasy
        self.lekcje = lekcje

    def dodawanie_ucznia_do_listy (self):
        nazwisko_ucznia = input("Podaj nazwisko ucznia:   ")
        imie_ucznia = input("Podaj imie ucznia:   ")
        nazwa_klasy = input("Podaj nazwe klasy:   ")
        lekcje = input("Podaj nazwe lekcji ucznia:   ")
        lista_uczniow[nazwisko_ucznia] = {"imie": imie_ucznia, "nazwa_klasy": nazwa_klasy, "lekcje": lekcje}


class Nauczyciel:
    def __init__(self, nazwisko_nauczyciela, imie_nauczyciela, przedmiot):
        self.nazwisko_nauczyciela = nazwisko_nauczyciela
        self.imie_nauczyciela = imie_nauczyciela
        self.przedmiot = przedmiot

    def dodawanie_nauczyciela_do_listy (self):
        nazwisko_nauczyciela = input("Podaj nazwisko nauczyciela:   ")
        imie_nauczyciela = input("Podaj imie nauczyciela:    ")
        przedmiot = input("Podaj przedmiot, którego nauczyciel uczy:    ")
        lista_nauczycieli[nazwisko_nauczyciela] = {"imie": imie_nauczyciela, "przedmiot": przedmiot}

class Wychowawca:
    def __init__(self, nazwisko_wychowawcy, imie_wychowawcy, nazwa_klasy):
        self.nazwisko_wychowawcy = nazwisko_wychowawcy
        self.imie_wychowawcy = imie_wychowawcy
        self.nazwa_klasy = nazwa_klasy

    def dodawanie_wychowawcy_do_listy(self):
        nazwisko_wychowawcy = input("Podaj nazwisko wychowawcy:   ")
        imie_wychowawcy = input("Podaj imie wychowawcy:    ")
        nazwa_klasy = input("Podaj nazwę klasy, którą prowadzi wychowawca:    ")
        lista_wychowawcow[nazwisko_wychowawcy] = {"imie": imie_wychowawcy, "nazwa_klasy": nazwa_klasy}

class Klasa:
    def __init__(self):
        pass

lista_uczniow = dict()
lista_nauczycieli = dict()
lista_wychowawcow = dict()
# lista_klas = ["1A", "1B", "2A", "2B", "3A", "3C", "4A", "4B"]

nowy_uczen = Uczen("nazwisko_ucznia", "imie_ucznia", "nazwa_klasy", "lekcje")
nowy_uczen.dodawanie_ucznia_do_listy()

nowy_nauczyciel = Nauczyciel("nazwisko_nauczyciela", "imie_nauczyciela", "przedmiot")
nowy_nauczyciel.dodawanie_nauczyciela_do_listy()

nowy_wychowawca = Wychowawca("nazwisko_wychowawcy", "imie_wychowawcy", "nazwa_klasy")
nowy_wychowawca.dodawanie_wychowawcy_do_listy()

print(lista_uczniow)
print(lista_nauczycieli)
print(lista_wychowawcow)

while True:
    pass