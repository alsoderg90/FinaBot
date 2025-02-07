## Dimension asettaminen elementille

[![](

*Chart beta -graafisiin raportteihin liittyvä parannus. Toiminto mahdollistaa sen, että jatkossa chartin elementeille on mahdollista antaa dimension arvo(ja)*

Olemme kertoneet aikaisemmassa artikkelissamme ["Uusi vaihtoehtoinen tapa luoda graafisia raportteja; chart beta"]( uudesta graafisesta raporttikirjastostamme. Kirjastoon sisältyy pylväs, viiva, pylväs & viiva, piirakka ja pinottu pylväskuvio. Tässä artikkelissa kerromme *kaikkiin edellä mainittuihin* graafisiin raportteihin tehdystä lisämahdollisuudesta.

# Dimension asettaminen elementille

Uusi lisämahdollisuus mahdollistaa sen, että graafisen raportin widgetissä elementtiä klikkaamalla päästään kertomaan, että mitä dimension arvoa kyseinen elementti raportoi. Jos käyttäjällä on siis esimerkiksi pylväs graafi, aukeaa ikkuna mitä tahansa pylvästä klikkaamalla.

Custom name -kentässä elementti voidaan uudelleennimetä halutulla tavalla.

[![](

Dimension Target -kohtaan voidaan valita yksi dimension arvo, tai useita. Mikäli valitaan useita saman dimension arvoja, nousee raporttiin luvut, jotka kohdistuvat jommalle kummalle dimension arvolle. Jos valitaan dimension arvot eri dimensioista, nousee raporttiin luvut, jotka kohdistuvat kyseiselle matriisille.

## Havainnollistavat esimerkit

Havainnollistamme logiikkaa muutamalla esimerkillä. Yrityksellä on dimensio "maa", jossa on arvot "Suomi" ja "Ruotsi". Sen lisäksi yrityksellä on toinen dimensio, joka on "kustannuspaikka". Tässä on arvot "hallinto" ja "markkinointi".

**Esimerkki 1:** 

Mikäli dimensio target -kenttään valitaan pelkästään hallinto. Näytetään vain luvut, jotka kohdistuvat dimension arvolle "hallinto".

**Esimerkki 2:**

Mikäli dimensio target -kenttään valitaan hallinto ja markkinointi. Näytetään luvut, jotka kohdistuvat joko hallinnolle TAI markkinoinnille.

**Esimerkki 3:**

Dimensio target -kenttään valitaan hallinto ja Suomi. Näytetään luvut, jotka kohdistuvat yhdistelmälle Hallinto ja Suomi.

**Esimerkki 4:**

Dimensio target -kenttään valitaan hallinto, markkinointi ja Suomi. Näytetään luvut, jotka kohdistuvat jollekin seuraavista yhdistelmistä; hallinto ja markkinointi, hallinto ja Suomi, markkinointi ja Suomi, hallinto + markkinointi + Suomi jne.

Uusi toiminto mahdollistaa useita erilaisia graafisia raportteja, kuten vaikkapa yllä kuvatun dimension arvon "hallinto" liikevaihdon vertailun eri vuosien välillä.

Alla olevassa kuvassa pylväs widget on laadittu siten, että pylväitä on kaksi. Kumpikin pylväistä raportoi liikevaihtoa; toinen pylväs kuluvaa tilikautta ja toinen edellistä. Widgettiä on muotoiltu siten, että X-Axis Key on month, jolloin eri vuosien kuukaudet esitetään vierekkäin. Lisäksi pylväiden päälle on editoitu numeeriset arvot ja pylväiden väriä on vaihdettu.

Pylväitä on lisäksi muotoiltu vielä siten, että kummankin pylvään dimensiokohde (dimension target) on dimensionarvo "hallinto". Näin pylväissä esitetään vain hallinnon liikevaihto.

[![](

[![](

*Toiminto on käytettävissä muillakin chart beta raporteilla. Logiikka on vastaava kuin tässä kuvattu*



artikkelin osoite on https://intercom.help/finazilla/fi/articles/6751929-uusi-grafiikkakirjasto-dimensiovalitsin-elementille

