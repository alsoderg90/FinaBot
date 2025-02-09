## Operatiivisen datan tiedoston laatiminen

Tämä artikkeli on suunnattu hieman edistyneemmille Finazilla -käyttäjille, sillä artikkelin ymmärtämisen edellytys on ymmärrys henkilöstökulujen budjetoimisesta sekä operatiivisen datan budjetoinnista.

Tässä artikkelissa kerromme vaihtoehtoisen tavan budjetoida henkilöstökuluja. Artikkelin kuvaama toimintatapa hyödyntää taustalla nk. operatiivista dataa. Artikkelin ymmärtämistä helpottaa, jos käyttäjä tietää mitä operatiivinen data on ja kuinka sitä tuodaan sisään Finazillaan. Lisäksi ymmärtämistä helpottaa, jos käyttäjä osaa budjetoida operatiivista dataa sekä ymmärtää Finazillan "perinteisen" henkilöstöbudjetin logiikan.

# Operatiivisen datan tiedoston laatiminen

Artikkelimme ["operatiivisen datan tuominen Finazillaan vakiomuotoisella csv -siirtotiedostolla"]( kuvaa laadittavaa siirtotiedostoa ja sen muotoa. Käytännössä ensimmäiseksi tuotavista palkkatiedoista tulee laatia artikkelimme ohjetta mukaillen siirtotiedosto.

Siirtotiedostossa tulee olla päivämäärä. Jos palkkoja budjetoidaan esimerkiksi vuodelle 2023, on päivämäärä 1.1.2023. Työntekijän palkkasumma syötetään amount -kenttään ja quatity -kenttään voidaan syöttää työntekijän lomapäivien määrä. Palkkasumma tuodaan vain kerran, ei siis jokaiselle kuukaudelle. Sarakkeeseen D laitetaan työntekijän nimi.

[![](

*Työntekijästä tulee dimension arvo Finazillaan ja riville 1 sarakkeeseen kirjoitettu nimi tulee dimension nimeksi.*

Mikäli jo tässä kohdin on tiedossa, että työntekijän palkka korottuu jossain kohdin, voidaan palkankorotus merkitä jo valmiiksi tiedostoon. Alla olevassa esimerkissä Jane Doen palkka on 1.1.2023 3500€ ja hän saa palkankorotuksen 500€ 1.6.2023.

[![](

# Operatiivisen datan tuominen Finazillaan

Kun tiedosto on luotu ja tallennettu, tuodaan tiedosto sisään käyttämällä Finazillan drop in -toimintoa.

Tiedoston sisäänluvun jälkeen käydään yrityksen dimensioissa ja käydäään merkitsemässä syntynyt työntekijä -dimensio budjetoinnissa aktiiviseksi, sillä operatiiviset dimensiot tulevat Finazillaan aina oletusarvoisesti budjetoinnista piilotettuna. Lisäksi dimension arvoille merkitään koodi (code). Ohje tähän löytyy [täältä.](

[![](

# Osabudjetille tehtävät muutokset

Palkkakuluja voidaan lähteä budjetoimaan Finazillan luomalla valmiilla osabudjetilla, joka on tuotu asiakkaille asiakkuuden perustamisvaiheessa. Henkilöstöbudjettipohjaa olemme kuvanneet mm. artikkelissamme [täällä.](

Henkilöstöbudjettia kannattaa lähteä muokkaamaan siten, että osabudjetissa on vain yksi hierarkinen rakenne. Hierarkinen rakenne tarkoittaa, että pohjaan ei luoda ensin omia rakenteitaan jokaiselle työntekijälle, vaan pohjaa työstetään vain yhdellä rakenteella.

## 1 Määritellään työntekijä 1 riville kohdistus

Ensimmäisenä osabudjetin työntekijä 1 rakenteelle täytyy käydä tekemässä dimensio -kohdistus; eli määritellä, kenen työntekijän tiedot ensimmäisessä rakenteessa on.

Määrittely tehdään rivin asetuksista asettamalla riville operatiivinen dimensio. Samalla rivin nimen voi muuttaa kyseisen työntekijän nimeksi. Koska työntekijä tieto on operatiivinen dimensio, valitetaan se operative values kentästä.

[![](

[![](

*Koska dimensio -kiinnitys tehdään hierarkisen rakenteen ylimmälle tasolle, valuu kohdistus kaikille lapsiriveille*

## 2 Luodaan uusi rivi tuotavalle palkkatiedolle

Seuraavaksi käydään lisäämässä osabudjetille 1 uusi rivi haluttuun kohtaan osabudjettia. Rivin nimi voi olla vaikka kuukausipalkka tuotuna. Kyseistä tietoa ei haluta kuitenkaan syöttää käsin, vaan palkkasumma halutaan tuoda automaattisesti operatiivisesta datasta. Tästä syystä riville tehdään hieman lisämäärittelyitä.

Riville täytyy käydä määrittelemässä seuraavat asiat:

* Mistä aineistosta tiedot tuodaan, eli mikä on aineiston Data group. Data group syntyy silloin, kun tiedosto ajetaan sisään Finazillaan ja on tyypillisesti tiedoston nimi
* Tuodaanko riville quantity vai amount määre. Jos halutaan tuoda eurot, tuodaan amount
* Huomaa, että dimensio -kohdistus tulee automaattisesti, sillä lapsirivi perii sen automaattisesti

Lisätietoja osabudjetin rivimäärittelyistä löytyy mm. [täältä](

[![](

. `Yllä olevat määrittelyt kertovat, että osabudjetin riville kuukausipalkka tuodaan vain Jane Doen palkka. Amount valinta kertoo, että riville tuodaan nimeomaan palkkasumma (eur)`

## 3 Lomapäivien muokkaaminen

Seuraavaksi käydään muokkaamassa lomapäivä -riviä, sillä lomapäiviä ei haluta enää syöttää käsin, vaan lomapäivätkin halutaan tuoda operatiivisesta datasta automaattisesti. Muokkaaminen tehdään rivityökaluissa.

[![](

Riville tehdään vastaavalla logiikalla määrittelyt kuin edellä. Tässä tapauksessa lomapäivien määrä on quantity, eikä amount määre, joten row data type on quantity.

[![](

Huomaa, että mikäli toit csv -tiedostossa lomapäivät yhteissummana ensimerkiksi tammikuulle, tulee nämä käsin korjata osabudjetille sen mukaan, miten työntekijä lomailee. Etuna tässä on kuitenkin se, että mikäli lomapäivät tuodaan pohjatiedoksi, ei myöhemmin tarvitse hakea lomapäivätietoa.

## 4 Muokataan kuukausipalkka -riviä

Seuraavaksi käydään muokkaamassa osabudjetin kuukausipalkka riviä. Rivi on oletuksena syöttörivi, mutta rivistä halutaan tässä tapauksessa tehdä kaavarivi. Kaavassa halutaan luonnollisesti päästä tilanteeseen, jolloin jokaisella kuukaudella on työntekijän palkkasumma ja palkankorotus huomioidaan siitä hetkestä eteenpäin, kun se astuu voimaan.

Ensimmäiseksi rivi kuukausipalkka muutetaan kaavariviksi ja sen jälkeen mennään kirjoittamaan riville kaavaa. Ensimmäiseksi kaavaan otetaan rivi "kuukausipalkka tuotuna". Seuraavaksi valitaan "column ref" kentästä miinus 1, syötetään + ja valitaan rivi "kuukausipalkka".

[![](

Tämän jälkeen Finazilla laskee riville työntekijän palkan kullekin kuukaudelle, sekä huomioi mahdolliset palkankorotukset

# Lukujen tuonti osabudjetille

Kun yllä kuvatut muutokset on tehty osabudjetille, voidaan seuraavaksi osabudjetille tuoda tiedot operatiivisesta datasta.

Import tehdään budjetin yläpalkin import -painikkeen kautta. Importissa määritellään, että tuotava data on operatiivista. From ja To -kohdissa voidaan määritellä, mistä aikavälistä luvut tuodaan ja minne ne tuodaan budjetilla.

[![](

Preview -painikkeen kautta tuotavaa dataa voidaan esikatsella ja import suorittaa tuonnin.

Tuonti tuodaan kerralla kaikille riveille, mihin on jotakin tuotavissa importissa annetuilla määrittelyillä. Tässä esimerkissä kerralla tuodaan siis työntekijän Jane Doe palkka, palkankorotus sekä lomapäivien määrä.

[![](

[![](

*Kaikki osabudjetin rivit, joissa on rivin nimen edessä tähtisymboli (\*), kaipaavat tiliohjauksen taakseen. Tiliohjaus ohjaa kyseisen rivin saldot pääbudjetille kyseiselle tilille tulokseen tai taseeseen.*

# Seuraavan työntekijän tekeminen osabudjetille

Kun osabudjetille on saatu ensimmäinen työntekijä lisättyä siten, että työntekijän palkkasumma, lomapäivät ja mahdolliset palkankorotukset tulevat operatiivisesta datasta ja osabudjetti laskee palkat ja palkkojen sivukulut oikein ja ohjaa ne pääbudjetille, voidaan osabudjetille lähteä lisäämään seuraavaa työntekijää.

Seuraavien työntekijöiden lisääminen tehdään eri tavalla - hyödyntämällä nk. duplicate toimintoa. Toiminto tekee seuraavien työntekijöiden lisäämisestä äärimmäisen helppoa ja nopeaa. Duplikointia olemme kuvanneet artikkelissamme [täällä.]( 

Uuden työntekijän lisääminen tehdään menemällä ensimmäisen työntekijän (Jane Doe) hierarkisen rakenteen otsikko -riville ja valitaan vaihtoehto "create duplicates".

[![](

Seuraavaksi valitaan kentästä "generate new row for dimension values" kaikki halutut dimensiot, eli työntekijät, jotka halutaan luoda. Tässä esimerkissä ensimmäinen työntekijä joka luotiin, oli Jane Doe, joten Jane Doe:ta ei valita enää uudellen. Tässä tapauksessa valittavana on siis vain John Doe.

[![](

Mikäli työntekijöitä olisi listassa enemmän, voitaisiin ne kaikki valita kerralla. Useat työntekijät näkyisivät kaikki samassa kentässä kuin alla olevassa esimerkissä John Doe.

Duplicate row -painike tekee duplikaatin osabudjetille.

[![](

Osabudjetille syntyy oma rakenteensa John Doelle ja rivit saavat automaattisesti kaikki oikeat kiinnitykset.

[![](

Seuraavaksi John Doelle voidaan tuoda palkkatiedot operatiivisesta datasta.

[![](

*Huomaa, että toteumat voidaan tuoda myös yhdellä ainoalla tuonnilla kerralla eli toteumaa ei tarvitse tuoda työntekijä kerrallaan. Osabudjetin rivimääritykset pitävät huolen siitä, että jokainen työntekijä saa oikeat tiedot taakseen.* 

*Toimintoa voidaan käyttää monella muullakin tavalla hyödyksi. On mahdollista esimerkiksi asettaa ylätasolle jokin kirjanpidon dimensio ja rakentaa sen alle hierarkisesti työntekijät ja käyttää kullakin työntekijällä yllä kuvattua metodia. Kirjanpidon dimensioita voi siis käyttää yhdessä operatiivisten dimensioiden kanssa*

# Palkkojen päivittäminen

Mikäli työntekijöiden palkkasummat muuttuvat, tulee uusia työntekijöitä tai tulee palkankorotuksia, voidaan tiedot päivittää tuomalla csv -tiedosto uudelleen sisään Finazillaan. Tiedot päivittyvät automaattisesti budjetille. Uudet työntekijät tulee duplikoida ohjeen mukaisesti, jolloin heidän muuttuneet palkkatietonsa tulevat jatkossa automaattisesti.



artikkelin osoite on https://intercom.help/finazilla/fi/articles/5928551-henkilostobudjetin-tekeminen-operatiivisena-datana

