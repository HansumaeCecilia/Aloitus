# LAPSEN RASVAPROSENTIN LASKENTA UUDEN LUOKAN LISÄÄMISELLÄ
# =========================================================

import fitness


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


class JunioriKuntoilija(Kuntoilija):

    # Luokka nuoren kuntoilijan tiedoille
    def __init__(self, nimi, pituus, paino, ika, sukupuoli):

        # Määritellään periytyminen, mitä ominsaisuuksia perii
        super().__init__(nimi, pituus, paino, ika, sukupuoli)

    def rasvaprosentti(self):
        self.rasvaprosentti = fitness.lapsen_rasvaprosentti(
            self.bmi, self.ika, self.sukupuoli)
        return self.rasvaprosentti


if __name__ == "__main__":

    kuntoilija = Kuntoilija('Kalle Kuntoilija', 171, 65, 40, 1)
    print(kuntoilija.nimi, 'painaa', kuntoilija.paino, 'kg')
    # print('painoineksi on', kuntoilija.painoindeksi())
    print('rasvaprosentti on', kuntoilija.rasvaprosentti())

    juniorikuntoilija = JunioriKuntoilija('Aku', 171, 65, 16, 1)
    print(juniorikuntoilija.nimi, 'painaa', juniorikuntoilija.paino, 'kg')
    print('rasvaprosentti on', juniorikuntoilija.rasvaprosentti())
