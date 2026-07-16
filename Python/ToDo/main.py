from tkinter import Listbox

from View import ToDoView
import json

class ToDoLogika:
    def __init__(self):
        # Tukaj bomo imeli seznam opravil v spominu
        self.opravila = []

        self.indeks_za_urejanje = None

        # v vmesnik shranimo celo logiko
        self.vmesnik = ToDoView(self)

        self.nalozi_opravila()

    def dodaj_opravilo(self):
        print("Logika: Dodajam opravilo...")
        novo_opravilo = self.vmesnik.vnos.get().strip()  # prebere iz vmesnika podatke
        datum = self.vmesnik.vnosDatum.get()
        izbrana_prioriteta = self.vmesnik.prioriteta.get()

        opravilo_datum = f"{izbrana_prioriteta} | {novo_opravilo} | {datum}"   #shrani vse v spremenljivko

        if novo_opravilo != "":
            if self.indeks_za_urejanje is None:  #preverimo ce smo v nacinu za urejanje ce ne dodamo opravilo
                self.vmesnik.ListBox.insert("end", opravilo_datum)
            else:
                self.vmesnik.ListBox.delete(self.indeks_za_urejanje)   #shranjene spremenljivke iz uredi shrani v opravilo
                self.vmesnik.ListBox.insert(self.indeks_za_urejanje, opravilo_datum)
                self.indeks_za_urejanje = None
                self.vmesnik.button1.config(text="Dodaj")

            self.vmesnik.vnos.delete(0, "end")
            self.shrani_opravila()
        else:
            print("Vnos je prazen")

    def brisi_opravilo(self):
        print("Logika: Brišem opravilo...")
        izbrano = self.vmesnik.ListBox.curselection()

        if izbrano:
            indeks = izbrano[0]
            text = self.vmesnik.ListBox.get(indeks)
            print(f"Izbrisano {text}")
            self.vmesnik.ListBox.delete(indeks)
            self.shrani_opravila()

            if self.indeks_za_urejanje == indeks:
                self.indeks_za_urejanje = None
                self.vmesnik.button1.config(text="Dodaj")
        else:
            print("Ni izbranega opravila")

    def opravljeno_opravilo(self):
        print("Logika: Označujem kot opravljeno...")
        izbrano = self.vmesnik.ListBox.curselection()

        if izbrano:
            indeks = izbrano[0]
            self.vmesnik.ListBox.itemconfig(indeks, bg="lightgreen")
        else:
            print("Ni izbranega opravila")

    def uredi_opravilo(self):
        print("Logika: Urejanje opravila...")
        izbrano = self.vmesnik.ListBox.curselection()  #izbere opravilo

        if not izbrano:
            print("Ni izbranega opravila za urejanje")
            return

        indeks = izbrano[0]  #index vrstice
        opravilo = self.vmesnik.ListBox.get(indeks)  #preberemo vrstico

        try:
            prioriteta, naziv, datum = opravilo.split(" | ", 2)  #razdfelimo na 3 dele ter shranimo v spremenljivke
        except ValueError:
            print("Opravilo ni v pričakovani obliki")
            return

        self.indeks_za_urejanje = indeks  #shranimo index izbrane vrstice

        self.vmesnik.vnos.delete(0, "end")  # delete zbrise stare in z inser dodamo nove podatke v spremenljivke ne pa shrani
        self.vmesnik.vnos.insert(0, naziv)

        self.vmesnik.vnosDatum.delete(0, "end")  # 0, "end"  pomeni od indexa 0 do konca
        self.vmesnik.vnosDatum.insert(0, datum)

        self.vmesnik.prioriteta.set(prioriteta)
        self.vmesnik.button1.config(text="Shrani")

    def shrani_opravila(self):
        vsa_opravila = list(self.vmesnik.ListBox.get(0,"end"))

        with open("opravila.json","w") as f:
            json.dump(vsa_opravila,f)

    def nalozi_opravila(self):
        try:
            with open("opravila.json","r") as f:
                self.vmesnik.ListBox.delete(0,"end")
                shranjena_opravila = json.load(f)

            for a in shranjena_opravila:
                self.vmesnik.ListBox.insert("end",a)

            print("Opravila uspešno naložena!")

        except FileNotFoundError:
            print("Datoteka opravila.json še ne obstaja.")


    def zazeni(self):
        self.vmesnik.zazeni()


# Zagon aplikacije
if __name__ == "__main__":
    aplikacija = ToDoLogika()
    aplikacija.zazeni()