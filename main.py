
# class Uczen:
#     def __init__(self, imie, nazwisko, imie_i_nazwisko, nazwa_klasy):
#         self.imie = imie
#         self.nazwisko = nazwisko
#         self.imie_i_nazwisko = imie_i_nazwisko
#         self.nazwa_klasy = nazwa_klasy
#
# class Nauczyciel:
#     def __init__(self, imie_i_nazwisko, nazwa_klasy, przedmiot):
#         self.imie_i_nazwisko = imie_i_nazwisko
#         self.nazwa_klasy = nazwa_klasy
#         self.przedmiot = przedmiot
#
# class Wychowawca:
#     def __init__(self, imie_i_nazwisko, nazwa_klasy):
#         self.imie_i_nazwisko = imie_i_nazwisko
#         self.nazwa_klasy = nazwa_klasy

numery_klas = ["1a", "1b", "2a", "2b", "3a", "3b", "4a", "4b"]
"""tu dodajemy pary 'uczen - nazwa klasy, lista potrzebna do znalezienia nazwy klasy, w której uczy się konkretny uczen
i dalej do wykorzystania do wygenerowania danych z 'listy nauczycieli (lekcje, nauczyciel)' w informacjach o uczniu"""
lista_uczniow = dict()

"""do poszcegolnych klas dodajemy uczniów - dane wykorzystywane do odczytu danych o klasie (uczniowie, wychowawca)"""
lista_klas = {
    '1a':  [],
    '1b':  [],
    '2a':  [],
    '2b':  [],
    '3a':  [],
    '3b':  [],
    '4a':  [],
    '4b':  []
}
"""do słowników klas dodajemy pary 'nauczyciel - przedmiot' - w wyświetlenie informacjach o uczniu (lekcje, nauczyciel"""
lista_nauczycieli = {
    '1a': dict(),
    '1b': dict(),
    '2a': dict(),
    '2b': dict(),
    '3a': dict(),
    '3b': dict(),
    '4a': dict(),
    '4b': dict()
}
"""tutaj dodajemu poszczegolnych nauczycieli i ich klasy - 
lista potrzebna do wygenerowania danych o nauczycielu (klasy, które prowadzi)"""
klasy_nauczycieli = dict()

"""do poszczegolnych klas dodajemy wychowawców klas  - dane potrzebne do informacji o klasie (jej wychowawca)"""
lista_wychowawcow = {
    '1a':  [],
    '1b':  [],
    '2a':  [],
    '2b':  [],
    '3a':  [],
    '3b':  [],
    '4a':  [],
    '4b':  []
}
"""tutaj dodajemy pary wychowawca - klasa, słownik potrzebny do wyszukania nazwy klasy prowadzonej przez wychowawcę, 
i dalej do wyszukania listy klas uczniów, ktrych wychowawca prowadzi"""
klasa_wychowawcy = dict()

"""lista do wpisywania nauczycieli, do kontroli czy taki istnieje, nie działa funkcja in na lisie "lista nauczycieli"""

nauczyciele = []
def wpisywanie_imienia_i_nazwiska():
    imie = input("Podaj imie:   ").strip()
    imie = imie.lower().capitalize()
    nazwisko = input("Podaj nazwisko:   ").strip()
    nazwisko = nazwisko.lower().capitalize()
    imie_i_nazwisko = imie + " " + nazwisko
    return imie_i_nazwisko

