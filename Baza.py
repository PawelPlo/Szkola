class Uczen:
    def __init__(self, imie_i_nazwisko, nazwa_klasy):
        self.imie_i_nazwisko = imie_i_nazwisko
        self.nazwa_klasy = nazwa_klasy

    def __str__(self):
        return f"Uczen: {self.imie_i_nazwisko} // Klasa: {self.nazwa_klasy}"

class Nauczyciel:
    def __init__(self, imie_i_nazwisko, przedmiot, nazwa_klasy):
        self.imie_i_nazwisko = imie_i_nazwisko
        self.przedmiot = przedmiot
        self.nazwa_klasy = nazwa_klasy

    def __str__(self):
        return f"Przedmiot: {self.przedmiot} || Nauczyciel: {self.imie_i_nazwisko}"


class Wychowawca:
    def __init__(self, imie_i_nazwisko, nazwa_klasy):
        self.imie_i_nazwisko = imie_i_nazwisko
        self.nazwa_klasy = nazwa_klasy
    def __str__(self):
        return f"Wychowawca: {self.imie_i_nazwisko} // Prowadzona klasa: {self.nazwa_klasy}"


def wpisywanie_imienia_i_nazwiska ():
    imie = input("Podaj imie:   ").strip()
    imie = imie.lower().capitalize()
    nazwisko = input("Podaj nazwisko:   ").strip()
    nazwisko = nazwisko.lower().capitalize()
    imie_i_nazwisko = imie + " " + nazwisko
    return (imie_i_nazwisko)


uczniowie = []
imienna_lista_uczniow = []
nauczyciele = []
imienna_lista_nauczycieli = []
wychowawcy = []
imienna_lista_wychowawcow = []
numery_klas = []

