## Dynamic start date -valikon vaihtoehdot

Silloin kun raportoinnissa on valittuna "Period type" -kentässä vaihtoehto "Accounting period" niin vaihtoehto "Dynamic start date" ja "dynamic end date" vaihtoehdot tulevat näkyviin.

[![](

# Dynamic start date -valikon vaihtoehdot

Dynamic start date valikossa on kuvanmukaiset vaihtoehdot silloin kun raportoidaan dataa tilikausi -valinnalla.

[![](

## Current month = kuluva kuukausi

Jos raporttia ollaan luomassa kesäkuussa, muodostuu raportin alkuajaksi kesäkuu. Seuraavassa kuussa current month on heinäkuu, joten silloin raportilla käytetään heinäkuuta. Dynaaminen valinta, joka ei ota kantaa varsinaisesti raportin luomishetkeen, vaan raportoi aina aukaistaessa sen hetkistä kuluvaa kuukautta.

## Locked month = lukittu kuukausi

Accounting periods -valikossa voidaan asettaa lukituspäivä. Jos

lukituspäivä on asetettu vaikkapa 31.5 päivään, tarkoittaa tämä, että

raportin alkuaika ko. valinnalla on toukokuu. Jos lukituspäivä vaihdetaan, päivittyy raporttikin käyttämään uutta lukituskautta.

## Start date of accounting period = tilikauden ensimmäinen kuukausi

Jos yrityksen tilikausi on esimerkiksi 1.1.2024 - 31.12.2024 tarkoittaa tämä siis tammikuuta 2024.

## Next month = seuraava kuukausi

Jos raporttia ollaan ottamassa kesäkuussa, niin ko. valinnan mukaan

raportti alkaa seuraavasta kuukaudesta eli heinäkuusta. Jos raportti aukaistaan uudelleen vaikkapa syyskuussa, niin raportin next month on tällöin lokakuu.

## Next open month = seuraava avoin kuukausi

Seuraava avoin kuukausi -vaihtoehto viittaa lukituskuukauteen. Jos

lukituspäiväksi on asetettu 31.5 niin ko. valinnalla raportti alkaa

kesäkuusta. Kun lukituspäivää muutetaan, päivittyy myös next open month sen mukaisesti.

# Dynamic end date -valikon vaihtoehdot

Dynamic end date valikossa on kuvanmukaiset vaihtoehdot:

[![](

Alla on kuvattu lyhyesti kukin vaihtoehto.

## End date of accounting period = tilikauden viimeinen kuukausi

Jos yrityksen tilikausi on esimerkiksi 1.1.2024 - 31.12.2024 tarkoittaa tämä joulukuuta 2024.

## Locked month = lukittu kuukausi

Accounting periods -valikossa voidaan asettaa lukituspäivä. Jos lukituspäivä on asetettu vaikkapa 31.5 päivään, tarkoittaa tämä, että raportin alkuaika ko.

valinnalla on toukokuu

## Current month = kuluva kuukausi

Jos raporttia ollaan luomassa kesäkuussa, muodostuu raportin loppuajaksi kesäkuu

# Toimintalogiikka

Toimintalogiikasta on hyvä tietää, että tilikausi -valinta vaikuttaa aina siihen, mikä raportti milläkin valinnalla saadaan. Mikäli valittuna on "Current period", tuottaa Finazilla raportin, missä on aktiivinen tilikausi ja valinta start day of accounting period viittaa nimenomaan kyseisen tilikauden alkuun.

Jos aktiivisena tilikautena on vuosi 2024; on raportin start day of accounting period siis 1.1.2024. Jos raportille on valittu kohtaan "Accounting period" vaihtoehto "Previous period" (mikä viittaa edelliseen tilikauteen), on start day of accounting period tällöin 1.1.2023.

***Esimerkki***

Yrityksellä on aktiivisena tilikautena tilikausi 2024 ja lukituspäivä on asetettu 31.5.2024. Otetaan raportille valinnaksi tilikausi -kenttään edellinen tilikausi (= Previous period).

Dynaaminen alku on asetettu lukituskuukauteen (= locked month) ja raportin dynaaminen loppuaika on asetettu lukituskuukauteen (= locked month). Finazilla tuottaa ko. valinnoilla raportin, jossa on kausi 5/2023 (edellisen vuoden lukittu kausi). Mikäli tilikaudeksi vaihdettaisiin previous period -valinnan tilalle current period, saataisiin raportti kaudesta 5/2024.

[![](

# Lisätietoja

[Lukitun kuukauden käyttäminen yhdessä ajanjakson valinnan kanssa](

[Toteuman ja ennusteen erottelu raportilla](

[Lukituspäivän käyttäminen mahdollistaa raportoinnin siihen saakka mihin kirjanpito on valmistunut](



artikkelin osoite on https://intercom.help/finazilla/fi/articles/4234059-dynaamiset-alku-ja-loppuajat-raportoinnissa-mahdollistavat-automaattisesti-paivittyvat-raportit

