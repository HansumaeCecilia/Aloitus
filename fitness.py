# Sovellus painoindeksin ja kehon rasvaprosentin laskemiseen
#===========================================================

# Muuttujat
# Kysytään käyttäjältä tiedot

pituus_teksti = input('Kuinka pitkä olet? (cm): ') # Input lukee käyttäjän vastaukset
paino_teksti = input('Kuinka paljon painat? (kg): ')
ika_teksti = input('Minkä ikäinen olet? ')
sukupuoli_teksti = input('Sukupuoli mies, vastaa 1, N -nainen: vastaa 0: ')

# Muutetaan vastaukset liukuluvuiksi
pituus = float(pituus_teksti)
paino = float(paino_teksti)
ika = float(ika_teksti)
sukupuoli = float(sukupuoli_teksti)

# Määritellään funktio painoindeksi laskentaan
def laske_bmi(paino, pituus):

    """ Laskee painoindeksin (BMI)

    Args:
        paino (liukuluku/float): paino (kg)
        pituus (liukuluku/float): pituus (cm)

    Returns:
        float: painoindeksi kahden desimaalin tarkkuudella
    """

    pituus = pituus / 100 # Muutetaan pituus metreiksi
    bmi = paino / pituus**2 # BMI:n matemaattinen laskukaava, rivit 23 ja 24
    bmi = round(bmi, 2) # Pyöristetään bmi kahteen desimaaliin, vaihtoehto 1
    return bmi # Palauta bmi-laskukaavan määritelmä allaolevaan koodiin

bmi = laske_bmi(paino, pituus)


# Määritellään funktio rasvaprosentin laskentaan
def aikuisen_rasvaprosentti(bmi, ika, sukupuoli):
    """Laskee aikuisen rasvaprosentin

    Args:
        bmi (float): painoindeksi
        ika (float): henkilön ikä
        sukupuoli (float): sukupuoli (0 = nainen, 1 = mies)

    Returns:
        float: kehon rasvaprosentti (aikuinen)
    """
    rasvaprosentti = 1.20 * bmi + 0.23 * ika - 10.8 * sukupuoli -5.4 # Aikuisen kehon rasvaprosentin laskentakaava
    rasvaprosentti = round(rasvaprosentti)
    return rasvaprosentti    

def lapsen_rasvaprosentti(bmi, ika, sukupuoli):
    """Laskee lapsen rasvaprosentin

    Args:
        bmi (float): painoindeksi
        ika (float): ikä
        sukupuoli (float): sukupuoli (tyttö = 0, poika = 1)

    Returns:
        float: kehon rasvaprosentti (lapsi)
    """

    rasvaprosentti = 1.51 * bmi + 0.7 * ika - 3.6 * sukupuoli + 1.4 # Lapsen kehon rasvaprosentin laskentakaava
    rasvaprosentti = round(rasvaprosentti, 2)
    return rasvaprosentti

if __name__ == "__main__":

    # Kysytään käyttäjältä tiedot
    pituus_teksti = input('Kuinka pitkä olet? (cm): ') # Input lukee käyttäjän vastaukset
    paino_teksti = input('Kuinka paljon painat? (kg): ')
    ika_teksti = input('Minkä ikäinen olet? ')
    sukupuoli_teksti = input('Sukupuoli mies, vastaa 1, N -nainen: vastaa 0: ')

    # Muutetaan vastaukset liukuluvuiksi
    pituus = float(pituus_teksti)
    paino = float(paino_teksti)
    ika = float(ika_teksti)
    sukupuoli = float(sukupuoli_teksti)

# Lasketaan painoindeksi funktiolla laske_bmi
oma_bmi = laske_bmi(paino, pituus)

# Yli 18-vuotiailla käytetään aikuisen kaavaa
if ika >= 18:
    oma_rasvaprosentti = aikuisen_rasvaprosentti(oma_bmi, ika, sukupuoli)

# Muussa tapauksessa käytetään lapsen kaavaa
else:
    oma_rasvaprosentti = aikuisen_rasvaprosentti(ika, oma_bmi, sukupuoli)

print('Oma painoindeksisi on', oma_bmi, 'ja kehon rasvaprosentti on', oma_rasvaprosentti)