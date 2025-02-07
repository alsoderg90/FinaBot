## Osabudjetin riveillä tehtävät valinnat

[![](

*Versiopäivityksessä 21.5.2021 tuotu kokonaan uusi toiminto. Toiminto mahdollistaa operatiivisen datan tuomisen osabudjetille.* 

Tämän artikkelin ymmärtämisen edellytyksenä on, että käyttäjä tietää mitä operatiivinen data on ja miten sitä voidaan hyödyntää Finazillassa eri tavoin. Käyttäjän tulee myös hallita perus budjetointiin, ja osabudjetteihin, liittyvät toiminnallisuudet, sillä toimintalogiikka on valtaosin samanlainen operatiivisessa datassa.

Osabudjetin riville, sekä sen lapsiriveille, voidaan tuoda operatiivista dataa "import data" toiminnon kautta. Import data -toiminto tuo dataa valitulle aikajaksolle, joka ei ole sidoksissa osabudjetin aikaväliin (eli mille ajanjaksolle osabudjetti aukeaa kun se avataan). Tuonti suoritetaan kaikille niille osabudjetin riveille, joilla on valittuna jokin operatiivinen kohdistus (eli nk. data group). Filtterin avulla voidaan myös rajata, mille riveille dataa tuodaan. Riville tuodaan luvut aina siltä data groupilta (ja dimensiolta), joka kyseiselle riville on valittu.

# Osabudjetin riveillä tehtävät valinnat

Riville tulee valita haluttu data group kohtaan "transfer to data group". Jos row data type -kenttään on valittu "quantity", tuodaan riville operatiivinen quantity, joka voi olla mitä tahansa määrettä, kuten vaikkapa tunteja tai kappaleita. Jos row data type -kenttään ei ole valittu vaihtoehtoa "quantity", tuodaan silloin ko. riville aina aineiston "amount" data, joka on euroja.

Lisäksi riveille tulee laittaa kohdistus operatiivisille dimensioille, mikäli halutaan, että kyseisille riveille tulee kyseiset arvot - muutoin riveille tulisi data groupin kautta ns. kaikki tieto.

[![](

Kun osabudjetin rivi/rivit on kiinnitetty data groupille, tulee niihin kiinnitystä kuvaava symbooli. Alla olevassa esimerkissä "tehdas 1" hierarkian rivit on kiinnitetty data groupille kun taas tehdas 2 rivejä ei ole kiinnitetty millekään data groupille.

[![](

# Datan tuominen kerralla koko budjettiin import data -toiminnolla

Data voidaan tuoda koko osabudjetille kerralla, samalla logiikalla kuin balance budjetillakin. Tällöin tuonti tehdään yläosan työkalu -painikkeista. Näin datat saadaan tuotua kerralla kaikille riveille, missä on kohdistuksia.

[![](

Dataa tuotaessa valintana on oletuksena kaikki, mutta data type -valinnalla voidaan valita, tuodaanko budjetille quantitya, amounttia vai molempia. Dimensions -filtterin takaa voidaan valita vaikka vain yksi haluttu dimension, joka saataa silti esiintyä useammalla rivillä, ja se päivitetään kaikkialle kerralla. Samalla logiikalla voidaan myös valita vain 5, jotka päivitetään.

# Datan tuominen rivikohtaisesti import data -toiminnolla

Yksittäiselle riville voidaan tuoda dataa rivin asetuksista settings -valikon kautta. Toiminnon nimi on "import data". Dataa tuotaessa valitaan ensin ajanjakso mistä dataa halutaan tuoda (from) ja mille ajanjaksolle se osabudjetilla tuodaan (to).

[![](

Tuonti on kertaluontoinen eli tuonnin jälkeen rivit käyttäytyvät normaalin input -rivin kaltaisesti.

[![](

*Ennustebudjeteilla operatiivinen data saadaan päivittymään automaattisesti käyttämällä rivityyppiä operative. Lue lisää artikkelistamme [täältä.]( 

# Ominaisuudessa huomioitavaa

* Osabudjetin riveille tulee kiinnittää ensin vähintään data group. Dataa tuodaan vain data groupilta, joka on riville valittu
* Jos rivin row data type on quantity, niin riville tuodaan operatiivinen quantity. Muutoin tuodaan amount (€).
* Jos rivillä on operatiivisia dimensio kohdistuksia, niin riville tuodaan vain kyseistä kohdistusta vastaavat luvut. Logiikka vastaa raporttivalintojen dimensio filtteriä ja raporttimallin dimensio filtteriä.

  Esimerkki: jos riville on valittu [PROJEKTI 1], [PROJEKTI 2], [PROJEKTI 3], [KAUPUNKI TRE] niin osabudjettiin tuodaan kaikkien kolmen projektin luvut, jotka on kohdistettu Tampereelle.

  Dimensiot, joita ei filtteri valinnassa ole sisällytetty, eivät vaikuta valintaan mitenkään. Tarkoittaa siis muita dimensioita kuin projekti ja kaupunki.
* Tuonti noudattelee tavallisen balance datan tuomista
* Tuonti voidaan tehdä joko koko osabudjetille kerralla tai rivikohtaisesti
* Luvut voi tuoda kertoimella, käyttäen "multiplier" valintaa (esimerkiksi 10% kasvu merkittäisiin 1.1)
* Lukuja voi esikatsella ennen tuontia preview -painikkeen avulla
* Jos yllä olevat logiikat vastaavat useampaa järjestelmästä löytyvää operatiivista lukua, niin soluun tuodaan näiden lukujen summa.


artikkelin osoite on https://intercom.help/finazilla/fi/articles/5258366-operatiivisen-datan-tuominen-osabudjetille-import-toiminnolla

