## Toiminnon mahdollisuudet

[![](

*Versiopäivityksessä 26.2.2024 tuotu kokonaan uusi toiminto. Toiminto mahdollistaa lukujen importtaamisen osabudjetilta toiselle. Ominaisuus toimii saman yrityksen sisällä, tai saman asiakkuuden eri yritysten välillä*

Tuotu ominaisuus on osa laajempaa kokonaisuutta. Tässä artikkelissa esitelty ominaisuus on osa 5, joka keskittyy nimenomaan usean toisen yrityksen osabudjetin lukujen tuomisesta toiselle yritykselle. Tuotavia osia on yhteensä 5. Toimintoon liittyy myös seuraavat ominaisuudet:

[Budjetin import, osa 1: toiselta yritykseltä lukujen tuominen](

[Budjetin import, osa 2: usealta tietolähteeltä lukujen tuominen](

[Budjetin import, osa 3: lukujen siirtäminen dimensionarvolta toiselle](

[Budjetin import, osa 4: usealta dimensiolta tuominen](

Tämä artikkeli koskettaa kaikkia asiakkaita, jotka käyttävät omassa budjetoinnissaan osabudjetteja tavalla tai toisella.

# Toiminnon mahdollisuudet

Toiminnolla voidaan importata halutun osabudjetin tietyn rivin luvut jollekin toiselle osabudjetin riville. Toimintoa voidaan käyttää saman budjetin eri osabudjettien välillä tai eri budjettien takana olevien osabudjettien välillä. Toiminto on käytettävissä myös saman asiakkuuden eri yritysten välillä.

Toiminto on erityisen kätevä esimerkiksi tilanteissa, missä konserniyhtiössä emo on budjetoinut osabudjettiin konsernimyynnit ja nämä halutaan tuoda tytäryrityksen osabudjetille, mihin kaivataan konserniostoja.

[![](

*Toiselta osabudjetilta haettuja lukuja ei voi muokata saman rivin sisällä. Lukua voi käyttää kaavan komponenttina ja sitä kautta hyödyntää laskennassa monin tavoin.*

*Osabudjetilta luvut tulevat aina yhteensä summana suhteessa dimensioihin. Toiminto ei mahdollista tietyn dimensionarvon lukujen hakemista, vaan haettaessa saadaan aina yhteissumma.* 

# Tehtävät määrittelyt osabudjetilla

Silloin kun osabudjetille halutaan kutsua jonkun toisen osabudjetin riviä, tulee rivityypiksi valita vaihtoehto "import sub budget row". Rivityyppi kertoo sen, että kyseiselle riville halutaan nimenomaan hakea luvut toisesta osabudjetista.

Kohdassa "select remote sub budget" määritellään, että mistä osabudjetista luvut halutaan hakea. Valikosta aukeaa lista, josta löytyy kaikki valitun yrityksen osabudjetit ja haluttu osabudjetti kiinnitetään kenttään.

Kun osabudjetti on valittu, tulee käyttäjälle vielä valittavaksi, että mikä osabudjetin rivi halutaan valita.

[![](

Tuonnin jälkeen kyseinen rivi näyttäytyy osabudjetilla oranssilla värityksellä. Sen lisäksi rivillä näkyy "jakosymboli", joka kuvaa sitä, että luku on tuotu toisaalta.

[![](

Jakosymbolista aukeaa erillinen popup -ikkuna, joka kertoo käyttäjälle, että mistä luvut on tuotu.

[![](

# Havainnollistavat esimerkit

Havainnollistamme toimintoa vielä muutamin erilaisin esimerkein.

## Esimerkki 1: yksittäisen yrityksen yhden budjetin sisällä

Yritys Magnusti Ltd. on tehnyt myyntien ja ostojen budjetoinnin osabudjettien avulla. Yritys haluaa hyödyntää osabudjettien myynti- ja ostolaskudataa laskeakseen maksettavan arvonlisäveron.

Magnusti Ltd. luo erillisen osabudjetin alv- velkaa varten. Osabudjettiin tehdään yksi rivi, johon "importataan" myynnit myyntien osabudjetilta ja toinen rivi, johon "importataan" ostojen määrä ostojen osabudjetilta. Kaavan kautta voidaan laskea maksettava vero. Vero voidaaan ohjata tilikiinnityksin menemään pääbudjetille haluttuun paikkaan.

## Esimerkki 2: yksittäisen yrityksen eri budjettien välillä

Yritys Magnusti Ltd. on tehnyt budjetin vuodelle 2024. Myynnit on budjetoitu erillisen osabudjetin avulla (osabudjetin nimi on myyntibudjetti 2024).

Magnusti Ltd. haluaa tehdä vuodelle 2024 toisen skenaariobudjetin. Tätä varten yritys on luonut uuden budjetin, jonka taakse tehdään myyntien osabudjetista uusi versio. Pohjana halutaan kuitenkin käyttää aikaisemman osabudjetin lukuja. Skenaariobudjetin taakse on luotu osabudjetti, johon halutaan hakea alkuperäisen osabudjetin myynnit.

Osabudjetin rivi, mihin myynnit halutaan hakea, muutetaan "import sub budget row" tyyppiseksi. Seuraavaksi kiinnitetään "select sub budget" kenttään alkuperäinen myyntien osabudjetti. Listaus esittää osabudjetit siten, että lihavoitu nimi tarkoittaa varsinaisen budjetin nimeä ja sen alla olevat ovat kyseisen budjetin osabudjetteja.

[![](

Osabudjetin valinnan jälkeen käyttäjälle aukeaa vielä yksi lisävalinta, nimeltä "sub budget row to import". Kentässä kerrotaan, minkä osabudjetin rivin saldo halutaan tuoda. Valikosta aukeaa kaikki osabudjetin rivit valittavaksi.

[![](

Saldot tulevat osabudjetille oranssilla värityksellä. Tämän lisäksi rivillä esitetään ennen tiliohjaus tietoa symboli, joka kertoo, että tieto on ns. jaettu.

[![](

Symbolia klikkaamalla käyttäjä saa lisätiedon siitä, mistä luvut on haettu osabudjetille. Info ikkunassa kerrotaan budjetin nimi, osabudjetin nimi ja rivin nimi.

[![](

## Esimerkki 3: yritykseltä toiselle

Toiminto mahdollistaa toisen yrityksen osabudjettilukujen tuomisen toiseen osabudjettiin, silloin kun varsinainen budjetointikin on tehty lähtöyrityksen päässä nimenomaan osabudjetille. Toiminto on erityisen kätevä tilanteissa, missä yritykselle A on budjetoitu sisäistä myyntiä osabudjetille 1 ja tämä luku halutaan saada yritykselle B sisäisiin ostoihin osabudjetille 2.

Asiakkuuden yritys Magnusti Ltd on budjetoinut myynnit erillisellä osabudjetilla "myyntibudjetti 2024". Myyntibudjetissa on oma rivinsä, jolla on budjetoitu sisäinen konsernimyynti.

Asiakkuuden toinen yritys, Wombat Oy, on budjetoinut ostot erillisellä osabudjetilla "ostot 2024". Ostobudjetissa on oma rivinsä, jolla on budjetoitu sisäiset ostot konsernin muilta yrityksiltä. Kyseiselle riville haluttaisiin Magnusti Ltd:n budjetoima konsernimyynti, sillä Magnustin myynti on Wombatin ostoa.

Wombat Oy:n osabudjetille "ostot 2024" voidaan hakea Magnustin myynti käyttämällä tässä artikkelissa kuvattua toimintoa. Rivityypiksi valitaan edelleen vaihtoehto "import sub budget row" ja sen jälkeen valitaan yritys, jonka osabudjeteista saldot halutaan tuoda. Alasvetovalikosta löytyy kaikki asiakkuuden yritykset. Kun yritys on valittu, aukeaa "select sub budget" listauksesta valitun yrityksen budjetit.

[![](

## Esimerkki 4: lukujen päivittäminen yritykseltä toiselle

Edellä kuvatussa esimerkissä tulee eteen tilanne, että Magnusti Ltd käy päivittämässä omaa konsernimyyntiensä osabudjettia ja budjetoi, että jatkossa konsernimyynnit ovatkin 1200€/kk aiemman 1000€/kk sijasta.

Tieto päivittyy automaattisesti myös Wombat Co:n konserniostojen osabudjetille.

## Esimerkki 5: lisäkohdistuksen käyttäminen

Magnusti Ltd on budjetoinut myyntiä käyttämällä lisäkohdistusta (additional dimension target) dimensionarvolle "hallinto". Hallinnolle on budjetoitu 2500€/kk.

Wombat Co. kutsuu kyseistä riviä. Riville tulee 2500€/kk, jonka Wombat Co. voi kohdistaa haluamallaan tavalla halutulle dimensionarvolle. Dimensiokohdistukset eivät koskaan tule yritykseltä toiselle, sillä dimensiot ovat yrityskohtaisia.

## Esimerkki 6: dimensio -kohdistukset

Magnusti Ltd on budjetoinut myyntiä käyttämällä "perinteistä" oikean yläkulman dimensiovalitsinta. Yhtä samaa osabudjetin riviä on kohdistettu useille dimensioille seuraavasti:

* Kohdistamaton eli nk. blank 500€/kk
* Hallinto 2000€/kk
* Kerta-asiakkaat 500€/kk
* Hallinto + Kuukausisopimukset 1500€/kk
* Yhteensä budjetoitu 4500€/kk

Wombat Co. kutsuu kyseistä riviä. Riville tulee 4500€/kk, jonka Wombat Co. voi jälleen kohdistaa haluamallaan tavalla halutulle dimensionarvolle.



artikkelin osoite on https://intercom.help/finazilla/fi/articles/8826350-budjetin-import-osa-5-osabudjetilta-toiselle-lukujen-tuominen

