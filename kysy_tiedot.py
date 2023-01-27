# OHJELMA, JOKA KYSYY BMI-TIETOJA USEASTA KUNTOILIJASTA
# =====================================================

# KIRJASTOT JA MODUULIT
#----------------------

# Tuodaan fitness.py:n sisältämät toiminnot ohjelmaan
import fitness

# Kysytään tiedot ja tulostetaan painoindeksi kunnes halutaan lopettaa
bmi_lista = []
nimilista = []

while True: # Ikuinen silmukka, jossa ollaan kunnes annetaan tyhjä pituus
    
    nimi = input('Nimi, tyhjä lopettaa: ')
        
    if nimi == '':
        break #Poistutaan silmukasta, jos vastaus tyhjä
    
    nimilista.append(nimi)    
    pituus_teksti = input('Pituus (cm): ')    
    paino_teksti = input('Paino (kg): ')

    # Yritetään muuttaa syötetyt tekstit luvuiksi ja laskea BMI
    try:
        pituus = float(pituus_teksti)
        paino = float(paino_teksti)

        # Lasketaan painoindeksi fitness-modulin laske_bmi-funktiolla
        bmi = fitness.laske_bmi(paino, pituus)

        # Luodaan monikko (tuple), jos nimi ja bmi
        monikko = (nimi, bmi)

        # Lisätään BMI listaan
        bmi_lista.append(monikko)

        # Näytetään tulokset ruudulla
        print('Painoindeksi on:', bmi)

    # Jos tapahtuu virhe, ilmoitetaa käyttäjälle
    except Exception as e:
        print('Syötteessä oli virhe, yritä uudelleen', e)

# Tulosta ruudulle lopuksi lista painoindekseistä
print('Nimet ja painoindeksit olivat:', bmi_lista)

# Puretaan lista ja tulostetaan se rivi riviltä
for henkilo in bmi_lista:
    
    # Monikossa on kaksi tietoa, joiden indeksit ovat 0 (ensimmäinen) ja 1 (toinen)
    print(henkilo[0],'painoindeksi on', henkilo[1])

# Listassa olevien monikoiden määrä
print('Listassa oli', len(bmi_lista), 'merkintää')

nimilista.sort()
print(nimilista)