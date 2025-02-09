## Ennustebudjetin luominen

Joskus voi olla miellekästä raportoida toteumaa ja ennustetta yhtäaikaa samassa raportissa siten, että raportista käy selkeästi ilmi mikä osuus on toteumaa ja mikä ennustetta.

Usein tämänkaltainen käyttötarve tulee esiin kun raportoidaan ennustetta, jossa on vaikka 2 kuukautta toteumaa ja loput 10 kuukautta ennustetta. Raportti päivittyy sitä mukaa kun toteumadataa saadaan sisään ja näin ollen ennuste korvautuu toteumadatalla.

# Ennustebudjetin luominen

Kun yrityksen budjetti on valmistunut, lukitusta budjetista otetaan kopio, jonka tyypiksi vaihdetaan "Forecast budget". Kopio tehdään samalle vuodelle kuin millä alkuperäinen budjettikin oli ja tehtävään kopioon sisällytetään kaikki data (eli kopioidaan myös luvut). Tätä versiota voidaan muokata ja sitä voidaan verrata alkuperäiseen lukittuun budjettiin.

# Toteuman tuominen ennustebudjetille

Kun budjetin tyyppi on "Forecast budget", muuttuu lock date -kenttä "Real balance end date" nimiseksi kentäksi. Tällä kentällä määritellään, mihin päivään saakka ennustebudjettiin halutaan tuoda toteumadataa. Loppuosa on ennustetta. Ennusteluvut korvautuvat aina toteumaluvuilla kun real balance end date -päivää päivitetään.

Real balance end date -kenttää voidaan hallinoida joko manuaalisesti syöttämällä siihen jokin haluttu päivämäärä tai käyttää valintaa "use accounting lock date", joka tuo ennustebudjetille aina oletuksena company -accounting periods valikossa asetetun lukituspäivän.

Tässä esimerkissä yrityksen lock date on asetettu 31.1.2021 päivään ja kyseisen budjetin real balance end date on asetettu käyttämään lukituspäivää.

[![](

# Raportin luominen

Luodaan raportille kaksi tietolähdettä, eli datasourcea, joissa molemmissa report type -valintana on "Accounting period". Taustalla on yksi yritys ja yksi ennustebudjetti, johon on tuotu toteumadataa siihen saakka kuin sitä on saatavilla. Loppuosa on ennustetta.

[![](

*Tietolähteet menevät raportille aina oletuksena aakkosjärjestyksessä. Jos tietolähteiden järjetyksen haluaa valita jo nimeämisvaiheessa, voi tietolähteet nimetä vaikka "1. Toteuma" ja "2. Ennuste", jolloin ne menevät numeroiden mukaiseen järjestykseen.*

## Toteumadatan valinnat

Ensimmäiseen tietolähteeseen valitaan ennustebudjetista toteumadatan aikaväli. Nimetään datalähde esim. "1. Toteuma." Kyseisessä tietolähteessä raportoidaan luotua ennustebudjettia ja dynaamisilla rajauksilla määritellään, mikä osuus ennustebudjetista esitetään raportilla.

Valintoina tulee olla kohdassa "Dynamic start date" vaihtoehto "Start date of accounting period", joka onkin ko. valikon oletusasetus. End date -kohtaan valitaan vaihtoehto "Lock date of accounting period".

[![](

​

## Ennustedatan valinnat

Toiseen tietolähteeseen valitaan ennuste. Nimetään datalähde esim. "2. Ennuste". Myös tässä tietolähteessä raportoidaan samaa ennustebudjettia, mutta jälleen dynaamisilla aikavalinnoilla kerrotaan, mitä aikaväliä halutaan raportoida.

Valintoina tulee olla kohdassa "Dynamic start date" vaihtoehto "Next open month". End date -kohtaan valitaan vaihtoehto "End date of accounting period".

[![](

## Luodun raportin muokkaaminen ja pivotointi

Tämän jälkeen luotua raporttia voi pivotoida kuten mitä tahansa muutakin raporttia. Raportista voi luoda myös graafin. Erilaisilla graafisilla raporteilla toteuman ja ennusteen katkon erotus on hieman toisistaan poikkeava -riippuen valitusta graafisesta raportista.

[![](

*Jos raportilla halutaan tuoda esimerkiksi toteuman ja ennusteen yhteenlaskettu summa, voidaan tämä toteuttaa hyödyntämällä kolmatta tietolähdettä, joka olisi kaava. Kaavassa laskettaisiin luodut kaksi tietolähdettä yhteen. Toinen tapa olisi luoda kolmas tietolähde, jossa raportoitaisiin ennustebudjettia valinnalla accounting period/column, joka esittää yhteenlasketun summan sarakkeilla.* 

# Lisätietoja

[Dynaamiset alku- ja loppuajat raportoinnissa mahdollistavat automaattisesti päivittyvät raportit](



artikkelin osoite on https://intercom.help/finazilla/fi/articles/4230329-toteuman-ja-ennusteen-erottelu-raportilla

