## Alkuperäisen raportin pivotointi ja muutokset uusissa graafisissa raporteissa

[![](

*Versiopäivityksessä 9.9.2022 tuotu kokonaan uusi toiminto. Toiminto on **vaihtoehtoinen** tapa luoda Finazillassa graafisia raportteja.*

Tässä artikkelissa kerromme yleisesti uudesta tuodusta ominaisuudesta, joka on laajemman kehitystyön tulos. Tuotu ***vaihtoehtoinen*** tapa luoda graafisia raportteja on nimensä mukaisesti nimenomaan vaihtoehtoinen tapa, eikä se korvaa tai poista Finazillan aikaisempia graafisia raportteja. Kaikki käyttäjien aikaisemmin luodut graafiset raportit toimivat siis aivan kuten ennenkin.

Jatkossa graafisien raporttien luomiseen on kaksi vaihtoehtoista tapaa - ja paikkaa. Käyttäjä voi valita kumpaa hän käyttää, tai käyttää molempia. Vanhoihin grafisiin raportteihin ei ole tehty mitään muutoksia, joten ne toimivat kuten ennenkin ja samassa paikassa kuin ennenkin. Tämän rinnalle on tuotu tässä artikkelissa kuvattu toinen grafiikkakirjasto.

Selkeyden vuoksi olemme päivittäneet käyttöohjettamme siten, että käyttöohjeessa on nyt "raportointi" kokoelman alla uusi kokoelma nimeltä "graafinen raportointi". Kokoelmasta löytyy kaksi alakokoelmaa; "Finazillan grafiikkakirjasto" ja "Uusi grafiikkakirjasto, beta -versio". Näin oikea käyttöohje on helpompi löytää.

[![](

*Työkalu on uusi ja se on beta -versio. Tämä tarkoittaa sitä, että toimintoa kehitetään edelleen.*

Otamme mielellämme kaikenlaista asiakaspalautetta ja kehitysajatuksia vastaan uudesta työkalusta osoitteeseen [asiakaspalvelu@finazilla.fi](mailto:asiakaspalvelu@finazilla.fi)

# **Alkuperäisen raportin pivotointi ja muutokset uusissa graafisissa raporteissa**

Uudessa grafiikkakirjastossa ei ole linkitystä pivot -ominaisuuksiin (poislukien kuukausien pivotoiminen raportilta pois). Tämä tarkoittaa sitä, että jos käyttäjä käy pivotoimassa raporttia Finazillan reports -valikossa, ei Dashboardin raporttiwidget päivity vastaamaan pivotointia.

Mikäli raporttia pivotoidaan sen jälkeen kun siitä on luotu widget Dashboardille käyttämällä uutta grafiikkakirjastoa, tulee käyttäjän muokata dashboardin raporttiwidgettiä myös, jotta muutokset saadaan heijastumaan Dashboardille. Tyypillinen esimerkki raportin pivotoinnista olisi esimerkiksi dimensioiden esittäminen raportilla halutussa paikassa.

Jos esimerkiksi kerran luotuun raporttiin käytäisiin jälkikäteen pivotoimassa dimensiot vaikkapa sarakkeille, ei nämä muutokset heijastu käyttäjälle Dashboard -raportin kautta automaattisesti. Graafiselta raportilta löytyy tämän jälkeen kyllä widgetin asetuksista ko. raportin dimensiot, mutta käyttäjän pitää kertoa, miten ne esitetään graafisessa raportissa.

[![](

[![](

*Uuden grafiikkakirjaston logiikka poikkeaa siis muiden Dashboardien osalta, sillä niistä puuttuu linkki pivot -ominaisuuksiin.* *Vanhat graafiset raportit toimivat edelleen kuten ennenkin.*

# 

Uusi graafisten raporttien kokonaisuus muodostuu useammasta erilaisesta graafisesta raportista, jonka käsittelemme kunkin omissa artikkeleissaan. Linkit löytyvät alta.

# Lisätietoja

[Osa 1: pylväs](

[Osa 2: viiva](

[Osa 3: pylväs ja viiva](

[Osa 4: Piirakka](

[Osa 5: pinottu pylväskuvio](



artikkelin osoite on https://intercom.help/finazilla/fi/articles/6544792-uusi-vaihtoehtoinen-tapa-luoda-graafisia-raportteja-chart