while True:
    print("""\n\n -----------BAZA SZKOLNA ------------\n
Wpisywanie danych - wpisz: 1
Wyświetlanie danych - wpisz: 2
Koniec - wpisz: 3\n\n""")

    wybor_1 = input("\n")
    if wybor_1 == "1":
        while True:
            print("""\n------------- WPISYWANIE DANYCH ------------
Uczeń - wpisz: 1
Nauczyciel - wpisz: 2
Wychowawca - wpisz: 3
Powrot do głównego menu - wpisz: q\n\n""")

            wybor_1_1 = input("\n")
            wybor_1_1 = wybor_1_1.lower()
            if wybor_1_1 != "1" and wybor_1_1 != "2" and wybor_1_1 != "3" and wybor_1_1 != "q":
                print("Wybrałeś złą opcję! Spróbuj jeszcze raz.")
                continue
            if wybor_1_1 == "1":
                while True:
                    print("Wpisz dane dotyczące ucznia\n")
                    imie_i_nazwisko = wpisywanie_imienia_i_nazwiska()
                    if imie_i_nazwisko in imienna_lista_uczniow:
                        print("Uczeń o takim imieniu i nazwisku jest już w bazie szkolnej! Spróbuj ponownie!")
                        continue
                    else:
                        nazwa_klasy = input("Podaj nazwę klasy:  ")
                        nazwa_klasy = nazwa_klasy.lower()
                        if nazwa_klasy not in numery_klas:
                            numery_klas.append(nazwa_klasy)
                        if nazwa_klasy in numery_klas:
                            nowy_uczen = Uczen(imie_i_nazwisko=imie_i_nazwisko, nazwa_klasy=nazwa_klasy)
                            uczniowie.append(nowy_uczen)
                            imienna_lista_uczniow.append(imie_i_nazwisko)
                        break
            if wybor_1_1 == "2":
                while True:
                    print("Wpisz dane nauczyciela\n")
                    imie_i_nazwisko = wpisywanie_imienia_i_nazwiska()
                    if imie_i_nazwisko in imienna_lista_nauczycieli:
                        print("Nauczyciel o takim imieniu i nazwisku jest już w bazie szkolnej! Spróbuj ponownie!")
                        continue
                    else:
                        przedmiot = input("Podaj nazwe przedmiotu nauczanego przez nauczyciela:   ")
                        wpisane_klasy = []
                        print("Podaj nazwy klas, aby zakończyć wpisz pusty tekst:")
                        while True:
                            nazwa_klasy = input()
                            if not nazwa_klasy:
                                break
                            nazwa_klasy = nazwa_klasy.lower()
                            if nazwa_klasy == "q":
                                break
                            if nazwa_klasy in wpisane_klasy:
                                print("Ta klasa została już wpisana! Wpisz inną klasę!")
                                continue
                            if nazwa_klasy not in numery_klas:
                                numery_klas.append(nazwa_klasy)
                            if nazwa_klasy in numery_klas:
                                wpisane_klasy.append(nazwa_klasy)
                                nowy_nauczyciel = Nauczyciel(imie_i_nazwisko=imie_i_nazwisko, przedmiot=przedmiot,
                                                     nazwa_klasy=wpisane_klasy)
                                nauczyciele.append(nowy_nauczyciel)
                                imienna_lista_nauczycieli.append(imie_i_nazwisko)
                        break
            if wybor_1_1 == "3":
                while True:
                    print("Wpisz dane wychowawcy\n")
                    imie_i_nazwisko = wpisywanie_imienia_i_nazwiska()
                    if imie_i_nazwisko in imienna_lista_wychowawcow:
                        print("Wychowawca o takim imieniu i nazwisku jest już w bazie szkolnej! Spróbuj ponownie!")
                        continue
                    else:
                        nazwa_klasy = input("Podaj nazwę klasy:  ")
                        nazwa_klasy = nazwa_klasy.lower()
                        if nazwa_klasy not in numery_klas:
                            numery_klas.append(nazwa_klasy)
                        if nazwa_klasy in numery_klas:
                            nowy_wychowawca = Wychowawca(imie_i_nazwisko=imie_i_nazwisko, nazwa_klasy=nazwa_klasy)
                            wychowawcy.append(nowy_wychowawca)
                            imienna_lista_wychowawcow.append(imie_i_nazwisko)
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
            if wybor_1_2 != "1" and wybor_1_2 != "2" and wybor_1_2 != "3" and wybor_1_2 != "4" and wybor_1_2 != "q":
                print("Wybrałeś złą opcję! Spróbuj jeszcze raz.")
                continue
            if wybor_1_2 == "1":
                while True:
                    szukana_klasa = input("Wpisz klase:   \n")
                    if szukana_klasa not in numery_klas:
                        print("Nie ma takiej klasy! Spróbuj jeszcze raz.")
                        break
                    else:
                        for prowadzacy in wychowawcy:
                            if prowadzacy.nazwa_klasy == szukana_klasa:
                                print(f"""\n\nKlasa {szukana_klasa}:,
Wychowawca: {prowadzacy.imie_i_nazwisko}""")
                        for dzieci in uczniowie:
                            if dzieci.nazwa_klasy == szukana_klasa:
                                print(f"Uczeń: {dzieci.imie_i_nazwisko}")
                        break

            if wybor_1_2 == "2":

                while True:
                    print("Podaj dane ucznia")
                    wpisany_uczen = wpisywanie_imienia_i_nazwiska()
                    if wpisany_uczen not in imienna_lista_uczniow:
                        print("Nie ma takiego ucznia! Spróbuj jeszcze raz")
                        break
                    else:
                        for poszukiwana_klasa in uczniowie:
                            if poszukiwana_klasa.imie_i_nazwisko == wpisany_uczen:
                                odnaleziona_klasa = poszukiwana_klasa.nazwa_klasy
                        print(f"""\n\n{wpisany_uczen}
Lista przedmiotów i nauczycieli ucznia.""")
                        for lekcje in nauczyciele:
                            if odnaleziona_klasa in lekcje.nazwa_klasy:
                                print(f"Przedmiot: {lekcje.przedmiot} - Nauczyciel: {lekcje.imie_i_nazwisko}")
                        break

            if wybor_1_2 == "3":
                while True:
                    print("Podaj dane nauczyciela.")
                    wpisany_nauczyciel = wpisywanie_imienia_i_nazwiska()
                    if wpisany_nauczyciel not in imienna_lista_nauczycieli:
                        print("Nie ma takiego nauczyciela! Spróbuj jeszcze raz")
                        break
                    else:
                        for poszukiwana_klasa in nauczyciele:
                            if poszukiwana_klasa.imie_i_nazwisko == wpisany_nauczyciel:
                                print(f"Klasy prowadzone przez nauczyciela: {poszukiwana_klasa.nazwa_klasy}")
                    break

            if wybor_1_2 == "4":
                while True:
                    print("Podaj dane wychowawcy")
                    wpisany_wychowawca = wpisywanie_imienia_i_nazwiska()
                    if wpisany_wychowawca not in imienna_lista_wychowawcow:
                        print("Nie ma takiego wychowawcy! Spróbuj jeszcze raz")
                        break
                    else:
                        for poszukiwana_klasa in wychowawcy:
                            if poszukiwana_klasa.imie_i_nazwisko == wpisany_wychowawca:
                                odnaleziona_klasa = poszukiwana_klasa.nazwa_klasy
                                print(odnaleziona_klasa)
                                print(f"""\n\n{wpisany_wychowawca} - wychowawca klasy: {odnaleziona_klasa}
Lista uczniów:""")
                            for dzieci in uczniowie:
                                if dzieci.nazwa_klasy == odnaleziona_klasa:
                                    print(dzieci.imie_i_nazwisko)
                    break

            if wybor_1_2 == "q":
                break

    if wybor_1 == "3":
        break
    else:
        print("Wybrałeś złą opcję! Spróbuj raz jeszcze.")
        continue