while True:
    print("""\n\nBAZA SZKOLNA\n
Wpisywanie danych - wpisz: 1
Wyświetlanie danych - wpisz: 2
Koniec - wpisz: 3\n\n""")
    wybor_1 = input("\n")

    if wybor_1 == "1":
        while True:
            print("""\nWPISYWANIE DANYCH\n
Uczeń - wpisz: 1
Nauczyciel - wpisz: 2
Wychowawca - wpisz: 3
Powrot do głównego menu - wpisz: q\n\n""")

            wybor_1_1 = input("\n")
            wybor_1_1 = wybor_1_1.lower()
            if wybor_1_1 == "1":
                print("Wpisz dane dotyczące ucznia\n")
                imie_i_nazwisko = wpisywanie_imienia_i_nazwiska()
                while True:
                    nazwa_klasy = input("Podaj nazwę klasy:   ").strip()
                    nazwa_klasy = nazwa_klasy.lower()
                    if nazwa_klasy not in numery_klas:
                        print("Nie ma takiej klasy! Wpisz inną klasę")
                        continue
                    else:
                        lista_klas[nazwa_klasy].append(imie_i_nazwisko)
                        lista_uczniow[imie_i_nazwisko] = nazwa_klasy
                        break
            if wybor_1_1 == "2":
                print("Wpisz dane nauczyciela\n")
                imie_i_nazwisko = wpisywanie_imienia_i_nazwiska()
                przedmiot = input("Podaj nazwe przedmiotu nauczanego przez nauczyciela:   ")
                wpisane_klasy = []
                while True:
                    print("""\nPodaj nazwy klas, w których uczy nauczyciel.
Numery klas to: 1a, 1b, 2a, 2b, 3a, 3b, 4a, 4b
Jeśli chcesz skończyć - wpisz: Q""")
                    nazwa_klasy = input().strip()
                    nazwa_klasy = nazwa_klasy.lower()
                    if nazwa_klasy == "q":
                        break
                    if nazwa_klasy not in numery_klas:
                        print("Nie ma takiej klasy! Wpisz inną klasę")
                        continue
                    else:
                        klasy_nauczycieli[imie_i_nazwisko] = nazwa_klasy
                        lista_nauczycieli[nazwa_klasy][imie_i_nazwisko] = przedmiot
                        wpisane_klasy.append(nazwa_klasy)
                        nauczyciele.append(imie_i_nazwisko)
                        break
                licznik = 0
                licznik = int(licznik)
                while licznik <= 6:
                    nazwa_klasy = input().strip()
                    nazwa_klasy = nazwa_klasy.lower()
                    if nazwa_klasy == "q":
                        break
                    if nazwa_klasy not in numery_klas:
                        print("Nie ma takiej klasy! Wpisz inną klasę!")
                        continue
                    if nazwa_klasy in wpisane_klasy:
                        print("Klasa została już wpisana! Wpisz inną klasę!")
                        continue
                    klasy_nauczycieli[imie_i_nazwisko] += nazwa_klasy
                    lista_nauczycieli[nazwa_klasy][imie_i_nazwisko] = przedmiot
                    licznik += 1
                    continue
            if wybor_1_1 == "3":
                print("Wpisz dane wychowawcy\n")
                imie_i_nazwisko = wpisywanie_imienia_i_nazwiska()
                while True:
                    nazwa_klasy = input("Podaj nazwę klasy, prowdzonej przez wychowawcę:   ").strip()
                    nazwa_klasy = nazwa_klasy.lower()
                    if nazwa_klasy not in numery_klas:
                        print("Nie ma takiej klasy! Wpisz inną klasę")
                        continue
                    else:
                        lista_wychowawcow[nazwa_klasy].append(imie_i_nazwisko)
                        break
                klasa_wychowawcy[imie_i_nazwisko] = nazwa_klasy
                continue
            if wybor_1_1 == "q":
                break

    if wybor_1 == "2":
        while True:
            print("""\n\nWyszukaj dane o klasie - wpisz: 1
Wyszukaj dane o uczniu - wpisz: 2
Wyszukaj dane o nauczycielu - wpisz: 3
Wyszukaj dane o wychowawcy - wpisz: 4
Powrot do głównego menu - wpisz: q\n\n""")

            wybor_1_2 = input("\n")
            wybor_1_2 = wybor_1_2.lower()
            if wybor_1_2 == "1":
                nazwa_klasy = input("Wpisz klase:   ")
                print("Uczniowie klasy {}: {}".format(nazwa_klasy,lista_klas[nazwa_klasy]))
                print("Wychowawca:{}".format( lista_wychowawcow[nazwa_klasy]))
                continue
            if wybor_1_2 == "2":
                print("Podaj dane ucznia")
                imie_i_nazwisko = wpisywanie_imienia_i_nazwiska()
                nazwa_szukanej_klasy = lista_uczniow[imie_i_nazwisko]
                print(lista_nauczycieli[nazwa_szukanej_klasy])
                continue
            if wybor_1_2 == "3":
                while True:
                    print("Podaj dane nauczyciela.")
                    imie_i_nazwisko = wpisywanie_imienia_i_nazwiska()
                    if imie_i_nazwisko not in nauczyciele:
                        print("\nNie ma takiego nauczyciela! Spróbuj jeszcze raz.\n")
                        break
                    else:
                        szukany_nauczyciel = klasy_nauczycieli[imie_i_nazwisko]
                        print(szukany_nauczyciel)
                        break
            if wybor_1_2 == "4":
                while True:
                    print("Podaj dane wychowawcy")
                    imie_i_nazwisko = wpisywanie_imienia_i_nazwiska()
                    if imie_i_nazwisko not in klasa_wychowawcy:
                        print("\nNie ma takiego wychowawcy! Spróbuj jeszcze raz.\n")
                        break
                    else:
                        szukana_klasa = klasa_wychowawcy[imie_i_nazwisko]
                        print("""\nWychowawca: {}
Klasa: {}
Uczniowie: {}\n""".format(imie_i_nazwisko, szukana_klasa, lista_klas[szukana_klasa]))
                        break
            if wybor_1_2 == "q":
                break
    if wybor_1 == "3":
        break