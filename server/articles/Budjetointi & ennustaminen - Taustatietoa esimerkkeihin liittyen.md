## Taustatietoa esimerkkeihin liittyen

Kerroimme artikkelissamme ["Dimensiokiinnitetty budjetti, osa 1: budjetin luominen"]( kuinka budjetteja voi jatkossa luoda dimensiokiinnitettyinä usein erilaisin tavoin. Tässä artikkelissa kerromme, kuinka dimensiokiinnitetyille budjeteille import -toiminto käyttäytyy.

Havainnollistamme asiaa artikkelissa seuraavin esimerkein.

# Taustatietoa esimerkkeihin liittyen

Yrityksellä 1 on myyntiä oheisesti:

10 000€ kohdistamatonta yritystasoista myyntiä

5 000€ myyntiä, joka kohdistuu asiakas dimension arvolle "kerta-asiakas"

15 000€ myyntiä, joka kohdistuu asiakas dimension arvolle "kerta-asiakas" sekä kaupunki dimension arvolle "Jyväskylä"

5 000€ myyntiä kaupungille Jyväskylä

Myynti yhteensä: 35 000€

# Yritystasoinen budjetti

Yritystasoisessa budjetissa import -näkymä on oheinen.

Datasource -otsikon alla valinnalla "single target" tai "multiple targets" käyttäjä voi vaikuttaa siihen ***mitä*** lukuja tuodaan. Mikäli käytetään valintaa single -target, tuodaan vain sen dimensioarvon lukuja joka on valittuna viereiseen kenttään "select dimension target".

Mikäli single target -valinnan vieressä oleva kenttä on tyhjänä, tuodaan pelkästään kohdistumattomat luvut.

[![](

Tuomalla toteumalukuja tällä valinnalla, käyttäjä saa samat luvut kuin mitä raportoinnissa saataisiin oheisella valinnalla. Kyseinen valinta tuottaa luvut, jotka esiintyvät blank -tunnisteella.

[![](

Mikäli single target kentän viereen on valittuna jokin dimensionarvo, tuodaan pelkästään kyseisen dimension arvon luvut ja ***uudelleen kohdistetaan ne*** budjetilla yritystasoisiksi. Jos siis valitaan tuoda vaikkapa dimensionarvon kerta-asiakas myynti, saadaan 5000€ myynti. Budjetille mihin luvut tuotiin, 5000€ myynti on kohdistumaton/dimensioimaton.

[![](

Multiple targets valinnalla budjetille tuotaisiin kokonaismyynti 35 000€ siten, että koko myynti olisi kohdistumatonta/dimensioimatonta myyntiä.

[![](

*Toteumia voi tuoda käyttämällä prosenttikerrointa (multiplier) tai euromääräistä lisäystä (static addition). Lukuja voi tuoda myös jostain toisesta budjetista. Budjetille voi lisäksi tuoda lukuja saman asiakkuuden toiselta yritykseltä joko toteumista tai budjetilta. Kaikissa näissä tulee huomioida, että sama tuontilogiikka pätee; luvuista tuodaan vain, ne jotka ovat yritystasoisia eli nk. blank -lukuja.*

# Yhteen dimensioon kiinnitetty budjetti

Mikäli budjetilla on käytössä yksikin dimensio, on import -näkymä erilainen kuin edellä kuvatussa esimerkissä. Tällöin ensimmäisenä näkyvä valinta on import mode -valinta.

## Import moden merkitys

Import mode -valinnassa otetaan kantaa siihen, ***mistä dimension arvosta*** lukuja halutaan tuoda taustalla auki olevaan budjettiin. Oletusvalinta "**current dimension target"** tarkoittaa, että lukuja tuodaan siltä dimension arvolta, mikä budjetilla on valittuna oikeassa yläkulmassa. Mikäli budjetilla ei ole mitään valittuna, tuodaan yritystasoiset kohdistamattomat (nk. blank) luvut.

Budjetin oikeaan yläkulmaan voi luonnollisestikin kiinnittää vain sellaisen dimension arvon, mihin budjetti on kiinnitetty. Mikäli budjetti on kiinnitetty asiakas -dimensioon, voidaan vain sen arvoja valita oikeaan yläkulmaan.

[![](

## Havainnollistavat esimerkit

### **Esimerkki 1:**

Budjetin oikeassa yläkulmassa ei ole mitään valittuna. Tuodaan toteumat valinnalla current dimension target. Budjetille tulee 10 000€ myynti eli kohdistamaton yritystasoinen myynti.

### **Esimerkki 2:**

Budjetin oikeaan yläkulmaan valitaan dimension asiakas arvo "kerta-asiakas".

[![](

Tuodaan toteumat valinnalla "current dimension target". Budjetille tulee 5 000€ myynti. Huomaa, että matriisikohdistuksen kerta-asiakas + Jyväskylä luvut eivät tule.

Import moden valinta **"all dimension targets"** tuo yhdellä tuonnilla kaikki mahdolliset dimensiokohdistuksilla olevat luvut ja tuo ne budjetille samoille dimensiokohdistuksille. Dimensiokiinnitetyissä budjeteissa tulee huomioida, että kiinnityksen ulkopuoliset luvut tuodaan, mutta ne *siirretään* budjetille kohdistumattomiin yritystasoisiin lukuihin. Ne näkyvät budjetin monitorissa siis tunnisteella blank.

### **Esimerkki 3:**

Tuodaan toteumat valinnalla "all dimension targets". Budjetille tulee 35 000€ myyntiä. Koko myynti siis siirtyy. Budjetin monitorista nähdään, että myynti jakaantuu seuraavasti:

* Blank -tunnisteella on myyntiä 15 000€. Tänne tulee alkuperäinen yritystasoinen myynti 10 00€ + budjetin dimensiokiinnityksen ohi menevä Jyväskylän myynti 5 000€. *Jyväskylän myynti siis uudelleen kohdistetaan blank arvolle.*
* Kerta-asiakkaille tulee myyntiä yhteensä 20 000€. Luku muodostuu alkuperäisestä kerta-asiakkaiden 5 000€ myynnistä, sekä 15 000€ myynnistä, joka oli matriisikohdistuksella kerta-asiakas + Jyväskylä. Matriisikohdistuksista matriisin toinen osapuoli jää pois ja koko arvo esitetään sillä matriisin osapuolella, joka on budjetin dimensiokiinnitystä vastaava. Huomaa siis, että myös matriisikohdistuksella oleva luku siirtyy vaikka matriisin toinen osapuoli (kaupunki) ei ole budjetilla kiinnitettynä dimensiona.
# Useampaan dimensioon kiinnitetty budjetti

Useampaan dimensioon kiinnitetyn budjetin import mode näkymässä on aina ensimmäisenä import mode -valinta, jolla otetaan kantaa siihen, mistä lukuja halutaan tuoda.

## Import moden merkitys

Import moden merkitys on vastaava kuin yhteen dimensioon kiinnitetyssä budjetissa. Current dimension target valinnalla tuodaan valitun dimension arvon lukuja ja all dimension targets - valinnalla kaikkia lukuja. Budjetin oikeaan yläkulmaan voi luonnollisestikin kiinnittää vain sellaisen dimension arvon, mihin budjetti on kiinnitetty. Mikäli budjetti on kiinnitetty asiakas -dimensioon + kaupunki dimensioon, voidaan vain näiden kahden dimension arvoja valita oikeaan yläkulmaan.

## Havainnollistavat esimerkit

### **Esimerkki 4:**

Budjetin oikeassa yläkulmassa ei ole mitään valittuna. Tuodaan toteumat valinnalla current dimension target. Budjetille tulee 10 000€ myynti eli kohdistamaton yritystasoinen myynti. Luku esitetään budjetilla tunnisteella blank monitorissa.

### **Esimerkki 5:**

Budjetin oikeaan yläkulmaan on valittuna asiakas dimension arvo "kerta-asiakas". Budjetille tulee 5 000€ myynti, joka kohdistuu kerta-asiakkaalle.

### **Esimerkki 6:**

Budjetin oikeaan yläkulmaan on valittuna asiakas dimension arvo "kerta-asiakas" sekä kaupunki dimension arvo "Jyväskylä". Budjetille tulee 15 000€ myyntiä. Myynniksi tulee siis matriisilla oleva myynti. Luku esitetään budjetin monitorissa samalla matriisiyhdistelmällä.

### **Esimerkki 7:**

Tuodaan toteumat valinnalla "all dimension targets". Budjetille tulee 35 000€ myyntiä. Koko myynti siis siirtyy. Budjetin monitorista nähdään, että myynti jakaantuu seuraavasti:

* Blank -tunnisteella on myyntiä 10 000€. Tänne tulee alkuperäinen yritystasoinen myynti 10 00€
* Kerta-asiakkaille tulee myyntiä 5 000€ eli alkuperäinen kerta-asiakkaalle kohdistuva myynti
* Jyväskylälle tulee myyntiä 5 000€, joka on alkuperäinen Jyväskylän myynti

* Jyväskylä + Kerta-asiakas matriisille tulee myyntiä 15 000€. Koska kumpikin matriisin osapuoli on budjetilla kiinnitettynä, esitetään myyntikin matriisilla.
[![](

*Mikäli import mode valintana on vaihtoehto "all dimension targets", ei lukuja voi tuoda toiselta yritykseltä - ei toteumista, eikä budjetista.* 

# Useampaan dimensioon kiinnitetty budjetti, jossa tase on yritystasoinen

Useampaan dimensioon kiinnitetyn budjetin import mode näkymässä on aina ensimmäisenä import mode -valinta, jolla otetaan kantaa siihen, mistä lukuja halutaan tuoda.

Tällainen budjetti tekee poikkeuksen sääntöön taseen osalta. Mikäli yrityksellä olisi budjetti, joka olisi kokonaan yritystasoinen, ei import modea näytettäisi lainkaan. Jos yrityksellä on budjetti, joka on vain taseen osalta yritystasoinen, näytetään import mode valinta.

## Import moden merkitys

Import moden merkitys on vastaava kuin yhteen dimensioon kiinnitetyssä budjetissa. Current dimension target valinnalla tuodaan valitun dimension arvon lukuja ja all dimension targets - valinnalla kaikkia lukuja. Budjetin oikeaan yläkulmaan voi luonnollisestikin kiinnittää vain sellaisen dimension arvon, mihin budjetti on kiinnitetty. Mikäli budjetti on kiinnitetty asiakas -dimensioon + kaupunki dimensioon, voidaan vain näiden kahden dimension arvoja valita oikeaan yläkulmaan.

## Havainnollistavat esimerkit

Alla olevissa esimerkeissä käytetään artikkelin yläosassa kerrottuja myyntejä:

10 000€ kohdistamatonta yritystasoista myyntiä

5 000€ myyntiä, joka kohdistuu asiakas dimension arvolle "kerta-asiakas"

15 000€ myyntiä, joka kohdistuu asiakas dimension arvolle "kerta-asiakas" sekä kaupunki dimension arvolle "Jyväskylä"

5 000€ myyntiä kaupungille Jyväskylä

Myynti yhteensä: 35 000€.

Sen lisäksi yrityksellä 1 on taseessa investointeja oheisesti:

100 000€ kohdistamatonta yritystasoista investointia

55 000€ investointeja, joka kohdistuu asiakas dimension arvolle "kerta-asiakas"

25 000€ investointeja, joka kohdistuu asiakas dimension arvolle "kerta-asiakas" sekä kaupunki dimension arvolle "Jyväskylä"

15 000€ investointia kaupungille Jyväskylä

Investoinnit yhteensä: 195 000€.

### **Esimerkki 8:**

Budjetin oikeassa yläkulmassa ei ole mitään valittuna. Tuodaan toteumat valinnalla current dimension target. Budjetille tulee 10 000€ myynti eli kohdistamaton yritystasoinen myynti. Luku esitetään budjetilla tunnisteella blank monitorissa. Vastaava tuonti taseen puolella tuo investointeihin 100 000€.

### **Esimerkki 9:**

Budjetin oikeaan yläkulmaan on valittuna asiakas dimension arvo "kerta-asiakas". Budjetille tulee 5 000€ myynti, joka kohdistuu kerta-asiakkaalle. Taseen puolella valintaa ei voi tehdä, sillä taseessa ei ole dimensioita käytössä, jolloin oikea yläkulma ei esitä valintaikkunaa lainkaan.

### **Esimerkki 10:**

Budjetin oikeaan yläkulmaan on valittuna asiakas dimension arvo "kerta-asiakas" sekä kaupunki dimension arvo "Jyväskylä". Budjetille tulee 15 000€ myyntiä. Myynniksi tulee siis matriisilla oleva myynti. Luku esitetään budjetin monitorissa samalla matriisiyhdistelmällä.

Taseen puolella valintaa ei voi tehdä, sillä taseessa ei ole dimensioita käytössä, jolloin oikea yläkulma ei esitä valintaikkunaa lainkaan.

### **Esimerkki 11:**

Tuodaan toteumat valinnalla "all dimension targets". Budjetille tulee 35 000€ myyntiä. Koko myynti siis siirtyy. Budjetin monitorista nähdään, että myynti jakaantuu seuraavasti:

* Blank -tunnisteella on myyntiä 10 000€. Tänne tulee alkuperäinen yritystasoinen myynti 10 00€
* Kerta-asiakkaille tulee myyntiä 5 000€ eli alkuperäinen kerta-asiakkaalle kohdistuva myynti
* Jyväskylälle tulee myyntiä 5 000€, joka on alkuperäinen Jyväskylän myynti

* Jyväskylä + Kerta-asiakas matriisille tulee myyntiä 15 000€. Koska kumpikin matriisin osapuoli on budjetilla kiinnitettynä, esitetään myyntikin matriisilla.

Taseen puolelle tulee investointeihin 195 000€ eli kaikki luvut tulevat taseeseen. Luvut esiintyvät tunnisteella blank.  
​

# Budjetti, johon on valittu kaikki yrityksen kirjanpidon dimensiot

Tällainen budjetti vastaa toimintalogiikaltaan Finazillan "vanhaa" budjettia. Kaikki dimensiot ovat käytettävissä sekä pääbudjetilla, taseessa sekä osabudjeteilla. Kohdistuksia voidaan tehdä kaikin mahdollisin metodein. Toteumaa voidaan tuoda, kuten kuvattu artikkelissamme mm. [täällä.](



artikkelin osoite on https://intercom.help/finazilla/fi/articles/8544892-dimensiokiinnitetty-budjetti-osa-2-toteumien-tuominen

