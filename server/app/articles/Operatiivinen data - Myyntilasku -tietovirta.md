## Myyntilasku -tietovirta

Tämä artikkeli koskettaa vain asiakkaita, joilla on lähdejärjestelmänä Procountor tai Netvisor ja siten Finazillaan siirtyy myyntilaskudataa. Artikkelissa esittelemme Procountorin sales -tietovirran avulla, miten Procountorin myyntilaskudatasta voidaan tuoda osabudjetille esimerkiksi edellisen vuoden toteumana toteutuneet myynnit.

Mikäli Procountorin sales -tietovirta on käsitteenä vielä vieras, suosittelemme lukemaan siihen liittyvän artikkelimme ["Procountor sales -tietovirta".]( Tässä yhteydessä Netvisor asiakkaiden tulee huomioida, että Netvisorin sales -tietovirta ei toistaiseksi mahdollista linkitystä kirjanpidon tiliin. Artikkeli, ja tässä kuvattu toiminto, kuitenkin soveltuu myös täysin Netvisor -asiakkaille.

[![](

*Procountor sales ja Netvisor Sales invoces -tietovirran tuottama data on operatiivista dataa, joten niihin sovelletaan operatiivisen datan rapotoinnin sekä budjetoinnin ohjeita.*

# Myyntilasku -tietovirta

Koska myyntilaskujen tietovirran data on operatiivista dataa, tehdään sen budjetointi aina osabudjetin kautta. Näin ollen yritykselle täytyy luoda budjetti, sekä sen taakse erillinen osabudjetti (esimerkiksi myyntibudjetti) tai osabudjetteja.

Budjetoija voi vapaasti päättää, että millä tasolla myyntejä halutaan budjetoida. Procountor sales -tietovirta mahdollistaa budjetoinnin joko yhtiötasolla (kaikki myynnit yhteensä), myyjäkohtaisesti, asiakastasolla ja/tai tuotetasolla. Kaikkia näitä voidaan myös yhdistää, eli budjetointi voidaan tehdä vaikkapa esimerkiksi siten, että osabudjetissa on kukin asiakas, sekä heille myydyt tuotteet.

Tässä esimerkissä budjetointi tehdään asiakaskohtaisesti, eli budjetoinnissa hyödynnetään myyntilaskujen tietovirrasta generoitunutta "customer" dimensiota. Kyseinen dimensio on operatiivinen dimensio.

# Osabudjetin luominen

Yritys on luonut budjetin vuodelle 2023. Seuraavaksi budjetille käydään luomassa uusi osabudjetti myyntejä varten.

[![](

Seuraavaksi luodulle osabudjetille lähdetään luomaan varsinaisia rivejä. Ensimmäisenä osabudjetille luodaan ensimmäinen asiakas, jolle halutaan budjetoida myyntiä. Asiaks luodaan lisäämällä osabudjetille uusi syöttörivi.

Uuden rivin luomisessa on tärkeää valita oikea data group, oikea data type sekä kohdistaa rivi operatiiviselle asiakas -dimensiolle. Tämä kolmen kombinaatio mahdollistaa sen, että myöhemmin osabudjetille voidaan hakea toteumaa nimenomaan procountor sales -tietovirrasta ja tietovirrasta haetaan eurot (amount määreet) ja vain valitun asiakkaan osalta. Näillä kohdistuksilla Finazilla tietää, mitä dataa riville halutaan tuoda.

Netvisor asiakkailla oheinen valinta eroaisi ainoastaan siten, että data group -kohdassa olisi valittuna vaihtoehto "SalesInvoice".

[![](

Seuraavaksi osabudjetin "Asiakas A" riville on mahdollista hakea toteumadataa. Toiminto on vastaava kuin budjetoinnissa muutoinkin oleva import actuals/budget data -toiminto. Toiminto löytyy rivityökaluista.

Ensimmäisenä tulee valita miltä ajanjaksolta toteumaa halutaan tuoda ja mille ajanjaksolle se tuodaan. Tässä esimerkissä tuodaan toteumat ajalta 1-12/2022 budjetin aikajaksolle 1-12/2023.

Data Group -kohtaan tulee kiinnittää Procountor sales(Netvisor asiakkailla SalesInvoice) ja data type kohtaan amount. Lisäksi dimensions -valikosta voidaan valita oikea asiakas. Jos osabudjetilla on vain yksi kohdistus, osaa Finazilla tuoda sen. Jos osabudjetilla on useita dimensioita, saadaan ne tuotua käyttämällä all dimensions -valintaa.

[![](

Tämän jälkeen osabudjetille tulee kyseisen asiakkaan myynti kullekin kuukaudelle toteuman mukaisesti. Lukuja voidaan tämän jälkeen muuttaa ylikirjoittamalla vanha luku - aivan kuten budjetilla muutoinkin.

[![](

*Kun osabudjetille on aika lisätä seuraava asiakas, kannattaa tässä hyödyntää Finazillan create duplicates -toimintoa. Tästä löytyy lisätietoa artikkelistamme "Osabudjetin operatiivisten rivien kopiointi duplicate -toiminnolla".*



artikkelin osoite on https://intercom.help/finazilla/fi/articles/5253320-esimerkki-edellisen-vuoden-myynnit-osabudjetille-pohjaksi

