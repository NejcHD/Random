from pathlib import Path  # ugotovi na akterem  sistemu tece



Kategorije = {
    "Dokumenti" : [".pdf", ".docx", ".txt"],
    "Slike" : [".jpg", ".png", ".gif", "webp"],
    "Video": [".mp4", ".mkv", ".avi"],
    "Glasba": [".mp3", ".wav", ".flac"],
}



pot_do_prenosov = Path.home() / "Downloads"   #avtomatska pot do home  /home ali \Users
print(pot_do_prenosov)

obrnjeni_slovar = {}

# obrnjemo Kategorije da iscemo kasneje koncnice
for kategorija, koncnice in Kategorije.items():    #gremo skopzi vse kljuce= katertgorija ter iteme koncnice

    for koncnica in koncnice:                  #gremo skozi vse koncnice oz iteme npr skoz vse dokumente
        obrnjeni_slovar[koncnica] = kategorija  # zapisemo pod kljuc = koncnica  item kategorija   "pdf" : "Dokumenti"



for datoteka in pot_do_prenosov.iterdir():  #iterdir pregleda ta direktori

    if datoteka.is_file():
        izvlecena_koncnica = datoteka.suffix.lower()

        ime_mape = obrnjeni_slovar.get(izvlecena_koncnica,"Unorganized")  #pogledamo v katero mapo slovarja spada ce v nobeno se re v Ostalo

        ciljna_mapa = pot_do_prenosov / ime_mape  # izdelamo koncno mapo npr Donloades/Dokuments

        ciljna_mapa.mkdir(exist_ok=True) # ustvari mapo ce ne obstaja

        datoteka.rename(ciljna_mapa / datoteka.name)  # srpemeni pot npr Downloads/porocilo.pdf v Downloads/Dokumenti/porocilo.pdf



print("🎉 Priden Python! Downloads folder je uspešno pospravljen!")
