# Sovellus painoindeksin ja kehon rasvaprosentin laskemiseen
#===========================================================

#Muuttujat
pituus = 163 # Pituus senttimetreinä (cm)
paino = 57.1 # Paino kilogrammoina (kg)

pituus_metreina = pituus / 100

# Lasketaan painoindeksi (BMI)
bmi = paino / pituus_metreina **2

print('Painoindeksisi on', bmi)