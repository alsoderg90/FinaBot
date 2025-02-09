## Raportointiryhmän asettaminen elementille

[![](

*Chart beta -graafisiin raportteihin liittyvä parannus. Toiminto mahdollistaa sen, että jatkossa chartin elementeille on mahdollista antaa raportointiryhmä/ryhmiä*

Olemme kertoneet aikaisemmassa artikkelissamme ["Uusi vaihtoehtoinen tapa luoda graafisia raportteja; chart beta"]( uudesta graafisesta raporttikirjastostamme. Kirjastoon sisältyy pylväs, viiva, pylväs & viiva, piirakka ja pinottu pylväskuvio. Tässä artikkelissa kerromme *kaikkiin edellä mainittuihin* graafisiin raportteihin tehdystä lisämahdollisuudesta.

# Raportointiryhmän asettaminen elementille

Uusi lisämahdollisuus mahdollistaa sen, että graafisen raportin widgetissä elementtiä klikkaamalla päästään kertomaan, että mitä dimension arvoa tai raportointiryhmää kyseinen elementti raportoi. Jos käyttäjällä on siis esimerkiksi pylväs graafi, aukeaa ikkuna mitä tahansa pylvästä klikkaamalla.

Custom name -kentässä elementti voidaan uudelleennimetä halutulla tavalla.

[![](

 mitä elementissä halutaan esittää

Raportointiryhmä päästään valitsemaan klikkaamalla otsikkoa "reporting groups". Tällöin valittavaksi tulee kyseisellä raportilla esiintyvät raportointiryhmät. Mikäli raportissa on useita ryhmiä, tulevat ne kaikki valittavaksi.

[![](

Reporting groups -kohtaan voidaan valita haluttu raportointiryhmä. Kuvan esimerkissä on vain yksi raportointiryhmä valittavissa, jolloin valitaan listaan tuleva "hallinto ja markkinointi" niminen ryhmä.

## Havainnollistavat esimerkit

Havainnollistamme logiikkaa muutamalla esimerkillä. Yrityksellä on raportointiryhmä nimeltä "hallinto ja markkinointi", jossa on arvot "hallinto" ja "markkinointi". Kumpikin dimensionarvoista on dimension Kustannuspaikka arvoja. Sen lisäksi yrityksellä on kustannuspaikoissa vielä arvo nimeltä "Myynti". Tämä dimensionarvo ei kuulu kyseiseen raportointiryhmään.

**Esimerkki 1:**

Mikäli reporting group -kenttään valitaan raportointiryhmä hallinto ja markkinointi, näytetään luvut, jotka kohdistuvat dimension arvolle "hallinto" TAI dimensionarvolle "markkinointi". Graafissa ei esitetä lainkaan dimensionarvon "myynti" lukuja.

**Esimerkki 2:**

Yritys luo toisen raportointiryhmän, nimeltä "Myynti". Raportointiryhmään kiinnitetään edellä kuvattu dimensioarvon "Myynti". Nyt yrityksellä on kaksi raportointiryhmää olemassa.

Mikäli reporting group -kenttään valitaan raportointiryhmä "hallinto ja markkinointi", näytetään luvut, jotka kohdistuvat dimension arvolle "hallinto" TAI dimensionarvolle "markkinointi". Jos kenttään valitaan raportointiryhmä "myynti", näytetään luvut, jotka kohdistuvat dimensionarvoon "myynti". Tällöin ei näytetä lainkaan lukuja, jotka kohdistuvat "hallinto" tai "markkinointi" dimensionarvoille.

**Esimerkki 3:**

Reporting group kenttään valitaan kumpikin yrityksen raportointiryhmistä. Tässä tapauksessa graafissa näytetään kaikkien kolmen dimensionarvon yhteenlaskettu arvo (hallinto + markkinointi + myynti)

**Esimerkki 4:**

Toimintoa voidaan käyttää hyödyksi myös siten, että pylväitä tehdäänkin kaksi. Toiseen pylvääseen kiinnitetään raportointiryhmä "hallinto ja markkinointi" ja toiseen kiinnitetään "myynti". Tällöin saadaan graafiin kaikki eurot, mutta jakauma pylväillä noudattelee raportointiryhmän logiikkaa. Toisessa pylväässä esitetään esimerkin 1 mukaiset hallinto tai markkinointi luvut yhteensä, ja toisessa pylväässä on myynnin luvut.

[![](

[![](

*Toiminto on käytettävissä muillakin chart beta raporteilla. Logiikka on vastaava kuin tässä kuvattu*

*Huomaa, että toiminnon käyttäminen graafisilla raporteille edellyttää, että yritykseltä löytyy raportti, jossa kyseistä raportointiryhmää/ryhmiä on käytetty*



artikkelin osoite on https://intercom.help/finazilla/fi/articles/8825444-uusi-grafiikkakirjasto-raportointiryhma-elementille

