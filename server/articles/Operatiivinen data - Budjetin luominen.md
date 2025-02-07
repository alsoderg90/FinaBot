## Budjetin luominen

Tämä artikkeli on edistyneemmille käyttäjille, joten oletusarvona on, että käyttäjä osaa jo luoda perinteisen kirjanpidon budjetin sekä raportoida tehtyä budjettia. Lisäksi käyttäjä osaa tuoda Finazillaan operatiivista dataa sekä raportoida sitä.

Tässä artikkelissa kuvataan yleisellä tasolla, miten operatiivista dataa voidaan budjetoida siten, että kyseistä operatiivista budjetointia voi hyödyntää kirjanpidon budjetin laskennassa.

# Budjetin luominen

Operatiivisen datan budjetointi alkaa siitä, että Finazillaan luodaan budjetti. Operatiivisen datan budjetoinnissa on tärkeää hahmottaa, että *operatiivinen data syötetään aina osabudjetin kautta*, joten budjetille tulee luoda myös osabudjetti. Operatiivista dataa ei voi siis koskaan budjetoida pääbudjetin kautta.

# Budjetoitavan datan kohdistaminen operatiivisille dimensioille

Operatiivisen datan budjetoinnissa kohdistus operatiivisille dimensioille tapahtuu aina rivikohtaisesti. Käytännössä tämä tarkoittaa sitä, että osabudjettiin luodaan rivi, mihin valitaan, mitä operatiivista dataa siihen syötetään ja mille data groupille data kohdistetaan. Jos rivin tyyppinä on "quantity", syötetään sille määreitä (kuten vaikkapa työtunteja). Jos rivin tyyppinä on "input" tai "formula", syötetään riville arvoja eli euroja.

Transfer to Data group -kenttään voidaan valita jokin alasvetovalikon valmiista vaihtoehdoista (eli ne operatiiviset datatyypit mitä Finazillaan on tuotu aikaisemmin sisään) tai kirjoitetaan siihen vapaasti jokin muu teksti. "Operative dimension target" -kenttään tulee valita se operatiivinen dimensio, jolle lukuja budjetoidaan.

[![](

Tämän jälkeen voidaan budjetoida normaalisti ja syöttää luodulle riville arvoja.

# Tiivistetysti

* Rivityypille Input ja Formula syötetään euroja
* Rivityypille Quantity syötetään esimerkiksi kappaleita, tunteja jne
* Transfer to Data group määrittää, mille datatyypille tieto kohdistetaan. Voidaan valita valmiista vaihtoehdoista tai kirjoittaa haluttu. Tulee näkyviin raportin riveihin.
* Operative dimension target määrittää, mille operatiiviselle dimensiolle tieto kohdistetaan. Valittavana yrityksen operatiiviset dimensiot. Logiikka on muutoin sama kuin balance -dimensiolle kohdistaminen.
# Budjetin raportoiminen

Tämän jälkeen tehtyä budjettia voidaan raportoida käyttämällä esimerkiksi systeemitason operatiivista raporttimallia. Valmiin raporttimallin nimi on "(System) Operative data". Raportillla näkyy syötetyt luvut rivillä, minkä nimi on annettu data group. Raportin luvut on kohdistettu niille dimension arvoille, mihin kohdistus budjetilla tehtiin (kunhan raportti on dimensio / column -valinnalla luotu).

Raporttia voi tämän jälkeen pivotoida halutunlaiseksi. Raporttimalleja voi luoda myös lisäksi itse, ja saada raporttia tätä kautta muokattua haluttuun suuntaan.

[![](

*Mikäli lukujen halutaan kohdistuvan pääbudjetin jollekin tilille, ja siten nousevan myös kirjanpidon kautta raportoitavaksi, tulee riveihin kiinnittää tiliohjaus. Aivan kuten osabudjetilla muutoinkin .*

# Lisätietoja

[Operatiivisen datan raportointi](

[Puhtaasti operatiivisen raporttimallin luominen](

[Operatiivisen datan budjetointi operatiivisille dimensioille](



artikkelin osoite on https://intercom.help/finazilla/fi/articles/4311726-operatiivisen-datan-budjetointi-osa-1-puhdas-operatiivinen-data

