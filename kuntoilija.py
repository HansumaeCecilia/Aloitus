# KUNTOILIJAN TIEDOT OLIO-OHJELMOINTINA
# =====================================

# KIRJASTOT JA MODULIT (LIBRARIES AND MODULES)
# ---------------------------------------------

import fitness

# LUOKKAMÄÄRITYKSET (CLASS DEFINITIONS)
# --------------------------------------


class Kuntoilija:
    """Luokka kuntoilijan tietoja varten"""

    # Olionmuodostin eli konstruktori
    def __init__(self, nimi, pituus, paino, ika, sukupuoli):

        # Määritellään tulevan olion ominaisuudet (properties), luokan kentät (fields)
        self.nimi = nimi
        self.pituus = pituus
        self.paino = paino
        self.ika = ika
        self.sukupuoli = sukupuoli
        self.bmi = fitness.laske_bmi(self.paino, self.pituus)

    # Metodi rasvaprosentin laskentaan (aikuinen)
    def rasvaprosentti(self):
        self.rasvaprosentti = fitness.aikuisen_rasvaprosentti(
            self.bmi, self.ika, self.sukupuoli)
        return self.rasvaprosentti

    def rasvaprosentti_lapsi(self):
        self.rasvaprosentti_lapsi = fitness.lapsen_rasvaprosentti(
            self.bmi, self.ika, self.sukupuoli)
        return self.rasvaprosentti


if __name__ == "__main__":

    # Luodaan olio luokasta Kuntoilija
    kuntoilija = Kuntoilija('Kalle Kuntoilija', 171, 65, 40, 1)
    kuntoilija2 = Kuntoilija('Samu Suutari', 150, 55, 15, 1)
    print(kuntoilija.nimi, 'painaa', kuntoilija.paino, 'kg')
    print('rasvaprosentti on', kuntoilija.rasvaprosentti())
    print(kuntoilija2.nimi, 'painaa', kuntoilija2.paino, 'kg')
    # print('painoineksi on', kuntoilija.painoindeksi())
    print('rasvaprosentti on', kuntoilija2.rasvaprosentti())
