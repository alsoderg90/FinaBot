## Käyttöoikeudet ja jaetut raportit

[![](

*Versiopäivityksessä 27.12.2021 tuotava parannus aikaisempaan rajoitetun roolin käyttäytymiseen.* 

# Käyttöoikeudet ja jaetut raportit

Olemme kuvanneet erilaisia käyttäjärooleja aikaisemmissa artikkeleissamme, kuten mm. artikkelissa ["mikä merkitys eri rooleilla on Finazillassa?"]( Tässä artikkelissa kerromme, miten esimerkiksi yrityksen pääkäyttäjät voivat luoda erilaisia raportteja ja jakaa yhtä ja samaa raporttia yritystasoisille käyttäjille siten, että käyttäjät saavat raportit auki omien käyttöoikeuksiensa mukaisesti.

**Esimerkki 1:**

Yrityksellä on dimensio nimeltä MAA, jossa on valuet "Ruotsi", "Suomi", "USA" ja "Ranska". Luodaan raportti valinnalla dimensio / column. Jaetaan raportti käyttäjälle A, jolla on oikeus kaikkiin muihin valueihin, paitsi "Ruotsi".

Käyttäjälle aukeaa kyseinen raportti siten, että siinä on vain valueiden "Suomi", "USA" ja "Ranska" arvot. Käyttäjä ei siis näe Ruotsin arvoja lainkaan. Raportti skaalautuu oikeuksien mukaisesti.

**Esimerkki 2:**

Yrityksellä on edelleen edellä kuvatut dimension valuet ja raportti. Käyttäjällä A on oikeus vain arvoon "Suomi", eikä mihinkään muuhun. Käyttäjälle aukeaa kyseinen raportti siten, että siinä on vain valuen "Suomi" luvut, eikä mitään muuta.

**Esimerkki 3:** 

Yrityksen pääkäyttäjä luo raportin valinnalla dimensio/column. Hän jakaa raportin yrityksen viidelle käyttäjälle, jolla kullakin on erilaiset roolit.

Kukin käyttäjä saa raportin auki ja heille näkyy vain raportista ne arvot, mihin heillä on oikeus. Yksi ja sama raportti skaalautuu siis usealle käyttäjälle heidän kunkin rooliensa mukaisesti.

**Esimerkki 4:**

Tosite on kohdistettu kirjanpidossa ns. matriisiin, eli kirjaus kohdistuu dimension "MAA" arvoon "Ruotsi" sekä dimensioon "TEHDAS" arvoon "Tehdas 3". Käyttäjällä on oikeus vain toiseen arvoon eli dimensioon "TEHDAS" ja siellä arvoon "Tehdas 3".

Käyttäjä ei näe lainkaan kyseistä tositetta. Matriisi -kohdistukset näkyvät vain, mikäli käyttäjällä on oikeus kumpaankin matriisin osapuoleen

**Esimerkki 5:**

Käyttäjällä A on oikeus dimensio valueen "USA". Yrityksessä budjetoidaan kuitenkin käyttämällä lisäksi valueita "Ruotsi", "Suomi" ja "Ranska".

Käyttäjä saa auki budjetin dimensiovaluen "USA" osalta. Käyttäjä ei saa auki mitään muita lukuja eikä voi käyttää esimerkiksi budjetin monitor -näkymää,

Budjettia raportoitaessa käyttäjä näkee vain dimensiovaluen "USA" luvut.

**Esimerkki 6:**

Pääkäyttäjä on luonut Dashboardin, missä on erilaisia raportteja erilaisin dimensiorajauksin. Pääkäyttäjä jakaa Dashboardin yrityksen 5 käyttäjän kesken.

Kukin käyttäjä näkee Dashboardista raporteista sen datan, mihin heillä on oikeus. Dashboardin raportit skaalautuvat käyttäjäoikeuksien mukaan.

[![](

*Yllä kuvattu logiikka pätee myös silloin kun käyttäjät luovat itse uusia raportteja. Mikäli rajoitetun roolin käyttäjä luo esimerkiksi raportin valinnalla dimensio /column, aukeaa raportti yhtälailla käyttäjän oikeuksien mukaisesti.* 

# Lisätietoja

[Mikä merkitys eri rooleilla on Finazillassa?](

[Roolien kautta määritellään yritystasoisen käyttäjän käyttöoikeudet Finazillassa](

[Esimerkki: roolin luominen. Annetaan käyttäjälle oikeudet vain yhteen dimensioon](



artikkelin osoite on https://intercom.help/finazilla/fi/articles/5799550-dimensiorajoitetut-kayttajat-ja-raporttien-jakaminen

