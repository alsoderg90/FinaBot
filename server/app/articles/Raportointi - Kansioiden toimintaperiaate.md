## Kansioiden toimintaperiaate

# Kansioiden toimintaperiaate

Raportteja voidaan kansioida. Käyttämällä customer -tai company tasoista kansiota, sen alla olevat raportit jaetaan samalla muiden käyttäjien kanssa. Kansioiden käytöllä voi olla siis kaksi funktiota; raporttien kansioiminen ja raporttien jakaminen toisten käyttäjien kanssa.

## Customer -tasoinen kansio

Customer -tasoinen kansio jakaa kaikki raportit, jotka ovat kyseisessä kansiossa, kaikkien asiakkuuden Customer -tasoisten käyttäjien kanssa. Kansio, sekä kaikki sen alle kiinnitetyt raportit, näkyvät aina "Reports" -valikossa - vaikka yritystä ei olisi valittu.

## Company -tasoinen kansio

Company -tasoinen kansio käyttäytyy käyttäjäroolin mukaisesti. Mikäli käyttäjän rooli on CompanySuperUser (eli yritystasoinen pääkäyttäjä), näkyy tällaiselle käyttäjälle Company -tasoinen kansio, sekä sen alla olevat raportit aina; myös vaikka yritystä ei olisi valittu.

Rajatun roolin käyttäjälle Company -tasoinen kansio taasen näkyy vain, jos hänen roolilleen on määritelty näkyvyys kyseiseen kansioon. Määrittely tehdään kansiokohtaisesti, jolloin voidaan määritellä mihin kaikkiin kansioihin (ja niiden alla oleviin raportteihin) käyttäjälle halutaan saada näkyvyys. Rajatun roolin käyttäjän kohdalla tulee myös huomioida, että roolille annetut muut oikeudet itse raportin sisältöön määrittelevät, mitä käyttäjä näkee.

# Kansion luominen

Reports -näkymässä on oikeassa yläkulmassa painike "new folder", josta uusi kansio voidaan luoda.

[![](

# 

Kansiolle annetaan nimi sekä valitaan context -kenttään, onko kansio company, customer vai user tasoinen. Create -painike luo kansion. User-tasoiset kansiot näkyvät vain sen luoneella käyttäjällä, kun taas company- ja customer-tasoiset kansiot näkyvät myös muille käyttäjille.

[![](

## Kansioiden näkyminen

Kansioidut raportit näkyvät Reports -toiminnoissa siten, että kansiot näkyvät listassa ensimmäisenä ja kunkin kansion edessä olevasta "väkäsestä" kansio aukeaa siten, että sen alla olevat raportit näkyvät. Ilman kansiota olevat raportit näkyvät ominaan. Lista on aakkosjärjestyksessä.

## Raportin lisääminen kansioon

Kun kansio on luotu reports -näkymässä, ilmestyy se listan alkuun aakkosjärjestyksessä. Reports -listalla olevia raportteja voidaan sen jälkeen raahata ottamalla niistä hiirellä kiinni ja tipauttamalla haluttuun kansioon.

## Raportin poistaminen kansiosta

Kun kansio aukaistaan, nähdään mitä raportteja kansio sisältää. Raportin perässä olevasta edit-painikkeesta aukeaa ikkuna, jossa kerrotaan raportin nimi ja mahdollinen kansio. Mikäli raportti halutaan ottaa kansiosta pois, voidaan kansio poistaa ruksista. Update report päivittää muutoksen ja palauttaa raportin takaisin reports- näkymään "kansiottomaan näkymään".

[![](

## Raportin lisääminen useampaan kansioon

Raportti voi sijaita useassa kansiossa samaan aikaan. Raportin voi ensin raahata yhteen haluttuun kansioon ja sen jälkeen aukaista raportin edit -painikkeesta ko. näkymän ja lisätä raportille toisenkin kansion. Huomaa, että kansiot tulee olla luotuna valmiiksi.

[![](

[![](

*Kansiot voidaan luoda vaikka siten, että Dashboardit ja kansiot mukailevat toisiaan. Kansion "johtoryhmä" alla olevat raportit kiinnitetään dashboardille, jonka nimi on "johtoryhmä" jne.*

*Vanhat raportit voi kansioida talteen esimerkiksi vuosiluvun sisältävällä kansiolla.*

# Lisätietoja

[Roolien kautta määritellään yritystasoisen käyttäjän käyttöoikeudet Finazillassa](



artikkelin osoite on https://intercom.help/finazilla/fi/articles/4373596-raporttien-kansioiminen-kansioi-raportin-seka-mahdollistaa-raportin-jakamisen

