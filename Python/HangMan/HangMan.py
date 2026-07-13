import random

print("Pozdravljeni, tukaj se bomo igrali vislice")

with open("Besede.txt", "r") as datoteka:
    izbranaBeseda = random.choice(datoteka.read().splitlines())

print(izbranaBeseda)

vpisane_crke = []
napacne_crke = []
seznam_crk = list(izbranaBeseda)
zivlenja = 6

while True:
    poskus = input("Poskus: ").upper()
    vpisane_crke.append(poskus)

    prikaz_crke = ""

    for crka in seznam_crk:
        if crka in vpisane_crke:
            prikaz_crke += crka + " "
        else:
            prikaz_crke += "-" + " "



    if poskus not in seznam_crk:
        zivlenja -= 1
        napacne_crke.append(poskus)

    print(f"Življenja = {zivlenja}")
    print(prikaz_crke)
    print("Napacne crke: ", napacne_crke)

    if "-" not in prikaz_crke:
        print("Čestitke! Uganili ste besedo!")
        break
    elif zivlenja == 0:
        print("Zmanjkalo je življenj!")
        break