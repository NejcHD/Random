from View import ToDoView

class ToDoLogika:
    def __init__(self):

        # Tukaj bomo imeli seznam opravil v spominu
        self.opravila = []

        # v vmesnik shranimo celo logiko
        self.vmesnik = ToDoView(self)

    def dodaj_opravilo(self):
        print("Logika: Dodajam opravilo...")
        novo_opravilo = self.vmesnik.vnos.get()
        datum = self.vmesnik.vnosDatum.get()
        opraviloDatum = f"{novo_opravilo} - {datum}"
        if novo_opravilo != "":
            self.vmesnik.ListBox.insert("end", opraviloDatum )
        else:
            print("Vnos je prazen")

    def brisi_opravilo(self):
        print("Logika: Brišem opravilo...")
        izbrano = self.vmesnik.ListBox.curselection()   #vrne izbran idex

        if izbrano:
            indeks = izbrano[0]
            text = self.vmesnik.ListBox.get(indeks)
            print(f"Izbrisano {text}")
            self.vmesnik.ListBox.delete(indeks)
        else:
            print("Ni izbranega opravila")

    def opravljeno_opravilo(self):
        print("Logika: Označujem kot opravljeno...")
        izbrano = self.vmesnik.ListBox.curselection()
        self.vmesnik.ListBox.itemconfig(izbrano, bg="lightgreen")

    def zazeni(self):
        self.vmesnik.zazeni()


# Zagon aplikacije
if __name__ == "__main__":
    aplikacija = ToDoLogika()
    aplikacija.zazeni()