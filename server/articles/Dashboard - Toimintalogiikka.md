## Toimintalogiikka

[![](

*Versiopäivityksessä 8.6.2023 tuotu kokonaan uusi toiminto. Toiminto mahdollistaa Dashboardilla olevien raporttien filtteröinnin raportointiryhmien mukaisesti*

Tämän artikkelin ymmärtämisen edellytys on, että käyttäjä osaa luoda raportteja käyttämällä niissä raportointiryhmiä, sekä osaa luoda Dashboardin ja kiinnittää sille erilaista sisältöä. Tässä artikkelissa kuvataan siis tilannetta, missä käyttäjä on luonut raportointiryhmän sisältävän raportin (tai raportteja), liittänyt ne Dashboardille, ja haluaan tämän jälkeen filtteröidä Dashboardia raportointiryhmän mukaan.

Toimintoon liittyy myös seuraavat osat:

[Dashboardin filtteröinti raporttifiltterillä osa 1: dimensiot](

[Dashboardin filtteröinti raporttifiltterillä osa 2: päivämäärät](

[Dashboardin filtteröinti raporttifiltterillä osa 3: yritys](

Filtterit löytyvät Dashboardin oikean yläkulman "show filters" painikkeen takaa.

[![](

# Toimintalogiikka

Dashboardin filtteri toimii siten, että filttereihin tuodaan ne ryhmät mitä on käytetty raportilla/raporteilla. Jos raporteilla ei ole raportointiryhmää lainkaan käytössä, ei myöskään Dashboardin filttereihin tule mitään.

**Esimerkki:**

Finazillaan on luotu raportti, johon on kiinnitetty raportointiryhmä nimeltä "vakioasiakkaat", jossa on oheiset kolme dimension arvoa.

[![](

Kyseinen raportti on kiinnitetty Dashboardille. Dashboardin filtteri löytyy Dashboardin oikeasta yläkulmasta valikosta "show filters". Filttereistä löytyy mm. raportointiryhmä.

[![](

Jos raportilla on useita raportointiryhmiä, tulevat ne kaikki näkyviin filttereihin.

[![](

Jos filttereistä valitaan esimerkiksi vakioasiakkaat, näytetään Dashboardin raportilla vain luvut, jotka kohdistuvat kyseisen raportointiryhmän dimension arvoille. Muu data filtteröidään siis pois.

[![](

*Raportointiryhmien filtteri toimii myös operatiivisella datalla*



artikkelin osoite on https://intercom.help/finazilla/fi/articles/7991633-dashboardin-filtterointi-raporttifiltterilla-osa-4-raportointiryhma

