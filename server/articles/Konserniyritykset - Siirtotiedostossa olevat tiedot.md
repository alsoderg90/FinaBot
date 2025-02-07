## Siirtotiedostossa olevat tiedot

Yrityksen kirjanpidon tilit on helpointa tuoda Finazillaan siten, että lähdejärjestelmästä tuodaan yrityksellä käytössä olevat tilit sisään. Yrityksen kirjanpidon tilien tuominen Finazillaan alkaa siitä, että yrityksellä käytössä olevat kirjanpidon tilit tulisi olla tuotuna kirjanpidon järjestelmästä Excel -tiedostoon. Excelissä tiedosto muokataan oikeaan muotoon ja lopuksi tiedosto tallennetaan Unicode -teksti muotoon. Tätä prosessia olemme kuvanneet mm. ohjeessamme [täällä](

# Siirtotiedostossa olevat tiedot

Siirtotiedostossa minimivaatimuksena on tieto tilin numerosta (sarake A) sekä tilin nimestä (sarake B). Näiden lisäksi siirtotiedostossa on mahdollista tuoda raportointikoodi (sarake C).

Raportointikoodin käyttöä olemme kuvanneet ohjeessamme [täällä.]( 

Konserniyritysten tiedot merkitään tiedostoon siten, että sarakkeeseen D laitetaan jokin merkki (esimerkiksi kuvanmukainen x) niiden tilien kohdalle, jotka tulee merkitä eliminoitavaksi. Pelkällä sarakkeen D merkinnällä tilille tulee accounts -listauksee tieto siitä, että tili tulee eliminoida konserniraporteilla.

Mikäli eliminointi halutaan linkittää tiettyyn yritykseen, merkitään tämä sarakkeeseen E. Yritys merkitään joko kirjoittamalla sen nimi (täsmälleen samoin kuin se on Finazillassa kirjoitettu) tai laittamalla kyseisen yrityksen Finazilla koodi. Koodi löytyy Finazillan oikeasta yläkulmasta. Kuvan yrityksellä "Movies Ltd" koodi on 221-100.

[![](

Yrityssidonnaisuuden merkitystä eliminoinneissa olemme kuvanneet enemmän artikkelissamme ["Tilin eliminointi riippuvaiseksi raportin yrityksestä".](

Alla on esimerkki siirtotiedostosta, jolla tilejä voidaan tuoda sisään Finazillaan. Kuvan esimerkkiin on pyritty laittamaan mahdollisimman monenlaisia vaihtoehtoja.

Siirtotiedoston ensimmäinen varsinainen rivi on tavallinen tili (rivi2). Näissä tapauksissa siirtotiedossa on pelkästään tilinnumero ja nimi. Riveillä 3 ja 4 on yritykseen sidotut eliminoitavat tilit. Rivillä 3 yrityssidonnaisuus on merkitty laittamalla sarakkeeseen E yrityksen nimi, kun taas rivillä 4 tämä on merkitty laittamalla yrityksen Finazilla -koodi. Rivillä 5 on tavallinen tili, jolle on kuitenkin haluttu merkitä nk. raportointikoodi (tili 5000). Siirtotiedoston viimeinen rivi on konsernitili, jolla ei ole yrityssidosta. Tällainen tili eliminoidaan aina konserniraporteilla.

[![](

# Tilien lukeminen Finazillaan

Siirtotiedoston laatimisen jälkeen yrityksen tilit voidaan lukea Finazillaan sisään. Ensin tarkistetaan oikeasta ylälaidasta, että valittuna on oikea yritys. Tämän jälkeen mennään Company -valikon Accounts -toimintoihin ja valitaan vaihtoehto "Import Accounts". Tämän jälkeen haetaan tallennettu tiedosto sen sijaintipaikasta ja tuodaan tiedosto Finazillaan.

# Uusien tilien lisääminen Finazillaan

Jos yhtiö ottaa kirjanpidossa käyttöön uusia tilejä, tilien numerot siirtyvät integraatioajossa automaattisesti tositteilta Finazillaan. Tilien nimet, samoin kuin tiedot tilien eliminoitavuudesta, eivät kuitenkaan siirry, joten nämä tiedot tulee lisätä joko manuaalisesti tai ajamalla massana tämän ohjeen mukaisesti siirtotiedostona. Siirtotiedostoon laitetaan tällöin vain päivitettävät tiedot; koko tililuetteloa ei ole tarve muodostaa enää uudelleen.

# **Tiedoston vaatimukset**

* Sarake A = tilin numero
* Sarake B = tilin nimi
* Sarake C = raportointikoodi, mikäli sellainen halutaan tuoda
* Sarake D = eliminointimerkintä, mikäli kyseinen tili halutaan eliminoida
* Sarake E = yrityssidonnaisuus, silloin kun tilin eliminointi on riippuvainen yrityskontekstista
* Tallennetaan unicode.txt muotoon
[![](

*Huomaa, että yllä olevasta listauksesta sarake A ja B ovat aina pakollisia. Muut tiedot ovat vapaaehtoisia*



artikkelin osoite on https://intercom.help/finazilla/fi/articles/7793578-esimerkki-konsernitilien-tuominen

