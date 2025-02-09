## Esimerkki 1: normaali kohdistus

Tositteen voi kohdistaa eri lähdejärjestelmissä eri dimensioille lukuisin tavoin. Procountorissa esimerkiksi voi jakaa tositteen kahdelle dimensiolle käyttäen % jakoa. Tässä artikkelissa kerromme, miten kyseinen kirjaus, sekä muutamat muut peruskirjaukset, näkyvät Finazillassa.

# Esimerkki 1: normaali kohdistus

Lähdejärjestelmä sanoo, että Finazillaan on siirtynyt 100€ tosite. Tosite tuli kun myytiin tampereella kahvinkeitin. Finazillaan muodostuu tästä yksi rivi; matriisi kohdistukselle TAMPERE+KAHVINKEITIN.

[![](
# Esimerkki 2: yksinkertainen dynaaminen kohdistus

Lähdejärjestelmä sanoo, että Finazillaan siirtyy tosite, jossa on myyntiä 100€. Lisäksi lähdejärjestelmä sanoo, että tästä satasesta myytiin puolet Tampereella ja puolet Jyväskylässä. Finazillaan tästä syntyy kaksi riviä; molemmille kaupungeille omansa.

[![](
# Esimerkki 3: jako + matriisi kohdistus

Otetaan esimerkkiin sama lähtötilanne kuin edellisessä; myytiin 100€, josta puolet on myyty Tampereella ja puolet Jyväskylässä. Tässä esimerkissä riviin on lisätietona merkattu, että kyseinen myynti oli monitoimikone ja se myytiin SF-Kaupassa. Finazilla tekee molempiin riveihin lisäkohdistukset, koska tositteelta nähdään, että koko 100€ kohdistuu vain yhteen TUOTE dimensioon ja yhteen KAUPPA dimensioon.

[![](
# Esimerkki 4: tuplajako prosenteilla

Finazillaan tulee tietoa, että on myyty 100€ edestä. Maitoa mennyt 10€ ja Kahvia 90€. Tampereella on myyty 60€ ja Jyväskylässä 40€. Saapuvasta tiedosta puuttuu tietoa, jotta saataisiin aukoton kuvaus siitä mitä on tapahtunut. Saapuvan tositteen mukaan ei voida tietää, että onko kuinka paljon maitoa myyty Tampereella.

Finazilla suorittaa tämän tyyppisen tositteen jakamisen siten, että jaetaan kaikki kohdistukset prosenttiosuuksiin. Koska tositteen kokonaissummasta 10% on maitoa, niin Finazilla päättelee, että sekä Tampereella että Jyväskylässä on myyty 10% maitoa ja 90% Kahvia.

Finazillaan tästä muodostuu 4 riviä; kaikkiin mahdollisiin dimension arvojen yhdistelmiin. Esimerkkinä vaikka TAMPERE+MAITO rivin summa muodostuu siten että:

* Jaetaan Kaupunki dimensio prosentteihin -> 60€ / 100€ = 60%
* Jaetaan Tuote dimensio prosentteihin -> 10€ / 100€ = 10%
* Yhdistetään kyseisen rivin prosentti osuudet -> Tositerivin summa \* Tampere osuus \* Maito osuus = 100€ \* 60% \* 10% = 6€
[![](
# Esimerkki 5: vajaa dimensio kohdistus

Finazillaan tulee tieto, että on myyty 100€. Tositteella ilmoitetaan, että myynnistä 60€ on myyty Tampereella, mutta ei ole ilmoitettu muuta. Tällöin Finazilla olettaa, että 40€ on myyty kokonaan ilman kaupunki -kohdistusta.

[![](

artikkelin osoite on https://intercom.help/finazilla/fi/articles/4859279-matriisidimensioille-jaettujen-tositteiden-kayttaytyminen-finazillassa

