## Hankintamenolaskelman laskennan taustaa

[![](

Versiopäivityksessä 18.4.2024 tuotu kokonaan uusi toiminto. Toiminto mahdollistaa hankintamenolaskelman mukaisten tositteiden kirjaamisen Finazillaan yhdellä kertaa.

Finazillassa voidaan kirjata nk. Finazilla tositteita. Finazilla tositteisiin on tehty uusi vaihtoehto, joka on FAS:n mukainen hankintamenolaskelma. Tositetyyppi on nimeltään "New Acquisition". Uusi ominaisuus on kehitetty konserniyritysten tarpeisiin.

# Hankintamenolaskelman laskennan taustaa

Hankintamenolaskelma on joukko tositteita, joita täytyy kirjata kirjanpitoon, kun yritys ostaa toisen yrityksen joko kokonaan, tai osittain. Havainnollistamme hankintamenolaskelmaan liittyvää laskentaa alla esimerkin avulla.

Yritys A ostaa yrityksen B. Yrityksen B hankintahinta on 1M€. Poistoaika on 25 vuotta.

Kuukausittaiset poistot ovat 4166,67€/kk. Vuositasolla tämä tekee 50 000€ ja 20 vuoden poistoajassa tästä kertyy 1M€, eli koko hankintahinta.

Hankintahinta 1M€ kirjataan tytäryrityksen osakkeisiin täysimääräisesti, silloin kun yrityksen koko osakekanta on ostettu.

Hankintahinta perustuu yleensä ostettavan yrityksen B taseeseen - eli siihen, mitä omaisuutta yrityksellä B on. Omaisuutta voi olla koneissa ja laitteissa, kiinteistöissä, maa-alueissa ja erilaisissa patenteissa jne. Taseen omaisuuden lisäksi hankintahinta voi sisältää "aineetonta hyvää", eli liikearvoa. Liikearvoa voisi kuvata vaikkapa brändilisäksi tai muuksi ei aineettomaksi hyväksi. Se mitä ei hankintahinnan osalta voida taseen osalta perustella, on liikearvoa. Jos siis aiemmin mainittu ostohinta 1M€ sisältää 800 000€ osalta taseen eriä, on liikearvoa jäljelle jäävä 200 000€.

Kun hankintamenolaskelmaan otetaan mukaan taseen eriä, muuttuu poistojen laskenta. Jos hankintahintaa 1M€ vasten ostetulla yrityksellä on 500 000€ arvosta vaikkapa koneita ja laitteita, lasketaan kuukausittaiset poistot jäljelle jääneen 500 000€ mukaan. Tällöin poistot on 2083,33€/kk. Vuositasolla tämä on 25 000€ ja 20 vuoden poistoajassa tästä kertyy 500 000,00€, eli jäljellä olevan liikearvon määrä (kun taas vastaavasti mikäli ostetulla yrityksellä on 800 000€ arvosta koneita ja laitteita, lasketaan kuukausittaiset poistot jäljelle jääneen 200 000€ mukaan). Poistot lasketaan siis aina liikearvon määrästä (goodwill).

# Hankintamenolaskelman kirjaaminen Finazillaan

Finazilla tositteita kirjataan company -valikossa kohdassa "vouchers". Näkymässä on painike "new acquisition", jolla voidaan kirjata tässä artikkelissa kuvattu hankintamenolaskelma.

[![](

New acquisition -painike aukaisee käyttäjälle lomakkeen, johon voidaan kirjata kerralla kaikki hankintamenolaskelman tapahtumat.

[![](

## Havainnollistava esimerkki 1: ostetaan 100% osakekannasta

Havainnollistamme hankintamenolaskelman tekemistä konkreettisella esimerkillä. Yritys Magnusti Ltd on hankkinut omistukseensa yrityksen Wombat Oy. Yritys on ostettu 1.4.2024. Magnusti on ostanut Wombat Oy:ön koko osakekannan eli 100% yrityksestä. Poistoaika on 20 vuotta, eli 240 kuukautta. Versio kenttään on kerrottu pakollinen versionumero, eli ensimmäistä kirjausta tehtäessä numero 1.

Acquisition name on yksilöivä tunnistetieto, joten se tulee huomioida tositetta luotaessa. yrityksellä ei voi olla kahta tai useampaa saman acquisition namea omaavaa tositetta. Mahdollinen dimensio -kohdistus valitaan dimensions -kenttään, josta se "valuu" myöhemmin kaikille tositteille.

[![](

Price of purchase -kohtaan merkitään hankintahinta, sekä kuvaus hankinnasta. Tässä esimerkissä hankintahinta Wombat Oy:ön osalta on 1 000 000,00€.

Kun hankintahinta syötetään tositteelle Finazillaan, Finazilla laskee automaattisesti tositteelle tytäryritysten osakkeiden arvon, liikearvon, kuukausittaisen poiston, sekä vuotuisen poiston.

[![](

Välilehdellä Equity of company bought kerrotaan, mitä kyseiseltä yritykseltä on ostettu ja mihin hintaan. Kuvan esimerkissä wombat Oy:ltä on ostettu 500 000€ edestä koneita ja laitteita. Patentteja on ostettu 300 000€ arvosta. Uusia rivejä pääsee lisäämään rivin perässä olevasta "add" painikkeesta.

[![](

Huomaa, että calculations kohdan luvut muuttuvat, kun omaisuuseriä lisätään. Seuraavaksi tositeriveille tulee käydä tekemässä tarvittavat tilikiinnitykset taustalaskentoihin. Tilikiinnitys tehdään rivin perässä olevasta valikosta. Valikosta löytyy kaikki yrityksen tilit.

[![](

Kun tilikiinnitykset on tehty kaikille riveille, voidaan tosite luoda "create vouchers" painikkeesta.

[![](

Create vouchers - toiminto luo Finazillaan automaattisesti tositteet; varsinaisen konsolidointi -tapahtuman (kuvassa keltaisella korostettu), johon kirjataan kaikki lomakkeen luvut, joilla on tilivalinta, (poislukien monthly depreciation, eli kuukausittainen poisto). Tämän lisäksi Finazillaan syntyy kuukausittaiset poistotositteet annetulle poistoaikavälille lomakkeelle lasketusta Goodwill -arvosta (kuvassa vihreällä korostettu).

Artikkelin esimerkissä poistot alkavat siis 1.4.2024 ja kestävät tuosta hetkestä 20 vuotta eteenpäin. Finazillaan syntyy siis 20 vuoden poistotositteet kullekin kuukaudelle automaattisesti. Automaattisesti esiin tulee vain ko. kuukauden tositteet; muut tositteet voidaan hakea yläosan haku -toiminnolla.

[![](

## Havainnollistava esimerkki 2: ostetaan 50% osakekannasta

Yritys Wombat Oy ostaa 1.3.2024 Magnusti Oy:stä 50%. Kauppahinta on 1 000 000,00€. Magnustilla on koneita ja kalustoa 800 000€ arvosta. Kaupan yhteydessä Wombat saa omistukseensa 50% Magnustin kalustosta, eli 400 000€. Liikearvoa syntyy 600 000€, sillä Wombat maksaa 1 000 000,00€ ja saa sitä vastaan kalustoa 400 000,00€ (50% kaluston arvosta).

Finazilla laskee tositteelle automaattisesti 50% mukaisesti kaikki hankintamenolaskelman luvut. Käyttäjän tehtäväksi jää tilikiinnitysten tekeminen tarvittaville riveille. Huomaa, että tässä esimerkissä on myös vähemmistöosakkeille oma rivinsä (minority shares), johon kiinnitetään haluttu tili.

[![](

# Hankintamenolaskelman tositteiden selaaminen

Tosite -näkymässä (vouchers) voidaan selata tositteita. Tositteiden selailussa tulee aina huomioida se, että mitä tositteita halutaan katsoa. Tositetyyppi -kentässä määritellään, halutaanko hakea kaikkia tositteita (all) vai esimerkiksi pelkästään hankintamenolaskelma -tositteita (Acquisition).

Hakukenttään tulee lisäksi valita ajanjakso, minkä aikavälin tositteita haetaan. Alla olevassa esimerkissä on haettu yrityksen Magnusti Ltd tositteista 1.4.2024 - 31.12.2024 aikavälin tositteet liittyen hankintamenolaskelmaan. Magnusti Ltd on ostanut 1.4.2024 Wombat Oy:n, joten ensimmäinen tosite löytyy päivältä 1.4.2024. Samalta päivältä löytyy yritysostoon liittyvä poistotosite. Vastaavat poistotositteet löytyvät myös vuoden muilta kuukausilta.

[![](

Tositerivit saadaan tarvittaessa auki klikkaamalla kyseistä tositetta selite -kentässä (description). Näkymä aukaisee kyseisen tositteen tositerivit.

[![](

# Hankintamenolaskelman tositteiden muokkaaminen

Mikäli jo tehtyä hankintamenolaskelmaa halutaan muokata, tehdään muokkaus varsinaiselle joko konsolidointitositteelle tai jollekin poistotositteelle. Muokkaamisen voi siis tehdä minkä tahansa tositteen kautta ja se kohdistuu oikeaan hankintamenolaskelmaan.

Tosite löytyy siltä päivältä, mihin se on kirjattu. Hakuehtona tulee käyttää voucher type "Aquisition" valintaa. Alla olevassa esimerkissä kyseinen varsinainen tosite on ylempi (alempi tosite on kyseisen kuukauden yksittäinen poistotosite).

[![](

Tosite klikataan listasta auki klikkaamalla selite -kentässä olevaa selitettä. Tämän jälkeen valitaan oikeasta yläkulmasta painike "Edit Acquisition".

[![](

Tämän jälkeen käyttäjälle aukeaa tosite ja sen kirjaukset. Tästä näkymästä käyttäjän tulee vielä painaa oikean yläkulman painiketta "New Version"

[![](

Kun Finazillaan luodaan hankintamenolaskelma, tulee tositteelle antaa aina pakollisena tietona versiointitieto (version). Versiointitieto voi olla esimerkiksi numero 1. Kun alkuperäistä tositetta muokataan, tulee muokkaukselle antaa uusi versiointitieto, esimerkiksi numero 2. Versioita voi olla niin monta kuin on tarpeen.

[![](

Silloin kun konsolidointitositetta muokataan, eikä se ole konsolidoinnin ensimmäinen versio, näytetään lomakkeella nykyisen/alkuperäisen konsolidoinnin tiedot. Konsolidointitositteella voidaan muokata kaikkea muuta, paitsi osakkeiden määrää (acquired sharehold %), poistoaikaa (depreciation time) ja selitettä (acquisition name).

Pohjatietoja pystyy muokkaamaan uuteen versioon haluamallaan tavalla. Muutokset laskentoihin näkyvät Change-sarakkeessa. Huom: Equity- ja Price-rivejä on oltava vähintään sama määrä kuin edellisessä versiossa.

Jos esimerkiksi todetaan, että ostetun yrityksen koneiden ja laitteiden tasearvo olikin 550 000€, eikä alkuperäisessä konsolidointitositteessa kirjattu 500 000€, kirjataan ko. riville uusi arvo. Finazilla laskee muutoksen jälkeen erotuksen sekä koneet ja kalusto riville, että liikearvoon. Myös poistojen osalta lasketaan muutos.

Silloin kun tosite ei ole konsolidoinnin ensimmäinen versio, näytetään lomakkeella aina kaikkien erien osalta nykyisen ja edellisen version tiedot, sekä näiden välinen muutos, kuten alla.

[![](

Haluttujen muokkausten jälkeen create vouchers- nappi luo konsolidoinnista uuden version, sekä mahdolliset muutostositteet Finazillaan. Uuden version luonnin voi perua Cancel-napista, jolloin uusi versio häviää välilehdiltä.

Uusi versio löytyy tositteista hakemalla. Selite -kentässä (Description) tositteella on se versionumero, mikä sille on annettu. Alla olevassa kuvassa keltaisella merkitty tosite on aivan ensimmäinen konsolidointitosite. Vihreä tosite on tehty muutos, jossa koneiden ja kaluston arvoa nostettiin +50 000€. Muut tositteet ovat konsolidointistositteen generoimia poistotositteita.

[![](

[![](

*Mikäli konsolidointitositteeseen tehdään jokin muutos, syntyy Finazillaan uudet erilliset poistotositteet, joissa on muutoksen määrä. Alkuperäiset poistotositteet jäävät Finazillaan alkuperäisillä euroilla. Ominaisuuden taustalla on ajatus siitä, että kirjaus ja siihen tehdyt muutokset ovat läpinäkyviä. Tapahtumille jää oma historiatietonsa näkyviin ja Finazillasta nähdään aina alkuperäinen kirjaus, sekä mahdolliset muutokset.*

# Hankintamenolaskelman tositteiden poistaminen

Mikäli tehty hankintamenolaskelma halutaan poistaa, tulee poistaminen tehdä jonkun hankintamenolaskelman tositteen kautta. Poistaminen voidaan siis tehdä joko varsinaiselta hankintamenolaskelman tositteelta, tai miltä tahansa poistotositteelta. Kun esimerkiksi poistotosite poistetaan, poistuu kaikki muutkin samaan tapahtumaan liittyvät tositteet (eli kaikkien muiden kuukausien poistotositteet, sekä varsinainen konsolidointitapahtuma).

Tosite löytyy siltä päivältä, mihin se on kirjattu. Hakuehtona tulee käyttää voucher type "Aquisition" valintaa. Alla olevassa esimerkissä kyseinen varsinainen tosite on ylempi (alempi tosite on kyseisen kuukauden yksittäinen poistotosite).

[![](

Kun tosite on löytynyt, voidaan se aukaista klikkaamalla kyseistä tositetta. Tositteen oikeassa yläkulmassa on edit acquisition -painike, jolla tositetta voidaan muokata.

[![](

Edit Acquisition -painikkeesta painamalla tositteen alareunaan tulee delete -painike, jolla tositteen voi poistaa. Kun tosite poistetaan, poistuu kaikki siihen liittyvät muutkin tositteet, eli kaikki poistotositteet sekä konsolidointitapahtuma samalla.

[![](

[![](

*Vain konsolidoinnin viimeisimmän version voi poistaa. Poistamalla konsolidoinnin ainoan version, poistuu myös koko konsolidointitapahtuma Finazillasta, sekä kaikki siihen liittyvät poistotositteet*

[![](

artikkelin osoite on https://intercom.help/finazilla/fi/articles/9121061-fas-hankintamenolaskelma

