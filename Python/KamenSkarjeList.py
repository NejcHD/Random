import random

print("Pozdravljen v Kamen / Skarje / List")



while True:

    print("Podaj svojo potezo (Kamen = k, Skarje = s, List = l)")

    seznam = ["Kamen","List","Skarje"]
    izbiraRac = random.choice(seznam)

    izbira = input()
    print(izbira)



    if (izbira == "Kamen" or izbira == "k") and izbiraRac == "Skarje":
        print("Zmagali ste, Kamen premga skarje")
    elif (izbira == "Kamen" or izbira == "k") and izbiraRac == "List":
        print("Zgubili ste, Kamen ne premga Lista")
    elif (izbira == "Skarje" or izbira == "s") and izbiraRac == "List":
        print("Zmagali ste, Skarje premga List")
    elif (izbira == "Skarje" or izbira == "s") and izbiraRac == "Kamen":
        print("Zgubili ste, Skarje ne premga Kamna")
    elif (izbira == "List" or izbira == "l") and izbiraRac == "Kamen":
        print("Zmagali ste, Papir premga Kamen")
    elif (izbira == "List" or izbira == "l") and izbiraRac == "Skarje":
        print("Zgubili ste, List ne premga Skarij")
    elif izbira == izbiraRac:
        print("Izenaceno")

    Nadaljuj = input("Podaj 'Stop' za konec ali 'next' da igras znova")
    if Nadaljuj == "Stop" or Nadaljuj == "stop":
        print("Hvala za igro")
        break
    elif Nadaljuj == "Next" or Nadaljuj == "n":
        print("Ovo na novo")
        continue
