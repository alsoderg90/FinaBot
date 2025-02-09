## Osabudjettien sijainti

# Osabudjettien sijainti

Osabudjetit löytyvät budjetilta välilehdeltä "Sub Budgets". Budjetin takaa löytyvät osabudjetit liittyvät vain siihen kyseiseen budjettiin, minkä takaa ne löytyvät.

[![](

# Uuden osabudjetin luominen

Uuden osabudjetin luominen aloitetaan New Sub Budget –painikkeesta, jolloin aukeaa täyttöikkuna. Vaihtoehtona on luoda täysin uusi osabudjetti tai kopioida valmis pohja.

Mikäli luodaan kokonaan uusi osabudjetti, annetaan sille tässä kohdin nimi kenttään "Name" ja valinnalla "create new sub budget" osabudjetti ilmestyy listaan. Tämän jälkeen luotua osabudjettia pääsee rakentamaan klikkaamalla osabudjetin nimeä listassa.

# Olemassa olevan osabudjetin kopioiminen

Jos taas kopioidaan jokin toinen asiakkuuden alla oleva osabudjetti, valitaan syöttöikkunassa "Copy sub budjet" oikea yritys, minkä osabudjetti halutaan kopioida ja tämän jälkeen olevasta vetovalikosta oikea osabudjetti. Kun osabudjettia kopioidaan toisesta yrityksestä, ei listassa näy budjettien nimiä vaan "none" tyyppinen listaus. Budjetit ovat kuitenkin samassa järjestyksessä kuin alkuperäisellä yrityksellä ovat, joten sen perusteella pystyy valitsemaan mistä budjetilta kopion ottaa.

Seuraavaksi valitaan alemmasta kohdasta "Copy selections", mitä tietoja halutaan kopioida. Jos mitään vaihtoehtoja ei valita, kopioidaan pelkkä osabudjetin rakenne.

[![](

[![](

*Osabudjettien dimensiot eivät kopioidu yritykseltä toiselle, sillä dimensiot ovat aina yrityskohtaisia. Kopioitu osabudjetti tulee tasolle "blank" eli dimensioimaton/kohdistamaton.*

Alla olevassa taulukossa on kuvattu mitä dataa voidaan kopioida ja mitä valinnat tarkoittavat käytännössä.

[![](

Valintojen jälkeen kopioidulle osabudjetille annetaan nimi ja tämän jälkeen toiminto "create sub budget" kopioi osabudjetin listaan. Kopioitua osabudjettia päästään muokkaamaan osabudjetin nimeä klikkaamalla - samoin kuin alusta saakka luotua osabudjettiakin.

# Osabudjetin avaaminen

Osabudjetti avataan klikkaamalla osabudjetin nimeä. Näkymä on työkalupainikkeita lukuun ottamatta tyhjä, mikäli mitään valmista pohjaa ei ole valittu. Jos osabudjetti on kopioitu, on tässä luonnollisesti kaikki ne rivit, mikä olivat alkuperäisessäkin osabudjetissa.

# Osabudjetin rakentaminen ja muokkaaminen

Alla kerromme, miten osabudjettia muokataan. Samat toiminnot pätevät sekä täysin tyhjään osabudjettiin, että myöskin kopioidun osabudjetin muokkaamiseen.

Osabudjetille lisättäviä rivityyppejä on useita. Rivityypit on kuvattu alla.

## Osabudjetin rivityypit

**Input** = Syöttörivi. Riville syötetään manuaalisesti lukuja.

**Header** = Otsikkorivi. Rivillä itsessään ei esitetä dataa, vaan se toimii otsikkona.

**Formula** = Kaavarivi. Kaavoja voidaan muodostaa kaikista budjetin riveistä.

**Percentage** = Prosenttirivi. Rivillä voidaan esittää prosentuaalista dataa.

**Actual** = rivi, joka käyttäytyy tavallisella budjetilla input rivin kaltaisesti. Ennustebudjetilla rivi päivittyy automaattisesti toteumien mukaan.

*Actual rivityypissä on kaksi vaihtoehtoa; actual input ja actual formula*

**\* Actual input** on syöttörivi. Ennusteella rivi päivittyy toteumien mukaan

**\* Actual formula** on kaavarivi. Budjetilla luku lasketaan kaavan mukaan ja ennusteella riville haetaan toteumaa

**Operative** = Edellä kuvatulle versio operatiiviselle datalle. Rivi päivittyy osabudjetilla aina automaattisesti kun uutta operatiivista tietoa tuodaan sisään.

*Operative rivityypissä on myös kaksi vaihtoehtoa; operative input ja operative formula.* Lisäksi rivityypissä voidaan valita budjetoitava määre, joka on amount (eurot) tai quantity (jokin muu määre)

**\* Operative input** on syöttörivi. Ennusteella rivi päivittyy toteumien mukaan

**\* Operative formula** on kaavarivi. Budjetilla luku lasketaan kaavan mukaan ja ennusteella riville haetaan toteumaa

**Import budget row** = rivityyppi, jolla voidaan hakea joltain toiselta budjetilta haluttu luku. Toiminto mahdollistaa myös toisen yrityksen budjetilta luvun hakemisen.

**Import sub budget row** = rivityyppi, jolla voidaan hakea joltain toiselta osabudjetilta haluttu luku. Toiminto mahdollistaa myös toisen yrityksen osabudjetilta luvun hakemisen.

Uusia rivejä lisätään osabudjetille yläosan työkalupalkin plus -painikkeesta.

[![](

Kun ensimmäinen rivi on luotu, niin uusien rivien lisääminen muuttuu hieman.

Seuraava rivi lisätäänkin juuri luodun rivin perässä olevasta työkalupainikkeesta.

[![](

# 

# Osabudjetin rivien rakenne

Tässä vaiheessa tulee miettiä osabudjetin rakennetta, eli lisätäänkö rivi alisteiseksi juuri luodulle riville vai luodaanko uusi rivi samalle tasolle. Rivin lisääminen myös yläpuolelle onnistuu, jos välistä jää rivi luomatta. Osabudjetin rakenteella on merkitystä, mikäli laadittua osabudjettirakennetta halutaan kopioida osabudjettiin useampaan kertaan.

Vaihtoehto "Add Row Above" lisää seuraavan rivin edellisen rivin yläpuolelle kun taas "Add Row Below" lisää rivin ensin luodun rivin alapuolelle. Toiminto "Add Row As A Child" tekee rivistä "alisteisen" sille riville, miltä valinta tehtiin.

# Rivityypin vaihtaminen

Kun osabudjettiin on tehty rivit valmiiksi, voidaan laskennassa tarvittavat rivit muuttaa syöttöriveiksi, kaavariveiksi tai prosenttimuotoisiksi riveiksi - ellei tätä tehty jo rivejä luotaessa. Muuttaminen tapahtuu avaamalla rivin asetukset kolmen pisteen takaa ja valikon rattaankuvasta muuttamalla "Row Type" halutuksi. Rivin väri kertoo, onko kyse syöttörivistä (vihreä), kaavarivistä (sininen), prosenttimuotoisesta rivistä (vaaleanpunainen), otsikkorivi (musta) vai määrärivistä (vihreä).

# Tiliohjauksen tekeminen osabudjetin riville

Lopuksi tulee tehdä myös tiliohjaus niille riveille, mistä lukujen halutaan siirtyvän pääbudjetin jollekin tilille. Kun tehdään tiliohjaus jollekin tilille, tili muuttuu pääbudjettinäkymässä violetiksi ja sille ei voi enää syöttää lukuja pääbudjettinäkymässä. Tiliohjauksia samalle tilille voi olla kuitenkin useita. Mikäli pääbudjetilla on jo syötetty lukuja tilille tulee huomautus, että haluatko varmasti tehdä ohjauksen tällaiselle tilille.

Tiliohjaus tehdään rivin asetuksissa kohdassa "Transfer to account". Alasvetovalikosta löytyvät kaikki yrityksen tilit.

[![](

# Osabudjetilla luodun rakenteen kopioiminen

Kun osabudjetille on luotu valmis rakenne ja samaa rakennetta hautaan hyödyntää uudelleen, kannattaa luotu rakenne kopioida, eikä luoda alusta saakka rivi kerrallaan. Hyvä esimerkki tästä on esimerkiksi henkilöstöbudjettiin uuden työntekijän lisääminen tai lainabudjettiin uuden lainan lisääminen.

Kopioiminen alkaa siitä, että ensin tehdään yksi rakenne alusta saakka valmiiksi ja testataan sen toimivuus. Rivien rakenne tehdään mieluisaksi, tileille tehdään tiliohjaukset kuntoon ja tarkistetaan, että tiliohjaukset toimivat. Kun rakenne on varmasti halutunlainen, voidaan se kopioida.

Kopiointi tehdään yläosan työkalupalkista plus -painikkeen takaa.

[![](

# Osabudjetin rivien siirtäminen

Osabudjettien rivien paikkoja voi siirtää myös jälkikäteen. Rivien siirtäminen tapahtuu rivin perässä olevan kolmen pisteen takaa toiminnolla "move row".

[![](

Tämän jälkeen käyttäjälle aukeaa näkymä, jossa voidaan nuoli näppäimin valita, mihin väliin rivi halutaan siirtää. Jos esimerkiksi rivi "myynti 2" haluttaisiin siirtää tehdas 1 rakenteeseen rivin myynti -jälkeen, painettaisiin myynti rivin perässä olevaa nuoli alaspäin symbolia.

Plussa painike siirtää rivin alisteiseksi lapsiriviksi.

[![](



artikkelin osoite on https://intercom.help/finazilla/fi/articles/4426574-uuden-osabudjetin-luominen-tai-osabudjetin-kopioiminen-toiselta-asiakkuuden-yritykselta

