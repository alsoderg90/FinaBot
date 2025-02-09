## Tagin käyttäminen budjetilla

Käsittelimme artikkelisamme "[Kaavarivit budjetoinnissa](" kaavarivien luomista, joka on tarpeellinen tieto tämän artikkelin ymmärtämistä varten. Laskentavakioiden ja tagien käytössä budjetilla on yhtäläisyyksiä, joten suosittelemme lukemaan myös artikkelimme "[Yrityskohtaisten laskentavakioiden luominen ja päivittäminen sekä niiden käyttäminen kaavassa](" sekä "[Budjettikohtaisten laskentavakioiden luominen ja päivittäminen](" ensin.

# **Tagin käyttäminen budjetilla**

Tag –toiminto mahdollistaa useamman merkityn budjettirivin summaamisen yhdellä valinnalla. Tagi auttaa kaavan luonnissa, jos halutaan tuoda kaavaan useita rivejä budjetilta. Erikseen valitsemisen sijaan voidaan tageja käyttämällä tuoda rivien summa yhdellä kertaa kaavaan.

## ***Esimerkki laskentavakion sekä tagin käyttämisestä kaavoissa***

Seuraavassa esimerkissä käydään läpi sekä tagien että laskentavakioiden käyttöä kaavoissa. Esimerkkiin liittyy seuraavat taustatiedot:

* Yrityksen myyntibudjetteja laatii useampi myyjä oman liiketoimintayksikkönsä osalta
* Myyjille on tehty valmiiksi osabudjetit, joihin he budjetoivat tilikauden arvion myynnistä. Arvio myynnistä perustuu myyjien arvioon solmituista sopimuksista
* Näiden osabudjettien luvut halutaan koota yhteen koko ko. liiketoiminta-alueen (Palvelut) myyntibudjettiin, siten että luvut myyntibudjetissa päivittyvät automaattisesti. Liiketoiminta-alueen myyntibudjetista luvut siirtyvät pääbudjetille liikevaihtoon

Finazillaan on laskentaa varten perustettu osabudjetit jokaiselle liiketoimintayksikölle sekä liiketoiminta-alueelle, johon yksiköt kuuluvat. Lisäksi on luotu laskentavakiot jokaisen liiketoimintayksikön sopimushinnoille.

Osabudjeteilla myyjät syöttävät arvionsa kuukausittain saatavista sopimuksista vihreälle syöttöriville. Osabudjetti laskee markkinointipalvelun (liiketoimintayksikkö) liikevaihdon viimeiselle riville kaavalla laskentavakio sopimuksen hinta kerrottuna sopimusten määrällä. Jokainen osabudjetti toimii vastaavalla tavalla.

[![](

Nyt näiltä osabudjeteilta halutaan koota liikevaihtorivit liiketoiminta-alueen osabudjettiin. Ensin pitää luoda uusi tagi.

# **Tagin luominen**

Valitaan rivin työkalupainikkeista kolmen pisteen takaa vaihtoehto "settings" (asetukset) ja tämän jälkeen mennään Tags –kentän oikeasta laidasta Tags -painikkeella ja luodaan uusi tagi toiminnolla "New Tag". Avautuvaan lomakkeeseen kirjoitetaan nimi ja symboli. Tagin taustaväriä ja fontin väriä voi muuttaa, jotta tagit erottaa helpommin toisistaan.

[![](

# **Tagin kiinnittäminen**

Nyt luotu tagi voidaan liittää liiketoimintayksikön markkinointi liikevaihtoriviin:

[![](

Liitetään tagi vastaavasti myös kilpailutuspalveluiden ja talouspalveluiden osabudjetteihin. Nyt koko liiketoiminta-alueen osabudjetille voidaan muodostaa liikevaihtoriville kaava tagista.

Tämä tehdään avaamalla rivin asetukset ja mennään formula valikkoon kaavaeditoriin. Kaavaeditorista löytyy kohta "Tags", johon valitaan luotu tagi ja hyväksytään valinta. Nyt rivi kerää summaksi kaikki tagilla merkityt rivit kaikista budjeteista.

[![](

# Tiliohjaus

Tehdään lopuksi vielä tiliohjaus Palvelut liiketoiminta-alueen osabudjetista pääbudjetille.

[![](

Nyt osabudjettien ja pääbudjetin liikevaihtorivit näyttävät seuraavilta:

[![](

# **Laskentavakion päivittäminen uuden hinnaston mukaiseksi**

Nyt markkinointipalvelussa otetaan käyttöön uusi hinnasto maaliskuun alusta ja sopimushinta nousee 1200 eurosta 1300 euroon. Käydään päivittämässä laskentavakio:

[![](

Tämän jälkeen palataan markkinointipalveluiden osabudjetille ja päivitetään laskentakaava Sopimushinta –rivin takaa, kuten alla kuvattu.

Sopimushinta muuttuu 1300 euroon maaliskuusta lähtien:

[![](

Nyt osabudjetissa myös summat liikevaihtoriville päivittyvät kaavan kautta. Samalla tavoin käydään päivittämässä koko liiketoiminta-alueen Palvelut osabudjetti; tällöin luvut päivittyvät myös sinne ja tätä kautta pääbudjetille, sillä ko. rivillä on tiliohjaus pääbudjetille.

[![](

*Tagin käytössä on syytä huomata, että tagi hakee kaikista budjeteista tagattuja rivejä. Tästä syystä tagien käytössä suositellaan käytettävän huolellisuutta eli on tärkeää tietää, mitkä kaikki rivit on tagattu ko. tagilla, kun tagia käytetään kaavassa.* 



artikkelin osoite on https://intercom.help/finazilla/fi/articles/4430333-tagien-kayttaminen-budjetilla-mahdollistaa-budjettirivien-summaamisen

