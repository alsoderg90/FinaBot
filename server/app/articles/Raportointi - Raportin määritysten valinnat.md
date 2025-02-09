## Raportin määritysten valinnat

Olemme käsitelleet dynaamisia alku- ja loppuaikoja aikaisemmassa artikkelissamme " [Dynaamiset alku- ja loppuajat raportoinnissa mahdollistavat automaattisesti päivittyvät raportit](". Kyseinen artikkeli esittelee toiminnon peruspiirteittäin. Tämä artikkeli havainnollistaa asiaa lisää.

Raportin määrityksistä löytyy valinta, että käytetään lukittua kuukautta rajaavana tekijänä. Valinta on kentissä dynaaminen alku- ja loppuaika. Näistä alasvetovalikoista löytyy useita erilaisia vaihtoehtoja, joita käyttämällä saadaan aikaan erilaisin määrityksin olevia raportteja.

# Raportin määritysten valinnat

Valinnat tehdään Reports -valikossa raportin tietolähteen valinnoissa. Kentät ovat nimeltään "dynamic start date" ja "dynamic end date". Tässä artikkelissa kuvataan, miten dynaamisissa alku- ja loppuajoissa olevat lukitut kuukaudet toimivat yhdessä periodin valinnan kanssa. Periodi valitaan kohdassa "period type".

[![](

# Havainnollistavat esimerkit

Havainnollistamme eri vaihtoehtojen tuottamaa dataa esimerkein. Taustatietona kerrotaan, että yrityksen aktiivisena tilikautena on 1.1.2024 - 31.12.2024 ja tilikauden lukitus on tehty 31.05.2024 päivään. Raportteja ollaan ajamassa 5.7.2024 jolloin kuluva kausi on 7/2024.

Alla on kuvattu, minkälaisia raportteja saadaan kun "period type" valintana on tilikausi (accounting period).

## Esimerkki 1: tilikauden alusta tilikauden loppuun

Dynaamisena alkuaikana on tilikauden alku ja dynaamisena loppuaikana on tilikauden loppu.

Oheinen valinta tuottaa raportin aikaväliltä 1.1.2024 - 4.7.2024. Heinäkuulle nousee lukuja niiltä osin, kuin heinäkuulle on ehtinyt syntymään tositteita. Uudet tositteet nousevat automaattisesti raporttiin, kunhan tositteet kohdistuvat kyseiselle tilikaudelle. Raporttiin nousee siis aikanaan automaattisesti elokuu, syyskuu ja niin edelleen.

[![](

## Esimerkki 2: lukitusta kuukaudesta tilikauden loppuun

Dynaamisena alkuaikana on lukittu kuukausi ja dynaamisena loppuaikana on tilikauden lukitus.

[![](

## Esimerkki 3: lukitusta kuukaudesta kuluvaan kuukauteen

Dynaamisena alkuaikana on lukittu kuukausi ja dynaamisena loppuaikana on kuluva kuukausi (joka tarkoittaa kuukautta, milloin raporttia aukaistaan). Tässä esimerkissä on heinäkuu.

[![](

Seuraavaksi näytämme vaihtoehtoja, mitä saadaan aikaan kun vaihdetaan periodin valinnaksi vaihtoehto ***"months from dynamic date".*** 

[![](

## 

## Esimerkki 4: lukitusta kuukaudesta 3 kuukautta eteenpäin

Dynaamisena alkuaikana on lukittu kuukausi ja raportoidaan 3 kuukautta eteenpäin ilman dynamic start -valintaa.

[![](

## Esimerkki 5: lukitusta kuukaudesta 3 kuukautta eteenpäin siten, että lukittu kuukausi on yksi kolmesta

Edeltävä valinta include dynamic start -valinnan kanssa.

[![](

## Esimerkki 6: lukitusta kuukaudesta 5 kuukautta taaksepäin

Dynaamisena alkuaikana on edelleen lukittu kuukausi ja raportoidaan 5 kuukautta taaksepäin ilman include dynamic start -valintaa.

[![](

[![](

*Esimerkeissä on valintana current period, joka viittaa tilikauteen 2024. Vaihtamalla tilikautta previous period valintaan, muodostuvat yllä mainitut raportit vuodelta 2023. Vastaavasti taas next period -valinta tuottaa samat raportit seuraavalta tilikaudelta, joka on esimerkissämme 2025.* 

# Lisätietoja

[Dynaamiset alku- ja loppuajat raportoinnissa mahdollistavat automaattisesti päivittyvät raportit](

[Lukituspäivän käyttäminen mahdollistaa raportoinnin siihen saakka mihin kirjanpito on valmistunut](



artikkelin osoite on https://intercom.help/finazilla/fi/articles/4167040-lukitun-kuukauden-kayttaminen-yhdessa-ajanjakson-valinnan-kanssa

