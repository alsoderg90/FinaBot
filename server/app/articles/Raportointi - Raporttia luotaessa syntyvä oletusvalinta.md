## Raporttia luotaessa syntyvä oletusvalinta

Olemme aikaisemmassa artikkelissamme ["raportin muotoilu -painikkeet"]( kuvanneet mitä toimintoja raportin options -valikon takaa löytyy. Lisäksi olemme artikkelissamme ["raportoinissa tehtävät ennakkomäärittelyt, kuten mm. perustiedot, esitystapa sekä tietolähteet"]( kuvanneet ennakkomäärittelyiden/esivalintojen kautta tehtäviä valintoja.

Tässä artikkelissa kerromme tarkemmin, miten raportin summia voidaan muotoilla eri vaihtoehdoin. Summien käyttäytymisen logiikka on muuttunut 21.5.2021 tuodussa versiopäivityksessä hieman aikaisemmasta. Jatkossa käyttäjä voi tehdä vapaasti valintoja, kuten ennenkin. Tiettyjen valintojen kanssa on kuitenkin luotu automatiikkaa johtuen siitä, että muutoin raporteille ei nousisi lukuja ilman erillistä raportin muokkausta.

# Raporttia luotaessa syntyvä oletusvalinta

Raporttia muodostettaessa Finazillan raporteille tulee aina oletusvalintana summaantumisen vaihtoehto "show for rows only". Tämä on useimmissa raporteissa hyvä valinta, sillä esimerkiksi taseraportteihin ei lähtökohtaisesti halutaan mitään yhteissummia mukaan.

käyttäjä voi halutessaan muuttaa raportin summavalintoja raportin kautta oikean yläkulman "options" valikon takaa.

# Raportin muotoilu -painikkeiden kautta tehtävät valinnat

Raportin muotoilu -painikkeiden takaa käyttäjällä on laajempi skaala erilaisia vaihtoehtoja valittavana. Valinnat löytyvät raportilla oltaessa options -valikon alta.

[![](

Options -valikosta löytyy oheiset valinnat:

[![](

Summaantumisen vaihtoehdoista voidaan karkeasti sanoa, että vaihtoehdot, joissa viitataan "columns" termiin summaavat aina sarakkeita jollain tavalla. Vastaavasti taas vaihtoehdot, joissa viitataan "rows" sanaan, summaavat rivisaldoja.

Esittelemme alla kunkin vaihtoehdon erikseen.

## GRAND TOTALS -VALINNAT

### Do not show grand totals

Ei näytetä summia.

*"show subtotal rows only" valinta tulee automaattisesti raportille valituksi.* 

### Show grand totals

Valinta tekee rivien summaantumisen raportin oikeaan reunaan viimeiseksi. Sarakkeen otsikkona on "grand total".

Lisäksi valinta tekee sarakkeiden summaantumisen raportin loppuun viimeiselle riville. Rivin otsikkona on "amount".

### Show for rows only

Valinta tekee rivien summaantumisen raportin oikeaan reunaan viimeiseksi. Sarakkeen otsikkona on "grand total"

### Show for columns only

Valinta tekee sarakkeiden summaantumisen raportin loppuun viimeiselle riville. Rivin otsikkona on "amount".

## SUBTOTALS -VALINNAT

### Do not show subtotals

Ei näytetä rivi- eikä sarakesummia.

"show subtotal rows only" valinta tulee automaattisesti raportille valituksi.

### Show subtotals

Oletusvalinta; näytetään sekä rivi- että sarakesummat. Ei mitään erillisiä summarivejä missään.

### Show subtotals rows only

Näytetään vain rivisummat. Ei mitään erillisiä summarivejä missään. Vastaa nk. tyypillistä tuloslaskelma mallia.

## Show subtotals columns only

Näytetään sarakesummat. Ei mitään erillisiä summarivejä missään.

[![](

*Raporteille tulee "show for rows only" valinta aina automaattisesti oletuksena. Nämä ohjaukset on tehty siksi, että tuloslaskelma ja tase tulostuvat aina mahdollisimman oikein ilman, että käyttäjän tarvitsee tehdä mitään erillisiä valintoja summaantumisen valintoja.*   
​

*Subtotals, kuten myös grand totals, solut näytetään aina boldattuina. Muutos näkyy myös kaikissa aikaisemmissa raporteissa.* 



artikkelin osoite on https://intercom.help/finazilla/fi/articles/5245562-raportin-muotoilupainikkeet-erilaiset-summaantumisvaihtoehdot

