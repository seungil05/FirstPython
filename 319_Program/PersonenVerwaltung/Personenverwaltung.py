import Person

def personerstellen():
    person = Person.Person()
    person.name = input("Name: ")
    person.vorname = input("Vorname: ")
    person.telefonnummer = input("Telefonnummer: ")
    person.adresse.strasse = input("Strasse: ")
    person.adresse.plz = int(input("PLZ: "))
    person.adresse.ort = input("Ort: ")
    person.adresse.land = input("Land: ")
    person.adresse.hausnummer = int(input("Hausnummer: "))
    print("Name: ", person.name +
          " ", person.vorname
          + "\nTelefonnummer: ", person.telefonnummer
          + "\nAdresse: ", person.adresse.strasse
          + "\nHausnummer: ", str(person.adresse.hausnummer)
          + "\nPLZ: ", str(person.adresse.plz)
          + "\nOrt: ", person.adresse.ort
          + "\nLand: ", person.adresse.land)

if __name__ == "__main__":
    print("Welcome!")
    personerstellen()
    print("Goodbye!")