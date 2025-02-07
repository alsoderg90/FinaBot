## Kaavan kirjoittaminen

[![](

*Chart beta -graafisiin raportteihin liittyvä parannus. Toiminto mahdollistaa sen, että jatkossa charttiin pystyy lisäämään laskentakaavoja.* Kaavassa on käytössä samat vaihtoehdot kuin "tavallisissa" raporteissa formula- tietolähteillä (plus, minus, kerto, jako ja %-diff)

Olemme kertoneet aikaisemmassa artikkelissamme ["Uusi vaihtoehtoinen tapa luoda graafisia raportteja; chart beta"]( uudesta graafisesta raporttikirjastostamme. Kirjastoon sisältyy pylväs, viiva, pylväs & viiva, piirakka ja pinottu pylväskuvio. Tässä artikkelissa kerromme *kaikkiin edellä mainittuihin* graafisiin raportteihin tehdystä lisämahdollisuudesta.

# Kaavan kirjoittaminen

Uusi lisämahdollisuus mahdollistaa sen, että graafisen raportin widgetissä voidaan kirjoittaa kaavoja add formula -toiminnolla. Kaavoja kirjoitetaan widgettiä luotaessa samassa näkymässä, missä raportin elementit valitaan.

Luonnollisesti, jotta kaava toimii, niin lukujen täytyy olla samalla aikavälillä. Esimerkiksi jos laskee kuluvaa tilikautta miinus (-) edellistä tilikautta niin on käytettävä month valintaa chartissa.

[![](

## Toimintalogiikka

Varsinainen kaavan kirjoittaminen on toimintalogiikaltaan samanlainen kuin "tavallisen" raportoinnin puolella tehtävä formula -tietolähde. Kaavan komponentit valitaan "select report scheme row" kenttiin ja laskentametodi valitaan niiden keskellä olevaan kenttään (kuvassa + -merkki -kohdasta aukeaa alasvetovalikko, josta valinta tehdään).

[![](

Alla olevassa esimerkissä on kirjoitettu kaava, jossa lasketaan kuluvan tilikauden liikevaihto miinus edellisen tilikauden liikevaihto. Kaavoissa on käytettävissä samat laskentaoperaattorit kuin tietolähteillä (plus, minus, kerto, jako ja %-diff).

[![](

Kun kaava on kirjoitettu widgettiin, on näkymä tämänkaltainen:

[![](

Varsinaiselle widgetille laskentakaava tulee tässä tapauksessa pylväänä, sillä kyseinen esimerkki on pylväs graafista. Pylvään nimeksi tulee raportin rivi sekä tietolähteiden rivit.

# Raportin editointi

Widgetin luomisen jälkeen raporttia voidaan editoida widgetin oikean yläkulman ratas -kuvakkeen takaa. Editoinnissa voidaan kertoa, että mikä on pylväiden "*x-akseli" (X-Axis Key)* eli onko esimerkiksi pylväät aseteltu vierekkäin kuukausittain. X- akselin valikosta voidaan vaihtaa valintaa. Kun valintaa vaihtaa, muuttuu raportti Dashboardilla. Näin käyttäjä näkee raportin muutokset heti, ilman että valintaa tarvitsee tallentaa.

## Legend type

*Legend type* -valikosta voidaan vaikuttaa siihen, missä widgetissä esitetään tietolähteiden nimet (tässä esimerkissä liikevaihto kuluva, liikevaihto edellinen ja liikevaihto kuluva miinus liikevaihto edellinen). Valikosta saa myös valinnan none, jolloin tietolähteiden nimiä ei esitetä lainkaan.

[![](

## Bar label settings

*Bar label settings* -valikon takaa graafista raporttia voidaan muokata lisää ja valikon kautta voidaan tuoda esimerkiksi pylväille näytettäväksi niiden arvot. Valikosta voidaan valita, näytetäänkö arvot graafin päällä, keskellä, alla vai ei lainkaan. Myös lukujen väriä voidaan vaihtaa.

[![](

## Advanced settings

*Advanced settings* -valikosta voidaan lisäksi valita, että esitetäänkö raportissa desimaaleja, esitetäänkö raportti tuhansissa vai tehdäänkö raportista ns. stacked bar -tyyppinen. Jälkimmäistä vaihtoehtoa on kuvattu laajemmin artikkelissamme [täällä.](

[![](

# Elementtiä klikkaamalla ja sitä kautta tehtävät muutokset

Elementtiä, eli pylväitä, klikkaamalla niiden väriä voidaan myös vaihtaa muuksi halutuksi. Värivalikosta löytyy valmiita värivaihtoehtoja, mutta sen lisäksi kentään voidaan syöttää mikä tahansa värikoodi käyttämällä # -merkkiä ja kyseisen värin koodia.

Dimension target kenttä mahdollistaa sen, että pylvään voi muuttaa raportoimaan tiettyä haluttua dimensionrvoa. Aihetta on kuvattu enemmän artikkelissamme [täällä.](

Custom name -kentässä elementti voidaan uudelleennimetä halutuksi, jolloin pylvään nimeksi saadaan mitä tahansa. Aiheesta lisää artikkelissamme ["Uusi grafiikkakirjasto: elementin nimeäminen".]( Tämä toiminto on erityisen kätevä esimerkiksi kaavan osalta, sillä sen nimi on usein pitkä.

Custom URL -kenttä on käyttäjille tuttu jo entuudestaan dashboardien kautta. Kenttään voidaan asettaa osoite, johon käyttäjä päätyy kyseistä elementtiä klikatessaan. Jos siis pylväälle asetetaan jokin URL - osoite, pylvästä klikkaamalla käyttäjä päätyy kyseiseen sijaintiin.

[![](

Alla olevassa kuvassa graafista raporttia on muokattu siten, että graafin pylväiden värit on vaihdettuna. Lisäksi raporttia on muotoiltu siten, että X-Axis Key on month, jolloin eri vuosien kuukaudet esitetään vierekkäin. Legend type kohtaan on valittu vaihtoehto "bottom", jolloin tiedot esitetään graafin alareunassa ja bar label settings kohtaan on valittu valinta "top", jolloin numeeriset arvot esitetään pylväiden päällä. Lisäksi kaavan osalta elementti on uudelleennimetty erotukseksi.

[![](

[![](

*Toiminto on käytettävissä kaikilla graafisilla raporteilla (chart beta). Toimintoa voi käyttää yhdessä myös pinotun pylväskuvion (stacked bar) kanssa*



artikkelin osoite on https://intercom.help/finazilla/fi/articles/6752089-uusi-grafiikkakirjasto-kaavojen-lisaaminen-widgettiin

