## Kohdistusten valuttaminen lapsiriveille

[![](

Versiopäivityksessä 13.4.2023 tuotava kokonaan uusi toiminto. *Toiminto mahdollistaa lisäkohdistettujen osabudjetin rivien lisäkohdistuksen periytymisen "lapsiriveille" sekä hierarkisten rakenteiden kopioimisen siten, että myös tehdyt kohdistukset kopioituvat.* 

Tuotu ominaisuus on osa laajempaa kokonaisuutta. Tässä artikkelissa esitelty ominaisuus on osa 3. Tuotavia osia on yhteensä 4.

Tässä artikkelissa kerromme, kuinka lisäkohdistuksia voidaan valuttaa lapsiriveille ja kopioida uusia hierarkisia rakenteita, joissa myös kohdistukset kopioituvat. Vastaava ominaisuus on jo toteutettu aikaisemmin operatiivisen datan puolelle ja sitä olemme esitelleet artikkeleissamme, jotka löytyvät alta.

* [Hierarkisen rakenteen hyödyntäminen operatiivisen datan budjetoinnissa](
* [Esimerkki: hierarkisen rakenteen kopioiminen dimensio kohdistuksin](
* [Esimerkki: dimensiokohdistuksen valuttaminen lapsiriveille](
# Kohdistusten valuttaminen lapsiriveille

Hierarkisen rakenteen ylemmälle tasolle lisäkohdistuksen laittaminen "valuttaa" saman kohdistuksen kaikille rakenteen alapuolella oleville riveille. Niillä riveillä, joille kohdistus on "valutettu", kohdistus näkyy kentässä "inherited additional values" kun taas alkuperäisessä rivissä se näkyy kohdassa "additional dimension values".

Jos osabudjetissa esimerkiksi budjetoidaan projektimyyntejä ja osabudjetissa on ylimpänä projektin nimi, ja tämän alla lapsiriveinä projektin tulot ja projektin menot, voidaan lisäkohdistusta hyödyntää siten, että lisäkohdistus asetetaan projektiriville. Näin toimien lisäkohdistus "valuu" myös projektin tuloille ja menoille.

[![](

## 

Yllä kuvatun kohdistuksen lisäksi "tavanomaisella" dimensiokohdistuksella, jossa valitaan oikeaan yläkulmaan haluttu dimension arvo, saadaan kohdistukseen mukaan jokin toinen dimensionarvo. Tämä voidaan toteuttaa myös vyörytyssääntöä käyttämällä.

[![](

*Jos hierarkiaa on useammassa tasossa, periytyy kohdistukset "lapsiriveille" aina kyseisen rivin yläpuolella olevan hierarkian mukaisesti.* 

# Hierarkisen rakenteen kopioiminen create duplicates -toiminnolla

Osabudjetin riviasetuksista löytyvä create duplicates -toiminto mahdollistaa sen, että osabudjetille voidaan kopioida nopeasti ja helposti isoja määriä hierarkisia rakenteita siten, että dimensiokohdistukset kopioituvat mukana.

Jos esimerkiksi käyttäjällä on laadittuna aikaisemmin kuvattu projektimyynnin osabudjetti, jossa on luotuna yksi projekti, sekä sen alla projektin tulot ja projektin menot -rivit, voidaan duplikoinnilla luoda helposti vastaava rakenne seuraaville projekteille. Kerralla voidaan luoda lukuisia projekteja, joten kopioimista ei tarvitse tehdä projekti kerrallaan.

Kopiointi, eli duplikointi, tehdään yllä kuvatussa esimerkissä projektin nimi riviltä riviasetuksista kohdasta "create duplicates". Duplicate mode -valinta on "copy for dimension values" ja kenttään "generate new row for dimensions value" valitaan alasvetovalikosta kaikki ne projektit, mille halutaan luoda vastaava rakenne.

[![](

Näin luotaville projekteille syntyy vastaava hierarkinen rakenne siten, että kullakin lapsirivillä on yläpuolella olevan "parent" rivin kohdistus. Aihetta on kuvattu enemmän (operatiivisen datan näkökulmasta) artikkelissamme "[Esimerkki: hierarkisen rakenteen kopioiminen dimensio kohdistuksin](

[![](

# Vyörytyssäännön ja lisäkohdistuksen käyttäminen yhdessä

Samalle riville voi antaa vyörytyssäännön, sekä lisäkohdistuksen käyttämällä additional dimension values -kenttää. Näin toimien vyörytyssääntö vyöryttää luvut tehdyssä jakosuhteessa valituille dimension arvoille ja tämän jälkeen lisäkohdistus ottaa vyörytetyt luvut itselleen.

*Esimerkki kun vyörytetään 100%*

Osabudjetilla on syöttörivi, jossa on vyörytyssääntö, joka vyöryttää 100% dimension arvolle "Tampere". Additional dimension values -kenttään on asetettu dimension arvo "Projekti A". Riville lukujen syöttäminen tapahtuu ns. "blank" dimensiolle, koska rivillä on vyörytyssääntö.

Kyseiselle riville budjetoidaan 1000€/kuukausi. Vyörytyssäntö vyöryttää syötetyn 1000€ dimension arvolle "Tampere". Seuraavaksi "additional dimension values" kohdistaa 1000€ Tampereelta kombinaatiolle "Tampere + Projekti A". Lopullinen lukujen kohdistus on siis matriisilla "Tampere + Projekti A".

*Esimerkki kun ei vyörytetä 100%*

Osabudjetilla on syöttörivi, jossa on vyörytyssääntö, joka vyöryttää 50% dimension arvolle "Tampere". Additional dimension values -kenttään on asetetty dimension arvo "Projekti A".

Riville budjetoidaan 1000€/kuukausi. Vyörytyssääntö vyöryttää 50% syötetystä 1000€:sta (500€) dimension arvolle "Tampere". Loput 500€ jää dimensiolle blank, eli nk. dimensioimattomiin arvoihin. Tämän jälkeen "additional dimension values" kohdistaa 500€ kombinaatiolle Tampere + Projekti A. Loput 500€ kohdistuu pelkästään dimension arvolle blank. Jos vyörytyssääntö on siis jotakin muuta kuin 100%, niin jäljelle jäävät luvut jäävät pysyvästi blank -dimensiolle (eli ovat nk. dimensioimattomia lukuja).

# Lisätietoja

[Lisäkohdistuksen käyttäminen osabudjetilla, osa 1](

[Lisäkohdistuksen käyttäminen osabudjetilla, osa 2: matriisikohdistus](

[Lisäkohdistuksen käyttäminen osabudjetilla, osa 3: lisäkohdistuksen periytyminen a rivien kopiointi](

Lisäkohdistuksen käyttäminen osabudjetilla, osa 4: tagit ja kaavat. \*\*HUOM: superuserin ominaisuus, artikkeli tulossa\*\*



artikkelin osoite on https://intercom.help/finazilla/fi/articles/6126927-lisakohdistuksen-kayttaminen-osabudjetilla-osa-3-lisakohdistuksen-periytyminen-ja-rivien-kopiointi

