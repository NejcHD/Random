import tkinter as tk
from tkcalendar import DateEntry


class ToDoView:
    def __init__(self,logika):   # tukaj spremeje vmsenik iz logike ter ga poimenujemo logika
        self.logika = logika
        self.okno = tk.Tk()
        self.okno.title("ToDo App")
        self.okno.geometry("400x500")



        self.okvir_gumbov = tk.Frame(self.okno)
        self.okvir_gumbov.pack(side = tk.TOP, pady=10)
        self.button1 = tk.Button(self.okvir_gumbov, text="Dodaj", width=8, command=self.logika.dodaj_opravilo)
        self.button1.pack(side=tk.LEFT, padx=5)
        self.button2 = tk.Button(self.okvir_gumbov, text="Delete",  width=8, command=self.logika.brisi_opravilo)
        self.button2.pack(side=tk.LEFT, padx=5)
        self.button3 = tk.Button(self.okvir_gumbov, text="Done",  width=8, command=self.logika.opravljeno_opravilo)
        self.button3.pack(side=tk.LEFT, padx=5)
        self.button_uredi = tk.Button(self.okvir_gumbov, text="Uredi", width=8, command=self.logika.uredi_opravilo)
        self.button_uredi.pack(side=tk.LEFT, padx=3)

        self.okvir_vnosa = tk.Frame(self.okno)
        self.okvir_vnosa.pack(pady = 20)
        self.vnos = tk.Entry(self.okvir_vnosa, width=18)
        self.vnos.pack(pady=30, side=tk.LEFT, padx=10)
        self.vnosDatum = DateEntry(self.okvir_vnosa, width=10, date_pattern='dd.mm.yyyy')
        self.vnosDatum.pack(pady=10, padx=10, side=tk.LEFT)


        self.prioriteta = tk.StringVar(value="Srednja")
        self.izbira_prioritete = tk.OptionMenu(
            self.okvir_vnosa,
            self.prioriteta,
            "Nizka",
            "Srednja",
            "Visoka"
        )
        self.izbira_prioritete.pack(side=tk.LEFT, padx=10)

        self.ListBox = tk.Listbox(self.okno, width=300, height=250)
        self.ListBox.pack(side=tk.BOTTOM, pady=30, padx = 20)

    def zazeni(self):
        self.okno.mainloop()
