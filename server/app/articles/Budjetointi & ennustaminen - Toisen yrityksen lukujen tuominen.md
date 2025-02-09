## Toisen yrityksen lukujen tuominen

[![](

*Versiopäivityksessä 8.6.2023 tuotu kokonaan uusi toiminto. Toiminto mahdollistaa toisen saman asiakkuuden yrityksen lukujen tuomisen yrityksen budjetille. Lukuja voidaan tuoda useasta datalähteestä kerralla ja erilaisin dimensioasetuksin. Toimintoa on laajennettu 26.2.2024 osalla 5.* 

Tuotu ominaisuus on osa laajempaa kokonaisuutta. Tässä artikkelissa esitelty ominaisuus on osa 4, joka keskittyy nimenomaan usean tietolähteen yhtäaikaisesta tuonnista Tuotavia osia on yhteensä 5. Toimintoon liittyy myös seuraavat ominaisuudet:

[Budjetin import, osa 1: toiselta yritykseltä lukujen tuominen](

[Budjetin import, osa 2: usealta tietolähteeltä lukujen tuominen](

[Budjetin import, osa 3: lukujen siirtäminen dimensionarvolta toiselle](

[Budjetin import, osa 5: osabudjetilta toiselle lukujen tuominen](

# Toisen yrityksen lukujen tuominen

Tässä artikkelissa kuvaamme tarkemmin dimensioiden vaikutusta tilanteissa, missä yrityksen 2 budjetille halutaan tuoda yrityksen 1 lukuja. Dimensiovalintoja päästään tekemään kohdassa multiple targets.

[![](

# Dimensioiden summaaminen

Huomaa että tämä ominaisuus korva myös kokonaan vanhan Import Moden "Sum of All dimensions to current". Jos siis halutaan tuoda kaikki valitun kohteen luvut (aiemmin "Sum of all dimensions targets") niin vasempaan kenttään valitaan "Multiple targets" ja oikeanpuolenen filtteröintimahdollisuus jätetään tyhjäksi.

# Havainnollistavat esimerkit

Havainnollistamme asiaa muutamalla esimerkillä alla.

Yrityksellä on myyntiä seuraavilla dimension arvoilla oheisesti per kuukausi

* 10 000€ ilman mitään dimensiokohdistusta
* Tampere 5000€
* Tampere + Projekti 1 (matriisikohdistus) 3000€
* Tampere + Projekti 2 (matriisikohdistus) 2000€
* Helsinki + Projekti 1 (matriisikohdistus) 4500€
* Helsinki + Projekti 2 (matriisikohdistus) 8500€
* Myyntiä yhteensä 33 000€/kk

**Esimerkki 1:**

Budjetille halutaan tuoda kaikki myynnit eli 33 000€.

Import balances -työkalussa valitaan kohdassa Datasource vasempaan reunaan multiple targets ja oikeaan reunaan ei valita mitään. Tällä valinnalla budjetille tuodaan kaikki myynnit eli 33 000€.

[![](

**Esimerkki 2:**

Budjetille halutaan tuoda kaikki myynnit, joissa Tampere on osallisena. Halutaan tuoda siis 10 000€ myynti.

Import balances -työkalussa valitaan kohdassa Datasource vasempaan reunaan multiple targets ja oikeaan reunaan Tampere.

Tällä valinnalla budjetille tuodaan kaikki myynnit, joissa Tampere on tavalla tai toisella osallinen. Budjetille tuodaan siis myynti 5000€ missä esiintyy pelkästään Tampere, sekä 3000€ myynti missä esiintyy Tampere ja Projekti 1 sekä 2000€ myynti, missä esiintyy Tampere ja Projekti 2.

[![](

**Esimerkki 3:**

Budjetille halutaan tuoda kaikki myynnit, joilla ei ole dimensiokohdistusta. Halutaan tuoda siis 10 000€ myynti.

Import balances -työkalussa valitaan kohdassa Datasource vasempaan reunaan single target ja oikeaan reunaan ei laiteta mitään.

[![](

**Esimerkki 4:**

Budjetille halutaan tuoda kaikki myynnit, jotka kohdistuvat Helsingille ja projekti 2:lle. Halutaan tuoda siis 8500€ myynti.

[![](

**Esimerkki 5:**

Budjetille halutaan tuoda kaikki myynnit, jotka kohdistuvat Tampereelle tai Helsingille. Halutaan tuoda siis 23 000€ myynti (kaikki muut, paitsi dimensioimaton 5000€ myynti).

[![](

[![](

*Multiple targets valitsin toimii samalla tavalla kuin dimensiokohteen valitsin raportilla ja raporttimallilla. Kaikista valituista dimensioista on löydyttävä jokin niistä valittu dimension arvo.* 



artikkelin osoite on https://intercom.help/finazilla/fi/articles/7942623-budjetin-import-osa-4-usealta-dimensiolta-tuominen

