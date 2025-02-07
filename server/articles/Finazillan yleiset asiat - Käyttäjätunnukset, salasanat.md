## Käyttäjätunnukset, salasanat

# Käyttäjätunnukset, salasanat

```
 Kysymys: Unohdin salanani. Mistä saan uuden salanana?
```

Vastaus: Yrityksenne pääkäyttäjä (nk. Customer tasoinen käyttäjä) voi antaa sinulle uuden salanan, joten ole yhteydessä yrityksenne pääkäyttäjään. Mikäli olet itse yrityksenne pääkäyttäjä, saat uuden salanan olemalla yhteydessä Finazillan asiakaspalveluun ([asiakaspalvelu@finazilla.fi](mailto:asiakaspalvelu@finazilla.fi)).

Salasana resetoidaan "Users" valikossa kohdassa "reset password".

Jos olet siirtynyt käyttämään kaksivaiheista tunnistautumista, et käytä enää salasanaa. Tällöin pääkäyttäjäkään ei voi resetoida sinulle uutta salasanaa, vaan tunnistautuminen tehdään valitsemallasi kaksivaiheisella tavalla.

```
 Kysymys: Haluan vaihtaa salanani. Mistä saan sen tehtyä?
```

Vastaus: Rippuu roolista, mikä käyttäjätunnuksellesi on annettu. Mikäli sinulla on oikeus vaihtaa oma salasanasi, pääset sinne kätevimmin oikean yläkulman käyttäjätunnuksen kautta. Käyttäjätunnuksesi kohdalta aukeaa alasvetovelikko, jossa on vaihtoehto "settings". Valikon kautta voi vaihtaa omaa salasanaa, mikäli on siihen oikeudet.

Customer -tasoiset asiakkuuden pääkäyttäjät voivat vaihtaa salasanansa milloin tahansa myös Customer -valikossa kohdassa "users" käyttämällä joko "change password" tai "reset password" vaihtoehtoa. Customer -käyttäjä voi vaihtaa salasanan myös kenelle tahansa toiselle Finazilla -käyttäjälle (poislukien käyttäjät, jotka käyttävät kaksivaiheista tunnistautumista).

Yritystasoiset pääkäyttäjät (CompanySuperUser) voivat vaihtaa salasanansa milloin tahansa myös Company -valikossa kohdassa "users" käyttämällä "change password" tai "reset password" -toimintoa.

"Rajatun roolin" salasanan vaihtaa aina asiakkuuden pääkäyttäjä, mikäli kyseisellä roolilla ei ole oikeuksia käyttäjänhallintaan.

Kaksivaiheista kirjautumista käyttävät käyttäjät eivät voi koskaan vaihtaa salasanaansa, sillä heillä ei ole salasanaa käytössä.

```
Kysymys: Meille tulee uusi käyttäjä Finazillaan. Miten minun tulee toimia?
```

