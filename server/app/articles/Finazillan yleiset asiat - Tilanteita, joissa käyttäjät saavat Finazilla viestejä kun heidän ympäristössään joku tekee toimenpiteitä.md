## Tilanteita, joissa käyttäjät saavat Finazilla viestejä kun heidän ympäristössään joku tekee toimenpiteitä

Olemme artikkelissamme ["Finazillan sisäiset viestit, eli notifikaatiot osa 1"]( kuvanneet, kuinka me Finazillalta voimme jatkossa viestiä asiakkaillemme mm. tulevista huoltokatkoista myös Finazilla -ohjelmiston sisällä. Finazillaviesteillä on myös asiakastasoinen ulottuvuus, josta kerromme tässä artikkelissa.

# **Tilanteita, joissa käyttäjät saavat Finazilla viestejä kun heidän ympäristössään joku tekee toimenpiteitä**

* Joku käyttäjä käynnistää manuaalisesti datojen synkronoinnin (api -rajapintaa käyttävät)
* Joku laskettaa saldot (api -rajapintaa käyttävät)
* Joku integroi tositteita (drop-in metodia käyttävät)
* Joku tuo operatiivista dataa sisään
* Joku poistaa yrityksen budjetin/budjetteja

Käytännössä tämä tarkoittaa sitä, että jos käyttäjä A tekee yllä mainittuja asioita asiakkuuden yrityksessä 1, saa myös käyttäjä B näistä tiedon kirjautuessaan sisään Finazillaan yritykseen 1. Viestit koskettavat siis vain sitä yritystä, jossa toimenpiteet on tehty ja viestit näistä toimenpiteistä menevät kaikille käyttäjille, joilla on pääsy kyseiseen yritykseen. Viesteistä ei näy, että kuka käyttäjä toimenpiteet on tehnyt.

## ***Esimerkki 1:***

Asiakkuudessa on 5 yritystä. Käyttäjä A käy tekemässä jotain sellaista, josta syntyy viesti. Hän tekee tämän yrityksessä 1. Viesti näkyy hänelle vain yrityksessä 1, eikä lainkaan yrityksissä 2-5.

Käyttäjä B kirjautuu Finazillaan yritykseen 1. Hän näkee saman viestin kuin yllä mainittu käyttäjä A. Käyttäjä B menee yritykseen 3. Hänelle ei näy mitään viestejä.

Kuvaamme viestejä alla vielä tarkemmin muutaman lisäesimerkin avulla.

## ***Esimerkki 2:***

Käyttäjä käynnistää tositteiden synkronoinnin manuaalisesti. Hän saa saman tien notifikaation, joka kertoo, että integraatiota on pyydetty.

[![](

Kun ajo etenee ja pyydetyt tositteet synkronoidaan Finazillaan, saa käyttäjä notifikaatiot, jotka kertovat, mitä on synkronoitu ja onko synkronointi ollut onnistunut. Alla olevassa esimerkissä ajo on ollut onnistunut.

[![](

Viestien perässä olevasta "More" painikkeesta käyttäjä saa ajosta vielä tarkempaa tietoa, kuten esimerkiksi ajossa olleiden tositteiden kappalemäärän. Dismiss painikkeesta viestin saa poistumaan listasta ja dismiss all poistaa kaikki viestit kerralla listasta.

## ***Esimerkki 3:***

Käyttäjä käynnistää tositteiden, myyntilaskujen ja ostolaskujen synkronoinnin manuaalisesti. Hän saa samantien notifikaation asiasta. Alla olevassa kuvassa notifikaatio on aukaistu "More" painikkeen kautta auki.

[![](

Kun ajo on mennyt onnistuneesti läpi, saa käyttäjä siitä lisää notifikaatioita. Alla esimerkki saapuneista notifikaatioista kun kaikki viestit on aukaistu auki "more" painikkeesta.

[![](

[![](

Manuaalisen datan ajamisen jälkeen käyttäjän tulee aina itse laskettaa saldot, mikäli lasketus ei ole käynnistynyt itsestään. Lähtökohtaisesti saldojen lasketuksen pitäisi käynnistyä aina kun tositteita haetaan. Aihetta on kuvattu tarkemmin artikkelissamme [täällä]( Myös saldojen lasketuksesta käyttäjä saa viestin, että lasketus on käynnistynyt.

## **Esimerkki 4:**

Käyttäjä tuo sisään operatiivista dataa. Finazilla generoi tästä viestin. More -painikkeen kautta nähdään, mille datagroupille dataa on tuotu ja kuinka paljon.

[![](

[![](

*Yöllisistä integraatioista syntyy myös notifikaatiot. Näiden elinikä on yksi päivä. Näin minimoidaan turhat moninkertaiset viestit käyttäjälle*

## ***Esimerkki 5:***

Käyttäjä poistaa vanhan budjetin. Finazilla generoi tästä viestin. Notifikaatio kertoo, mikä yrityksen budjeteista on poistettu.

[![](

[![](

*Yritystasoisen käyttäjän, jolla on jokin personoitu rooli, oikeuksia notifikaatioihin voidaan rajoittaa roolien luomisessa kohdassa "notifcations"*



artikkelin osoite on https://intercom.help/finazilla/fi/articles/6655602-asiakkaan-saamat-viestit-eli-notifikaatiot-osa-2

