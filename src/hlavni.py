
class Pojisteny:
    def __init__(self, jmeno, prijmeni, vek, telefon):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefon = telefon

    def __str__(self):
        return f"{self.jmeno} {self.prijmeni}, Věk: {self.vek}, Tel.: {self.telefon}"

class SpravaPojistenych:
    def __init__(self):
        self.pojisteni = []

    def pridat_pojisteneho(self, jmeno, prijmeni, vek, telefon):
        novy_pojisteny = Pojisteny(jmeno, prijmeni, vek, telefon)
        self.pojisteni.append(novy_pojisteny)
        print(f"Pojištěný {jmeno} {prijmeni} byl úspěšně přidán.")

    def zobrazit_pojistene(self):
        if not self.pojisteni:
            print("Žádní pojištění nejsou evidováni.")
        else:
            print("Seznam pojištěných:")
            for pojisteny in self.pojisteni:
                print(pojisteny)

    def vyhledat_pojisteneho(self, jmeno, prijmeni):
        nalezeni = [p for p in self.pojisteni if p.jmeno == jmeno and p.prijmeni == prijmeni]
        if nalezeni:
            print("Nalezený pojištěný:")
            for pojisteny in nalezeni:
                print(pojisteny)
        else:
            print(f"Pojištěný {jmeno} {prijmeni} nebyl nalezen.")


if __name__ == "__main__":
    sprava = SpravaPojistenych()

    while True:
        print("\nSpráva pojištěných")
        print("1. Přidat pojištěného")
        print("2. Zobrazit všechny pojištěné")
        print("3. Vyhledat pojištěného")
        print("4. Ukončit")

        volba = input("Vyberte možnost: ")

        if volba == "1":
            jmeno = input("Zadejte jméno: ")
            prijmeni = input("Zadejte příjmení: ")
            vek = int(input("Zadejte věk: "))
            telefon = input("Zadejte telefonní číslo: ")
            sprava.pridat_pojisteneho(jmeno, prijmeni, vek, telefon)
        elif volba == "2":
            sprava.zobrazit_pojistene()
        elif volba == "3":
            jmeno = input("Zadejte jméno: ")
            prijmeni = input("Zadejte příjmení: ")
            sprava.vyhledat_pojisteneho(jmeno, prijmeni)
        elif volba == "4":
            print("Program byl ukončen.")
            break
        else:
            print("Neplatná volba, zkuste to znovu.")