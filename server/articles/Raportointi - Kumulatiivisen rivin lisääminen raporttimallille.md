## Kumulatiivisen rivin lisääminen raporttimallille

[![](

*Versiopäivityksessä 7.8.2024 tuotu parannus raporttimallien logiikkaan. Parannus mahdollistaa kumulatiivisten raporttien luomisen entistä helpommin*

Olemme kuvanneet aikaisemmassa artikkelissamme [täällä]( kuinka raportin luvut voidaan muuttaa kumulatiiviseksi käyttämällä raportin puolella aggregation -toimintoa.

Tässä ohjeessa esittelemme ***vaihtoehtoisen tavan*** kumulatiivisten raporttien tekemiseen, joka toimii myös aiempaa paremmin raporteilla, missä on prosentuaalista dataa (esimerkiksi vaikkapa kateprosentteja jne).

# Kumulatiivisen rivin lisääminen raporttimallille

Kun raporttimallille lisätään rivi, jonka tyyppi on "balance data", aukeaa käyttäjälle oheiset valinnat. Valinnat näkyvät oheisesti vain balance data -tyyppisillä riveillä.

[![](

Raporttimallin valinnoissa kerrotaan haluttu tili (tai tiliväli), tilin merkkisyys ja kohdassa "Balance Type" kerrotaan, miten tilin summaantuminen halutaan käsitellä. Oletusvalinta "Balance" tarkoittaa perinteistä tilin saldoa. Valinnalla change, saadaan raportoitua muutos ja valinta "cumulative", raportoi luvut kumulatiivisena.

Alla olevilla valinnoilla saadaan tilien 3000-3599 yhteenlaskettu saldo raportille kumulatiivisesti.

[![](

Valintojen havainnollistamiseksi alla on raportti, joka on tehty raporttimallilla, jossa on tehty liikevaihto käyttäen kutakin eri balance type -valintaa. Raporttimallin valinnat ovat siis muutoin kullakin rivillä identtiset, mutta ensimmäisessä rivissä balance type -valinta on balance, seuraavassa change ja kolmannessa cumulative.

[![](



artikkelin osoite on https://intercom.help/finazilla/fi/articles/9739693-esimerkki-kumulatiivisen-raportin-luominen

