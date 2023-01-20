# Sovellus painoindeksin ja kehon rasvaprosentin laskemiseen
#===========================================================

#Muuttujat
pituus = 163 # Pituus senttimetreinä (cm)
paino = 57.1 # Paino kilogrammoina (kg)
pituus_teksti = input('Kuinka pitkä olet? (cm): ') # Input lukee käyttäjän vastaukset
paino_teksti = input('Kuinka paljon painat? (kg): ')
pituus = float(pituus_teksti) # Muutetaan liukuluvuksi
paino = float(paino_teksti)

'''
pituus_metreina = pituus / 100

# Lasketaan painoindeksi (BMI)
bmi = paino / pituus_metreina **2

print('Painoindeksisi on ', bmi)

'''
# Määritellään funktio painoindeksi laskentaan
def laske_bmi(paino, pituus):

    """ Laskee painoindeksin (BMI)

    Args:
        paino (liukuluku/float): paino (kg)
        pituus (liukuluku/float): pituus (cm)

    Returns:
        float: painoindeksi 2:n desimaalin tarkkuudella
    """

    pituus = pituus / 100 # Muutetaan pituus metreiksi
    bmi = paino / pituus**2 # BMI:n matemaattinen laskukaava, rivit 23 ja 24
    bmi = round(bmi, 2) # Pyöristetään bmi kahteen desimaaliin, vaihtoehto 1
    # print('Painoindeksisi on ', bmi)
    return bmi # Palauta bmi-laskukaavan määritelmä allaolevaan koodiin

bmi = laske_bmi(paino, pituus)
# x = round(bmi,2) # Pyöristetään bmi kahteen desimaaliin, vaihtoehto 2
print('Painoindeksisi on:', bmi)