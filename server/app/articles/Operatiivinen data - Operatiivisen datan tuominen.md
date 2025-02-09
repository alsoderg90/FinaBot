## Operatiivisen datan tuominen

Olemme kuvanneet aikaisemmassa artikkelissamme ["Operatiivisen datan tuominen Finazillaan vakiomuotoisella csv -siirtotiedostolla"]( missä muodossa operatiivista dataa tuodaan sisään Finazillaan.

Tässä esimerkkiartikkelissa näytämme vaihe vaiheelta esimerkin omaisesti miten Finazillaan tuodaan operatiivinen data ja miten tuotua dataa raportoidaan sekä valmiilla raporttimallilla, että luomalla oma uusi raporttimalli. Artikkeli on suunnattu käyttäjille, joilla on jonkinlainen ymmärys raporttimallien luomisesta, raportoinnista sekä operatiivisen datan hyödyntämisestä yleisellä tasolla.

# Operatiivisen datan tuominen

Tuodaan oheinen data sisään. Tiedosto on tallennettu csv -muotoon nimellä "tuotemyynnin tehtaittain".

[![](

Mennään Company - Settings valikkoon ja tuodaan siirtotiedosto sisään tipauttamalla se "integration file drop-in kohtaan. Valinnaksi laitetaan "operative data" datatyyppi -kohtaan. Data Group identifier kenttään tulee oletuksena tiedoston nimi. Nimen voi tarvittaessa vaihtaa kirjoittamalla uusi nimi. Save -painike ajaa datan sisään.

[![](

Onnistunut sisäänajo näyttäytyy oheisesti

[![](

# Mitä Finazillassa tapahtuu aineiston sisäänluvun jälkeen

Onnistuneen ajon jälkeen Company - Dimensions valikosta löytyy Datagroup nimeltä "tuotemyynti" (tai jos tiedostolle annettiin sisäänajossa jokin muu nimi, on Datagroup annettu nimi).

Jos sama aineisto ajetaan myöhemmin uudelleen Finazillaan sisään samalla tiedostonimellä, ei Finazillaan synny enää uutta Datagrouppia. Jos sama aineisto vastaavasti taas ajettaisiin sisään uudelleen eri nimellä, syntyisi dimension "datagroup" alle uusi datagroup, jonka nimi olisi tiedoston nimi.

[![](

*On tärkeää hahmottaa Datagroupin merkitys. Jos samaa dataa halutaan ajaa aina uudelleen Finazillaan ja raportoida uuden datan valossa, on datagroupin merkitys suuri.*

Onnistunut ajo luo Finazillaan aineistossa olleet operatiiviset dimensiot. Dimension "tehdas" alta löytyy dimensiovaluet tehdas 1, tehdas 2 ja tehdas 3. Dimension "kategoria" alta löytyvät dimensiovaluet "kiinnitystarvikkeet" sekä "koneen osat". Dimension "tuote" altaa löytyy dimensiovaluet akseli, mäntä, holkki. Lisäksi dimension "Myyjä" alta löytyvät dimensiovaluet Matti Myyjä, Maija Myyyjä, Jane Doe ja John Doe.

Jos sama aineisto ajetaan myöhemmin uudelleen Finazillaan sisään samoilla dimensiolla, ei Finazillaan synny enää uusia dimensioita. Jos sama aineisto vastaavasti taas ajettaisiin sisään uudelleen siten, että dimensiossa tehdas olisi vaikkapa uusi tehdas nimeltä "tehdas 4", syntyisi dimension "tehdas" alle uusi dimensiovalue, jonka nimi olisi tehdas 4.

[![](

# Operatiivisen datan raportointi valmiilla raporttimallilla

Raportointi tehdään Reports -valikossa luomalla uusi raportti "new report" painikkeesta. Operatiivisen datan raportointiin on olemassa yksi valmis raporttimalli nimeltä "operative data (system). Raportoidaan ko. mallilla. Ohessa esimerkki raporttivalinnoista.

[![](

Kyseiset valinnat tuottavat oheisen raportin. Koska raportin valinnoissa raportti muodostettiin dimensions total -valinnalla, summaa raportti kaikki dimensiot yhteen.

[![](

Jos sama raportti otetaan valinnalla dimensions /column, päästään pivotoinnin kautta kiinni samaan dataan dimensiotasolla. Pivotoinnissa voidaan valita, mitä dimensioita filtteröidään mihinkin paikkaan raportilla.

[![](

# Operatiivisen datan raportointi luomalla oma raporttimalli

Samaa dataa voidaan raportoida myös luomalla oma raporttimalli, joka vastaa paremmin omiin raportoinnin tarpeisiin. Näin saadaan myös raportin otsikot paremmin kuvaaviksi. Operatiivisen raporttimallin luomista olemme kuvanneet artikkelissamme [täällä.](

Seuraavaksi mennään luomaan oma raporttimalli Company- valikossa kohdassa "Report Scheme". Uusi raporttimalli luodaan painikkeesta "New Report Scheme". Raporttimallille annetaan nimi sekä tehdään muut määrittelyt. Create Report Scheme -painike luo raporttimallin.

[![](

Seuraavaksi aletaan luomaan raporttimallin raporttipuuta. Tämä tapahtuu klikkaamalla luodun raporttimallin nimeä raporttimallilistassa. Raporttimallin rakentaminen toimii samalla logiikalla kuin "tavallisen" kirjanpidon datan raporttimallin luominenkin toimii.

Lisätään raporttimallille uusi rivi, joka on tyypiltään "operative data (new)", jolloin riville tulee kiinnittää se Data Group, jolla ko. tieto on tuotu sisään. Määreeksi valitaan "Quantity", koska riville halutaan nousevan se data, mikä oli sisäänajotiedostossa "quantity" sarakkeessa.

[![](

Seuraavaksi luodaan toinen rivi, joka luodaan edellisen rivin kohdalla olevasta "new row" -painikkeesta. Näin rivi saadaan "samaan tasoon" aikaisemman kappalemäärä rivin kanssa. Luotavalle riville halutaan nousevan operatiivisen datan eurot, joten rivin määreeksi valitaan "Amount". Valinnat tehdään muutoin samoin kuin edellisessä rivissäkin tehtiin.

[![](

Raporttimallin raporttipuu on nyt oheinen.

[![](

Kun luodulla raporttimallilla raportoidaan, näyttää raportti oheiselta valinnalla dimensions total.

[![](

Raporttivalinta dimensions / column mahdollistaa datan pivotoimisen jälleen dimensiotasolle halutulla tavalla, kuten edellisessäkin esimerkissä.



artikkelin osoite on https://intercom.help/finazilla/fi/articles/4871985-esimerkki-operatiivisen-datan-tuominen-finazillaan-ja-datan-raportointi

