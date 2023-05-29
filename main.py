numery_klas = ["1A", "1B", "2A", "2B", "3A", "3B", "4A", "4B"]
class Uczen:
    def __init__(self, imie_i_nazwisko, nazwa_klasy):
        self.imie_i_nazwisko = imie_i_nazwisko
        self.nazwa_klasy = nazwa_klasy

    # def wyszukiwanie_klasy_ucznia(self):
    #     imie = input("Podaj imie ucznia:   ")
    #     nazwisko = input("Podaj nazwisko ucznia:   ")
    #     imie_i_nazwisko = imie + " " + nazwisko
    #     if imie_i_nazwisko in lista_uczniow:
    #         print("znalzlem")

class Nauczyciel:
    def __init__(self, imie_i_nazwisko, nazwa_klasy, przedmiot):
        self.imie_i_nazwisko = imie_i_nazwisko
        self.nazwa_klasy = nazwa_klasy
        self.przedmiot = przedmiot

    # def dodawanie_nauczyciela_do_listy(self):
    #     imie = input("Podaj imie nauczyciela:   ")
    #     nazwisko = input("Podaj nazwisko nauczyciela:   ")
    #     imie_i_nazwisko = imie + " " + nazwisko
    #     przedmiot = input("Podaj nazwe przedmiotu nauczanego przez nauczyciela:   ")
    #     nazwa_klasy = input("Podaj nazwe klasy:   ")
    #     nazwa_klasy = nazwa_klasy.capitalize()
    #     if nazwa_klasy in lista_klas:
    #         lista_nauczycieli[nazwa_klasy] += {imie_i_nazwisko, przedmiot}

class Wychowawca:
    def __init__(self, imie_i_nazwisko, nazwa_klasy):
        self.imie_i_nazwisko = imie_i_nazwisko
        self.nazwa_klasy = nazwa_klasy

    # def dodawanie_wychowawcy_do_listy(self):
    #     imie = input("Podaj imie wychowawcy:   ")
    #     nazwisko = input("Podaj nazwisko wychowawcy:   ")
    #     imie_i_nazwisko = imie + " " + nazwisko
    #     nazwa_klasy = input("Podaj nazwe klasy:   ")
    #     nazwa_klasy = nazwa_klasy.capitalize()
    #     if nazwa_klasy in lista_klas:
    #         lista_wychowawcow[nazwa_klasy].append(imie_i_nazwisko)

"""tu dodajemy pary 'uczen - nazwa klasy"""
lista_uczniow = dict()

"""do poszcegolnych klas dodajemy uczniów"""
lista_klas = {
    '1A':  [],
    '1B':  [],
    '2A':  [],
    '2B':  [],
    '3A':  [],
    '3B':  [],
    '4A':  [],
    '4B':  []
}
"""do słowników klas dodajemy pary 'nauczyciel - przedmiot'"""
lista_nauczycieli = {
    '1A': dict(),
    '1B': dict(),
    '2A': dict(),
    '2B': dict(),
    '3A': dict(),
    '3B': dict(),
    '4A': dict(),
    '4B': dict()
}
"""tutaj dodajemu poszczegolnych nauczycieli i ich klasy"""
klasy_nauczycieli = dict()

"""do poszczegolnych klas dodajemy wychowawców klas"""
lista_wychowawcow = {
    '1A':  [],
    '1B':  [],
    '2A':  [],
    '2B':  [],
    '3A':  [],
    '3B':  [],
    '4A':  [],
    '4B':  []
}
"""tutaj dodajemy pary wychowawca - klasa"""

klasa_wychowawcy = dict()


