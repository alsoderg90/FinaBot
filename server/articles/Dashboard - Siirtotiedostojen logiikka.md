## Siirtotiedostojen logiikka

Olemme kertoneet artikkelissamme ["Finazillan valmiit Dashboardit, osa 1"]( Finazillan uusista Dashboardeista, jotka asiantuntijamme ovat rakentaneet valmiiksi. Dashboardeilla on kymmeniä raportteja, jotka ovat asiakkaidemme käytettävissä jo heti, mutta Dashboardit sisältävät myös valmiita raportteja, joiden näkyminen vaatii valmiin siirtotiedoston tuomisen Finazillaan. Tässä artikkelissa neuvomme, kuinka loput Dashboardin raportit saadaan raportoimaan niissä olevia asioita.

Tämän ohjeen avulla voit tuoda Finazillan vakiodashboardeille tietoa valmiiksi rakennetuilla sisäänlukutiedostoilla. Kunkin siirtotiedoston kohdalla on lyhyet ohjeet siitä, kuinka tiedostoa tulee täydentää - ja millä tiedoilla. Siirtotiedostoihin löytyy suora linkki kustakin kappaleesta. Linkin kautta voi ladata siirtotiedoston itselleen. Ladattu tiedosto tulee käyttäjälle oheisen kaltaisesti näkyviin, josta tiedoston pääsee tallentamaan itselleen.

Tiedoston lataamisen jälkeen tiedostoon tulee täydentää itse kunkin tiedoston mukaiset tiedot. Tämän jälkeen tiedosto tallennetaan ja tämän jälkeen tuodaan sisään Finazillaan.

[![](

[![](

Huomioithan, että **tiedoston** **nimeä ei tule missään nimessä muuttaa millään tavalla** (nimi on tietovirran yksilöivä tieto, jonka perusteella tiedot raportoituvat vakioraporteilla). ***HUOM: joissakin tapauksissa tiedoston lataaminen omalle koneelle tekee tiedoston nimen perään numeron. Numeroa ei tule jättää lopulliseen tiedostoon, vaan nimen tulee olla kaikissa tiedostoissa ilman latausnumeroita, kuten alla:***

[![](

Siirtoaineiston **logiikka on ”poista kaikki - lisää kaikki”**, jolloin samalla päivämäärällä tuotava tieto poistaa aina päivämäärärajauksella kaikki tiedot ja korvaa vanhat tiedot.

# Siirtotiedostojen logiikka

Siirtotiedostot tuodaan sisään Finazillaan nk. operatiivisena datana. Tiedosto tipautetaan Finazillaan sisään, jonka jälkeen Dashboardeilla olevat raportit alkavat raportoimaan automaattisesti tuotua dataa.

# **Offers lost**

Offers lost tuo Finazillan Sales Dashboardille tietoa hävityistä tarjouksista.

Valmis siirtotiedostopohja offers lost löytyy [tästä](

* Date/Päivämäärä:

  + Suositus: päivämääräksi tarjouksen häviämispäivämäärä
  + Raportoi tietoa koska tarjous on merkitty hävityksi
  + Voit seurata miten tehtyjä tarjouksia on hävitty
  + Ei suositella: tarjouksen päivämääräksi tarjouksen päivämäärä
  + Raportoi hävittyjä tarjouksia tarjouspäivämäärän mukaan, eli minä päivänä tehtyjä tarjouksia on hävitty
  + Huomioi, että vanhat hävityt tarjoukset poistuu, jos aiemmissa aineiston sisäänluvuissa on ollut hävittyjä tarjouksia samalla päivällä
* Quantity

  + Ei pakollinen tieto
  + Mahdollistaa lisäämällä arvon 1, voit raportoida hävittyjen tarjousten kappalemääriä
* Amount

  + Pakollinen tieto
  + Anna tarjouksen arvo rahana
  + Valmiiksi asetetut operatiiviset dimensiot, joilla raporttia voi ryhmitellä
* Customer = Asiakas

  + Nimeä tarjouksella oleva asiakas
* CustomerGroup = Asiakasryhmä

  + Nimeä halutessasi asiakasryhmä
* Product = Tuote

  + Nimeä tarjottu tuote
* ProductGroup = Tuoteryhmä

  + Nimeä halutessasi tuotteen ryhmä
* Seller = Tarjouksen tehnyt myyjä

  + Nimeä myyjä
* Customer Contact Person = Asiakkaan yhteyshenkilö

  + Nimeä esimerkiksi tarjouksen saanut henkilö
* Probability = Tarjouksen todennäköisyys
* Hävityn tarjouksen arvo voi olla esim. ”Hävitty” tai ”0”
* Offer number = Tarjouksen yksilöivä numero

  + Anna numero, jos tarjouksen voi yksilöidä
# **Offers new**

Offers new tuo Finazillan Sales Dashboardille tietoa uusista tehdyistä tarjouksista.

Valmis siirtotiedosto offers new löytyy [tästä.](

* Date/Päivämäärä:

  + Suositus: Päivämääräksi tarjouksen tekemisen tai toimittamisen päivämäärä
  + Raportoi tietoa tarjousten syntymisestä
  + Voit seurata miten uusia tarjouksia on syntynyt
  + Ei suositella: muita päivämääriä
* Quantity

  + Ei pakollinen tieto
  + Mahdollistaa lisäämällä arvon 1, voit raportoida tarjousten kappalemääriä
* Amount

  + Pakollinen tieto
  + Anna tarjouksen arvo rahana
  + Valmiiksi asetetut operatiiviset dimensiot, joilla raporttia voi ryhmitellä
* Customer = Asiakas

  + Nimeä tarjouksella oleva asiakas
* CustomerGroup = Asiakasryhmä

  + Nimeä halutessasi asiakasryhmä
* Product = Tuote

  + Nimeä tarjottu tuote
* ProductGroup = Tuoteryhmä

  + Nimeä halutessasi tuotteen ryhmä
* Seller = Tarjouksen tehnyt myyjä

  + Nimeä myyjä
* Customer Contact Person = Asiakkaan yhteyshenkilö

  + Nimeä esimerkiksi tarjouksen saanut henkilö
* Probability = Tarjouksen todennäköisyys
* Hävityn tarjouksen arvo voi olla esim. ”Hävitty” tai ”0”
* Offer number = Tarjouksen yksilöivä numero

  + Anna numero, jos tarjouksen voi yksilöidä
# **Offers open**

Offers open tuo Finazillan Sales Dashboardille tietoa kyseisenä hetkenä auki olevista tarjouksista. Valmis siirtotiedostopohja offers open löytyy [tästä.](

* Date/Päivämäärä:

  + Suositus: Päivämääränä aineiston sisäänlukuhetki, esimerkiksi kuun viimeinen päivä
  + Raportoi kuinka paljon avoimia tarjouksia on ollut minäkin kuukautena/sisäänlukuhetkenä
  + Tarjouskannan historia pysyy tallessa, kun data tuodaan kuukausittain omalla päivämäärällä
  + Ei suositella: Muita päivämääriä
* Quantity

  + Ei pakollinen tieto
  + Mahdollistaa lisäämällä arvon 1, voit raportoida tarjousten kappalemääriä
* Amount

  + Pakollinen tieto
  + Anna tarjouksen arvo rahana
* Valmiiksi asetetut operatiiviset dimensiot, joilla raporttia voi ryhmitellä
* Customer = Asiakas

  + Nimeä tarjouksella oleva asiakas
* CustomerGroup = Asiakasryhmä

  + Nimeä halutessasi asiakasryhmä
* Product = Tuote

  + Nimeä tarjottu tuote
* ProductGroup = Tuoteryhmä

  + Nimeä halutessasi tuotteen ryhmä
* Seller = Tarjouksen tehnyt myyjä

  + Nimeä myyjä
* Customer Contact Person = Asiakkaan yhteyshenkilö

  + Nimeä esimerkiksi tarjouksen saanut henkilö
* Probability = Tarjouksen todennäköisyys
* Hävityn tarjouksen arvo voi olla esim. ”Hävitty” tai ”0”
* Offer number = Tarjouksen yksilöivä numero

  + Anna numero, jos tarjouksen voi yksilöidä
# **Orders new**

Orders new tuo Finazillan Sales Dashboardille tietoa uusista tilauksista, eli voitetuista tarjouksista. Valmis siirtotiedostopohja oders new löytyy [tästä.](

* Date/Päivämäärä:

  + Suositus: Päivämääräksi tilauksen vastaanoton päivämäärä
  + Raportoi tietoa koska tarjous on muuttunut tilaukseksi
  + Raportoi koska uusia kauppoja on saatu
  + Ei suositella: muita päivämääriä
* Quantity

  + Ei pakollinen tieto
  + Mahdollistaa lisäämällä arvon 1, voit raportoida tarjousten kappalemääriä
* Amount

  + Pakollinen tieto
  + Anna tarjouksen arvo rahana
* Valmiiksi asetetut operatiiviset dimensiot, joilla raporttia voi ryhmitellä
* Customer = Asiakas

  + Nimeä tarjouksella oleva asiakas
* CustomerGroup = Asiakasryhmä

  + Nimeä halutessasi asiakasryhmä
* Product = Tuote

  + Nimeä tarjottu tuote
* ProductGroup = Tuoteryhmä

  + Nimeä halutessasi tuotteen ryhmä
* Seller = Tarjouksen tehnyt myyjä

  + Nimeä myyjä
* Customer Contact Person = Asiakkaan yhteyshenkilö

  + Nimeä esimerkiksi tarjouksen saanut henkilö
* Probability = Tarjouksen todennäköisyys
* Hävityn tarjouksen arvo voi olla esim. ”Hävitty” tai ”0”
* Offer number = Tarjouksen yksilöivä numero

  + Anna numero, jos tilausta edeltäneen tarjouksen voi yksilöidä
* Order number = Tilauksen yksilöivä numero

  + Anna numero, jos tilauksen voi yksilöidä
# Orders open

Orders open tuo Finazillan Sales Dashboardille tietoa kyseisenä hetkenä auki olevista tilauksista. Valmis siirtotiedostopohja orders open löytyy [tästä.]( 

* Date/Päivämäärä:

  + Suositus: Päivämääränä aineiston sisäänlukuhetki tai esimerkiksi kuun viimeinen päivä
  + Raportoi kuinka paljon avoimia/toimittaattomia tilauksia on ollut minäkin kuukautena
  + Avoimien tilausten historia pysyy tallessa, kun data tuodaan kuukausittain omalla päivämäärällä
  + Ei suositella: muita päivämääriä
* Quantity

  + Ei pakollinen tieto
  + Mahdollistaa lisäämällä arvon 1, voit raportoida tarjousten kappalemääriä
* Amount

  + Pakollinen tieto
  + Anna tarjouksen arvo rahana
* Valmiiksi asetetut operatiiviset dimensiot, joilla raporttia voi ryhmitellä
* Customer = Asiakas

  + Nimeä tarjouksella oleva asiakas
* CustomerGroup = Asiakasryhmä

  + Nimeä halutessasi asiakasryhmä
* Product = Tuote

  + Nimeä tarjottu tuote
* ProductGroup = Tuoteryhmä

  + Nimeä halutessasi tuotteen ryhmä
* Seller = Tarjouksen tehnyt myyjä

  + Nimeä myyjä
* Customer Contact Person = Asiakkaan yhteyshenkilö

  + Nimeä esimerkiksi tarjouksen saanut henkilö
* Probability = Tarjouksen todennäköisyys
* Hävityn tarjouksen arvo voi olla esim. ”Hävitty” tai ”0”
* Offer number = Tarjouksen yksilöivä numero

  + Anna numero, jos tilausta edeltäneen tarjouksen voi yksilöidä
* Order number = Tilauksen yksilöivä numero

  + Anna numero, jos tilauksen voi yksilöidä
# SalesInvoice

SalesInvoice tuo Finazillan Sales Dashboardille tietoa laskutukseen päätyneistä tilauksista / kuukausittaisen myynnin (ei liikevaihto). Valmis siirtotiedostopohja sales invoice löytyy [tästä.]( 

* Date/Päivämäärä:

  + Suositus: Päivämääräksi Laskun päivämäärä
  + Raportoi tietoa koska tilaus on muuttunut laskuksi
  + Raportoi koska uusia laskuja on tehty
  + Raportoi myyntiä
  + Ei suositella: muita päivämääriä
* Quantity

  + Ei pakollinen tieto
  + Mahdollistaa lisäämällä arvon 1, voit raportoida tarjousten kappalemääriä
* Amount

  + Pakollinen tieto
  + Anna tarjouksen arvo rahana
* Valmiiksi asetetut operatiiviset dimensiot, joilla raporttia voi ryhmitellä
* Customer = Asiakas

  + Nimeä tarjouksella oleva asiakas
* CustomerGroup = Asiakasryhmä

  + Nimeä halutessasi asiakasryhmä
* Product = Tuote

  + Nimeä tarjottu tuote
* ProductGroup = Tuoteryhmä

  + Nimeä halutessasi tuotteen ryhmä
* Seller = Tarjouksen tehnyt myyjä

  + Nimeä myyjä
* Customer Contact Person = Asiakkaan yhteyshenkilö

  + Nimeä esimerkiksi tarjouksen saanut henkilö
* Probability = Tarjouksen todennäköisyys
* Hävityn tarjouksen arvo voi olla esim. ”Hävitty” tai ”0”
* Offer number = Tarjouksen yksilöivä numero

  + Anna numero, jos tilausta edeltäneen tarjouksen voi yksilöidä
* Order number = Tilauksen yksilöivä numero

  + Anna numero, jos tilauksen voi yksilöidä
* Invoice number = Laskun yksilöivä numero

  + Anna laskun numero
# Staff working hours

Staff working hours tuo Finazillan Personale and Efficiency Dashboardille uuntitietoja, joiden avulla voidaan raportoida toiminnan tehokkuutta perustuen työtunteihin ja liiketoiminnan tuotoksiin. Valmis siirtotiedostopohja staff working hours löytyy [tästä.](

* Date/Päivämäärä:

  + Tuntikirjauksen päivämäärä
  + Koontina tietoja tuotaessa kuun viimeinen päivä
* Quantity

  + Ei pakollinen tieto
* Amount

  + Pakollinen tieto
* Anna kirjattujen tuntien määrä joko,

  + Per palkkalaji (tietojen tuonti päivittäin, henkilöittäin, palkkalajeittain)
  + Per päivä (tietojen tuonti päivittäin, henkilöittäin)
  + Per päivä (tietojen tuonti päivittäin)
  + Per kk (tietojen tuonti esim. Henkilöittäin kuukausikoontina)
* Employee

  + Nimeä työntekijä
* Gender

  + Määritä sukupuoli
* Salary type

  + Määritä tuntikirjauksen tyyppi = esim. palkkalaji


artikkelin osoite on https://intercom.help/finazilla/fi/articles/8068925-finazillan-valmiiden-dashboardien-jalostaminen-valmiiksi-rakennetuilla-sisaanajotiedostoilla

