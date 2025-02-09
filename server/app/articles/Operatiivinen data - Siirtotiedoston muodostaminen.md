## Siirtotiedoston muodostaminen

Artikkelissamme ["Mitä operatiivinen data on ja miten sitä voidaan käyttää Finazillassa"]( olemme kuvanneet operatiivisen datan käyttömahdollisuuksia Finazillassa yleisellä tasolla. Tässä artikkelissa neuvomme vaihe vaiheelta, miten operatiivista dataa tuodaan Finazillaan sisään.

[![](

*Operatiivisen datan käsitteleminen Finazillassa on kokonaan oma maailmansa, mistä johtuen suosittelemme vahvasti konsultoimaan Finazillan henkilökuntaa ennen operatiivisen datan käsittelemistä Finazillassa.* 

# Siirtotiedoston muodostaminen

Operatiivista dataa tuodaan sisään CSV- tiedostolla. Valmiin siirtotiedoston voi ladata [täältä]( Valmis pohja on valmiiksi csv -muodossa. Tiedostoon tulee nimetä dimensiot halutulla tavalla (dimensio 1, dimensio 2). Mikäli käytössä on vain yksi dimensio, voi toisen poistaa. Lisää dimensioita voi lisätä lisäämällä uuden otsikon seuraavaan sarakkeeseen.

Tiedoston tulee täyttää tietyt kriteerit, jotta tietojen sisäänluku onnistuu. Pääideana on, että dimension nimi poimitaan CSV:n otsikkorivistä (nk. header -rivi) ja dimension arvo on kyseisen otsikon kohdalla oleva arvo datassa.

## Pakolliset tiedot siirtotiedostossa

Pakollisia tietoja siirtotiedostossa ovat otsikkorivi, josta löytyy vähintään alla olevan kuvan mukaiset sarakkeet. Kaikissa sarakkeissa ei ole pakko esittää tietoja, mutta suosittelemme jättämään silti sarakkeet A-C aineistoon mukaan, jotta aineiston sisäänajossa ei ilmene ongelmia.

Amount -kenttään syötetään euroja ja quantity -kenttään jotakin muuta määrettä, kuten esimerkiksi tehtyjä työtunteja tai kappalemääriä. Samassa tiedostossa voi olla molempia tietoja; sekä euroja (amount), että esimerkiksi työtunteja (quantity) tai vain toinen tiedoista.

[![](

## Valinnaiset muut tiedot siirtotiedostossa

Näiden lisäksi siirtotiedostoon voidaan laittaa muuta haluttua dataa, kuten esimerkiksi ihmisten nimiä, osien nimiä, projektien tunnisteita, alv-koodeja tai mitä tahansa dataa mitä halutaan siirtyväksi Finazillaan. Kaikki muut sarakkeet tulevat dataan dimensioina.

Esimerkiksi alla olevassa kuvassa sarakkeet D ja E siirtyvät Finazillaan dimensioiksi siten, että "worker" on dimensio ja "Jane Doe", "John Doe" jne ovat ko. dimension dimensiovalueita. Sama logiikka pätee sarakkeeseen E.

[![](

[![](

*Sisäänajotiedoston voi luoda tyhjästä, mutta myös olemassaolevaa excel -tiedostoa voi olla miellekästä käyttää pohjana. Mikäli lähtötiedot ovat jossain järjestelmässä, voi olla järkevää selvittää, saako tiedot ajettua lähtöjärjestelmästä valmiiksi exceliin - ennemmin kuin alkaa rakentamaan sisäänajotiedostoa tyhjästä.* 

Olemassaolevan Excel -tiedoston saa helposti vaadittuun CSV -formaattiin tallentamalla tiedosto ko. valinnalla:

[![](

# Siirtotiedoston ajaminen sisään Finazillaan

Kun haluttua dataa sisältävä CSV- tiedosto on tehty, navigoidaan "Company settings" sivulle ja raahataan tiedosto "integration file drop-in" laatikkoon ja valitaan vaihtoehto "operative data" kohtaan "data type". Source system -valintaan suosittelemme valitsemaan vaihtoehdon "Generic".

[![](

Data Group identifier kohta saa aina automaattisesti tiedoston nimen arvokseen. Jos tiedoston nimi ei kuitenkaan ole halutunlainen, niin kenttä voidaan avata hiirellä ja syöttää käsin eri arvo. Painamalla "save" valinta tallentuu.

[![](

*Nimeämiseen kannattaa kiinnittää huomiota, sillä tässä kohdin annettu tiedostonimi on sama nimi, millä kyseinen data haetaan aina jatkossa raporteille. Tästä syystä dokumentin nimen tulisi olla mahdollisimman kuvaava, jotta käyttäjän on helppoa löytää oikea tiedosto useiden joukosta myöhemminkin.* 

*Lisäksi tulee huomioida, että aina kun operatiivista dataa tuodaan sisään, luo Finazilla datasta uuden data groupin ellei käyttäjä valitse jotain jo olemassa olevaa Data Groupia.* 

*Näin ollen jos esimerkiksi Finazillaan tuodaan vaikkapa työtunteja kerran kuukaudessa ja ensimmäisellä tuontikerralla data on tuotu siten, että data groupiksi on syntynyt "työntekijöiden työtunnit 2020", tulee tämä vaihtoehto valita data group identifier -kenttään aina kun uusia tunteja tuodaan - muuten uudet tunnit tulevat eri data groupille.* 

## Siirtotiedoston ajaminen uudelleen sisään Finazillaan

Jos samaa dataa halutaan ajaa uudelleen sisään, ei aineistoa tarvitse ajaa kokonaan tietojen alusta saakka; riittää kun ajetaan uudet tiedot sisään. Tällöin tulee kuitenkin muistaa valita uusinta-ajossa sama Data Group Identifier kuin ensimmäiselläkin kerralla. Näin kumpikin aineisto raportoituu yhdessä.

Lisäksi suosittelemme, että mikäli tiedostoa päivitetään, tehdään päivitykset alkuperäiseen excel tiedostoon (eikä jo tallennettuun csv -tiedostoon) ja tämän jälkeen tiedosto tallennetaan csv -muotoon.

## Ominaisuudessa huomioitavaa:

* Konsultoi mahdollisuuksien mukaan Finazillan tiimiä ensin jos haluat hyödyntää operatiivisen datan mahdollisuuksia.

* Jos eteen nousee tarve saada lähdejärjestelmän tuottamaa operatiivista dataa sellaisenaan Finazillaan, tai saada laajempia mahdollisuuksia customoida dataa esimerkiksi suomenkielelle, voidaan tämä toteuttaa erillisenä integraatioprojektina. Näissä tilanteissa suosittelemmekin kontaktoimaan myyntiämme ([myynti@finazilla.fi](mailto:myynti@finazilla.fi)) parhaan vaihtoehdon kartoittamiseksi.

* Mikäli tuodaan operatiivisena datana lukuja Finazillaan (esimerkiksi vaikka myyntejä), tulee huomioida, että plus -merkkiset luvut tulevat plussana ja miinusmerkkiset miinuksena. Toimintalogiikka eroaa siis Vouchereiden syöttämisestä, jossa noudatetaan kirjanpidon credit / debit logiikkaa.

* Huomioi Data Groupin merkitys datan tuonnissa. Jos tarkoituksena on tuoda esimerkiksi työtunteja säännöllisesti Finazillaan, luo ensimmäisellä tuontikerralla Data Group "työtunnit" ja valitse jatkossa aina sama Data Group kun tuot työtunteja - muutoin jokainen tuotu tiedosto on omana Data Grouppinaan.
* Aineistosta generoituu automaattisesti operatiiviset dimensiot, mikäli sellaisia on käytetty.
* Muokkaukset ja lisäykset tiedostoon kannattaa tehdä excel -muotoiseen tiedostoon, joka tallennetaan csv -muotoon ennen sisäänlukua.
* Uusi tiedosto yliajaa vanhan. Jos jokin tieto täytyy saada poistettua, on helpoin tapa tuoda se uudelleen sisään nollasaldoisena, jolloin se saadaan nollattua. Käyttäjä ei pysty itse ns. poistamaan tuomaansa dataa muutoin.
# Lisätietoja

[Mitä operatiivinen data on ja miten sitä voidaan käyttää Finazillassa?](



artikkelin osoite on https://intercom.help/finazilla/fi/articles/4276823-operatiivisen-datan-tuominen-finazillaan-vakiomuotoisella-csv-siirtotiedostolla

