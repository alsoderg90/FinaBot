## Rivityypit (row type)

Raporttimallien kanssa toimiessa on hyvä tietää muutama termi, joita esiintyy raporttimalleilla kun rivejä aletaan luomaan tai muokkaamaan. Ensimmäisenä käyttäjä törmää rivityyppeihin, jotka olemme avanneet alla olevassa ikkunassa.

# Rivityypit (row type)

**Header** = Otsikkorivi. Usein rivistä käytetään myös termiä "parent" -rivi.

**Balance data** = rivi, jolla esitetään kirjanpidon lukuja joko joltain

tietyltä tililtä, tiliväliltä tai lukuisilta tiliväleiltä. Voidaan käyttää yhdessä dimensio -filtterin kanssa, jolloin raportille nousee vain filtteriin valittu dimensio, dimensiot tai raportointiryhmä.

**Formula** = kaavarivi. Rivillä voidaan laskea raporttimallilla jo olevia

rivejä, käyttää laskentavakiota hyväksi laskennassa jne.

**Operative Data**= operatiivisen datan raportointiin liittyvä rivityyppi

Jos käytetään rivityyppiä "balance data", tulee vastaan muutamia uusia määrittelyitä, joita on hyvä avata hieman lisää.

# Balance data rivin lisämäärittelyt

**Start** = tili, josta aloitetaan vs **End** = tili, mihin lopetetaan. Muodostavat

yhdessä tilivälin.

**Row factor** = debit tarkoittaa positiivista lukua ja credit negatiivista

lukua. Määrittää siis sen, miten valittu tili/tiliväli esitetään raportilla

**Visible** = valinta tarkoittaa sitä, näkyykö kyseinen rivi raportilla vai ei.

**Sum account range to parent** = tarkoittaa, että summataanko saldo "parent"

riville, joka on yleensä edellinen header -tyyppinen rivi.

**Filter data by dimensions** = tarkoittaa datan rajaamista dimensiolla, tietyillä dimensioilla tai raportointiryhmällä. Filtteröintiä voidaan suorittaa useamman yrityksen asiakkuuden tapauksessa siten, että kaikki yrityksille voidaan valita haluttu rajaus. Kyseessä on vaihtoehtoinen tapa raportin kautta datan rajaamiselle.

**Balance type** = valinnalla voidaan vaikuttaa siihen, raportoiko

raporttimallin rivi kauden saldoa (Balance), muutosta edellisestä

kaudesta (Change) vai kumulatiivista saldoa (Cumulative). Tyypillisesti käytetään oletusvalintaa Balance, mutta esimerkiksi ”Rahoituslaskelma” raporttimallissa raportoidaan taseen saldojen osalta muutosta edellisestä kaudesta, jolloin valinta on "Change".

**Previous month count** = määrittelee, montako kuukautta taaksepäin

raportoidaan. Oletusvalinnalla 0 raportoidaan raportointihetken kuukausi.

Jos haluttaisiin raportoida vaikkapa 12 kuukautta taaksepäin, valittaisiin

ko. kenttään 11. (Logiikka on siis kuluva kuukausi + kenttään syötetty määrä kuukausia taaksepäin).

**Previous month balance type** =liittyy edelliseen valintaan. Vaihtoehto balance from given months ago tarkoittaa loppusaldoa. Vaihtoehto sum months together summaa kuukaudet yhteen.

***Esimerkki:*** raportilla haetaan tilin 3000 saldoa. Previous month count kenttään valitaan 3 ja valinta on balance from given months. Raportille nousee kaudelle 1/2024 kauden 10/2023 luvut. Kaudelle 2/2024 nousee kauden 11/2023 luvut jne.

**Esimerkki:** raportilla haetaan tilin 3000 saldoa. Previous month count kenttään valitaan 3 ja valinta on sum months together. Raportille nousee kaudelle 4/2024 kausien 1-4/2024 yhteenlaskettu liikevaihto, kaudelle 5/2024 nousee kausien 2-5/2024 yhteenlaskettu liikevaihto jne.

Jos raporttimalliin tehdään kaavoja, tai muokataan olemassa olevia kaavoja, tulee vastaan muutamia uusia määrittelyitä, jotka liittyvät kaavojen luomiseen. Olemme avanneet näitä hieman lisää alla.

Koska kaavojen käyttäminen on kuitenkin hieman laajempi kokonaisuus, viittaamme alla myös muutamaan lisäartikkeliin, joista voi olla apua syvemmälle kaavoihin mentäessä.

# 

# Formula rivin lisämäärittelyt

**Visible** = valinta tarkoittaa sitä, näkyykö kyseinen rivi raportilla vai ei.

**Data aggregate** = Nämä valinnat vaikuttavat raportoinnissa Total Period -

sarakkeen luvun laskentatapaan. Oletusvalinta SUM on hyvä useimmissa

käyttötapauksissa, joten yleensä tätä ei ole tarvetta muuttaa. Tämä

kokonaisuus on esitelty tarkemmin artikkelissamme, johon löytyy linkki sivun

alalaidasta.

**Report Scheme rows** = alasvetovalikko, josta kaavaan voi valita

raporttimallissa jo aikaisemmin esiintyneitä rivejä.

**Calculation contstants** = laskentavakio. Asiaa on avattu artikkelissamme,

jonka linkki löytyy sivun alalaidasta.

# Lisätietoja

[Kaavojen kirjoittaminen raporttimalleille](

[Mitä laskentavakiot ovat ja miten niitä käytetään?](

## 

​



artikkelin osoite on https://intercom.help/finazilla/fi/articles/4358878-raporttimallien-rivityyppien-seka-rivien-balance-data-ja-formula-tarkemmat-maarittelyt-avattuna

