class Uczen:
    def __init__(self, nazwisko_ucznia, imie_ucznia, nazwa_klasy, lekcja, kolejna_lekcja, uczniowie):
        self.nazwisko_ucznia = nazwisko_ucznia
        self.imie_ucznia = imie_ucznia
        self.nazwa_klasy = nazwa_klasy
        self.lekcja = lekcja
        self.kolejna_lekcja = kolejna_lekcja
        self.uczniowie = uczniowie

    def dodawanie_ucznia_do_listy (self):
        nazwisko_ucznia = input("Podaj nazwisko ucznia:   ")
        imie_ucznia = input("Podaj imie ucznia:   ")
        nazwa_klasy = input("Podaj nazwe klasy:   ")
        lista_klas[nazwa_klasy] = {"uczniowie": nazwisko_ucznia + " " + imie_ucznia + ", "}
        if nazwa_klasy in lista_klas:
            lista_klas[nazwa_klasy]["uczniowie"] += nazwisko_ucznia + " " + imie_ucznia + ", "
        lekcja = input("Podaj nazwe lekcji ucznia:   ")
        lista_uczniow[nazwisko_ucznia] = {"imie": imie_ucznia, "nazwa_klasy": nazwa_klasy, "lekcje_ucznia":lekcja}
        while True:
            zapytanie_1 = input("Czy chcesz dodac kolejne lekcje? t/n:  ")
            if zapytanie_1 == "t":
                kolejna_lekcja = ", " + input("Podaj nazwe lekcji ucznia:   ")
                lista_uczniow[nazwisko_ucznia]["lekcje_ucznia"] += kolejna_lekcja
                continue
            else:
                break



class Nauczyciel:
    def __init__(self, nazwisko_nauczyciela, imie_nauczyciela, przedmiot, nazwa_klasy):
        self.nazwisko_nauczyciela = nazwisko_nauczyciela
        self.imie_nauczyciela = imie_nauczyciela
        self.przedmiot = przedmiot
        self.nazwa_klasy = nazwa_klasy

    def dodawanie_nauczyciela_do_listy (self):
        nazwisko_nauczyciela = input("Podaj nazwisko nauczyciela:   ")
        imie_nauczyciela = input("Podaj imie nauczyciela:    ")
        przedmiot = input("Podaj przedmiot, którego nauczyciel uczy:    ")
        nazwa_klasy = input("Podaj nazwę klasy, którą prowadzi nauczyciel:    ")
        lista_nauczycieli[nazwisko_nauczyciela] = {"imie": imie_nauczyciela, "przedmiot": przedmiot, "nazwa_klasy": nazwa_klasy}

class Wychowawca:
    def __init__(self, nazwisko_wychowawcy, imie_wychowawcy, nazwa_klasy):
        self.nazwisko_wychowawcy = nazwisko_wychowawcy
        self.imie_wychowawcy = imie_wychowawcy
        self.nazwa_klasy = nazwa_klasy

    def dodawanie_wychowawcy_do_listy(self):
        nazwisko_wychowawcy = input("Podaj nazwisko wychowawcy:   ").strip()
        imie_wychowawcy = input("Podaj imie wychowawcy:    ").strip()
        nazwa_klasy = input("Podaj nazwę klasy, którą prowadzi wychowawca:    ").strip()
        lista_wychowawcow[nazwisko_wychowawcy] = {"imie": imie_wychowawcy, "nazwa_klasy": nazwa_klasy}



"""trzeba stworzyc w tej klasie finkcje do wyszukiwania danych z innych klas, np A1 in Lista_uczniow"""
# class Klasa:
#     def __init__(self, nazwa_klasy, nazwisko_wychowawcy, imie_wychowawcy):
#         self.nazwa_klasy = nazwa_klasy
#         self.nazwisko_wychowawcy = nazwisko_wychowawcy
#         self.imie_wychowawcy = imie_wychowawcy
#     def wyszukiwanie_informacji_o_klasie (self):
#         nazwa_klasy = input("Wpisz nazwe szukanej klasy:  ")
#         if nazwa_klasy in lista_wychowawcow[nazwa_klasy].values:
#             print("znalazles")
#             print("Wychowawca klasy to {} {}".format(lista_wychowawcow[nazwisko_wychowawcy][imie_wychowawcy]))


lista_uczniow = dict()
lista_nauczycieli = dict()
lista_wychowawcow = dict()
lista_klas = dict()


nowy_uczen = Uczen("nazwisko_ucznia", "imie_ucznia", "nazwa_klasy", "lekcja", "kolejna_lekcja", "uczniowie")
nowy_uczen.dodawanie_ucznia_do_listy()

nowy_nauczyciel = Nauczyciel("nazwisko_nauczyciela", "imie_nauczyciela", "przedmiot", "nazwa_klasy")
nowy_nauczyciel.dodawanie_nauczyciela_do_listy()

nowy_wychowawca = Wychowawca("nazwisko_wychowawcy", "imie_wychowawcy", "nazwa_klasy")
nowy_wychowawca.dodawanie_wychowawcy_do_listy()



print(lista_uczniow)
print(lista_nauczycieli)
print(lista_wychowawcow)
print(lista_klas)

while True:
    szukana_klasa = input("Wpisz nazwe szukanej klasy:").strip()
    if szukana_klasa in lista_wychowawcow:
        print("znalazles")
    else:
        print("nie znalazles")
        continue
