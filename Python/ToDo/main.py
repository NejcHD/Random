from View import ToDoView


class ToDoLogika:
    def __init__(self):
        # Tukaj bomo imeli seznam opravil v spominu
        self.opravila = []

        self.indeks_za_urejanje = None

        # v vmesnik shranimo celo logiko
        self.vmesnik = ToDoView(self)

    def dodaj_opravilo(self):
        print("Logika: Dodajam opravilo...")
        novo_opravilo = self.vmesnik.vnos.get().strip()
        datum = self.vmesnik.vnosDatum.get()
        izbrana_prioriteta = self.vmesnik.prioriteta.get()

        opravilo_datum = f"{izbrana_prioriteta} -- {novo_opravilo} - {datum}"

        if novo_opravilo != "":
            if self.indeks_za_urejanje is None:
                self.vmesnik.ListBox.insert("end", opravilo_datum)
            else:
                self.vmesnik.ListBox.delete(self.indeks_za_urejanje)
                self.vmesnik.ListBox.insert(self.indeks_za_urejanje, opravilo_datum)
                self.indeks_za_urejanje = None
                self.vmesnik.button1.config(text="Dodaj")

            self.vmesnik.vnos.delete(0, "end")
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
        izbrano = self.vmesnik.ListBox.curselection()

        if not izbrano:
            print("Ni izbranega opravila za urejanje")
            return

        indeks = izbrano[0]
        opravilo = self.vmesnik.ListBox.get(indeks)

        try:
            prioriteta, ostalo = opravilo.split(" -- ", 1)
            naziv, datum = ostalo.rsplit(" - ", 1)
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

    def zazeni(self):
        self.vmesnik.zazeni()


# Zagon aplikacije
if __name__ == "__main__":
    aplikacija = ToDoLogika()
    aplikacija.zazeni()