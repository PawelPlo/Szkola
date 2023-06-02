class Uczen:
    def __init__(self, imie_i_nazwisko, nazwa_klasy):
        self.imie_i_nazwisko = imie_i_nazwisko
        self.nazwa_klasy = nazwa_klasy

    def __str__(self):
        return f"Uczen: {self.imie_i_nazwisko} // Klasa: {self.nazwa_klasy}"

class Nauczyciel:
    def __init__(self, imie_i_nazwisko, nazwa_klasy, przedmiot):
        self.imie_i_nazwisko = imie_i_nazwisko
        self.nazwa_klasy = nazwa_klasy
        self.przedmiot = przedmiot
    def __str__(self):
        return f"""Nauczyciel: {self.imie_i_nazwisko} // Przedmiot: {self.przedmiot}
// Klasa: {self.nazwa_klasy} // """
class Wychowawca:
    def __init__(self, imie_i_nazwisko, nazwa_klasy):
        self.imie_i_nazwisko = imie_i_nazwisko
        self.nazwa_klasy = nazwa_klasy
    def __str__(self):
        return f"Wychowawca: {self.imie_i_nazwisko} // Prowadzona klasa: {self.nazwa_klasy}"

def wyszukiwanie_wychowawcy(nazwa_klasy):
    return nazwa_klasy.imie_i_nazwisko
def wyszukiwanie_uczniow_klasy(nazwa_klasy):
    return nazwa_klasy.imie_i_nazwisko
def wpisywanie_imienia_i_nazwiska ():
    imie = input("Podaj imie:   ").strip()
    imie = imie.lower().capitalize()
    nazwisko = input("Podaj nazwisko:   ").strip()
    nazwisko = nazwisko.lower().capitalize()
    imie_i_nazwisko = imie + " " + nazwisko
    return (imie_i_nazwisko)
def wyszukiwanie_informacji_o_uczniu (imie_i_nazwisko):
    return imie_i_nazwisko.nazwa_klasy
    return nazwa_klasy.imie_i_nazwisko, przedmiot

uczniowie = []
nauczyciele = []
wychowawcy = []
numery_klas = ["1a", "1b", "2a", "2b", "3a", "3b", "4a", "4b"]

