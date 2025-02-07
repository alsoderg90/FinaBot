## Raportin muodostaminen

[![](

*Versiopäivityksessä 11.9.2023 tuotu kokonaan uusi toiminto. Toiminto on **vaihtoehtoinen** tapa luoda Finazillassa graafisia raportteja.*

Tuotu ominaisuus on osa laajempaa kokonaisuutta. Tässä artikkelissa esitelty ominaisuus on osa 7. Tuotavia osia on yhteensä 7. Toimintoon liittyy myös seuraavat ominaisuudet:

[Osa 1: Pylväs](

[Osa 2: viiva](

[Osa 3: pylväs ja viiva](

[Osa 4: Piirakka](

[Osa 5: pinottu pylväskuvio](

[Osa 6: Donitsi (amount)](

# Raportin muodostaminen

Dashboard asetetaan editointi -tilaan ja lähdetään luomaan uutta sisältöä add widget -painikkeen kautta. Valinta on nimeltään "Chart".

[![](

## Haluttu raportti

Seuraavaksi widget -ikkunassa tulee valita kohtaan "report", että mistä raportista graafinen raportti halutaan luoda ja visualization -kentässä kerrotaan, että minkälaista graafista raporttia ollaan luomassa. Tässä artikkelissa käsitellään nimenomaan valintaa donitsi eli "Donut".

[![](

## Donitsin tyyppi (Donut type)

Donitsi (donut) graafeja on kahdenlaisia. Toinen malli on "amount" malli ja toinen on "target". Amount donitsi toimii samalla tavalla kuin piirakka ja on siten käytännössä ihan sama asia kuin piirakka ilman keskustaa.

Target tyyliselle donitsille voi taasen käsin antaa tavoitteen, jolloin donitsi piirtyy tavoitteen mukaan. Donitsin keskellä näytetään, että montako prosenttia tavoitteesta on saavutettu.

Tässä artikkelissa kuvaamme nimenomaan target -tyyppisen donitsin toimintaa. Amount donitsista on erillinen ohje täällä.

## Target amount

Target amount kentässä target tyyliselle donitsille voi käsin antaa tavoitteen. Donitsi piirtyy tavoitteen mukaan ja keskellä näytetään, että montako prosenttia tavoitteesta on saavutettu. Tavoitteen voi syöttää käsin tai valita valikon kautta.

Jos esimerkiksi liikevaihtotavoite on vaikkapa 900 000€, syötetään tämä arvoksi target amount -kenttään.

## Haluttu raporttimallin rivi

Widgetin luonti-ikkunassa kerrotaan kentässä "Report Scheme Row" se raportin rivi, mistä donitsi halutaan piirtää. Lisäksi data source valinnassa kerrotaan, mistä raportin tietolähteestä on kyse.

[![](

Create widget -painike luo Dashboardille graafisen raportin, jota voidaan tämän jälkeen muokata haluttuun suuntaan widgetin oikean yläkulman ratas -painikkeen takaa.

Tavoiteliikevaihdoksi asetettiin 900 000€ ja kyseisen yrityksen liikevaihto on kyseisellä hetkellä 868 687,00€, jolloin keskiosan prosenttikenttään tulee tätä kuvaava prosentuaalinen arvo. 97% tavoite liikevaihdosta on siis saavutettu.

[![](

# Raportin editointi

Widgetin luomisen jälkeen raporttia voidaan editoida widgetin oikean yläkulman ratas -kuvakkeen takaa. Editoinnissa voidaan kertoa, että mikä on donitsi -muotoisen raportin "*pie value key*" eli onko kyseinen rivi jaettu paloiksi jonkun tietyn dimension mukaan -ja jos on niin minkä.

Esimerkin liikevaihto -raportti on luotu raportoinnin puolella valinnalla dimensio/column. Tämän johdosta raportin editoinnissa näkyy valikossa "pie value key" myös kaikki raportin dimensiot.

[![](

Kun raportille on valittu haluttu dimensio, voidaan valita erikseen valinnalla "show blank", halutaanko kohdistamattomat luvut, eli ns. blank -luvut, esittää graafissa.

## Legend type

*Legend type* -valikosta voidaan vaikuttaa siihen, missä widgetissä esitetään tietolähteiden nimet (tässä esimerkissä liikevaihto kuluva). Valikosta saa myös valinnan none, jolloin tietolähteiden nimiä ei esitetä lainkaan.

[![](

## Label settings

*Label settings* -valikon takaa graafista raporttia voidaan muokata lisää ja valikon kautta voidaan tuoda esimerkiksi donitsin sektoreille näytettäväksi niiden arvot tai dimensioiden nimet. Valikosta voidaan valita, näytetäänkö tiedot graafin päällä, keskellä, alla vai ei lainkaan. Myös lukujen/tekstien väriä voidaan vaihtaa.

[![](

## Advanced settings

*Advanced settings* -valikosta voidaan vaikuttaa siihen, näytetäänkö raportissa desimaaleja tai onko raportti kenties tuhansissa.

Alla olevassa kuvassa dimension arvojen nimet esitetään graafin oikeassa reunassa (legend type: right) ja raportti on prosentuaalisessa muodossa (text: percent) siten, että prosentit esitetään donitsin sektoreiden sisäpuolella (position: inside)

Lisäksi piirakkaa on muokattu sektoreiden värien osalta klikkaamalla haluttua sektoria ja valitsemalla haluttu väri.

[![](

## Elementtiä klikkaamalla ja sitä kautta tehtävät muutokset

Elementtiä, eli donitsin sektoreita, klikkaamalla niiden väriä voidaan myös vaihtaa muuksi halutuksi. Värivalikosta löytyy valmiita värivaihtoehtoja, mutta sen lisäksi kenttään voidaan syöttää mikä tahansa värikoodi käyttämällä # -merkkiä ja kyseisen värin koodia.

Custom URL -kenttä on käyttäjille tuttu jo entuudestaan dashboardien kautta. Kenttään voidaan asettaa osoite, johon käyttäjä päätyy kyseistä elementtiä klikatessaan. Jos siis pylväälle asetetaan jokin URL - osoite, pylvästä klikkaamalla käyttäjä päätyy kyseiseen sijaintiin.

[![](

[![](

*Dimensioittain esitettävissä raporteissa luvut ovat aina kumulatiivisia*



artikkelin osoite on https://intercom.help/finazilla/fi/articles/8347839-uusi-grafiikkakirjasto-osa-7-donitsi-target

