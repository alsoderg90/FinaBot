## Balance -tyyppiset dimensiot

Dimensioista puhuttaessa puhutaan yrityksen laskentakohteista. Erilaisia laskentakohteita voi olla yrityksestä riippuen esimerkiksi kustannuspaikka, projekti tai liiketoiminta-alue. Finazillassa näistä kaikista käytetään yleiseisesti termiä dimensio.

Dimensiot, eli seurantakohteet, voivat olla Operative tai Balance -tyyppisiä.

# **Balance -tyyppiset dimensiot**

Balance -tyyppiset dimensiot siirtyvät Finazillaan kirjanpidon tositteilta. Seurantatasojen kohteita (dimension values) voivat olla esimerkiksi kustannuspaikka tai projekti.

# **Operative -tyyppiset dimensiot**

Operatiiviset dimensiot siirtyvät Finazillaan myynti- ja ostolaskuilta (rajapinta Procountor ja Netvisor -järjestelmissä). Operatiivisten seurantatasojen kohteita (dimension values) voivat olla esimerkiksi tuote, asiakas tai toimittaja.

Operatiiviset dimensiot ovat siis seurantakohteita, jotka voivat tulla Finazillaan joko kirjanpidon datan tai operatiivisen datan mukana. Operatiivista dataa voidaan tuoda Finazillaan csv -tiedostolla ja aineistosta syntyy sisäänluvussa aineiston mukaiset dimensiot. Dimensioiden käyttö mahdollistaa raportoinnin haluttujen seurantakohteiden mukaisesti.

# **Mistä dimensiot löytyvät Finazillasta?**

Company -valikosta löytyy valikko nimeltä Dimensions. Kyseissä valikossa hallinnoidaan yrityksen dimensioita eli seurantakohteita. Lähtökohtainen toimintalogiikka on, että seurantakohteet siirtyvät Finazillaan kirjanpidon toteumadatan mukana.

# **Uusien dimensioiden luominen**

Dimensioita ja niiden arvoja on mahdollista luoda itse Finazilassa, mutta *emme suosittele* tätä tehtäväksi. Tilanteessa, jossa on tarpeen budjetoida dimension arvolle, joka ei ole vielä siirtynyt Finazillaan kirjanpidon toteumista, suositellaan perustettavan ko. arvo ensin lähdejärjestelmään. Tämän jälkeen tehdään ”nollakirjaus”, joka kohdistetaan tälle arvolle. Nyt dimension arvo siirtyy Finazillaan seuraavan tiedonsiirron yhteydessä kyseiseltä tositteelta ja sille voidaan kohdistaa budjetoitaessa.

Näin menettelemällä varmistetaan se, että kun tulevaisuudessa kyseiselle arvolle siirtyy lähdejärjestelmästä toteumadataa, se kohdistuu samalle arvolle kuin mille budjetoidut luvut on kohdistettu ja näin ollen budjetoitujen lukujen vertailu toteumaan on mahdollista.

# **Dimensioiden muuttaminen tai poistaminen**

Dimensioita ei myöskään suositella muutettavan (edellä selostetusta syystä) tai poistettavan. Jos turhan dimension poistaa, niin se siirtyy uudelleen Finazillaan tiedonsiirrosssa, mikäli sille on tehty kohdistuksia sillä ajanjaksolla, jolta tietoa Finazillan tuodaan. Dimension, mitä ei ole käytetty missään, voi poistaa.

Tarpeettomat dimensiot tai dimensioiden arvot voidaan myös piilottaa, jolloin niille ei voi budjetoida eivätkä ne ole raportoinnissa valittavissa. Tämä on toimivin vaihtoehto silloin kun dimension poistaminen ei onnistu sillä olevan datan vuoksi.

# Lisätietoja

[Yrityksen dimensiot](

[Dimensioiden tai dimensiovalueiden piilottaminen](

[Dimensioiden ja dimensiovalueiden järjesteleminen haluttuun järjestykseen](



artikkelin osoite on https://intercom.help/finazilla/fi/articles/4171022-mita-dimensiot-ovat-ja-miten-niita-kaytetaan