while True:
    print("""\n\n -----------BAZA SZKOLNA ------------\n
Wpisywanie danych - wpisz: 1
Wyświetlanie danych - wpisz: 2
Koniec - wpisz: 3\n\n""")
    wybor_1 = input("\n")

    if wybor_1 == "1":
        while True:
            print("""\n------------- WPISYWANIE DANYCH ------------\n
Uczeń - wpisz: 1
Nauczyciel - wpisz: 2
Wychowawca - wpisz: 3
Powrot do głównego menu - wpisz: q\n\n""")

            wybor_1_1 = input("\n")
            wybor_1_1 = wybor_1_1.lower()
            if wybor_1_1 == "1":
                while True:
                    print("Wpisz dane dotyczące ucznia\n")
                    imie = input("Podaj imie:   ").strip()
                    imie = imie.lower().capitalize()
                    nazwisko = input("Podaj nazwisko:   ").strip()
                    nazwisko = nazwisko.lower().capitalize()
                    imie_i_nazwisko = imie + " " + nazwisko
                    if imie_i_nazwisko in uczniowie:
                        print("Uczeń o takim imieniu i nazwisku jest już w bazie szkolnej! Spróbuj ponownie!")
                        continue
                    else:
                        nazwa_klasy = input("Podaj nazwę klasy:  ")
                        nazwa_klasy = nazwa_klasy.lower()
                        if nazwa_klasy not in numery_klas:
                            print("Nie ma takiej klasy! Wpisz inną klasę")
                            continue
                        else:
                            nowy_uczen = Uczen(imie_i_nazwisko=imie_i_nazwisko, nazwa_klasy=nazwa_klasy)
                            uczniowie.append(nowy_uczen)
                            break
            if wybor_1_1 == "2":
                while True:
                    print("Wpisz dane nauczyciela\n")
                    imie = input("Podaj imie:   ").strip()
                    imie = imie.lower().capitalize()
                    nazwisko = input("Podaj nazwisko:   ").strip()
                    nazwisko = nazwisko.lower().capitalize()
                    imie_i_nazwisko = imie + " " + nazwisko
                    if imie_i_nazwisko in nauczyciele:
                        print("Nauczyciel o takim imieniu i nazwisku jest już w bazie szkolnej! Spróbuj ponownie!")
                        continue
                    else:
                        wpisane_klasy = []
                        print("""\nPodaj nazwy klas, w których uczy nauczyciel.
Numery klas to: 1a, 1b, 2a, 2b, 3a, 3b, 4a, 4b
Jeśli chcesz skończyć - wpisz: Q""")
                        nazwa_klasy = input().strip()
                        nazwa_klasy = nazwa_klasy.lower()
                        if nazwa_klasy == "q":
                            break
                        if nazwa_klasy in wpisane_klasy:
                            print("Ta klasa została już wpisana! Wpisz inną klasę!")
                            continue
                        if nazwa_klasy not in numery_klas:
                            print("Nie ma takiej klasy! Wpisz inną klasę")
                            continue
                        else:
                            wpisane_klasy.append(nazwa_klasy)
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
                                    print("Ta klasa została już wpisana! Wpisz inną klasę!")
                                    continue
                                else:
                                    licznik += 1
                                    wpisane_klasy.append(nazwa_klasy)
                                    continue
                            przedmiot = input("Podaj nazwe przedmiotu nauczanego przez nauczyciela:   ")
                            nowy_nauczyciel = Nauczyciel(imie_i_nazwisko=imie_i_nazwisko, nazwa_klasy=wpisane_klasy, przedmiot=przedmiot)
                            nauczyciele.append(nowy_nauczyciel)
                            break
            if wybor_1_1 == "3":
                print("Wpisz dane wychowawcy\n")
                imie = input("Podaj imie:   ").strip()
                imie = imie.lower().capitalize()
                nazwisko = input("Podaj nazwisko:   ").strip()
                nazwisko = nazwisko.lower().capitalize()
                imie_i_nazwisko = imie + " " + nazwisko
                if imie_i_nazwisko in wychowawcy:
                    print("Wychowawca o takim imieniu i nazwisku jest już w bazie szkolnej! Spróbuj ponownie!")
                    continue
                else:
                    nazwa_klasy = input("Podaj nazwę klasy:  ")
                    nazwa_klasy = nazwa_klasy.lower()
                    if nazwa_klasy not in numery_klas:
                        print("Nie ma takiej klasy! Wpisz inną klasę")
                        continue
                    else:
                        nowy_wychowawca = Wychowawca(imie_i_nazwisko=imie_i_nazwisko, nazwa_klasy=nazwa_klasy)
                        wychowawcy.append(nowy_wychowawca)
                        break
            if wybor_1_1 == "q":
                break
    if wybor_1 == "2":
        while True:
            print("""\n\n--------- WYSZUKIWANIE DANYCH -----------
Wyszukaj dane o klasie - wpisz: 1
Wyszukaj dane o uczniu - wpisz: 2
Wyszukaj dane o nauczycielu - wpisz: 3
Wyszukaj dane o wychowawcy - wpisz: 4
Powrot do głównego menu - wpisz: q\n\n""")

            wybor_1_2 = input("\n")
            wybor_1_2 = wybor_1_2.lower()
            if wybor_1_2 == "1":
                while True:
                    szukana_klasa = input("Wpisz klase:   \n\n")
                    if szukana_klasa not in numery_klas:
                        print("Nie ma takiej klasy! Spróbuj jeszcze raz.")
                        continue
                    else:
                        for prowadzacy in wychowawcy:
                            if prowadzacy.nazwa_klasy == szukana_klasa:
                                print(f"""Klasa {szukana_klasa}:,
Wychowawca: {prowadzacy.imie_i_nazwisko}""")
                        print("Uczniowie:")
                        for dzieci in uczniowie:
                            if dzieci.nazwa_klasy == szukana_klasa:
                                print(dzieci.imie_i_nazwisko)
                        break
            if wybor_1_2 == "2":
                print("Podaj dane ucznia")
                imie_i_nazwisko = wpisywanie_imienia_i_nazwiska()
                print(wyszukiwanie_informacji_o_uczniu(imie_i_nazwisko))
                break
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
            else:
                print("Wybrałeś złą opcję! Spróbuj raz jeszcze.")
                continue
    if wybor_1 == "3":
        break
    else:
        print("Wybrałeś złą opcję! Spróbuj raz jeszcze.")
        continue