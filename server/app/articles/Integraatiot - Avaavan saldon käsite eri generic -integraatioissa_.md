## Avaavan saldon käsite eri generic -integraatioissa:

Tämä artikkeli on tarkoitettu ainoastaan niille Finazillan käyttäjille, joiden integraationa on vaihtoehto "generic". Finazillassa on valmiina neljä eri "generic" nimistä vaihtoehtoa integraatioksi. Valinta näiden kolmen integraation välillä tehdään sen perusteella, missä formaatissa asiakkaan data tulee lähdejärjestelmästä. Ero on taseen avaavien käsittelyssä.

Koska taseen käsittely ratkaisee sen, mikä neljästä generic -mallista soveltuu, on hyvä ymmärtää taseen käsittelystä Finazillassa hieman enemmän.

# **Avaavan saldon käsite eri generic -integraatioissa:**

Finazillan ei tarvitse tietää mikä on avaava saldo. Jos siirtyvässä aineistossa tulee esimerkiksi tilille 2000 luku 2 500 € historian alussa, eikä koskaan sen jälkeen enää, on oikea valinta Generic. Jos kyseinen saldo tulee jokaisen tilikauden alussa, on oikea valinta generic cumulative for accounting period. Jos taas kyseinen saldo tulee joka kuukauden alussa, on valinta generic opening balance per month. Genericin do not calculate vaihtoehto sopii asiakkaille, joiden tiedostossa taseen saldot tulevat suoraan siten, miten niiden halutaan olevan - taseelle ei siis suoriteta mitään kumulointia.

# **Tositeaineiston muodostaminen:**

Sarake A = Tilinumero

Sarake B = Vuosi

Sarake C = Kuukausi

Sarake D = Summa

Sarake E = Dimensiotason nimi (mikäli ko. rivillä on dimensiokohdistus)

Sarake F = Dimension arvo (mikäli ko. rivillä on dimensiokohdistus)

