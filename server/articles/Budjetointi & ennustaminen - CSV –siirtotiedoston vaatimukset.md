## CSV –siirtotiedoston vaatimukset

Jos lukuja on Excelissä paljon ja esimerkiksi on budjetoitu dimensioittain, voi luvut tuoda myös csv –tiedoston avulla sen sijaan, että budjetoidaan suoraan Finazillan budjetointi -näkymässä.

Valmis siirtotiedoston pohja löytyy [täältä.]( Tiedostossa on valmiiksi otsikot ja se on tallennettu csv -muotoon. Huomaa, että tiedostoon pitää itse nimetä dimensiot ja dimensionarvot.

# **CSV –siirtotiedoston vaatimukset**

* Siirtotiedosto pitää olla CSV -muodossa tallennettuna koneella ennen siirtoa
* Tuottoluvut tulee olla miinusmerkkisenä
* Tuhaterottimia ei saa olla sisäänajodatassa; muuten luku voi tallentua siten, että esim, 10 000€ syötetty luku tulee Finazillaan 10€ lukuna
* Tuotavien lukujen tulee olla siirtotiedostossa samalle kaudelle kuin luotu budjetti
* Siirtotiedostossa tulee olla kaikki alla mainitut otsikot, vaikka niissä ei olisikaan mitään dataa. Otsikot tulee olla täsmälleen kuvatulla tavalla kirjoitettu.
* Siirtotiedostossa ei saa olla mitään muuta ylimääräistä dataa
* Sama rivi ei voi esiintyä aineistossa identtisenä useita kertoja
* Jos budjetille tulee jotain lukuja osabudjetin kautta niin tällaisia lukuja ei voi tuoda siirtotiedostolla -tai sitten ko. budjetin rivi tulee käydä muuttamassa syöttö -riviksi
* Vyörytyssääntöjen kanssa on sama logiikka kuin yllä; tällä hetkellä riveille, missä on vyörytyssääntö, ei voi tuoda dataa toisesta tiedostosta.
* Kaikki dimensiokohdistukset tulee tuoda yhdessä ja samassa siirtotiedostossa kerralla

**Esimerkki 1**

Yrityksellä on käytössä dimensio nimeltä "seurantakohde". Dimensio löytyy Finazillasta valikosta "dimension". Kyseisen dimension code on 2.

[![](

Dimension "seurantakohde" alla yrityksellä on useita dimension arvoja, joista yksi arvo on nimeltään "Business Finland". Kyseisen dimension arvon code on 95.

[![](

Alla on esimerkki siitä, minkälainen sisäänlukutiedosto tästä voidaan muodostaa. Siirtoaineiston 2 ensimmäistä riviä kohdistuvat dimension arvolle "business finland" ja kaksi seuraavaa eivät kohdistu millekään dimension arvolle.

[![](

**Esimerkki 2** 

Esimerkki sisäänajodatan muodostamisesta exceliin, kun dimension nimi ja code ovat samat. Alla olevan kuvan esimerkissä 4 ensimmäistä kirjausta kohdistuvat dimensioille.

Ensimmäinen rivi kohdistuu dimensiolle, minkä code ja nimi on "asiakasryhmä" ja varsinainen dimensiovalue, mihin 5 000€ myynti kohdistuu on codeltaan "kuukausisopimukset". Tässä esimerkissä siis dimension nimi ja code ovat samat.

[![](

## 

## **Siirtotiedoston otsikot sarakkeittain vaaditussa muodossa**

Sarake A = Tilinumero

Sarake B = Vuosi

Sarake C = Kuukausi

Sarake D = Summa

Sarake E = DimensionCode

Sarake F = DimensionValueCode

[![](

 *Huom: sarakkeeseen E tulee syöttää dimension code (ei nimi) ja sarakkeeseen F dimensiovaluen code (ei nimi). Joissakin tapauksissa nimi ja code voivat toki olla samat.* 

[![](

# **Tiedoston tallentaminen csv -muotoon**

Luotu siirtotiedosto tulee tallentaa csv -muotoon ennen kuin sitä lähdetään tuomaan budjetille. Huomaa, että siirtotiedoston tulee olla oheisessa csv -muodossa.

[![](

# **Siirtotiedoston tuominen budjetille**

Luodun siirtotiedoston tuominen tapahtuu painamalla kuvan painiketta ja hakemalla tallennettu CSV –tiedosto.

[![](

Tämän jälkeen aukeaa hakuikkuna, jolla haetaan oikea tiedosto "Choose file" -painikkeella ja haetaan tiedosto kansiosta, mihin se on tallennettuna. Jos tiedoston muodossa on vikaa, Finazilla antaa herjan, jossa on osoitettu vialliset rivit.

[![](

Mikäli tiedosto päätyy yllä olevan esimerkin kaltaiseen virhetilanteeseen, tulee tiedostoa korjata virheiden / puutteiden osalta ja sisäänajoa voidaan kokeilla sen jälkeen uudellen.

Kun tiedonsiirto onnistuu, tulee alla oleva ilmoitus:

[![](

Painamalla yläosan painiketta "Create budget balances", tapahtumat siirtyvät Finazillan budjetti -näkymään.

Tapahtumia voi päivittää myöhemminkin, tuomalla saman ohjeen mukaan uudelleen dataa sisään. Siirtotiedostolla tulee aina tuoda koko haluttu data uudelleen. Tuontia ei voi siis tehdä osissa, koska uusi tiedosto ylikirjoittaa aina vanhat tiedot budjetilta. Tiedostosiirrolla tuotua dataa voi käsitellä budjetilla muutoin kuten normaalistikin sinne syötettyä dataa. Tietoja voi siis mm. korjata ja poistaa normaalisti.

[![](

*Huomaa myös, että tiedostolla tuomisen rajoitteena dimensioiden suhteen on se, että ns. matriisidimensioita ei voida tuoda eli samaa lukua ei voi kohdistaa seurantatason 1 kohteelle 1 ja seurantatason 2 kohteelle 3 (Esim Tuotanto Suomi)*

[![](

*Budjetin voi viedä ensin Finazillasta ulos Exceliin ja käyttää tätä oikeanlaisen siirtotiedoston laatimiseen, jolla tiedot voidaan tuoda sitten sisään. Ulosviety aineisto ei välttämättä sellaisenaan ole sisäänlukukelpoinen, mutta säästää aikaa.*



artikkelin osoite on https://intercom.help/finazilla/fi/articles/4373303-lukujen-tuonti-csv-tiedostolla-finazillan-budjetille-pohjatiedoksi

