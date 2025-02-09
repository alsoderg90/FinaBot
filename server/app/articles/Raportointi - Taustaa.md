## Taustaa

Olemme kertoneet artikkelissamme ["Esimerkki: kuinka saan luotua toteumadatasta dimensiokohtaisen raportin?"]( miten käyttäjä voi luoda raportin, missä esitetään dimensioarvoja (dimension value). Tässä artikkelissa avaamme enemmän dimensioiden raportoimisen logiikkaa muutamin esimerkein.

Tämän artikkelin ymmärtämisen edellytys on, että käyttäjä osaa jo luoda perusraportin jollakin tasolla, sekä osaa pivotoida luomaansa raporttia.

# Taustaa

Yrityksellä on käytössään kolme dimensiota: Kaupunki, Tehdas ja Yksikkö.

Kaupunki dimension alla on value Jyväskylä ja Helsinki, tehdas dimension alla on yrityksen kolme tehdasta; tehdas 1, tehdas 2 ja tehdas 3. Yksikön alla on yrityksen yksiköt koneistus ja kokoonpano.

Tammikuulla 2022 on seuraavanlaiset myynnit:

* 4 000€ dimension arvolle Jyväskylä
* 500€ dimension arvoille Jyväskylä + Tehdas 1
* 5 000€ dimension arvoille Jyväskylä + Tehdas 1 + Koneistus

  Myynti yhteensä 9 500€
# Uuden raportin muodostaminen

Raportin muodostaminen aloitetaan menemällä "Reports" -toimintoihin ja klikkaamalla siellä ”New Report” –painiketta. Raportille valitaan haluttu raporttimalli (report scheme) alasvetovalikosta.

## Dimensioihin liittyvät valinnat

### Yksittäinen dimension arvo ilman muuta rajausta

"Dimension presentation type" kohdassa on vaihtoehto "include dimensions", joka tulee valita aina kun dataa halutaan raportoidaan dimensioittain. Tämän lisäksi valitaan haluttu dimension arvo kohdassa Dimensions. Tässä esimerkissä on valittu kaupunki -dimension alta dimension arvo Jyväskylä.

[![](

Kyseinen Jyväskylä valinta tarkoittaa käytännössä sitä, että raportille nousee kaikki tositteet, missä esiintyy kyseinen dimension arvo Jyväskylä. Tämä tarkoittaa myös sellaisia tositteita, missä Jyväskylän kanssa esiintyy jokin toinen dimension arvo eli ns. matriisikohdistus.

Kaikki yrityksen myynti tammikuussa 2022 kohdistui dimension arvolle Jyväskylä (vaikkakin osassa tapahtumia oli myös jokin toinen dimensiokohdistus Jyväskylän lisäksi), jolloin raportille nousee koko myynti 9 500€.

[![](

## Yksittäinen dimension arvo require exact dimension selection -valinnan kanssa

Mikäli tarpeena olisi raportoida vain ne tositteet, missä Jyväskylä esiintyy yksin ilman mitään muuta dimensiokohdistusta, voidaan käyttää valintaa "require exact dimension selection".

[![](

Tällä valinnalla Finazilla tuottaa raportin, missä on vain ne tositteet, joissa kohdistus Jyväskylä esiintyy yksin, ilman mitään muuta kohdistusta. Raportille nousisi tällöin vain 4 000€ myynti.

[![](
## Kaksi dimension arvoa ilman muuta rajausta

Kun tarpeena on raportoida kahta dimension arvoa, valitaan dimensions- kenttään kyseiset kaksi arvoa. Tässä esimerkissä on valittu arvot Jyväskylä sekä Tehdas 1. Lisäksi edelleen "dimension presentation type" kohdassa on vaihtoehto "include dimensions".

[![](

Tehty valinta tuottaa raportin, jossa on kaikki tositteet, jotka kohdistuvat dimension arvoille Jyväskylä + Tehdas 1. Huomaa, että raportissa on siis mukana myös tosite, joka kohdistui dimension arvoille Jyväskylä + tehdas 1 + koneistus, mutta ei tositetta, joka kohdistui pelkästään dimension arvolle Jyväskylä.

Kun rajauksiin on valittu kaksi arvoa, on edellytyksenä tositteet nousemiselle raportille siis se, että tositteesta löytyy vähintään *kumpikin* valituista arvoista.

[![](

## Kaksi dimension arvoa require exact dimension selection -valinnan kanssa

Jos edellä kuvattu raportti tehtäisiin "require exact dimension selection" -valinnalla, Finazilla tuottaisi raportin, missä olisi vain ne tositteet, joissa kohdistus Jyväskylä + Tehdas 1 esiintyisivät ilman mitään muuta kohdistusta.

Raportille ei siis nouse tosite, joka kohdistui dimension arvolle Jyväskylä, eikä tosite, joka kohdistui dimension arvoille Jyväskylä + Tehdas 1 + Koneistus.

[![](

​

[![](

*Ohje toimii myös operatiivisten dimensioiden kanssa sillä erotuksella, että dimensions -kenttään tulee aina valita lisäksi Data Group nimeltä "operatiivinen data\_quantity" silloin kun käytetään exact -valintaa.* 

[![](

artikkelin osoite on https://intercom.help/finazilla/fi/articles/5913634-dimensioiden-raportoiminen-kayttamalla-dimension-rajausta