Aineisto tulee tallentaa CSV -muotoon ennen sisäänlukua. Samaan aineistoon laitetaan kaikki tapahtumat (tase sekä tulos) halutulta aikaväliltä (esimerkiksi kuukausi tai tilikausi). Valmiin pohjan voi ladata [tästä.]( Tiedosto on valmiiksi csv -muodossa.

## **Lukujen merkkisyydet aineistossa**

* Taseen vastaavaa -puoli on merkkisyydeltään debit. Plussaluvut tulevat siis raportille plussana ja credit merkkiset miinuksena (eli vähentävät taseen saldoa)
* Taseen vastattavaa -puoli on merkkisyydeltään credit. Plussaluvut tulevat siis raportille miinuksena (eli vähentävät taseen saldoa) ja credit merkkiset plussana.
* Tulot tuodaan miinusmerkkisinä
* Kulut tuodaan debit merkkisinä
[![](

*Aineiston sisäänlukijan pitää tietää miten luvut tiedostoon tulee, eli minkä laskentalogiikan valitsee.*

## Esimerkki 1: generic

* Taseen avaavat saldot tulevat historian alussa , eikä enää uudelleen
* Kumuloi tasetta itse
* Kuukausilla on kumulatiiviset loppusaldot siten, että avaavana saldona toimii tiedostossa ensimmäisenä ollut saldo ja kumulointia tehdään siitä eteenpäin tuleville vuosille

Tuodaan dataa sisään Finazillaan oheisesti CSV -muotoisella siirtotiedostolla. Tiedostomuoto ja tiedoston sisältö voi olla tapauskohtaisesti myös erilainen, mutta tässä on yksi esimerkki.

[![](

Finazilla raportoi datan oheisesti vuodelle 2023

[![](

Vuosi 2024 puolestaan näyttää oheiselta

[![](

Kuvista voidaan huomata, että tase kumuloituu koko ajan, kuten Generic -integraatiossa kuuluu. Kaudella 12/2023 tilin 1030 kumulatiivinen saldo oli 25 169,75€. Tositeaineistossa on kaudelle 1/2024 ko. tilin saldona 5000€, jolloin kauden 1/2024 taseraportin saldo on haluttu 30 169,75€, sillä tase kumuloituu yli tilikausien.

## Esimerkki 2: Generic cumulative for accounting period

* Taseen avaavat saldot tuodaan jokaisen tilikauden alussa
* Kumuloi tasetta itse tilikauden aikana
* Kuukausilla on kumulatiiviset loppusaldot siten, että avaavana saldona toimii tiedostossa oleva vuoden ensimmäisenä ollut saldo ja kumulointia tehdään siitä eteenpäin tuleville kuukausille

Tuodaan sisään aiemmin esimerkissä 1 mainittu data. Huomattava, että rivit 2 ja 3 ovat vuoden 2023 avaavat saldot. Vastaavasti riveillä 22 ja 23 on vuoden 2024 avaavat saldot (eli kauden 12/2023 loppusaldot) kyseisille tileille. Kumulointi lähtee siten oheisista saldoista liikkeelle. Jos riveillä 22 ja 23 tuotaisiin jokin muu summa kuin oikeellinen alkusaldo, alkaisi kumulointi siitä saldosta.

[![](

Finazilla raportilla oheinen näyttää vuoden 2023 osalta seuraavalta

[![](

Vuosi 2024 näkyy oheisesti

[![](

Edelleen Finazilla raportoi kumulatiivista saldoa. Ainoa ero edelliseen on siinä, että kumuloinnin lähtökohdaksi on otettu aina kauden avaava saldo. Vuoden 2024 kumulointi alkaa siis tiedostossa olleesta saldosta kaudella 1/2024 (5000€ tilin 1030 kohdalla ja 12 000€ tilin 1160 osalta).

## Esimerkki 3: Generic opening balance per month

* Taseen avaavat saldot tuodaan jokaisen kuukauden alussa
* Kausilla avaavat saldot sekä muutostositteet
* Ei kumuloi tasetta kuukausien yli

Tuodaan sisään oheinen data. Data on hieman esimerkeistä 1-2 poikkeava. Rivit 2-3 ovat tammikuun avaavat saldot, rivit 4-5 helmikuun, rivit 6-7 maaliskuun jne. Aineistossa on mukana myös muutostositteita, kuten esimerkiksi rivit 8, 11, 16 jne.

[![](

Finazilla raportoi kyseisen datan oheisesti:

[![](

Huomaa, että maaliskuussa 2023 aineistossa oli tilille 1030 kaksi erillistä riviä; yhdessä rivissä oli saldona 2000€ ja toisessa rivissä 500€. Finazilla raportoi täten taseen saldoksi kaudella 3/2023 2500€. Tositteet summataan yhteen.

## Esimerkki 4: Generic do not calculate

* Ei tarvitse ottaa kantaa taseen avaaviin saldoihin
* Jokaisen kuukauden osalta tuodaan kyseisen kuun loppusaldo
* Jos samaan kuukauteen ja tiliin liittyy useita rivejä, lasketaan ne yhteen ja yhteenlaskettu summa esitetään taseen loppusaldona
* Mitään ei kumuloida

Tuodaan sisään oheinen data.

[![](

Finazilla raportoi taseen oheisesti. Kullakin kuukaudella on saldona tiedostossa tuotu summa.

[![](

## Tuloksen tilien laittaminen aineistoon

Tuloslaskelman tapahtumat tuodaan aineistossa siten, että myyntitilien saldo on negatiivinen (credit) ja kulutilien positiivinen (debit). Alla pieni esimerkki aineistosta.

[![](

Finazilla raportoi tämän jälkeen kyseisen datan oheisesti (esimerkissä taustalla tuloslaskelma -raporttimalli).

[![](

## Dimensioiden laittaminen aineistoon

Mikäli joku/jotkut tositerivit kohdistuvat dimensioille, tulee tämä tieto laittaa siirtotiedostoon sarakkeisiin E ja F. Sarake E määrittelee sen, mistä dimensiosta on kyse (esimerkiksi projekti, kustannuspaikka jne) ja sarakkeessa F kerrotaan, mikä on kyseisen dimension arvo (esimerkiksi Projekti A, Projekti B, Kustannuspaikka 1, Kustannuspaikka 2 jne).

[![](



artikkelin osoite on https://intercom.help/finazilla/fi/articles/4774435-esimerkki-integraationa-generic-datan-tuominen-ja-kayttaytyminen-finazillassa

