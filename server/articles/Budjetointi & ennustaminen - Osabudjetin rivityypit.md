## Osabudjetin rivityypit

[![](

Versiopäivityksessä 5.5.2023 tuotu uusi toiminto. Toiminto mahdollistaa osabudjetille rivien luonnin siten, että niihin haetaan aina toteutuneet luvut. Toiminto on suunniteltu erityisesti ennustebudjetteja varten.

Tuotu ominaisuus on osa laajempaa kokonaisuutta. Tässä artikkelissa esitelty ominaisuus on osa 1/2. Toimintoon liittyy myös seuraavat ominaisuudet:

* [Automaattisesti päivittyvä osabudjetti, osa 2: dimensiokohdistukset actual ja operative riveillä](

Tämän artikkelin ymmärtämisen edellytys on, että lukija tietää, mitä Finazillan ennustebudjetit ovat ja osaa luoda ennustebudjetteja. Lisäksi käyttäjän on hyvä ymmärtää osabudjettien merkitys ja niiden luominen. Rivityypin operative ymmärtämisen edellytys on, että käyttäjä ymmärtää mitä operatiivinen data on ja kuinka sitä budjetoidaan.

# Osabudjetin rivityypit

Aikaisemmin osabudjeteilla oli olemassa 4 vaihtoehtoa, minkälaisia rivejä osabudjetille voi luoda. Rivityypit olivat syöttörivi (input), otsikko (header), kaava (formula) ja prosenttirivi (percentage). Nyt rivityyppeihin on tuotu näiden lisäksi kaksi uutta rivityyppiä, jotka ovat actual ja operative.

[![](

Uudet rivityypit on luotu siksi, että tällä mahdollistetaan ennustebudjetin ominaisuuksien tuominen osabudjeteille saakka. Toiminto on siis suunniteltu nimenomaan ennustebudjetteja (forecast budget) varten. Normaalilla budjetilla kyseiset rivit toimivat kuten tavalliset syöttörivit; rivien väritys on vain normaalista syöttörivistä (vihreä) poikkeava (ruskea). Tämä artikkeli kuvaa erityisesti tilanteita, missä budjetin tyyppinä on ennustebudjetti (forecast budget).

# **Uusien rivityyppien actual ja operative tilimäärittelyt**

Mikäli osabudjetille on luotu rivejä, joiden tyyppi on joko actual tai operative, tuodaan näissä tilanteissa kyseisille riveille dataa ennustebudjetin real balance end date -päivään saakka. Tuotu data on toteumadataa ja se tuodaan sellaisenaan siltä tililtä, mikä kyseiselle riville on kiinnitetty lähtötiliksi.

Lähtötili (eli tili mistä toteumadataa tuodaan) asetetaan kohtaan "transfer from". Mikäli toteuma halutaan tuoda ***yksittäiseltä tililtä***, on valinta "accounts" ja haluttu tili laitetaan alempaan kenttään (select accounts). Toteumaa voi hakea myös ***tiliväliltä***, jolloin valitaan transfer from -kohtaan valinta "account range" ja kerrotaan haluttu tiliväli. Transfer from kohtaan voidaan myös kiinnittää ***tiliryhmä***, jolloin toteumaa haetaan koko tiliryhmästä. Tiliryhmä valitaan käyttämällä valintaa "accounts" ja alasvetovalikosta valitaan haluttu tiliryhmä.

Nämä määrittelyt määräävät sen, mistä tililtä/tilivälistä/tiliryhmästä toteumat tuodaan ja minne ne pääbudjetilla ohjataan (transfer to account). Real balance end date:n jälkeisen ajan käyttäjä voi budjetoida itse käsin, aivan kuten ennenkin.

Sum all data from all dimensions -valinta mahdollistaa sen, että actual riville voidaan tuoda toteumat kootusti kaikilta dimensionarvoilta. Luvut tuodaan yhteenlaskettuna.

[![](

[![](

*Rivejä voi luoda suoraan myös ennustebudjetille. Tämä mahdollistaa jo olemassa oleville ennustebudjeteille päivittyvien rivien lisäämisen. Toteumat tulevat uudelle riville heti ja real balance end date:n jälkeinen aika on nollana, kunnes se budjetoidaan.* 

Havainnollistamme toimintoa vielä tarkemmin kummankin rivityypin osalta erilaisin esimerkein.

# Actual -rivityyppi

## Yksittäinen tili

Mikäli osabudjetille luodaan rivi, joka on tyypiltään "actual", on näkymä oheinen. Kohdassa "transfer to account" kerrotaan, että mille budjetin tilille kyseisen rivin saldo ohjataan. Kohdassa "transfer from accounts" kerrotaan, että miltä tililtä saldo haetaan riville. Nämä kaksi kenttää mahdollistavat sen, että käyttäjä voisi kertoa, että osabudjetille haetaan vaikkapa tilin 3003 saldo, mutta varsinaisella budjetilla saldo halutaan ohjata tilille 3000.

[![](

Mikäli transfer to account ja from account ovat yksi ja sama tili, haetaan saldot samalta tililtä, minne ne budjetillakin ohjataan. Osabudjetilla luotu rivi näyttäytyy oheisesti.

[![](

***Esimerkki 1: yksittäinen tili haetaan ja ohjataan samaan paikkaan***

Yrityksellä on olemassa osabudjetti, millä budjetoidaan myynnit. Osabudjetille on tehty rivi, jonka tyyppi on "actual". Rivin asetuksissa kerrotaan, että riville tuodaan saldot tilistä 3000. Kyseiselle riville budjetoidut eurot halutaan ohjata pääbudjetilla tilille 3000.

Yritys budjetoi vuoden 2024 myynnit kuukausittain. Kauden 1/2024 budjetoitu myynti on 550 000€ , kauden 2/2024 budjetoitu myynti on 785 000€ ja kauden 3/2024 budjetoitu myynti on 645 000€.

Kyseisestä budjetista tehdään ennustebudjetti. Ennustebudjetille kerrotaan, että real balance end date on 28.2.2024. Osabudjetin kauden 1/2024 budjetoitu myynti ylikirjoitetaan toteutuneella myynnillä, samoin kauden 2. Kausi 3/2024 jää ennalleen. Osabudjetin riville tulee siis toteutuneet myynnit real balance end date päivään saakka. Loppuosa on edelleen ennustetta ja sitä voidaan päivittää manuaalisesti.

***Esimerkki 2: yksittäinen tili haetaan eri tililtä kuin mihin se ohjataan***

Yrityksellä on edelleen olemassa osabudjetti, millä budjetoidaan myynnit. Osabudjetille on tehty rivi, jonka tyyppi on "actual". Rivin asetuksissa kerrotaan, että riville tuodaan saldot tilistä 3010. Kyseiselle riville budjetoidut eurot halutaan ohjata pääbudjetilla tilille 3000.

Yritys budjetoi vuoden 2024 myynnit kuukausittain. Kauden 1/2024 budjetoitu myynti on 550 000€ , kauden 2/2024 budjetoitu myynti on 785 000€ ja kauden 3/2024 budjetoitu myynti on 645 000€.

Kyseisestä budjetista tehdään ennustebudjetti. Ennustebudjetille kerrotaan, että real balance end date on 28.2.2024. Osabudjetin kauden 1/2024 budjetoitu myynti ylikirjoitetaan toteutuneella myynnillä (tilin 3010 myynnit), samoin kauden 2. Kausi 3/2024 jää ennalleen. Osabudjetin riville tulee siis toteutuneet myynnit real balance end date päivään saakka tilitä 3010. Loppuosa on edelleen ennustetta ja sitä voidaan päivittää manuaalisesti. Kun ennustebudjettia tarkastellaan pääbudjetin puolelta, budjetin monitorista tai raportin kautta, näkyvät kyseiset myynnit tilillä 3000.

***Esimerkki 3: tiliväli***

Yrityksen osabudjetilla budjetoidaan myyntejä actual -rivityypillä. Rivin asetuksissa kerrotaan, että riville tuodaan saldot tiliryhmästä "yleiset myyntitilit". Tili -kohtaan ei ole siis valittu yksittäistä tiliä, vaan tiliryhmän otsikko. Kyseisen tiliryhmän saldot ohjataan pääbudjetin tilille 3000.

[![](

Yritys budjetoi vuoden 2024 myynnit kuukausittain. Budjetoitu myynti on kaudella 1/2024 50 000€, kaudella 2/2024 65 000€ ja kaudella 3/2024 40 000€.

Yrityksen toteumat on alla olevat:

Kausi 1/2024

tilillä 3000 yhteensä 10 000€

tilillä 3003 myynti on 25 000€

tilillä 3100 myynti on 10 000€

Tiliryhmän myynti on siis yhteensä 45 000€

Kausi 2/2024

tilillä 3000 yhteensä 20 000€

tilillä 3003 myynti on 15 000€

tilillä 3100 myynti on 20 000€

Tiliryhmän myynti on siis yhteensä 55 000€

Kausi 3/2024

tilillä 3000 yhteensä 30 000€

tilillä 3003 myynti on 5 000€

tilillä 3100 myynti on 15 000€

Tiliryhmän myynti on siis yhteensä 50 000€

Kyseisestä budjetista tehdään ennustebudjetti ja ennusteella real balance end date on 28.2.2024. Osabudjetin kauden 1/2024 budjetoitu myynti (50 000€) ylikirjoitetaan toteutuneella myynnillä (45 000€) ja kauden 2/2024 budjetoitu myynti (65 000€) ylikirjoitetaan toteumalla (55 000€). Kausi 3/2024 jää edelleen budjetoiduksi, eli siellä on myyntiä 40 000€. Lukua voi halutessaan päivittää.

# Actual -rivityyppi

## Tiliväli

Mikäli osabudjetille luodaan rivi, joka on tyypiltään "actual", on näkymä oheinen. Kohdassa "transfer to account" kerrotaan, että mille budjetin tilille kyseisen rivin saldo ohjataan, kun taas kohdassa "transfer from" kerrotaan, että miltä tiliväliltä saldo haetaan riville. Nämä kaksi kenttää mahdollistavat sen, että käyttäjä voisi kertoa, että osabudjetille haetaan vaikkapa kaikkien myyntitilien saldo, mutta varsinaisella budjetilla saldo halutaan ohjata tilille 3000.

[![](

***Esimerkki 1: yksi tiliväli***

Yritys on budjetoinut myyntiä vuodelle 2024 kuukausittain. Budjetoitu myynti on kaudella 1/2024 50 000€, kaudella 2/2024 65 000€ ja kaudella 3/2024 40 000€.

Yrityksen toteumat ovat oheiset:

Kausi 1/2024

tilillä 3000 yhteensä 10 000€

tilillä 3003 myynti on 25 000€

tilillä 3100 myynti on 10 000€

tilillä 3999 myynti on 20 000€

Tiliryhmän myynti on siis yhteensä 65 000€

Kausi 2/2024

tilillä 3000 yhteensä 20 000€

tilillä 3003 myynti on 15 000€

tilillä 3100 myynti on 20 000€

tilillä 3999 myynti on 15 000€

Tiliryhmän myynti on siis yhteensä 70 000€

Kausi 3/2024

tilillä 3000 yhteensä 30 000€

tilillä 3003 myynti on 5 000€

tilillä 3100 myynti on 15 000€

Tiliryhmän myynti on siis yhteensä 50 000€

Budjetista tehdään ennuste, jolloin actual -rivityyppi alkaa hakemaan toteumalukuja riville. Ennusteen real balance end date on 28.2.2024, jolloin kaudelle 1 tuodaan myynti yhteensä tileiltä 3000-3999 (kuten rivin asetuksissa on kerrottu). Riville tuodaan toteumaksi myyntiä siis 65 000€. Kaudelle 2/2024 tuodaan 70 000€. Kausi 3/2024 jää, kuten budjetoitu. Summana on 50 000€.

***Esimerkki 2: useampi tiliväli***

Yritys haluaa tuoda ennustebudjetin osabudjetille jollekin tietylle riville lukuja, jotka muodostuvat useammista eri tiliväleistä. Tilanne voi olla myös sellainen, että yrityksellä on käytössään 4 ja 5 numeroisia tilejä, ja saldoja halutaan tuoda molemmilta tilinumerosarjoilta.

Transfer from kohdassa valinnalla account range voidaan tuoda lukuja riville myös useasta tilivälistä. Tilivälin perässä oleva "add" painike lisää uuden rivin, johon voidaan laittaa uusi tiliväli.

[![](

# Actual -rivityyppi

## Dimensiot summattuna

Actual rivityypissä on mahdollisuus valita kohdassa "sum all data from all dimensions", että riville tuodaan saldot kaikilta dimensionarvoilta. Valintaa ei voi käyttää yhdessä valinnan "additional dimension values" valinnan kanssa, sillä nämä ovat päällekkäiset valinnat.

**Esimerkki 1: kahdesta dimensiosta vain toinen käytössä**

Yrityksen toteuma kohdistuu dimensiolle tehdas siten, että tehtaan 1 myynti on 1000€. Tehtaan 2 myynti on 2000€, tehtaan 3 myynti on 5000€ ja lisäksi myyntiä on 10 000€ dimensiolla kaupunki (dimensionarvolla Helsinki). Kokonaismyynti on siis 18 000€.

Yritys tekee ennustebudjetin. Budjetilla on käytössä ainoastaan dimensio "tehdas", eikä lainkaan dimensiota kaupunki. Osabudjetille tulee toteumaan myyntiä 18 000€. Toteuma näkyy osabudjetilla blank tasolla.

Mikäli yllä kuvattu rivi ohjataan pääbudjetille ja budjettia katsotaan monitorista, niin Helsingille kohdistuva 10 000€ myynti näkyy dimensionarvolla "blank", eli kohdistumaton/dimensioimaton. Muu myynti näkyy niillä dimensionarvoilla, mihin ne kohdistuvat (tehdas 1, tehdas 2 ja tehdas 3).

**Esimerkki 2: dimension lisääminen jälkikäteen käyttöön**

Yritys käy jälkikäteen lisäämässä edellä kuvatulle ennustebudjetille käyttöön toisenkin dimension, eli dimension "kaupunki". Osabudjetilla ei tapahdu muutoksia; rivillä näkyy edelleen 18 000€ myyntiä blank tasolla.

Pääbudjetin monitorissa aiemmin budjetilla esiintynyt 10 000€ myynti, joka oli dimensioimaton/kohdistamaton, kohdistuu nyt dimensionarvolle "Helsinki".

# Operative -rivityyppi

Mikäli osabudjetille luodaan rivi, joka on tyypiltään "operative", tarkoitetaan tällä riviä, mihin haetaan operatiivista dataa. Operatiivinen data voi olla esimerkiksi vaikkapa työntekijöiden työtunteja. Käyttämällä rivityyppiä "operative", saadaan rivistä automaattisesti päivittyvä.'

**Esimerkki: työtunnit**

Finazillaan on tuotu työntekijöiden työtunnit kausille 1-3 operatiivisena datana. Käyttäjä on luonut osabudjetin, jossa on rivi kullekin työntekijälle. Rivien taakse on tehty operatiivisen datan määrittelyt (datagroup, row data type sekä operatiivinen dimensio). Tunnit on budjetoitu vuodelle 2023. Forecast budjetille asetetaan real balance end date 31.3.2023, jolloin kausien 1-3 budjetoidut tunnit ylikirjoittuvat toteumalla ja kaudet 4-12 ovat edelleen budjetoidut tunnit.

Aikanaan kun Finazillaan tuodaan työntekijöiden tunnit kaudelle 4, ja real balance end date päivitetään 30.4.2023 päivälle, päivittyvät työtunnit jälleen automaattisesti osabudjetille.



artikkelin osoite on https://intercom.help/finazilla/fi/articles/7435750-automaattisesti-paivittyva-osabudjetti-osa-1-rivityypit-actual-ja-operative

