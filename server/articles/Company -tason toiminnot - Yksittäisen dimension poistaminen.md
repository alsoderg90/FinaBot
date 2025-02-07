## Yksittäisen dimension poistaminen

Olemme kertoneet artikkelissamme [Dimensioiden tai dimensiovalueiden piilottaminen]( kuinka dimensioita ja niiden valueita voi piilottaa joko raportoinnista tai budjetoinnista - tai molemmista. Tässä artikkelissa kerromme, miten dimensioita ja/tai dimensiovalueita voi poistaa.

# Yksittäisen dimension poistaminen

Dimensioiden poistamisessa tulee huomioida se, onko kyseisiä dimensioita käytetty jossakin datassa, mikä on Finazillassa. Mikäli dimensiota on käytetty, ei poistaminen ole mahdollista.

Mikäli Finazillasta yritetään vahingossa poistaa sellainen dimensio tai dimension value, mikä on käytössä jossakin datassa Finazillassa, tulee Finazillasta virheilmoitus, joka kertoo, missä kyseistä dimensiota tai sen valueta on käytetty.

[![](

Jos tarve on kuitenkin saada kyseinen dimension value poistettua, tulee ensin poistaa dimension valuen kohdistuminen. Yllä oleva virheilmoitus kertoo, että dimension valueta on käytetty operatiivisessa datassa. Tällöin tulisi kohdistaminen operatiivisesta datasta poistaa ensin ja sen jälkeen dimension valuen poistaminen onnistuu (mikäli dimension valueta ei ole käytetty tämän lisäksi jossain muuallakin).

Jos vastaavasti yritetään poistaa dimensio, joka on käytössä esimerkiksi jollain budjetilla, tulee vastaava virheilmoituksen. Virheilmoitus kertoo, missä dimension valueta on käytetty.

[![](

Sen jälkeen kun kaikki kohdistukset dimensioille on poistettu, voidaan dimensio poistaa Finazillasta.

# Dimensioiden poistaminen massana

Dimensioita voi poistaa myös massana. Poisto tehdään company -valikossa kohdassa "dimensions". Näkymässä voidaan merkitä ruksilla kaikki dimensiot, jotka halutaan poistaa.

Mikäli käyttäjä poistaa dimension, jossa on vaikkapa 20 dimension arvoa, joista 10 on käytössä ja 10 ei, poistuu vain kyseiset 10 käyttämätöntä arvoa. Mikäli dimension yksikään arvo ei ole käytössä, poistuu kaikki.

[![](

[![](

*Dimensiot siirtyvät aina toteumadatan mukana Finazillaan, joten vaikka jokin dimensio poistettaisiin, siirtyy se Finazillaan yöllisessä integraatiossa uudelleen jos sille on lähdejärjestelmässä kohdistuksia.* 

# Lisätietoja

[Mitä dimensiot ovat ja miten niitä käytetään?](

[Dimensioiden tai dimensiovalueiden piilottaminen](



artikkelin osoite on https://intercom.help/finazilla/fi/articles/4838944-dimensioiden-poistaminen

