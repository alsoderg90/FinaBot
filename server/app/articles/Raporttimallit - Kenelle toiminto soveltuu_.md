## Kenelle toiminto soveltuu?

Olemme käsitelleet raporttimallien yleistä merkitystä mm. aikaisemmissa artikkeleissamme ["Yleiskuvaus raporttimalleista sekä kuvaus Finazillan valmiiksi luomista raporttimalleista"]( sekä ["Raporttimallit ovat raportoinnissa käytettävä työkalu".]( 

# **Kenelle toiminto soveltuu?**

Tyypillisesti datan rajaaminen koskettamaan jotakin tiettyä dimensiota, dimensioita tai raportointiryhmiä tehdään raportoinnin puolella käyttämällä raportoinnin rajauksia. Tämä artikkeli on tarkoitettu sellaisille Finazillan käyttäjille, joille perinteinen datan rajaaminen dimensioiden kautta reports -toiminnoissa ei ole riittävä, vaan rajausta on tarpeen tehdä jo raporttimallilla.

Toiminto palvelee mm. konserniyrityksiä, joilla on tarve saada raportin riville valitut kustannuspaikat useista yrityksistä. Toimintoa voi toki käyttää kuka tahansa muukin Finazillan käyttäjä. Raporttimallin kautta datan rajaaminen esittelee ***vaihtoehtoisen*** tavan filtteröidä dataa raportille.

Finazillan raporttimalleilta tämä ominaisuus löytyy raporttirivien luomisikkunassa nimeltä "filter data by dimensions". Ominaisuus on sekä kaikissa uusissa luotavissa raporttimalleissa, että myöskin kaikissa vanhoissa raporttimalleissa.

Toimintalogiikka toteutuksen taustalla on, että haetaan ensin data kuten aikaisemminkin, mutta tämän hakemisen jälkeen sitten filteröidään datasta kaikki arvot pois, mitkä eivät vastaa kyseiselle riville valittuja filttereitä.

# **Filtteröinti dimensiolla tai useammilla dimensioilla**

Yksittäiset dimensiot voidaan valita "select dimensions" kentästä. Kentästä aukeaa valikko kaikista yrityksen dimensioista, joita ei ole piilotettu raportoinnista. Itse filtteröinnin suorittaminen tapahtuu samalla logiikalla kuin raporttivalinnoissa. Dimension itsensä valinta toimii identtisesti siihen nähden, että olisi valittu kaikki sen alla olevat arvot.

Dimensioiden joukossa on valittavana myös nk. blank. Blank tarkoittaa Finazillassa kohdistumatonta/dimensioimatonta.

[![](

[![](

*Jos valitaan arvoja useammasta dimensiosta, niin jotta luku päätyisi kyseiselle riville, on sen oltava matriisi kohdistus, joka sisältää jonkin valituista arvoista kustakin valitusta dimensiosta.*

# **Filtteröinti raportointiryhmällä**

Filtteröintiä voidaan suorittaa myös tekemällä dimensioista raportointiryhmiä. Yritykselle tehdyt raportointiryhmät löytyvät "Reporting group" kentän alasvetovalikosta. Raporttiryhmän valinta toimii identtisesti siihen nähden, että olisi valittu kaikki siihen kuuluvat arvot käsin.

[![](

Toimintoa voidaan käyttää myös siten, että yritykselle 1 kiinnitetään filtteriksi jokin dimensio tai dimensioita ja yritykselle 2 kiinnitetäänkin raportointiryhmä.

[![](

*Vaikka raporttimallilla kerrotaan, millä dimensioilla ja/tai raportointiryhmillä dataa rajataan, voi käyttäjä kuitenkin raportoinnissa valita vaihtoehdon dimensio / column, jolloin raportille voi pivotoida muutakin dataa näkyviin*

# Lisätietoja

[Yleiskuvaus raporttimalleista sekä kuvaus Finazillan valmiiksi luomista raporttimalleista](

[Valmiin raporttimallin hyödyntäminen raportoinnissa](

[Valmiin raporttimallin muokkaaminen omiin tarpeisiin sopivaksi](

[Raporttimallin rakentaminen alusta saakka](

[Mitä dimensiot ovat ja miten niitä käytetään?](

[Dimensioiden valitseminen raportille](

[Mitä raportointiryhmät ovat ja miten niitä käytetään?](

[Raportointiryhmän luominen](



artikkelin osoite on https://intercom.help/finazilla/fi/articles/4829360-raporttimallin-avulla-dimensioiden-filtterointi

