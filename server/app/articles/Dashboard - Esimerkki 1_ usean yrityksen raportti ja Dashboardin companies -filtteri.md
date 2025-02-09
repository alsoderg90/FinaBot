## Esimerkki 1: usean yrityksen raportti ja Dashboardin companies -filtteri

[![](

*Versiopäivityksessä 17.3.2023 tuotu kokonaan uusi toiminto. Toiminto mahdollistaa Dashboardilla olevien raporttien filtteröinnin datassa olevien yritysten mukaisesti*

Kyseinen toiminto koskettaa ainoastaan asiakkuuksia, joilla on useampi yritys omassa asiakkuudessaan (eli esimerkiksi konserniyrityksiä).

Tämän artikkelin ymmärtämisen edellytys on, että käyttäjä osaa luoda usean yrityksen raportteja, sekä osaa luoda Dashboardin ja kiinnittää sille erilaista sisältöä. Tässä artikkelissa kuvataan siis tilannetta, missä käyttäjä on luonut usean yrityksen raportin (tai raportteja), liittänyt ne Dashboardille, ja haluaan tämän jälkeen filtteröidä Dashboardia yritysvalinnan mukaan.

[![](

 *Jos Dashboardilla ei ole yhtään usean yrityksen raporttia, ei company -filtteri tule lainkaan näkyviin. Filtteri näkyy siis vain silloin, kun sillä voidaan oikeasti filtteröidä jotain.* 

Toimintoon liittyy myös seuraavat osat:

[Dashboardin filtteröinti raporttifiltterillä osa 1: dimensiot](

[Dashboardin filtteröinti raporttifiltterillä osa 2: päivämäärät](

[Dashboardin filtteröinti raporttifiltterillä osa 4: raportointiryhmä](

# Esimerkki 1: usean yrityksen raportti ja Dashboardin companies -filtteri

Kun käyttäjä tekee usean yrityksen raportteja, tulee yritysfiltteriin valittavaksi kaikki ne yritykset, joita Dashboardin raporteissa on olemassa.

Filtteri löytyy Dashboardin oikeasta yläkulmasta valikosta "show filters".

[![](

Filtterillä käyttäjä voi valita, että haluaa nähdä vain tietyn yrityksen (tai yritysten) datat. Koko Dashboard filtteröityy tällöin tehtyä valintaa vasten.

[![](

Jos usean yrityksen raportteja on tehty myös valinnalla companies total, tulee yritysfiltteriin valittavaksi vielä yllä olevien lisäksi "companies total" valinta. Tällaiset raportit näkyvät Dashboardilla vain kun kyseinen filtteri on päällä (tai valintana on select all).

# Esimerkki 2: konserniraportit ja Dashboardin companies -filtteri

Kun käyttäjä tekee konserniraportteja, eli raportteja valinnalla consolidated company/column, tulee yritysfiltteriin valittavaksi myös eliminoinnit ja konsolidoidut luvut yhteensä ikään kuin yrityksiksi.

Jos raportteja on tehty myös valinnalla consolidated total, tulee yritysfiltteriin valittavaksi vielä "companies total" valinta.

[![](

Käytännössä consolidated company/column raportteihin tulee yhteen sarakkeeseen konsolidoidut luvut yhteensä, seuraavaan sarakkeeseen tulee eliminoinnit yhteensä, kolmanteen sarakkeeseen yritys 1 ja neljänteen sarakkeeseen yritys 2. Jos filtteristä valitaan "eliminations", suodattuu raportti siten, että siellä näkyy vain eliminoinnit.

Consolidated total -valinnalla tehdyissä raporteissa on vain yksi sarake; konserniyritykset yhteensä eliminointeineen. Tällainen raportti ei näy Dashboardilla millään muulla valinnalla kuin "companies total" (tai select all).

[![](

*Company-filtteri ei tule näkyviin filttereille ollenkaan jos dashboardin raportit sisältää alle kahdelta yritykseltä dataa -tai käyttäjän oikeudet ei riitä raportin dataan*

# Käyttöoikeuksien vaikutus companies -filtteriin

Mikäli Dashboardilla on vaikkapa kolmen yrityksen raportti ja kyseinen Dashboard (ja sen raportti) on jaettu käyttäjälle, jolla on oikeus vain kahteen yritykseen, näkyy tällaiselle käyttäjälle Dashboardin filttereissä vain 2 yritystä. Hän näkee datan siis käyttöoikeuksiensa mukaisesti.

Yllä olevassa esimerkissä konserniraporteista käyttäjälle näkyy vain niiden kahden yrityksen eliminoinnit ja konsolidoidut luvut, mihin hänellä on oikeus.

# Lisätietoja

[Dashboardin filtteröinti raporttifiltterillä osa 1: dimensiot](

[Dashboardin filtteröinti raporttifiltterillä osa 2: päivämäärät](



artikkelin osoite on https://intercom.help/finazilla/fi/articles/6857666-dashboardin-filtterointi-raporttifiltterilla-osa-3-yritys

