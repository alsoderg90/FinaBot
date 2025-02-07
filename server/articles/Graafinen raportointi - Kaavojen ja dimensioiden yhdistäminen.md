## Kaavojen ja dimensioiden yhdistäminen

[![](

*Versiopäivityksessä 15.12.2022 tuotu parannus. Jatkossa widgetillä voidaan käyttää dimensionarvoja kaavoissa*

Olemme aikaisemmissa artikkeleissamme kertoneet, kuinka graafisen raportin widgetille voidaan lisätä kaavoja, sekä kuinka jokin dimensio voidaan asettaa widgetin halutuksi elementiksi. Artikkelimme kaavoihin liittyen löytyy linkistä [tästä]( ja dimensiovalitsin elementille artikkelimme löytyy [ohesta.](

Tässä artikkelissa kerromme kuinka kahta aikaisemmin toteutettua ominaisuutta voidaan käyttää jatkossa yhdessä. Toiminto mahdollistaa esimerkiksi kaavan, jossa käytetään eri dimensionarvoja, kuten vaikkapa myynti Jyväskylä miinus myynti Tampere.

# Kaavojen ja dimensioiden yhdistäminen

Widgetin luominen lähtee liikkeelle siitä, että valitaan mitä graafista raporttia ollaan piirtämässä (pylväs, viiva, pylväs & viiva, piirakka). Kaavoja kirjoitetaan widgettiä luotaessa samassa näkymässä, missä raportin elementit valitaan. Widgettiin voi tehdä joko pelkän kaavan tai kaavan muun sisällön ohella.

[![](

## Kaavan kirjoittaminen

Varsinainen kaavan kirjoittaminen on toimintalogiikaltaan samanlainen kuin "tavallisen" raportoinnin puolella tehtävä formula -tietolähde. Kaavan komponentit valitaan "select report scheme row" kenttiin ja laskentametodi valitaan niiden keskellä olevaan kenttään (kuvassa miinus -merkki -kohdasta aukeaa alasvetovalikko, josta valinta tehdään). Alla olevassa esimerkissä on siis valittu miinus -vaihtoehto.

Alla olevassa esimerkissä widgetille ei ole valittu mitään muita pylväitä (bars) kuin kaavan kautta tuleva erotus. Kaavoissa on käytettävissä samat laskentaoperaattorit kuin tietolähteillä (plus, minus, kerto, jako ja %-diff).

[![](

Kun kaava on kirjoitettu widgettiin, on näkymä tämänkaltainen:

[![](

Varsinaiselle widgetille laskentakaava tulee tässä tapauksessa pylväänä, sillä kyseinen esimerkki on pylväs graafista. Pylvään nimeksi tulee raportin rivi sekä sen sisältämä laskentametodi. Graafi vaatii vielä muokkauksia, sillä johtuen sen kaavasta, pylväisiin ei tule vielä mitään.

[![](

## Dimension valitseminen

Seuraavaksi elementille halutaan määritellä dimensionarvot. Dimensionarvoja päästään määrittelemään klikkaamalla joko yksittäistä pylvästä tai klikkaamalla graafin alaosassa näkyvää tietolähteen nimeä.

Kun elementti josta klikataan on kaava, on näkymä oheinen. Ensimmäisenä valitaan, että mikä on se dimensionarvo, mitä halutaan käyttää kuluvan tilikauden liikevaihtona josta lasketaan seuraavassa kentässä määritellyn dimensioarvon erotus.

Custom name -kentässä elementille voidaan antaa jokin muu haluttu nimi.

[![](

Tässä esimerkissä on valittu, että graafissa halutaan esittää markkinointi -dimensionarvon liikevaihto miinus hallinto -dimensionarvon liikevaihto

[![](

Tämän jälkeen pylväs -graafi raportoi oheisesti

[![](

[![](

*Kyseinen esimerkki on vain yksi esimerkki siitä, miten kaavoille voidaan lisätä dimensionarvoja. Toiminto on käytettävissä kaikilla graafisilla raporteilla (chart beta). Toimintoa voidaan käyttää myös laskemaan erotuksia eri tilikausien välillä*



artikkelin osoite on https://intercom.help/finazilla/fi/articles/6803740-uusi-grafiikkakirjasto-kaavojen-ja-dimensioiden-yhdistaminen-samalle-widgetille