Vastaus: Yrityksen pääkäyttäjä voi luoda uudelle käyttäjälle käyttäjätunnukset Users -valikossa. Customer users -valikkoon luodut käyttäjät ovat pääkäyttäjiä ja company users -valikkoon luodut ovat rajoitetumman oikeuden käyttäjiä. Company users -valikkoon luodulle käyttäjälle tulee aina kiinnittää jokin rooli. Rooleista lisää mm. [täällä.]( 

Suosittelemme luotujen käyttäjätunnusten testaamista ennen niiden luovuttamista, jotta voidaan varmistua tunnusten toimivuudesta, sekä oikeista käyttöoikeuksista.

```
Kysymys: Miten saan poistettua käyttäjän?
```

Vastaus: Yrityksen pääkäyttäjä pystyy hallinnoimaan käyttäjätunnuksia Users-valikossa. Jos kyseiselle käyttäjälle on jaettu raportteja/dashboardeja niin poisto ei onnistu suoraan, vaan tällöin tulee ensin poistaa tällaiset jaot ja sen jälkeen käyttäjätunnuksen voi poistaa.

Käyttäjätunnuksen voi myös laittaa päivämäärin päättyneeksi, mikäli tunnusta ei haluta kokonaan poistaa.

```
Kysymys: Mistä tiedän mitä oikeuksia minulla on Finazillassa?
```

Vastaus: Yrityksenne pääkäyttäjä voi kertoa sinulle oikeuksistasi. Jos olet itse yrityksenne pääkäyttäjä, on sinulla kaikki oikeudet.

```
Kysymys: Miten saan käyttäjän lisättyä asiakkuuden toisenkin yrityksen alle?
```

Vastaus: Jos käyttäjä on Customer -tasoinen, on hänellä jo oikeudet kaikkialle. Company -tasoiselle käyttäjälle oikeudet määritellään roolien kautta Company - Users -valikossa. Kun käyttäjälle ollaan kiinnittämässä roolia, voidaan määritellä samalla mihin yritykseen rooli sidotaan. Valitaan haluttu yritys "Company" alasvetovalikosta.

# Tiedonsiirto, datat

```
Kysymys: Tein muutoksia kirjanpitoon.   
Miten voin päivittää muutokset Finazillaan kesken päivän?
```

Vastaus: Tämä riippuu siitä, millä metodilla datat tuodaan Finazillaan. Finazillan asiakkaat voivat käyttää tiedonsiirtoon joko API -rajapintaa/integraatiota, sftp- palvelimelta noutoa tai manuaalisempaa drop in -tapaa. *Päivitystapa riippuu siitä, mikä menetelmä yrityksellä on käytössä.* 

Datat voi päivittää Finazillaan milloin tahansa valikossa company kohdassa settings. Näkymässä on välilehti "integrations", jossa datat päivitetään. Päivitystapa riippuu onko käytössä integraatio vai drop in -tyyppinen tiedonsiirto.

Mikäli käytössä on ***API -rajapinta/integraatio,*** täpätään mitä aineistoa halutaan tuoda, sekä aikaväli ja käynnistetään ajo. API -rajapintaa/integraatiota käyttävien (mm. Procountor, Netvisor, Lemonsoft, Fivaldi jne) päivitystapa on kuvattu tarkemmin [täällä.]( 

***Drop in tiedonsiirrossa*** oikea siirtotiedosto tipautetaan integration file drop -in laatikkoon. Tarkemmat ohjeet löytyvät [täältä.](#h_4fc66572c9) 

Mikäli käytössä on ***sftp -palvelimelta nouto***, tulee uusi tiedosto ladata kansioon, mistä Finazilla noutaa aineiston ajastuksen mukaisesti. Kansiosta ja noutosyklistä on sovittu käyttöönoton yhteydessä. Tyypillisesti kansio on asiakkaan omalla sftp -palvelimella ja noutosykli on lukuisia kertoja päivän aikana.

```
Kysymys: Mistä johtuu, että Finazillan raportointi ja   
kirjanpidon järjestelmämme raportointi näyttävät eri lukuja?
```

Vastaus: Jos käytössä on integraatio, tulee huomioida, että jos kirjanpitoon on tehty muutoksia yli 100 päivää taakse, niin muutokset puuttuvat Finazillasta. Lisäksi jos verrataan lähdejärjestelmän raporttia ja Finazillaa keskenään, niin Finazillasta puuttuu aina myös kuluvan päivän tositteet, sillä yöllinen integraatio ajaa tositteet siitä hetkestä 100 päivää taaksepäin. Mikäli tämä on erotuksen syy, tulee aineistot ajaa manuaalisesti uudelleen sisään.

Jos käytössä on drop- in tiedonsiirto, tulee muutosten jälkeen uusi tiedosto tuoda Finazillaan.

Mikäli näistä ei ole apua, tulee olla yhteydessä asiakaspalveluumme.

```
Kysymys: Mistä johtuu, että Finazillan tase raportoi yhtäkkiä   
uudella tilikaudella taseen muutosta eikä kumulatiivista saldoa?
```

Vastaus: Todennäköisesti lähdejärjestelmässä ei ole suljettu kuukausia, jolloin taseen avaavia saldoja ei muodostu. Asian saa korjattua sulkemalla kaudet, tuomalla datat sisään uudelleen (jos muutos on yli 100 päivää taaksepäin).

# Yleiset asetukset, muut

```
Kysymys: Tilikautemme vaihtuu. Mitä minun pitää muistaa tehdä Finazillassa?
```

Vastaus: Aktiivinen tilikausi tulee vaihtaa valikossa Company kohdassa "Accounting period". Samalla on hyvä varmistaa, että onko Finazillassa tilikausia riittävän pitkälle tulevia budjetteja varten, sillä budjetin voi luoda vain tilikausille, jotka löytyvät Finazillasta.

```
Kysymys: Konserniimme tulee uusi yritys. Mitä minun tulee tehdä Finazillassa?
```

Vastaus: Asiakkuuden pääkäyttäjä voi perustaa uuden yrityksen Finazillaan. Ensin tulee luoda yritys, määrittää sille tilikartta ja tuoda sisään kirjanpidon tilit. Täsmäytystilit tulee määritellä tämän jälkeen. Yritykselle määritellään myös tilikaudet ja valitaan oikea tilikausi aktiiviseksi.

Luodulle yritykselle voidaan kopioida halutut raporttimallit valmiiksi sekä luoda valmis "master budget" osabudjetteineen.

Jos yritys on integraation piirissä, kytketään viimeisenä integraatio päälle ja tuodaan datat halutulta ajalta sisälle ja lasketetaan saldot. Yritykselle tulee tuoda sisään vähintäänkin tase ja tuloslaskelma, jotta saldot lähtevät juoksemaan oikein.

Raportit tulee täsmäyttää lähdejärjestelmään.

Suosittelemme myös katsomaan konserneihin liittyvät ohjeemme [konsernitilien merkitsemiseen]( ja [yrityksen konserniin kuulumiseen]( liittyen. Kaikki konserneihin liittyvät ohjeet löytyvät [täältä.]( 

```
Kysymys: En osaa luoda Finazillaan sellaista raporttia/  
raporttimallia tms, minkä tarvitsisin. Mitä minun tulee tehdä?
```

Vastaus: Suosittelemme katsomaan käyttöohjeestamme ohjeet liittyen raporttimalleihin. Ohjeet löytyvät [täältä.](

Neuvomme asiakaspalvelussa aina kaikessa käyttämiseen liittyvässä teknisessä asiassa koulutettuja pääkäyttäjiä. Tämän lisäksi teemme paljon asiakkaillemme valmiita raportteja/raporttimalleja tms. tuntityönä, joten tämäkin vaihtoehto kannattaa pitää mielessä.

```
Kysymys: Yrityksemme haluaisi alkaa hyödyntämään operatiivista dataa Finazillassa.   
Kuinka pääsisimme asiassa eteenpäin?
```

Vastaus: Operatiivinen data on oma maailmansa ja tätä ei ehditä käymään peruskoulutuksessa läpi. Tästä syystä suosittelemme, että varaatte erillisen koulutuksen aiheesta. Koulutus voidaan räätälöidä vastaamaan juuri teidän tarpeitanne.

Help Centeristämme löytyy myös ohjeita [operatiivisen datan]( kokoelman alta.

# Raportointi, raporttien jakaminen

```
Kysymys: Miten saan jaettua käyttäjälle A tekemäni raportin?
```

Vastaus: Raportin voi jakaa Reports -toiminnoissa raportin nimen perässä olevan "share" -painikkeen kautta. Avautuvasta syöttöikkunasta valitaan käyttäjätunnus, jolle raportti halutaan jakaa.

Toinen tapa jakaa raportti on kansioida sen tagin avulla. Tagin tyypiksi tulee valita esimerkiksi "Company", jos raportti halutaan jakaa Company -tasoisille käyttäjille. Käyttäjän roolille voidaan määrittää oikeus tähän kysiseen tagiin eli kansioon. Tässä tulee huomioida, että raportti näkyy tällöin kaikille company -tasoisille käyttäjille joilla on oikeus kyseisee tagiin.

Eri tapoja jakaa raportteja Finazillassa, olemme kuvanneet tarkemmin [täällä.]( 

```
Kysymys: Miksi en saa raporttia auki?
```

Vastaus: Ensimmäisenä tulee tarkistaa, onko raporttiin oikeudet. Onko raportti itse tehty vai jonkun toisen tekemä? Jos raportti on jonkun toisen luoma, tulee tekijän jakaa raportti henkilöille, joiden tulee saada raportti auki.

Jos raportti ei käyttöoikeuksista huolimatta aukea, voidaan kokeilla seuraavia toimenpiteitä: 1) tyhjennä välimuisti ja kokeile uudelleen. 2) ota raportista kopio ja kokeile aukeaako kopio? Ongelmatilanteissa tulee olla aina yhteydessä asiakaspalveluumme.

```
Kysymys: Miten useamman dimension raportteja kannattaa rakentaa?
```

Vastaus: Tähän on useita tapoja ja lopullinen valinta riippuu raportin sisällöstä ja tarpeesta. Yksi, ja ehkä yleisin, tapa on valita kaikki data raportoitavaksi ja otetaan valinta "include dimensions" raportin asetuksissa. Oletuksena tällä valinnalla dimensiot tulevat raportin filttereihin. Tämän jälkeen raporttia voi järjestellä haluttuun formaattiin pivotoinnin kautta.

Toinen tapa on valita yksi dimensio aina yhteen tietolähteeseen. Tällöin raportille tulee vain luvut, jotka on kohdistettu näille arvoille.

# Dashboard

```
Kysymys: Päivitin raporttia Finazillassa, mutta muutos ei päivittynyt Dashboardille.   
Mitä minun tulee tehdä?
```

Vastaus: Dashboard hyödyntää välimuistia, joten kesken päivän tehdyt muutokset eivät lataudu automaattisesti heti raportille (esimerkiksi lukituspäivän muutos).

Dashboardilla on raportin oikeassa yläkulmassa "päivitysnappi", jota painamalla raportin luvut haetaan uudelleen välimuistista ja ne päivittyvät. Päivittyminen tapahtuu myös jos käyttäjä käy raportit -välilehdellä avaamassa kyseisen raportin ja palaa sen jälkeen takaisin Dashboardille. Tällöin käyttäjän ei tarvitse painaa enää "refresh" päivitysnappia Dashboardilla erikseen.

# Budjetointi

```
Kysymys: Miksi en pysty budjetoimaan haluamalleni dimensiolle?
```

Vastaus: Tarkista, että kyseisillä dimensioilla/arvoilla ei ole hidden from budgeting täppää valikossa Company - Dimensions.

Dimensioita voidaan myös rajata käyttöoikeuksin. Onhan sinulla oikeudet kyseiseen dimensioon?

```
Kysymys: Miksi en pysty tekemään budjettiin muutoksia?
```

Vastaus: Tarkista onko budjetti lukittu. Usein budjetin valmistumisen jälkeen budjetti lukitaan. Lukitus estää syötön pääbudjetille sekä osabudjeteille.

Lukitus näkyy budget -valikossa kyseisen budjetin perässä olevan "edit" toiminnon kautta. Lock date kenttä indikoi lukituksesta. Lukituksen voi poistaa, tehdä korjaukset budjettiin ja laittaa lukituksen uudelleen päälle. Huomaa tässä kuitenkin yrityksenne sisäiset ohjeistukset ja toimintatavat sen suhteen, saako lukittua budjettia vielä muuttaa.

Budjetille voidaan myös rajata muokkausoikeuksia käyttäjätunnuskohtaisesti. Onko sinulla oikeudet muokata kyseistä budjettia?

```
Kysymys: Yritin muuttaa rullaavan budjetin aikaväliä, mutta saan oheisen  
error ilmoituksen. Miksi? 
```
[![](

Vastaus: tilikausista puuttuu seuraava tilikausi. Ongelma poistuu kun käy lisäämässä uuden tilikauden.

```
Kysymys: En saa kopioitua osabudjettia toiselle asiakkuuden yritykselle.   
Saan "400 Bad Request error" ilmoituksen. Miksi?   

```

Vastaus: Syynä voi olla se, että osabudjetilla on jokin tiliohjaus sellaiselle tilille, mitä tällä toisella yrityksellä ei ole olemassa. Ongelman voi ratkaista joko perustamalla puuttuvan tilin yritykseen, josta se puuttuu tai poistamalla osabudjetista tiliohjauksen ennen kopiointia. Jos valitaan jälkimmäinen vaihtoehto, tulee tiliohjaus palauttaa takaisin kopion jälkeen, sekä tarkistaa tiliohjaus kuntoon uudelle kopioidulle osabudjetille.



artikkelin osoite on https://intercom.help/finazilla/fi/articles/4311864-yleisimmin-kysytyt-kysymykset

