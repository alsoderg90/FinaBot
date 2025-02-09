## Ennen raportointia

# Ennen raportointia

Ennen kuin päästään raportoimaan Finazillassa on tätä edeltänyt erilaisia asiakkuuden ja yhtiön perustoimenpiteitä, jotka on yleensä tehty Finazillan tiimin puolesta.

Raportointia edeltää myös tarpeellisten raporttimallien luominen, joihin liittyvät artikkelit löytyvät esimerkiksi hakusanalla "raporttimalli". Perusraporttimalleja, kuten mm. tuloslaskelma, tase, rahoituslaskelma, erilaiset kateprosentit, myyntisaamiset jne löytyy myös valmiina kattava valikoima. Jos valmiit mallit täyttävät raportoinnille asetetut tarpeet, voi raportoimaan alkaa vaikka heti.

# Raportointi

Raportointi –toimintoon mennään sivun yläkulman Reports –painikkeesta. Raportointinäkymässä näkyy kaikki raportit, jotka käyttäjätunnuksella on luotu. Raportit ovat siis käyttäjäkohtaisia.

Uuden raportin muodostaminen alkaa "new report" painikkeen kautta.

[![](

## Raportin perustiedot

Ennen tietolähteiden muodostamista raportti nimetään aina. Nimitieto on pakollinen aina jos raportti halutaan tallentaa. Tämän lisäksi kahta saman nimistä raporttia ei voi olla saman yrityksen raporteissa. Nimeäminen suositellaan tehtäväksi mahdollisimman kuvaavasti ja nimen alussa on hyvä olla yrityksen tunnus, jos käyttäjällä on oikeus useampaan yritykseen. Näin raportit on nopeampi löytää raporttilistalta.

[![](

Raporttimallin valinta tapahtuu kohdassa "Report scheme"**.** Alasvetovalikosta valitaan raporttimalli, jolla halutaan raportoida (tässä esimerkissä on valittu system tasoinen tuloslaskelma).

***Raporttimalli määrittää raportin rakenteen*** eli minkä nimisiä rivejä raportilla on ja minkä tilien tietoa tai mitä kaavoja rivit sisältävät. Finazillassa on valmiina tyypillisimmät raporttimallit ja lisäksi raporttimalleja voi rakentaa itse tarpeen mukaan lisää.

Raporttimalli valitaan alasvetovalikosta, jossa asiakkuuden raporttimallit ovat aakkosjärjestyksessä. Kunkin raporttimallin perässä lukee sulkeissa sen "scope". Jos "scopessa" lukee "System", tarkoittaa se, että raporttimalli on valmis Finazillan luoma raporttimalli. Scope "Customer" taasen viittaa asiakkaan itsensä luomaan omaan asiakastasoiseen raporttimalliin. Mahdolliset yrityskohtaiset raporttimallit ovat tunnisteella company.

[![](

## Raportin lisäasetukset (advanced settings)

Raporteille voidaan jo ennakkoon määritellä esitystapaan liittyviä asioita. Date Format kohdassa on oletuksena vaihtoehto ” Year And Month”, joka on hyvä valinta useimmille raporteille. Jos kuitenkin raportille muodostetaan useita tietolähteitä, joilla on eri aikajaksovalinnat (esimerkiksi Previous ja Current) suositellaan valittavaksi ”Month” esitystapa. Tällöin tietolähteille saa paremman esitystavan valmiilla raportilla. Vastaavasti taas esimerkiksi operatiivisen datan raporteissa voidaan valita year and month and day, jolloin raportti saadaan päivätasoisena.

Raportin lisäsetuksissa voidaan muuttaa mm. luvun tarkkuuttaa (precision). Vaihtoehtona esittää luvut tuhansina tai miljoonina. Lisäksi valuutan voi myös vaihtaa, mikäli se on jokin muu kuin euro.

[![](

## Tietolähteiden määrittely

Kun raportille valitaan raporttimalli, tekee Finazilla automaattisesti raportille yhden tietolähteen, jota voidaan lähteä määrittelemään ja muokkaamaan. Tietolähteitä pitää olla raportilla vähintään 1, mutta niitä voi olla myös useita. Tietolähteissä valitaan mitä dataa (toteutunutta vai budjetoitua dataa) raportoidaan ja miltä ajalta (esimerkiksi kuluva tilikausi, edellinen jne.)

Jos siis esimerkiksi halutaan samalle raportille edellinen tilikausi ja kuluva tilikausi, tehdään raportille kaksi erillistä tietolähdettä. Toinen tietolähde on edellinen tilikausi ja toinen tietolähde on kuluva tilikausi.

Finazillan raportointi on dynaamista, mikä tarkoittaa käytännössä sitä, että tilikauden vaihtuessa tehtyjä raportteja ei tarvitse tehdä uudelleen eikä kopioida uudelleen. Kun yrityksen asetuksista käydään vaihtamassa uusi tilikausi aktiiviseksi, raportoi Finazillan sen mukaisesti esimerkiksi yllä mainitulla edellinen tilikausi vs nykyinen tilikausi raportilla.

Raportilla oleva tietolähde voi olla myös kaava, joka hyödyntää raportin muita tietolähteitä, eli esimerkiksi kuluva tilikausi miinus edellinen tilikausi. Kaavoja voi muodostaa myös myöhemminkin raportin ollessa jo valmis pivotointi –toiminnossa lisäämällä ”Add calculated value”.

# Raportin muodostaminen kostuu siis tiivistetysti aina seuraavista päävaiheista:

1. Raportin perustietojen ja asetusten määritteleminen (settings)
2. Raportin esitystavan ennakkomäärittelyt, mikäli tarpeen muuttaa (advanced settings)
3. Tietolähteiden määrittely (datasource)

Raportin muodostamista olemme opastaneet tarkemmin työohjeissamme, jotka löytyvät hakusanalla "raportointi".



artikkelin osoite on https://intercom.help/finazilla/fi/articles/4362794-raportoinnissa-tehtavat-perusmaarittelyt

