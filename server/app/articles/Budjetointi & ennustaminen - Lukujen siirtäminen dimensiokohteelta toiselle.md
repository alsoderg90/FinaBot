## Lukujen siirtäminen dimensiokohteelta toiselle

[![](

*Versiopäivityksessä 8.6.2023 tuotu kokonaan uusi toiminto. Toiminto mahdollistaa toisen saman asiakkuuden yrityksen lukujen tuomisen yrityksen budjetille. Lukuja voidaan tuoda useasta datalähteestä kerralla ja erilaisin dimensioasetuksin. Toimintoa voidaan käyttää myös saman yrityksen sisällä. Toimintoa on laajennettu 26.2.2024 osalla 5.* 

Tuotu ominaisuus on osa laajempaa kokonaisuutta. Tässä artikkelissa esitelty ominaisuus on osa 3, joka keskittyy nimenomaan tietyn dimension arvon lukujen siirtämiseen jollekin toiselle dimension arvolle. Tuotavia osia on yhteensä 5. Toimintoon liittyy myös seuraavat ominaisuudet:

[Budjetin import, osa 1: toiselta yritykseltä lukujen tuominen](

[Budjetin import, osa 2: usealta tietolähteeltä lukujen tuominen](

[Budjetin import, osa 4: usealta dimensiolta tuominen](

[Budjetin import, osa 5: osabudjetilta toiselle lukujen tuominen](

# Lukujen siirtäminen dimensiokohteelta toiselle

Tässä artikkelissa kuvaamme tarkemmin tilanteita, missä dataa tuodaan saman yrityksen sisällä siten, että haetaan tietyn dimensionarvon luvut ja siirretään ne budjetilla toiselle dimensioarvolle.

Vastaava toteutus on ollut Finazillassa jo aikaisemmin, mutta toteutus muuttuu tässä yhteydessä. Tässä artikkelissa kuvaamme uuden toteutuksen.

# Havainnollistavat esimerkit

Havainnollistamme asiaa erilaisin esimerkein alla.

**Esimerkki 1:** 

Yrityksellä A on tilillä 3000 myyntiä yhteensä 8 585 627,80€. Myynti kohdistuu erilaisille dimensionarvoille.

Budjetilla halutaan tuoda vuoden 2023 toteumaluvut tilille 3000 siten, että koko myynti 8 585 627,80€ halutaan esittää dimensionarvolla "kerta-asiakkaat", huolimatta siitä, missä ne kirjanpidossa ovat.

Ensimmäisenä budjetille tulee valita oikeaan yläkulmaan se dimensionarvo, millä luvut halutaan esittää jatkossa. Voisi siis sanoa, että oikeaan yläkulmaan valitaan dimensionarvo, jolle luvut *tuodaan.* 

[![](

Seuraavaksi mennään import balance -työkaluun. Työkaluun mennään budjetin siltä tasolta, mille tasolle lukuja halutaan tuoda. Tässä esimerkissä halutaan tuoda pelkästään tilin 3000 toteumat, jolloin työkaluun mennään kyseisen rivin rivityökaluista.

[![](

Seuraavaksi valitaan *tuotavan* datan asetukset. Import mode on current dimension target, joka tarkoittaa, että lukuja tuodaan dimensionarvolle "kerta-asiakkaat". From ja To kohdissa valitaan, mistä myynnit tuodaan ja minne ne budjetilla tuodaan. Datasource kohdassa näkyy yritys, jolta myynnit tuodaan ja sen alla olevaan kenttään valitaan vaihtoehto "multiple targets". Multiple targets valinta tarkoittaa nimenomaan, että tuodaan kaikki luvut, missä hyvänsä ne alkuperäisesti kirjanpidossa esiintyvät.

[![](

**Esimerkki 2:**

Yrityksellä A on tilillä 3000 myyntiä yhteensä 8 585 627,80€. Myynti kohdistuu erilaisille dimensionarvoille. Dimensionarvolle "kerta-asiakkaat" on myyntiä yhteensä 427,68€.

Budjetilla halutaan tuoda vuoden 2023 toteumaluvut tilille 3000 siten, että kerta-asiakkaiden 427,68€ myynti halutaan esittää dimensionarvolla "kuukausisopimukset".

Ensimmäisenä budjetille tulee valita oikeaan yläkulmaan se dimensionarvo, millä luvut halutaan esittää jatkossa. Tässä tapauksessa valitaan siis dimensionarvo "kuukausisopimukset".

Seuraavaksi valitaan *tuotavan* datan asetukset. Import mode on current dimension target, joka tarkoittaa, että lukuja tuodaan dimensionarvolle "kuukausisopimukset". From ja To kohdissa valitaan, mistä myynnit tuodaan ja minne ne budjetilla tuodaan. Datasource kohdassa näkyy yritys, jolta myynnit tuodaan ja sen alla olevaan kenttään valitaan vaihtoehto "single target". Jälkimmäiseen kenttään valitaan, minkä dimensionarvon luvut halutaan tuoda.

[![](

[![](

*Singe target -kenttään voi valita yhden dimensionarvon tai matriisikohdistuksen. Kenttään ei voi valita useita dimensionarvoja siten, että ne olisivat ns. erillisiä valintoja* 

**Esimerkki 3:**

yrityksellä A on laajalti lukuja matriisidimensioilla D-company + kerta-asiakkaat. Budjetille halutaan tuoda koko profit and loss -näkymään kaikki luvut, jotka kohdistuvat tälle matriisille.

Ensimmäisenä mennään budjetin yläosan työkaluvalikosta import -työkaluun. Datasource kohtaan valitaan vaihtoehto "multiple targets" ja jälkimmäiseen kenttään valitaan kumpikin matriisin osapuolista.

[![](

**Esimerkki 4:**

Yrityksellä A on tilillä 3000 myyntiä yhteensä 2 610,51€. Myynti kohdistuu matriisille D-Company + Kerta-asiakkaat.

Budjetilla halutaan tuoda vuoden 2023 toteumaluvut tilille 3000 siten, että koko myynti 2 610,51€.€ halutaan esittää dimensionarvolla "kerta-asiakkaat", huolimatta siitä, että kirjanpidossa kyseinen luku kohdistuu matriisille.

Ensimmäisenä budjetille tulee valita oikeaan yläkulmaan se dimensionarvo, millä luvut halutaan esittää jatkossa. Budjetin oikeaan yläkulmaan valitaan dimensionarvo "kerta-asiakkaat".

Seuraavaksi valitaan datasource kohtaan vaihtoehto multiple targets, ja kerrotaan jälkimmäisessä kentässä kumpikin dimensionarvo. Näin toimien matriisin D-Company + Kerta-asiakkaat myynnit tuodaan budjetille dimensionarvolle "Kerta-asiakkaat".

[![](

[![](

*Myös kertoimella tuonnit (multiplier) sekä tasamääräiset muutokset (static addition) ovat mahdollisia*



artikkelin osoite on https://intercom.help/finazilla/fi/articles/7979646-budjetin-import-osa-3-lukujen-siirtaminen-dimensionarvolta-toiselle