while True:
    print("""Wpisywanie danych - 1
Wysietlanie tabel - 2
Koniec - 3\n\n""")
    wybor_1 = input("Wpisz cyfre wyboru:  \n")

    if wybor_1 == "1":
        print("""Wpisz ucznia - 1
Wpisz nauczyciela - 2
Wpisz wychowawce - 3
Powrot do głównego menu - q\n\n""")

        wybor_1_1 = input("Twoj wybor:   \n")
        if wybor_1_1 == "1":
            imie = input("Podaj imie ucznia:   ")
            nazwisko = input("Podaj nazwisko ucznia:   ")
            imie_i_nazwisko = imie + " " + nazwisko
            nazwa_klasy = input("Podaj nazwe klasy:   ")
            nowy_uczen = Uczen(imie_i_nazwisko=imie_i_nazwisko, nazwa_klasy=nazwa_klasy)
            #if nazwa_klasy in lista_klas:
            lista_klas[nazwa_klasy].append(imie_i_nazwisko)
            lista_uczniow[imie_i_nazwisko] = nazwa_klasy
            continue
        if wybor_1_1 == "2":
            imie = input("Podaj imie nauczyciela:   ")
            nazwisko = input("Podaj nazwisko nauczyciela:   ")
            imie_i_nazwisko = imie + " " + nazwisko
            przedmiot = input("Podaj nazwe przedmiotu nauczanego przez nauczyciela:   ")
            nazwa_klasy = input("Podaj nazwe klasy:   ")
            nowy_nauczyciel = Nauczyciel(imie_i_nazwisko=imie_i_nazwisko, nazwa_klasy=nazwa_klasy, przedmiot=przedmiot)
            #if nazwa_klasy in lista_klas:
            lista_nauczycieli[nazwa_klasy][imie_i_nazwisko] = przedmiot
            klasy_nauczycieli[imie_i_nazwisko] = nazwa_klasy
            print(lista_nauczycieli)
            continue
        if wybor_1_1 == "3":
            imie = input("Podaj imie wychowawcy:   ")
            nazwisko = input("Podaj nazwisko wychowawcy:   ")
            imie_i_nazwisko = imie + " " + nazwisko
            nazwa_klasy = input("Podaj nazwe klasy:   ")
            nowy_wychowawca = Wychowawca(imie_i_nazwisko=imie_i_nazwisko, nazwa_klasy=nazwa_klasy)
            #if nazwa_klasy in lista_klas:
            lista_wychowawcow[nazwa_klasy].append(imie_i_nazwisko)
            klasa_wychowawcy[imie_i_nazwisko] = nazwa_klasy
            continue
        if wybor_1_1 == "q":
            break
            wybor_1 = input("Wpisz cyfre wyboru:  ")

    if wybor_1 == "2":
        print("""Dane o klasach - 1
Dane o uczniu - 2
Dane o nauczycielu - 3
Dane o wychowawcy - 4
Powrot do głównego menu - q\n\n""")

        wybor_1_2 = input("Wpisz, które dane chcesz wyswietlic:   \n")
        if wybor_1_2 == "1":
            nazwa_klasy = input("Wpisz klase:   ")
            print(lista_klas[nazwa_klasy])
            print("Wychowawca:{}".format( lista_wychowawcow[nazwa_klasy]))
            continue
        if wybor_1_2 == "2":
            imie = input("Podaj imie ucznia:   ")
            nazwisko = input("Podaj nazwisko ucznia:   ")
            imie_i_nazwisko = imie + " " + nazwisko
            nazwa_szukanej_klasy = lista_uczniow[imie_i_nazwisko]
            print(lista_nauczycieli[nazwa_szukanej_klasy])
            continue
        if wybor_1_2 == "3":
            imie = input("Podaj imie nauczyciela:   ")
            nazwisko = input("Podaj nazwisko nauczyciela:   ")
            imie_i_nazwisko = imie + " " + nazwisko
            szukany_nauczyciel = klasy_nauczycieli[imie_i_nazwisko]
            print(szukany_nauczyciel)
            continue
        if wybor_1_2 == "4":
            imie = input("Podaj imie wychowawcy:   ")
            nazwisko = input("Podaj nazwisko wychowawcy:   ")
            imie_i_nazwisko = imie + " " + nazwisko
            szukana_klasa = klasa_wychowawcy[imie_i_nazwisko]
            print(lista_klas[szukana_klasa])
            continue
        if wybor_1_2 == "q":
            break
            wybor_1 = input("Wpisz cyfre wyboru:  ")

    if wybor_1 == "3":
        break