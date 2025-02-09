## Miksi käyttää toimintoa

[![](

*Versiopäivityksessä 17.11.2023 tuotu kokonaan uusi toiminto. Toiminto mahdollistaa budjetin kiinnittämisen halutuille dimensioille. Toimintoa parannettu 12.1.2024 päivityksessä yritystasoisen taseen osalta.*

Olemme kuvanneet budjetin luomista mm. artikkelissamme [täällä.]( Tässä artikkelissa kerromme, kuinka budjetti voidaan luoda siten, että se sidotaan johonkin tiettyyn dimensioon / dimensioihin. Toiminto mahdollistaa myös taseen tekemisen "yritystasoisena", vaikka pääbudjetille olisi valittu dimensio/dimensioita.

# Miksi käyttää toimintoa

Kun budjetille on valittu tietty dimensio/dimensiot, on budjetti nopeampi käyttää kuin sellainen budjetti, jossa kaikki dimensiot ovat käytössä.

Lisäksi budjetin lukujen kohdistaminen helpottuu merkittävästi, kun valittavana on vain ne dimensiot, joita halutaan käyttää.

Toiminto on myös kätevä tilanteissa, missä tulosbudjetilla halutaan käyttää dimensioita, mutta tasetta halutaan budjetoida yritystasoisesti.

# Toimintalogiikka tiivistetysti

Budjetille voidaan asettaa, mitä dimensioita kyseisessä budjetissa käytetään. Tämän lisäksi voidaan määritellä, käytetäänkö aiempaa asetusta taseella, vai onko tase kokonaan yritystasoinen. Asetus tekee tämän jälkeen seuraavat asiat:

* Samat valinnat ovat myös kaikilla budjettiin liittyvillä osabudjeteilla
* Budjettia ei voi syöttää asetuksen ulkopuolisille dimensioille
* Ennustebudjetti (forecast budget) uudelleen kohdistaa tuodut toteumat soveltumaan budjettiin valitulle asetukselle. Uudelleen kohdistus riippuu tilanteesta (mikäli dimensiota ei ole lainkaan kyseisellä budjetilla käytössä, on uudelleen kohdistus "blank". Matriisikohdistuksissa uudelleen kohdistus tehdään sille osapuolelle, joka on budjetille valittuna - jos kumpaakaan ei ole, kohdistetaan tämäkin tunnisteelle "blank")
* Import työkalulla budjetille toteuman tuonnissa toteumat kohdistetaan uudelleen valituille dimensioille

Lisäksi mikäli tase on valittu tehtävän yritystasoisena:

* Taseeseen ei voi syöttää millekään dimensiolle
* Import työkalulla budjetille toteuman tuonti tuo luvut yritystasolle (nk. blank) riippumatta siitä, mikä on toteumadatan varsinainen dimensiokohdistus
* Kaikki tuloslaskelmalta tulevat luvut kohdistetaan taseessa yritystasolle eli nk. blank tasolle; myös tuloslaskelman kautta laskettava tilikauden voitto/tappio
* Kaavaviittaukset taseesta tuloslaskelmaan hakee laskentaan luvun kaikilta dimensioilta
[![](

*Kaikki vanhat Finazilla -budjetit ovat automaattisesti kaikille yrityksen dimensioille kiinnitettyjä. Mikään ei siis muutu käyttäjien budjeteissa automaattisesti, vaan vanhat budjetit toimivat kuten ennenkin.*

# Dimensiokiinnitetyn budjetin luominen

Budjettia luotaessa dimensiot voidaan valita kohdassa "dimensions used in this budget". Mikäli kenttään ei valita mitään, tulee budjetista yritystasoinen. Yritystasoisessa budjetissa ei ole siis lainkaan dimensioita käytössä.

[![](

Dimensions used in this budget -listaukseen tulee valittavaksi vain ne dimensiot, joita ei ole piilotettu budjetoinnista dimensions -näkymässä. Näkymään voi valita yhden tai useamman dimension. Mikäli budjetissa halutaan kohdistaa lukuja pelkästään kustannuspaikoille; valitaan vain kustannuspaikka. Jos budjetissa on tarve kohdistaa kustannuspaikoille ja asiakasryhmille, valitaan molemmat.

[![](

Kun budjetti on luotu siten, että se on kiinnitetty vaikkapa dimensiolle "kustannuspaikka", näkyy kiinnitetty dimensio/dimensiot budjetin edit -painikkeen takaa.

[![](

Alla kuvaamme erilaisia budjetteja tarkemmin.

## Yritystasoinen budjetti

Yritystasoinen budjetti luodaan siten, että budjettia luotaessa kenttään "dimensions used in this budget" ei valita mitään. Jättämällä kenttä tyhjäksi, luodaan budjetista yritystasoinen. Yritystasoisessa budjetissa lukuja ei voi kohdistaa millään tavalla mihinkään dimensioon. Tällaisessa budjetissa ei myöskään näy monitor -näkymä, eikä oikean yläkulman dimensions -valinta.

Yritystasoisessa budjetissa käyttäjä ei voi kohdistaa lukuja dimensioille myöskään osabudjettien kautta. Osabudjettien puolella käytössä ei ole seuraavat toiminnot:

* Osabudjetin luonnin yhteydessä tehtävä dimensiokiinnitys (target to dimension value)
* Osabudjetin oikean yläkulman dimensio -kohdistus ei näy
* Kirjanpidon dimensiot eivät ole valittavissa riviasetuksien kautta
* Vyörytyssääntö -välilehti ei näy lainkaan
## Dimensiokiinnitetty budjetti

Dimensiokiinnitetty budjetti käyttäytyy pääpiirteittäin samalla tavoin kuin budjetit aikaisemminkin. Ainoa ero aikaisempaan nähden on siinä, että budjetin oikeaan yläkulmaan tulee valittavaksi vain ne dimensiot ja dimensionarvot, jotka on kiinnitetty budjetille.

Dimensiokiinnitetyn budjetin lukuja ei voi millään metodilla kohdistaa sellaiselle dimensiolle, jota ei ole kiinnitetty budjetille. Jos budjetille on siis valittu pelkästään dimensio asiakasryhmä, tulee valittavaksi vain kyseinen dimensio.

[![](

Dimensiokiinnitetyssä budjetissa on käytettävissä monitor -näkymä, joka näyttää kaikki budjetin luvut kohdistuksin.

Osabudjettien puolella lukuja voidaan kohdistaa vain dimensiolle/dimensioille, jotka on määritelty budjetin asetuksiin. Osabudjetilla on käytössä seuraavat toiminnot:

* Osabudjetin luonnin yhteydessä tehtävä dimensiokiinnitys (target to dimension value) listauksessa näkyy vain budjetille kiinnitetyt dimensiot
* Osabudjetin oikeassa yläkulmassa on valittavissa vain budjetille kiinnitetyt dimensiot
* Riviasetuksissa näkyy vain budjetille kiinnitetyt dimensiot
* Vyörytyssääntö välilehti on näkyvissä. Vyörytyssääntö -listauksessa näkyy vain ne vyörytyssäännöt, jotka osuvat budjetin asetuksiin. Käyttäjä ei voi siis vyöryttää budjetin lukuja sellaiselle dimensiolle, mikä ei ole budjetilla käytettävissä

Dimensiokiinnitetyn budjetin tase toimii samalla logiikalla. Taseen osalta on huomioitavaa, että Finazilla laskee automaattisesti tilikauden voiton/tappion ja vie tämän taseeseen omaan pääomaan sekä vastakirjauksena pankkitilille. Tämä kirjaus on yritystasoinen.

## Dimensiokiinnitetty budjetti, jossa tase on yritystasoinen

Budjettia luotaessa voi valita, että budjetilla on dimensiot käytössä, mutta tase tehdään yritystasoisena. Valinta tehdään kentässä "remove dimensions from balance sheet".

[![](

Oheisella valinnalla tehdyllä budjetilla taseen puolella käyttäjille ei näy lainkaan oikean yläkulman dimensio -kohdistus syöttönäkymässä. Mikäli taseeseen ohjataan lukuja osabudjetin kautta, näyttää monitor -näkymä, mistä osabudjetista taseen luvut tulevat. Itse luvut ovat kohdistamattomia, eli näkyvät tunnisteella "blank".

[![](

Jos osabudjetin kautta yritetään "vahingossa" ohjata lukuja taseeseen dimensioille (esimerkiksi rivin lisäkohdistuksen kautta), luvut muutetaan dimensioimattomiksi. Käyttäjä ei voi siis vahingossakaan kohdistaa taseen lukuja dimensioille. Toimintalogiikka tuloksen osalta noudattelee aiemmin kuvattua logiikkaa; luvut siirretään taseeseen tilikauden voitto/tappio tilille yritystasoisena, huolimatta siitä, missä luvut tuloslaskelmassa ovat.

# Ennustebudjetit

Mikäli ennustebudjetille on määritelty käytettäväksi vain tietty dimensio/dimensiot, uudelleen kohdistetaan luvut soveltumaan budjetin valintaa vasten.

Jos ennustebudjetille on valittu käytettäväksi vain 1 dimensio (ja toteumaa olisi oikeasti kahdella dimensiolla), niin ennusteeseen tulee kaikki luvut. Lukujen kohdistuminen muuttuu. Muutos riippuu siitä, miten luvut on toteumissa.

* Matriiseilla olevat luvut (dimensio 1 + dimensio 2) esitetään sillä matriisin osapuolella, joka on budjetilla käytössä
* Dimensiolla x olevat luvut näytetään tunnisteella "blank", mikäli dimensio x ei ole budjetilla käytössä lainkaan

**Esimerkki: yrityksellä on myyntiä oheisesti**

* 10 000€ myyntiä dimensionarvolle hallinto
* 15 000€ myyntiä dimensionarvolle hallinto + Jyväskylä

Mikäli ennustebudjetilta on rajattu pois dimensio, missä dimensionarvo Jyväskylä on, esitetään koko myynti 25 000€ dimensionarvolla hallinto.

# Lisätietoja

[Dimensiokiinnitetty budjetti, Osa 2: toteumien tuominen](



artikkelin osoite on https://intercom.help/finazilla/fi/articles/8516822-dimensiokiinnitetty-budjetti-osa-1-budjetin-luominen

