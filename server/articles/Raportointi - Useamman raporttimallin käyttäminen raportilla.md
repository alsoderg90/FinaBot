## Useamman raporttimallin käyttäminen raportilla

[![](

*Versiopäivityksessä 30.11.2024 tuotu kokonaan uusi toiminto. Toiminto mahdollistaa useamman raporttimallin käyttämisen yhdessä ja samassa raportissa. Raporttimalli voidaan valita jokaiselle raportin tietolähteelle erikseen.* 

# Useamman raporttimallin käyttäminen raportilla

Mikäli jollain raportilla halutaan käyttää useaa eri raporttimallia, tulee lisäasetuksista (advanced settings) asettaa kyseinen valinta päälle kohdasta "Datasource specific report scheme".

[![](

Kun asetuksista on laitettu päälle valinta, että raportilla halutaan käyttää tietolähdekohtaista raporttimallia, tulee valintaikkuna näkyviin jokaiselle raportin tietolähteelle. Oletuksena kentässä on valittuna se raporttimalli, mikä raportin asetuksiin (settings) on valittu, mutta valintaa voi muuttaa.

[![](

Kun käyttäjä tekee raporttiin seuraavan tietolähteen (datasource), tulee sinne oletuksena jälleen raportin settings -valikossa valittu oletusraporttimalli. Raporttimallin voi vaihtaa alasvetovalikosta.

# Mitä toiminto mahdollistaa

Usean raporttimallin yhdistäminen yhteen ja samaan raporttiin tuo raportointiin lisää ketteryyttä, sillä käyttäjän ei tarvitse välttämättä luoda kaikkia tilanteita varten uutta raporttimallia, vaan olemassa olevia raporttimalleja voidaan käyttää suoraan ja yhdistellä samaan raporttiin.

Havainnollistamme ominaisuuden mahdollisuuksia muutamalla esimerkillä alla.

## Esimerkki 1: yhdistellään tuloksen dataan tasetta

Käyttäjällä on oma hieman muokattu tuloslaskelma -raporttimalli. Osassa raporteissa haluttaisiin kuitenkin tuoda raporttiin mukaan pankkitilin saldo. Osassa tätä ei haluta.

Toiminto mahdollistaa sen, että tuloslaskelma -raporttimalliin ei tarvitse tehdä muutoksia. Käyttäjä voi tehdä uuden raporttimallin, missä raportoidaan pankkitili. Tämän jälkeen raportille tehdään kaksi tietolähdettä: toiseen valitaan tuloslaskelma ja toiseen pankkitili -raporttimallit. Näin ollen kyseiseen raporttiin saadaan halutut tiedot ja muihin raportteihin, joihin pankkitiliä ei haluta, ei tarvitse tehdä mitään muutoksia. Niissä voidaan käyttää "normaalia perinteistä" yhden raporttimallin taktiikkaa.

## Esimerkki 2: talousdatan ja operatiivisen datan yhdistäminen

Yrityksellä on olemassa kirjanpidossa myyntiä kausilla 1-6. Tätä pidemmälle myyntiä ei vielä ole olemassa. Yrityksellä on kuitenkin Finazillassa tilauskanta, joka kertoo, mitä myyntiä on jo varmistunut kausille 7-12.

Alla olevassa raportissa on kaksi tietolähdettä, joissa on kummassakin oma raporttimallinsa. Ensimmäinen raporttimalli raportoi kirjanpidon myyntiä tililtä 3000 ja toinen raporttimalli raportoi operatiivisena datana Finazillassa olevaa tilauskantaa.

[![](

[![](

*Korostamme, että toiminnon avulla voidaan yhdistellä aivan vapaasti talousdataa ja operatiivista dataa ja tehdä näiden välillä laskentaa. Yllä kuvatut esimerkit ovat vain murto-osa mahdollisuuksista, mitä toiminto mahdollistaa.*

# Yleinen toimintalogiikka

Jokaisella Finazillan raportilla on aina raporttimalli. Raporttimalli valitaan raportilla kohdassa settings. Normaalissa tavallisessa raportoinnissa raporttimallin valinnat on nyt tehty ja sen suhteen kaikki on valmista.

Mikäli halutaan tehdä raportointia, jossa käytetään useampaa raporttimallia, on logiikasta hyvä ymmärtää se, että ***settings -valikossa valittu raporttimalli on aina raportin oletusvalinta***. Oletusvalintaa voidaan muuttaa raportin tietolähteillä siten, että kullekin tietolähteelle voidaan valita oma erillinen jokin muu raporttimallinsa. Tällöin tietolähteelle valittu raporttimalli pätee kyseisen tietolähteen osalta. Oletusvalinta pätee siis aina, mikäli muuta ei ole valittu.

## Havainnollistava esimerkki:

settings -valikkoon on valittu yleiseksi raporttimalliksi tuloslaskelma (system). Raportilla on kaksi tietolähdettä:

* Toteuma kuluvalta tilikaudelta
* Toteuma edelliseltä tilikaudelta

Kuluvalle tilikaudelle käydään valitsemassa raportin tietolähteisiin erikseen raporttimalliksi asiakkaan itsensä tekemä tuloslaskelma -raporttimalli. Näin ollen varsinainen raportti muodostetaan siten, että edellinen tilikausi raportoidaan system tasoisella tuloslaskelma -raporttimallilla ja kuluva tilikausi asiakkaan omalla tuloslaskelma -raporttimallilla.

Jos käyttäjä käy laittamassa myös edelliselle tilikaudelle tietolähteelle kiinnitykseksi itse tekemänsä tuloslaskelma -raporttimallin, käytetään sitä myös edellisen tilikauden raportissa.

Huomaa, että tietyissä tilanteissa settings -valikon raporttimallilla ei ole välttämättä vaikutusta raporttiin, vaan se kertoo, mikä raporttimalli otettaisiin käyttöön jos:

* Joltain tietolähteeltä poistettaisiin tietolähdekohtainen raporttimalli ja/tai
* Raportille lisättäisiin uusi tietolähde ilman tietolähdekohtaista raporttimallia
[![](

*Suosittelemme katsomaan webinaarimme 27.11.2024, jonka aiheena on edistyksellinen raportointi. Webinaarin alussa esitellään usean raporttimallin käyttämistä ja tällaisen raportin nostamista Dashboardille. Webinaarit löytyvät system Dashboardilta Finazilla webinars.* 

​



artikkelin osoite on https://intercom.help/finazilla/fi/articles/10125837-useamman-raporttimallin-kayttaminen-samalla-raportilla

