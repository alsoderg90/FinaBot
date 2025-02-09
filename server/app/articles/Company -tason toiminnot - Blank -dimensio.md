## Blank -dimensio

[![](

*Versiopäivityksessä 18.3.2022 tuotu parannus aikaisempaan roolien luomiseen ja näkymän rajaamiseen liittyen dimensioihin. Jatkossa käyttäjälle voidaan antaa oikeus myös dimensioimattomiin lukuihin.* 

# Blank -dimensio

Jatkossa rooleille, ja sitä kautta käyttäjille, voidaan antaa oikeus nk. blank dimensioon. Blank dimensio voi olla käyttäjille jo tuttu entuudestaan Finazillan raporttien ja budjetin monitorin näkymän myötä.

Tällaiset luvut näyttäytyvät Finazillan raporteilla ja budjetin monitorissa termillä "blank". Tämä tarkoittaa käytännössä siis dimensioimatonta/kohdistamatonta lukua. Finazillassa kyseisen dimension nimi on "blank" ja se löytyy roolien luomisessa "dimensions" valikon alta.

[![](

*Kuva: roolin luonnista löytyvä uusi vaihtoehto "blank, joka tarkoittaa dimensioimatonta yritystasoista "dimensiota". Antamalla tähän "dimensioon" oikeuden, käyttäjä näkee dimensioimattomat luvut.* 

# Havainnollistavat esimerkit

Havainnollistamme toimintoa käytännön esimerkin avulla.

Raportointi

**Esimerkki 1:** 

Yrityksen myynti on kaudella 1/2022 yhteensä 50 000€. Myynti kohdistuu dimensiolle siten, että projektille A kohdistuu 20 000€ ja projektille B kohdistuu 15 000€. Loput 15 000€ eivät kohdistu millekään dimensiolle.

Mikäli käyttäjällä ***on oikeus*** kaikkiin dimensioihin, näkyy hänelle myyntinä 50 000€ ja hän näkee myynnin myös halutessaan dimensiokohtaisesti. 15 000€ osuus, joka ei kohdistu mihinkään, näkyy tunnisteella "blank" raportilla.

**Esimerkki 2:** 

Jos vastaavasti taas käyttäjällä ***ei ole oikeutta*** blank -dimensioon, näkyy hänelle myyntinä edelliseen esimerkkiin perustuen kaudella 1/2022 yhteensä 35 000€ ja haluttaessa näiden kohdistuminen projektille A ja B. Käyttäjälle ei näy millään tavalla 15 000€ myynti, johon hänellä ei ole roolinsa puolesta oikeuksia.

Budjetointi

**Esimerkki 3:** 

Käyttäjällä ***on oikeus*** blank -dimensioon, sekä kahteen muuhun yrityksen dimensioon. Käyttäjä menee yrityksen budjetille. Käyttäjälle aukeaa pääbudjetin näkymä normaalisti, jossa näkyy dimensioimattomat luvut (tämä on juurikin nk. blank dimensio).

Käyttäjä voi aukaista myös kahden muun dimension budjettinäkymän, sillä niihin hänellä on oikeus. Vastaavasti taas käyttäjä ei voi aukaista monitor -näkymää, sillä hänellä ei ole oikeutta kaikkiin dimensioihin. Avausyritys tuottaa virheilmoituksen.

Osabudjetit aukeavat käyttäjälle oikeuksien mukaisesti. Jos yrityksellä on osabudjetteja, mitkä eivät ole dimensiokiinnitettyjä, saa käyttäjä nämä auki osabudjetin aukaisemalla. Osabudjetista näkyy dimensioimattomat luvut. Kahden muun dimension luvut käyttäjä näkee vaihtamalla oikeaan yläkulmaan kyseisen dimension.

**Esimerkki 4:**

Jos käyttäjälle ***ei ole oikeutta*** blank -dimensioon ja hän menee yrityksen budjetille, näkyy hänelle ns. tyhjä näkymä. Tämä johtuu siitä, että ko. näkymä on juurikin blank -dimension näkymä, mihin hänellä ei ole oikeutta. Budjetti aukeaa, kun käyttäjä valitsee oikeaan yläkulmaan jonkin dimension arvon, mihin hänellä on oikeus.

Osabudjetit aukeavat tällaiselle käyttäjälle siten, että sub budget -valikossa valitaan ensin oikeaan yläkulmaan haluttu dimension arvo (mihin on oikeus) ja sen jälkeen valitaan haluttu osabudjetti.

Myöskään monitor -näkymä ei aukea käyttäjälle, jolla ei ole oikeutta kaikkiin dimensioihin. Avausyritys tuottaa virheilmoituksen.

[![](

*Kyseisellä blank -dimensio oikeudella on vaikutuksia myös mm. tositteisiin ja vyörytyssääntöihin. Rajoitetun roolin käyttäjä voi tehdä asioita ja näkee asioita roolinsa sallimissa rajoissa.* 



artikkelin osoite on https://intercom.help/finazilla/fi/articles/6046736-esimerkki-annetaan-kayttajalle-oikeus-blank-dimensioon

