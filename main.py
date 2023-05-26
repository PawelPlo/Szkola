class Uczen:
    def __init__(self, imie_ucznia, nazwisko_ucznia, nazwa_klasy, lekcje):
        self.nazwisko_ucznia = nazwisko_ucznia
        self.imie_ucznia = imie_ucznia
        self.nazwa_klasy = nazwa_klasy
        self.lekcje = lekcje

    def dodawanie_ucznia_do_listy (self):
        nazwisko_ucznia = input("Podaj nazwisko ucznia:   ")
        imie_ucznia = input("Podaj imie ucznia:   ")
        nazwa_klasy = input("Podaj nazwe klasy:   ")
        lekcje = input("Podaj nazwe lekcji ucznia:   ")
        print(nazwisko_ucznia, imie_ucznia, nazwa_klasy, lekcje)
        lista_uczniow[nazwisko_ucznia] = {"imie": imie_ucznia, "nazwa_klasy": nazwa_klasy, "lekcje": lekcje}

class Nauczyciel:
    def __init__(self):
        pass
class Wychowawca:
    def __init__(self):
        pass
class Klasa:
    def __init__(self):
        pass

lista_uczniow = dict()

# lista_nauczycieli = [{"imie": "Zbigniew", "nazwisko": "Wisniewski", "lekcje": "matematyka"}]
# lista_wychowawcow = [{"imie": "Ryszard", "nazwisko": "Pawlak", "nazwa_klasy": "1C"}]
# lista_klas = ["1A", "1B", "2A", "2B", "3A", "3C", "4A", "4B"]

nowy_uczen = Uczen("nazwisko_ucznia", "imie_ucznia", "nazwa_klasy", "lekcje")

nowy_uczen.dodawanie_ucznia_do_listy()


print(lista_uczniow)

while True:
    pass