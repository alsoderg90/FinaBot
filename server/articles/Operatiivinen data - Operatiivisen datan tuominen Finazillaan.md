## Operatiivisen datan tuominen Finazillaan

Operatiivista dataa voidaan tuoda Finazillaan ja tuotua tietoa voidaan raportoida joko puhtaasti operatiivisena datana sellaisenaan, yhdessä kirjanpidon datan kanssa tai yhdistelemällä näitä kahta ja suorittamalla näiden välillä laskentaa. Tämä artikkeli käsittelee edellämainituista vaihtoehdoista ensimmäistä.

Tämä artikkeli vastaa tarpeeseen, jossa halutaan tuoda operatiivinen data Finazillaan ja raportoida sitä *sellaisenaan* rikastamatta.

# Operatiivisen datan tuominen Finazillaan

Jotta operatiivista dataa voidaan raportoida Finazillassa, tulee Finazillaan tuoda ensin operatiivinen data. Pähkinän kuoressa tiedon tuominen tapahtuu siten, että valitaan tiedosto, joka haluaan tuoda Finazillaan tai luodaan itse CSV -tiedosto, jossa on header-rivi josta löytyy seuraavat columnit: Date, Amount *TAI* Quantity. Data tuodaan operatiivisena datana sisään.

Jos / kun tuodaan operatiivista dataa, missä on uusia dimensioita ja / tai dimensiovalueita, tulee näille käydä antamassa manuaalisesti dimension code, jotta ne nousevat raportille mukaan. Dimensiocoden muokkaaminen on opastettu artikkelissamme "[Dimension ja dimensioarvon koodin muokkaaminen kun aineistossa on mukana uusia dimensioita](".

# Operatiivisen datan raportointi

Itse raportointi tapahtuu Reports -välilehdellä, jossa valitaan "New report" ja valitaan raportille raporttimalliksi "system operative data". Raportille annetaan nimi sekä valitaan haluttu aikaväli ja muut halutut raportin asetukset.

Kun raportti avataan, tulee raportille kaikki yrityksen operatiiviset data groupit omille riveilleen. Raporttia voi tämän jälkeen pivotoida haluttuun formaattiin.

[![](

*Kyseinen raporttimalli näkyy yrityksissä joissa on customer asetuksista System -tasoiset raporttimallit näkyvissä.*

# Lisätietoja

[Mitä operatiivinen data on ja miten sitä voidaan käyttää Finazillassa?](

[Operatiivisen datan tuominen Finazillaan vakiomuotoisella CSV -siirtotiedostolla](



artikkelin osoite on https://intercom.help/finazilla/fi/articles/4301546-operatiivisen-datan-raportointi

