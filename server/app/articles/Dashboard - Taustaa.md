## Taustaa

Tunnusluku widgetit (key figures widget) ovat dashboardilla käytössä oleva ominaisuus, jolla voidaan helposti lisätä erilaisia raporttien tuottamia arvoja Dashboardille nähtäväksi. Tunnusluku widget voi olla joko yksittäinen arvo tai widget voidaan muodostaa siten, että siinä verrataan tunnuslukua vaikkapa edelliseen vuoteen tai budjettiin nähden.

Tässä artikkelissa kerromme, miten yhdestä raportista voidaan muodostaa (useita) tunnusluku widgettejä dashboardille. Artikkelin ymmärtämistä helpottaa, jos käyttäjä ymmärtää mitä widgetit ovat ja miten niitä luodaan.

# Taustaa

Yritys on luonut tuloslaskelma -raportin kuluvalle vuodelle tilikausi yhteenlaskettuna. Raporttimalli mitä raportoinnissa on käytetty taustalla määrittelee sen, mitä tunnuslukuja luodusta raportista on mahdollista luoda.

Alla on kuva yrityksen luomasta tuloslaskelmasta supistettuna otsikkotasolle.

[![](

# Tunnusluvun luominen Dashboardille

Seuraavaksi mennään halutulle dashboardille ja lähdetään luomaan tunnuslukuwidgettia actions -valikon takaa edit -toiminnolla. Valitaan widget tyypiksi vaihtoehto "key figures" ja kerrotaan, mistä raportista tunnuslukuja halutaan lähteä luomaan.

[![](

Tämän jälkeen käyttäjän tulee kertoa, mistä raportin rivistä tunnusluku halutaan piirtää. Alasvetovalikosta löytyy kaikki raportin rivit. Yhdestä raportista voi siis piirtää tarvittaessa useita tunnuslukuja.

[![](

Seuraavaksi tunnuslukuwidgetin luonnissa tulee määritellä tietolähteet. Tässä esimerkissä ei ole vertailua edelliseen vuoteen, joten ensimmäiseen kenttään valitaan vaihtoehto "kuluva" ja jälkimmäiseen kenttään ei valita mitään.

[![](

# Lisäasetukset (optional settings)

Tunnuslukuwidgettiä luotaessa tietolähteiden jälkeen on otsikko "optional settings", josta voidaan avata ns. lisäasetukset.

Lisäasetuksissa widggetille voidaan määritellä haluttu otsikko, millä widget esiintyy Dashboardilla. Haluttu otsikko voidaan kirjoittaa custom title -kenttään. Mikäli kenttään ei kirjoiteta mitään, saa widget sen otsikon, mikä on raportin rivin nimenä kyseisellä raporttimallilla.

Custom URL -kentän toimintaa olemme kuvanneet artikkelissamme [täällä.]( 

Description kenttään voidaan kirjoittaa kyseisestä raportista lisätietoja. Lisätiedot aukevat Dashboardilla erillisestä i -painikkeesta omaan pop up -ikkunaansa.

Comparison colors -kohdassa tunnusluku widgetille voidaan määritellä omat halutut värit. Valinta liittyy tunnuslukuihin, jotka ovat vertailevia. Mikäli käyttäjä ei valitse mitään, on väreinä vihreä, keltainen ja punainen. Vihreä silloin kun arvo on kasvanut ja punainen kun arvo on pienentynyt. Keltainen kuvaa neutraalia.

[![](

Lopuksi haluttu tunnusluku piirretään dashboardille toiminnolla "create widget". Tämän jälkeen käyttäjä voi piirtää samasta raportista toisen haluamansa tunnusluvun.

[![](

[![](

*Useamman tunnusluku widgetin piirtäminen samasta raportista nopeuttaa dashboardien latautumista merkittävästi, joten suosittelemme toimintoa vahvasti kaikille käyttäjille*

Toiminto mahdollistaa myös vertailevien tunnusluku widgettien luomisen yhdestä raportista, silloin kun raportissa on mukana toinen tietolähde. Tällöin tulee valita widgetin luomisikkunassa tietolähteet (datasource). Data Source -kenttään valitaan se tietolähde mikä halutaan piirtää ja data source to compare -kohtaan se tietolähde, mihin arvoa halutaan verrata.

[![](

Finazillan oletuslogiikka on, että vertailevissa tunnusluvuissa valittu tunnusluku tuodaan siten, että datasource -kenttään valittu arvo tuodaan ylös ensimmäiseksi isolla. Tunnusluvun alaosassa esitetään erotus näiden kahden välillä (eli kuvan esimerkissä arvo 971 513 tarkoittaa, että kuinka paljon pienempi liikevaihto oli edellisellä vuodella).

Vihreä väri tarkoittaa, että arvo on kasvanut ja punainen, että arvo on pienentynyt verrattavaan lukuun nähden.

[![](

Mikäli väritykset eivät ole tunnuslukuun sopivat, voidaan niitä muuttaa widgetin luomisikkunassa valikon "optional settings" alla.

[![](

[![](

*Mikäli molemmat luvut halutaan esittää valkoisella värillä, voidaan värikoodiin syöttää koodi #FFFFFFF.* 

# Lisätietoja

[Yrityksen tunnusluvut apuna talouden raportoinnissa](

[Esimerkki: yksittäisen tunnusluvun kiinnittäminen Dashboardille käyttäen key figures -toimintoa](

[Esimerkki: tehdään useita tunnuslukuwidgettejä yhdestä raportista](



artikkelin osoite on https://intercom.help/finazilla/fi/articles/5626652-tunnuslukujen-kiinnittaminen-dashboardille

