## Valmiit raporttimallit

Raporttimallit, eli Report Schemes, ovat raportoinnissa apuna tarvittava työkalu. Raporttien muodostaminen on helppoa ja nopeaa, kun taustalle valitaan valmis raporttimalli. Customer -tasolle luotu raporttimalli mahdollistaa kaikkien asiakkuuden yritysten raportoinnin kerran luodulla mallilla.

# **Valmiit raporttimallit**

Finazillassa raporttimalleja (Report Scheme) on valmiina kaikille yrityksille, jotka käyttävät liikekirjurin tilikarttaa. System -tasoisia raporttimalleja on useita kymmeniä ja näitä voidaan käyttää millä tahansa yrityksellä raportoinnissa.

Mikäli käytössä ei ole liikekirjurin tilikartta, perustetaan asiakkaalle vähintäänkin tuloslaskelma ja tase raporttimallit valmiiksi.

Valmiiden Raporttimallipohjien (Scope = System) avulla luotujen raporttimallien oikeellisuudesta vastaa Finazilla, silloin kun käytössä on myös System –tasoiset Account Scheme Templatet eli tilikarttapohjat (kuten liikekirjurin tilikartta, yleensä on käytössä).

# **Omien raporttimallien luominen**

Raporttimalleja voi itse luoda lisää joko valmiiden raporttimallien pohjalta muokkaamalla tai rakentamalla alusta asti ilman pohjaa.

Asiaa voi olla helpompaa lähestyä siitä näkökulmasta, että mikäli yrityksellä on jo jokin valmis raportti Excelissä, tai muussa järjestelmässä, mietitään miten saman raportin voisi toteuttaa Finazillassa.

Tässä kohden tulee huomioida, että raportille haettavat tiedot (kuten raportoitavat yhtiöt, raportoitavan datan tyyppi ja ajanjakso) määritellään vasta raportoitaessa. Raportin ulkoasu määritellään valmiiseen raporttiin.

Raporttimalleilla on keskeinen merkitys raportoinnin oikeellisuuden kannalta. Sen vuoksi suosittelemme seuraavia toimenpiteitä aina kun raporttimallia muokataan tai rakennetaan kokonaan uusi raporttimalli alusta.

* Raporttimallilla luodaan raportti, joka täsmäytetään lähdejärjestelmän tietoihin (Procountor, Netvisor tms) eli toisin sanoen varmistetaan, että malli raportoi oikein

* Huomioidaan käyttöoikeudet eli keillä käyttäjillä on oikeus muokata raporttimalleja
# **Rakenteen havainnollistaminen**

Raporttimallin rakenteen ymmärtämistä helpottaa, jos tarkastellaan sitä vielä yhden esimerkin kautta. Yksinkertaisena esimerkkinä on Käyttökate –raporttimalli. Käyttökate on käytännössä liikevaihto vähennettynä kiinteillä ja muuttuvilla kuluilla (poistoja ja rahoituseriä ei huomioida). Käyttökatteen raporttipuu näyttää seuraavalta:

[![](

Jos tarkastellaan kahta ensimmäistä riviä tarkemmin, logiikka on seuraava:

* 3000-6799 (account range summed to the parent) rivillä käsky summaa käyttökatteeseen tilit 3000-6799, eli tilit liikevaihdosta palkkoihin.

* 7000-8999 (account range summed to the parent) rivillä käsky summaa käyttökatteeseen tilit 7000-8999 eli liiketoiminnan muut kulut.

Näin ollen käyttökate on yllä olevien tilien summa. Käyttökate -rivi on raporttipuussa ns. parent -rivi, ja sen alla olevat rivit summaantuvat siihen. Koska tuotot ja kulut ovat vastakkaisen merkkisiä, summakaava toimii. Raportoitaessa tällä pohjalla, valmiilla raportilla näkyy vain yksi rivi ”käyttökate”.

# **Mihin uudet raporttimallit kannattaa luoda?**

Accounting –tyyppiset eli kirjanpidon dataan perustuvat Raporttimallit kannattaa yleensä rakentaa Customer –tason alle. Tällöin raporttimallia voi hyödyntää kaikkien asiakkuuden yritysten alla suoraan ja näin ollen raporttimalleja ei tarvitse luoda erikseen jokaisen yrityksen alle.

# **Raporttimallit operatiivisessa datassa**

Finazillassa on valmiina raporttimalli "System operative data" operatiivisen datan raportointiin silloin kun operatiivista dataa ei ole tarvetta rikastaa millään toisella datalla tai laskennalla.

Mikäli on tarve rakentaa itse operatiivisen datan raportointiin raporttimalli niin tässä yhteydessä on hyvä huomioida, että tällaiset raporttimallit yleensä tehdään suoraan yrityksen alle, sillä ne perustuvat yrityksen osto- ja myyntilaskuilta tulevaan tietoon esimerkiksi asiakkaista, tuotteista ja toimittajista (ns. operatiiviset dimensiot).

[![](

*Raporttimallin hahmotteleminen kannattaa aloittaa lisäämällä esimerkiksi otsikkoriveinä kaikki ne rivit, joita valmiilla raportilla on tarkoitus esittää. Kun rakenne on valmis, rivien alle voi lisätä lapsirivejä, joilla määritetään, minkä tilien tietoa kyseiselle riville haetaan (balance data) tai rivin voi muuttaa kaavariviksi ja lisätä kaavan riville hyödyntäen muita jo aiemmin raporttimalille lisättyjä rivejä.*

*Otsikkorivejä voi myös lisätä jälkikäteen sopivaan väliin. Tässä tulee huomioida, että kun rivin alle on lisätty lapsirivejä (Child Row) niin rivin tyyppiä ei voi enää muuttaa (otsikkoa voi kuitenkin muokata, rivin tyyppiä ei voi enää vaihtaa). Lisäksi tulee huomioida, että raporttimallilla ei voi olla kahta samannimistä riviä.*

*Balance data –riveillä logiikka on se, että lapsiriveille valitut tilivälit summaantuvat emoriviin (Parent). Tästä johtuen tulee huomioida Row Factorit debit ja kredit tilivälejä valitessa.* 

# Lisätietoja

[Mikä merkitys tileillä, tilikartalla ja raporttimalleilla on Finazillassa? Mihin näitä käytetään?](

[Raporttimallit ovat raportoinnissa käytettävä työkalu](

[Valmiin raporttimallin hyödyntäminen raportoinnissa](

[Valmiin raporttimallin muokkaaminen omiin tarpeisiin sopivaksi](

[Raporttimallin rakentaminen alusta saakka](

[Operatiivisen raporttimallin luominen silloin kun raportoitava data on 100% operatiivista dataa](

[Operatiivista dataa ja kirjanpidon dataa yhdistävän raporttimallin luominen Finazillaan](



artikkelin osoite on https://intercom.help/finazilla/fi/articles/4341662-yleiskuvaus-raporttimalleista-seka-kuvaus-finazillan-valmiiksi-luomista-raporttimalleista

