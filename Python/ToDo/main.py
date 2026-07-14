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
        self.vmesnik.ListBox.

    def brisi_opravilo(self):
        print("Logika: Brišem opravilo...")

    def opravljeno_opravilo(self):
        print("Logika: Označujem kot opravljeno...")

    def zazeni(self):
        self.vmesnik.zazeni()


# Zagon aplikacije
if __name__ == "__main__":
    aplikacija = ToDoLogika()
    aplikacija.zazeni()