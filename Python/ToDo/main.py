from tkinter import Listbox
from View import ToDoView
import json
from PIL import Image, ImageDraw
import pystray
import threading

import pystray
print(pystray.Icon.__module__)


class ToDoLogika:
    def __init__(self):
        self.opravila = []
        self.indeks_za_urejanje = None

        # 1. Dodamo varnostno zastavico za izhod
        self.zahtevaj_izhod_flag = False

        self.vmesnik = ToDoView(self)
        self.nalozi_opravila()

        # 2. Zaženemo periodično preverjanje zastavice znotraj Tkinterja
        self.preveri_zahtevo_za_izhod()

        slika = Image.new("RGB", (64, 64), "blue")
        narisi = ImageDraw.Draw(slika)
        narisi.rectangle((16, 16, 48, 48), fill="red")

        # Meni sedaj NE kliče uničevanja okna neposredno, ampak samo spremeni flag
        meni = pystray.Menu(
            pystray.MenuItem("Prikaži", lambda icon, item: self.vmesnik.prikazi_okno(), default=True),
            pystray.MenuItem("Izhod", lambda icon, item: self.postavi_izhod_flag())
        )
        self.ikona = pystray.Icon("todo_app", slika, "ToDo Aplikacija", meni)

        self.nit_ikone = threading.Thread(target=self.ikona.run, daemon=True)
        self.nit_ikone.start()

    def postavi_izhod_flag(self):
        print("Logika: Nastavljam zastavico za izhod...")
        self.zahtevaj_izhod_flag = True

    def preveri_zahtevo_za_izhod(self):
        # Če je ikona javila izhod, najprej ugasnemo njo, nato varno zapremo okno
        if self.zahtevaj_izhod_flag:
            print("Logika: Zaznana zahteva za izhod. Čistim komponente...")
            self.ikona.stop()
            self.vmesnik.okno.destroy()
            return

        # Vsakih 100 milisekund v Tkinter niti preverimo, če je uporabnik kliknil Izhod
        self.vmesnik.okno.after(100, self.preveri_zahtevo_za_izhod)

    def dodaj_opravilo(self):
        print("Logika: Dodajam opravilo...")
        novo_opravilo = self.vmesnik.vnos.get().strip()
        datum = self.vmesnik.vnosDatum.get()
        izbrana_prioriteta = self.vmesnik.prioriteta.get()

        opravilo_datum = f"{izbrana_prioriteta} | {novo_opravilo} | {datum}"

        if novo_opravilo != "":
            if self.indeks_za_urejanje is None:
                self.vmesnik.ListBox.insert("end", opravilo_datum)
            else:
                self.vmesnik.ListBox.delete(self.indeks_za_urejanje)
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
            self.shrani_opravila()
        else:
            print("Ni izbranega opravila")

    def uredi_opravilo(self):
        print("Logika: Urejanje opravila...")
        izbrano = self.vmesnik.ListBox.curselection()

        if not izbrano:
            print("Ni izbranega opravila za urejanje")
            return

        indeks = izbrano[0]
        opravilo = self.vmesnik.ListBox.get(indeks)

        try:
            prioriteta, naziv, datum = opravilo.split(" | ", 2)
        except ValueError:
            print("Opravilo ni v pričakovani obliki")
            return

        self.indeks_za_urejanje = indeks

        self.vmesnik.vnos.delete(0, "end")
        self.vmesnik.vnos.insert(0, naziv)

        self.vmesnik.vnosDatum.delete(0, "end")
        self.vmesnik.vnosDatum.insert(0, datum)

        self.vmesnik.prioriteta.set(prioriteta)
        self.vmesnik.button1.config(text="Shrani")

    def shrani_opravila(self):
        vsa_opravila = []
        stevilo_elementov = self.vmesnik.ListBox.size()

        for i in range(stevilo_elementov):
            tekst = self.vmesnik.ListBox.get(i)
            barva = self.vmesnik.ListBox.itemconfig(i, "bg")[-1]
            je_opravljeno = (barva == "lightgreen")

            slovar_opravila = {
                "tekst": tekst,
                "opravljeno": je_opravljeno
            }
            vsa_opravila.append(slovar_opravila)

        with open("opravila.json", "w") as f:
            json.dump(vsa_opravila, f)

    def nalozi_opravila(self):
        try:
            with open("opravila.json", "r") as f:
                shranjena_opravila = json.load(f)

            self.vmesnik.ListBox.delete(0, "end")

            for i, opravilo in enumerate(shranjena_opravila):
                self.vmesnik.ListBox.insert("end", opravilo["tekst"])
                if opravilo["opravljeno"]:
                    self.vmesnik.ListBox.itemconfig(i, bg="lightgreen")

            print("Opravila uspešno naložena!")
        except FileNotFoundError:
            print("Datoteka opravila.json še ne obstaja.")

    def zazeni(self):
        self.vmesnik.zazeni()


if __name__ == "__main__":
    aplikacija = ToDoLogika()
    aplikacija.zazeni()