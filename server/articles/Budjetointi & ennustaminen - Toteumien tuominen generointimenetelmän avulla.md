## Toteumien tuominen generointimenetelmän avulla

Olemme kuvanneet aikaisemmassa artikkelissamme ["Budjetin generointimenetelmä, osa 1: asetusten laittaminen tilikartalle"]( kuinka tilikartalle voidaan jatkossa kertoa erilaisia asetuksia, miten budjetille halutaan generoida lukuja.

Tässä artikkelissa kerromme, kuinka toteumaluvut tuodaan sen jälkeen, kun tilikartalle on tehty halutut määrittelyt.

Tuotu ominaisuus on osa laajempaa kokonaisuutta. Tässä artikkelissa esitelty ominaisuus on osa 2, joka keskittyy nimenomaan lukujen generoimiseen budjetille tilikartan asetusten kautta. Tuotavia osia on yhteensä 3. Toimintoon liittyy myös seuraavat ominaisuudet

[Budjetin generointimenetelmä, osa 1: asetusten laittaminen tilikartalle](

[Budjetin generointimenetelmä, osa 3: budjetin luominen esivalinnoilla](

# **Toteumien tuominen generointimenetelmän avulla**

Toteumien tuominen noudattelee samaa logiikkaa kuin "tavallisten" toteumalukujen tuominen pääbudjetille muutoinkin noudattelee. Ominaisuutta on kuvattu tarkemmin mm. artikkelissamme "[Toteumadatan tuominen budjetille pohjatiedoksi"](

[![](

Import mode-kohdassa voidaan ottaa kantaa siihen, miten luvut halutaan tuoda suhteessa dimensioihin. Kohdassa "From" ja "To" määritellään, että mistä luvut tuodaan ja minne ne tuodaan.

Toteumat voidaan tuoda:

* Yhdelle riville
* Yhdelle tiliryhmälle
* Koko budjetille (se välilehti missä ollaan, eli esim. profit and loss -näkymä)

Kun toteumat halutaan tuoda budjetille käyttämällä generointimenetelmää, on tärkeää valita "Import data transformation method" kohtaan vaihtoehto "Account scheme default forecasting method" vaihtoehto. Tämä valinta nimenomaan määrää sen, että toteumat tuodaan juuri generointimenetelmää hyödyntämällä.

# Havainnollistavat esimerkit

Kuvaamme eri generointimentelmiä tarkemmin muutamien esimerkkien avulla.

## *Esimerkki 1 (average)*

Yrityksellä A on vuodella 2022 tilillä 3003 toteuneita myyntejä yhteensä 132 406,23€. Eurot jakaantuvat vuoden kuukausilla siten, että jokaisella kuukaudella on eri summat.

Yrityksen A tilikartalle on merkitty, että tilin 3003 generointimenetelmä on "average". Tämä tarkoittaa keskiarvoa.

Kun tilille 3003 tuodaan toteumaluvut vuodelta 2002, tulee budjetin total -sarakkeeseen 132 406,23€ ja jokaiselle kuukaudelle tulee 11 033,85€. Finazilla laskee siis toteumista keskiarvon, ja tuo sen budjetin kuukausille. Jokaisella kuukaudella on siis sama keskiarvoinen myynti.

## *Esimerkki 2 (latest)*

Yrityksellä A on kaudella 12/2022 tilillä 3100 toteutuneita myyntejä yhteensä 36 548,91€. Yrityksen A tilikartalle on merkitty, että tilin 3100 generointimentelmä on "latest". Tämä tarkoittaa viimeisintä arvoa.

Kun tilille 3100 tuodaan toteumaluvut, tulee jokaiselle tiilikauden kuukaudelle arvoksi 36 548,91€. Jokaiselle kuukaudelle tuodaan siis kauden 12/2022 arvo eli nk. viimeisin arvo.

## *Esimerkki 3 (skip account)*

Yrityksellä A on vuodella 2022 tilillä 3200 toteuneita oheispalvelumyyntejä. Yrityksen A tilikartalle on merkitty, että tilin 3200 generointimenelmä on "skip account". Tämä tarkoittaa, että tili ns. ohitetaan. Sille ei käytännössä tehdä siis mitään.

Kun tilille 3200 tuodaan vuoden 2022 toteutuneet oheispalvelumyynnit, ei budjetille tule mitään.

## *Esimerkki 4 (skip account)*

Yrityksen A tilikartalle on määritelty, että tiliryhmä "oheispalvelut" generoidaan menetelmällä "skip account". Asetus on laitettu tilikartalla nk. "parent" riville, jolloin se valuu kaikille tiliryhmän lapsiriveille.

Kun tiliryhmälle oheispalvelut tuodaan toteumaluvut, ei budjetille tule mitään. Kaikki tiliryhmän tilit jäävät ennalleen.

## *Esimerkki 5 (average ja skip account)*

Yrityksen A tilikartalle on määritelty, että tiliryhmä "yleiset myyntitilit" generoidaan menetelmällä "average" ja tiliryhmä oheispalvelut menetelmällä "skip account".

Kun tiliryhmälle "myyntituotot" tuodaan toteumaluvut, tulee tiliryhmään "yleiset myyntitilit" keskiarvoiset myyntiluvut ja tiliryhmään "oheispalvelut" ei tuoda mitään, sillä se ohitetaan.

## *Esimerkki 6 (fit a line, linear)*

Yrityksen A tilikartalle on määritelty, että tilille 4000 ostot generoidaan menetelmällä "fit a line, linear". Kyseessä on nk. lineaarinen menetelmä, joka sovittaa "suoran viivan" eri pisteiden välille. Koko menetelmän tarkoituksena on, että suorasta viivasta tiedetään, mihin se on menossa, vaikka se menis kuinka pitkälle.

Tästä generointimentelmästä on hankalaa antaa esimerkkiä siten, että jos toteuneissa ostoissa on tietty määrä euroja, niin mitä budjetille syntyy. Kyseessä on matemaattinen laskentatapa, jonka ymmärtämisen edellytys on, että käyttäjä tietää itse mitä lineaarinen menetelmä tarkoittaa.

[![](

## *Esimerkki 7 (latest same calendar month)*

Yrityksen A tilikartalle on määritelty, että tiliryhmä "oheispalvelut" generoidaan menetelmällä "latest same calendar month". Yritys A tekee budjettia vuodelle 2025.

Kun tiliryhmälle "oheispalvelut" tuodaan toteumaluvut, tulee tiliryhmään "oheispalvelut" kunkin tilin viimeisimmän vastaavan kuukauden myynnit, eli esimerkiksi tammikuun 2025 kohdalle tulee tammikuun 2024 myynnit, helmikuun 2025 kohdalle tulee helmikuun 2024 myynnit ja niin edelleen.

## *Esimerkki 8 (latest same calendar month)*

Latest same calendar month menetelmän kanssa voi tulla eteen se tilanne, että tulevaisuuden budjettiin ollaan generoimassa lukuja siten, että niitä ei ole vielä olemassa. Tämä tilanne voi tulla vastaan tilanteissa, missä generointimenetelmää käytetään saman vuoden budjettiin mikä on sillä hetkellä menossa, tai tilanteissa, missä tehdään skenaariobudjetteja pidemmälle tulevaisuuteen (vaikkapa kahden vuoden päähän).

Yrityksellä A on toteumalukuja kausilla 1-11/2023. Joulukuulla 2023 ei ole vielä toteumaa. Marraskuun oheispalvelut ovat yhteensä 150 000€. Yritys tekee vuodelle 2025 budjettia käyttämällä generointimenetelmää "latest same calendar month". Budjetin 2025 kausista 12 on "ongelmallinen", sillä sille kuukaudelle ei ole olemassa vielä lukuja. Budjettiin tuodaan generoinnissa kaudelle 11/2025 oheispalveluihin 150 000€. Sama summa tulee myös kauden 12/2025 oheispalveluihin.



artikkelin osoite on https://intercom.help/finazilla/fi/articles/8753820-budjetin-generointimenetelma-osa-2-toteumien-tuonti

