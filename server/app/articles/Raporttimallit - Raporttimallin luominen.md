## Raporttimallin luominen

Artikkelimme ["Raporttimallin avulla dimensioiden filtteröinti"]( kuvaa toimintoa yleisellä tasolla. Tässä työohjeessa neuvomme esimerkin avulla vaihe vaiheelta, miten luodaan yksinkertainen raporttimalli käyttämällä dimensiofiltteriä ja miten raporttimallilla raportoidaan. Artikkelin ymmärtämistä helpottaa, jos käyttäjä tietää jo mitä raporttimallit ovat ja mihin niitä käytetään Finazillassa.

Raporttimallit suositellaan tehtävän Customer -tasolla, jotta ne ovat käytettävissä kaikilla asiakkuuden yrityksillä. Raporttimallit löytyvät "report scheme" valikosta.

Tässä esimerkissä luodaan raporttimalli, jossa on mukana liikevaihto ja rajauksia dataan tehdään dimensiofiltterin kautta.

# **Raporttimallin luominen**

Uusi raporttimalli luodaan Customer -valikossa kohdassa "Report Scheme" valitsemalla "New Report Scheme" -painike. Raporttimallille annetaan nimi sekä tarkempi muu haluttu kuvaus kohdassa "description". Tässä esimerkissä raporttimallin taustalle ei oteta mitään valmista mallia, vaan raporttimalli luodaan tyhjästä - siksi kenttään "from template" ei valita mitään.

[![](

Create report scheme -painike tallentaa tehdyn raporttimallin, jonka jälkeen se löytyy "report scheme" näkymästä sille annetulla nimellä. Klikkaamalla raporttimallin nimeä, päästään luomaan nk. raporttipuuta.

# **Raporttipuun luominen**

Seuraavaksi on vuorossa varsinaisen "raporttipuun" luominen. Tämä alkaa klikkaamalla raporttimallin nimeä raporttimallilistassa, jolloin avautuu raportin rakenne eli ”raporttipuu”. Tässä esimerkissä luomme raporttimallin, jossa on seuraavat rivit:

• Liikevaihto

## **Rivien lisääminen**

Raporttimallin nimeä klikatessa avautuva näkymä on tyhjä, sillä mitään valmista pohjaa ei ole käytetty. Raporttimallin rakentaminen alkaa klikkaamalla ”New Row” –painiketta.

[![](

1. Rivin tyypiksi valitaan ”Header”, joka tarkoittaa ns. otsikkoa. Käytännössä tämä on ensimmäinen rivi, joka tulee näkyviin valmiille raportille. Nimetään rivi ”Liikevaihto” ja ”visible” kohtaan laitetaan ruksi, koska haluamme, että rivi Liikevaihto näkyy itse raportilla.

Rivin luomisen jälkeen näkymä on seuraava:

[![](

## **Lapsirivin lisääminen**

Raportilla halutaan esittää tietoa juuri luodulla "Liikevaihto" rivillä, joten raporttimallille lisätään uusi ”Child row”eli ns. lapsirivi klikkamalla painiketta "New Child Row" -painiketta juuri luodun liikevaihto rivin perästä. Käyttäjälle aukeaa tämän jälkeen uuden rivin syöttöikkuna.

[![](

Luodun "lapsirivin" tyypiksi valitaan ”Balance data”, joka tarkoittaa sitä, että tietoa tällä rivillä esitetään kirjanpidon datasta. ”Visible” kohtaan tulee jälleen automaattisesti ruksi, koska luvun halutaan näkyvän raportilla.

## **Tilivälin valitseminen**

Seuraavaksi valitaan tiliväli, josta rivin halutaan laskevan saldot yhteen. Kyseisessä raporttimallin rivissä ollaan laskemassa liikevaihtoa, joten tässä tapauksessa rajaus on tilistä 3000 tiliin 3599.

*HUOM! Riippuen yhtiöstä ja käytettävistä tileistä, välille saattaa kuulua myös liiketoiminnan muiden tuottojen tilejä; asiakas vastaa aina itse rakennettujen raporttimallien raportoinnin oikeellisuudesta itse.*

## **Row factor -valinta**

”Row Factor” kohdassa valitaan joko vaihtoehto "Credit" tai "Debit". Liikevaihtotilien luvut ovat kirjanpidossa credit- eli miinusmerkkisiä kun taas raportoinnissa tuottoluvut yleensä halutaan esittää positiivisena, joten tässä käytetään kertojana miinusta. Näin ollen lopputulos on positiivinen.

## **Saldojen summautumisen valinnat**

”Sum account range to parent” valinta tarkoittaa sitä, että saldojen summa näkyy parent rivillä (joka on tässä tapauksessa ensimmäiseksi luotu liikevaihtorivi). Valitaan kyseinen vaihtoehto, sillä haluamme tilien saldojen summan näkyvän liikevaihtorivillä.

Jos valinta jätettäisiin tekemättä, raportilla olisi seuraava esitystapa:

[![](

## **Dimensiofiltterin lisääminen**

"Filter data by dimensions" kohdassa määritellään dimensiorajaus. Tässä esimerkissä yritykselle "Movies Ltd" on valittu dimensiovalue "Finlands" ja yritykselle "Series Ltd" on valittu koko dimensio "tapahtumat", jolloin raportille nousee kyseisen yrityksen kohdalle kaikki dimensiovaluet, jotka ovat ko. dimension alla.

Kyseinen raporttimallin valinta tuottaa siis raportin, johon nousee liikevaihdoksi yrityksen "Movies Ltd" tapahtumat tiliväliltä 3000 - 3599 niiltä osin, missä dimensiovaluena on Finland. Samaan raporttiin nousee yrityksen "Series Ltd" liikevaihdoksi tapahtumat tiliväliltä 3000 - 3599 niiltä osin, missä dimensiovaluena on mikä tahansa dimension "tapahtumat" valueista.

Muihin raporttimallin kohtiin jätetään oletusvalinnat.

Kun rivi on tallennettu, raporttirakenne näyttä seuraavalta (huomaa, että liikevaihto-otsikon edessä olevasta nuolesta tiedot saa auki):

[![](

Tämän jälkeen raporttimalli on valmis käytettäväksi ja sillä voidaan raportoida normaalisti "reports" -valikossa. Raportointi aloitetaan normaalisti luomalla uusi raportti "New Report" painikkeesta. Kohtaan "Report Scheme" valitaan juuri luotu raporttimalli. Raportin luomista olemme kuvanneet artikkelissamme [Raportin muodostaminen](

[![](

*Mikäli Finazillassa on jo valmiina tarpeisiin sopiva raporttimalli (tai hyvin lähellä oleva), johon halutaan lisätä dimensiofiltteri käyttöön, kannattaa valmis raporttimalli kopioida ja muokata lisäämällä siihen mm. halutut filtterit. Näin säästetään valtavasti aikaa siihen nähden, että luodaan kokonaan uusi raporttimalli tyhjästä.* 

# Lisätietoja

[Valmiin raporttimallin hyödyntäminen raportoinnissa](

[Valmiin raporttimallin muokkaaminen omiin tarpeisiin sopivaksi](

[Raporttimallin rakentaminen alusta saakka](



artikkelin osoite on https://intercom.help/finazilla/fi/articles/4877992-esimerkki-liikevaihto-raporttimallin-luominen-kayttamalla-dimensiofiltteria

