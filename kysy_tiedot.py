# OHJELMA, JOKA KYSYY BMI-TIETOJA USEASTA KUNTOILIJASTA
# =====================================================

# KIRJASTOT JA MODUULIT
#----------------------

# Tuodaan fitness.py_n sisältämät toiminnot ohjelmaan
import fitness

while True:
        
    pituus_teksti = input('Pituus (cm), tyhjä lopettaa: ')
    
    if pituus_teksti == '':
        break

    paino_teksti = input('Paino (kg): ')

    pituus = float(pituus_teksti)
    paino = float(paino_teksti)

    # Lasketaan painoindeksi fitness-modulin laske_bmi-funktiolla
    bmi = fitness.laske_bmi(paino, pituus)

    print('Painoindeksi on:', bmi)