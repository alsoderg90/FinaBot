## Pohjatiedot

Tämä artikkeli on kirjoitettu auttamaan hahmottamaan Finazillan roolien luomista. Tämä artikkeli täydentää aikaisempia artikkeleitamme ja artikkelin ymmärtämistä auttaa, jos käyttäjä tietää jo mitä roolit ovat ja ymmärtää jotain erilaisten roolien luomisesta.

# Pohjatiedot

Käyttäjälle "John Smith" halutaan antaa oikeudet yrityksen "Movies Ltd" toteumadatan, budjettidatan ja ennustedatan katseluun. Oikeus halutaan kuitenkin rajata siten, että hän näkee vain dimension "USA" arvot. Yrityksellä on dimension "Country" alla muitakin dimensioita, kuten alla olevasta kuvasta käy ilmi.

[![](

Tämän lisäksi käyttäjälle "John Smith" halutaan antaa oikeus budjetoida yrityksen osabudjetille nimeltä "Sales Budget".

# Roolin luominen

Aloitetaan luomalla käyttäjälle rooli. Roolin nimeksi tulee tässä esimerkissä "Sales Manager". Luodaan roolille halutut oikeudet. Usein helpointa on valita ensin kaikki mahdolliset oikeudet kaikkialle ja sen jälkeen lähteä poistamaan / rajamaan yksitellen oikeuksia.

## Roolille tulevat automaattiset oikeudet

Uusi rooli saa aina automaattisesti oikeudet tileihin, tilikausiin, tilikarttamalleihin, laskentavakioihin ja vyörytyssääntöihin sekä lukuoikeuden tilikarttaan ja vyörytyssääntöihin. Näitä ei tarvitse valita, vaan oikeudet tulevat aina automaattisesti jokaiselle uudelle roolille.

[![](

# Oikeuksien rajaaminen

*Accounting periods* tarkoittaa yrityksen tilikausia. Kaikki käyttäjät saavat aina oletusarvoisesti lukuoikeuden yrityksen tilikausiin, sillä tilikaudet ovat keskeinen tekijä sekä budjetoinnissa, että raportoinnissa. Ilman tilikausien lukuoikeutta käyttäjä ei voisi katsoa raportteja eikä budjetoida. Tilikausien editointi -oikeus mahdollistaa mm. lukituspäivän muokkaamisen

*Account Schemes* tarkoittaa tilikarttaa. Käyttäjän tulee saada lukuoikeus ko. toimintoon, jotta hän voi katsella raportteja, sillä tilikartta toimii raporteilla taustatietona. Muut oikeudet voi rajata pois.

Seuraavana on kohta "*All sub budgets*", joka voidaan poistaa kokonaan. Roolille ei haluta antaa kollektiivisia oikeuksia kaikkiin yrityksen osabudjetteihin, vaan hänelle halutaan antaa oikeus vain yhteen osabudjettiin (ja tämä tehdään erikseen myöhemmin eri kohdassa). Poistetaan "all subgets" kokonaan.

Seuraava kohta on "*budgets*". Valikon alta löytyy kaikki yrityksen budjetit sekä niiden alla olevat osabudjetit. Tällä toiminnolla voidaan rajata siis hyvin tarkasti vain tietyt budjetit ja/tai osabudjetit, mihin roolilla on oikeus.

Yrityksen "Movies Ltd" alla on lukuisia budjetteja. Roolille halutaan antaa kuitenkin ainoastaan budjettiin nimeltä "221-100 Budjetti" pelkkä lukuoikeus ja kyseisen budjetin alla olevaan osabudjettiin nimeltä "Sales budget" sekä luku- että muokkausoikeus.

Nyt ko. käyttäjä näkee kokonaisuudessaan budjetin 221-100, mutta ei pysty muokkaamaan sitä, eikä poistamaan sitä. Vastaavasti taas osabudjettiin "Sales budget" käyttäjä pystyy tekemään myös muutoksia - eli budjetoimaan. Koska käyttäjällä on sekä edit, että input -oikeus, pystyy käyttäjä myös halutessaan muokkaamaan osabudjetin rakenteita (mm. tilikiinnitykset, rivien lisääminen/poistaminen jne).

Jos käyttäjälle olisi haluttu antaa osabudjettiin pelkkä budjetointioikeus, olisi input -oikeus ollut riittävä. Tällöin käyttäjä ei pysty muokkaamaan rakenteita, mutta pystyy budjetoimaan.

[![](

*Cash flow* tarkoittaa kassavirtaa. Koska käyttäjällä ei ole tarvetta nähdä kassavirtaa, voidaan tämä poistaa kokonaan.

Seuraavaksi on kohta "*dimensions*" ja tämä on nyt kohta, missä käyttäjän näkyvyyttä dataan rajataan. Rajaus vaikuttaa siis kaikkeen aikaisemmin valittuun. Dimensions valikon alla on kaiki yrityksen dimensiot, ja näitä voidaan rajata yksitellen halutulla tavalla.

Dimensioissa esiintyvä blank tarkoittaa dataa, joka on dimensioimatonta eli ns. yritystasoista dataa. Tähän voidaan antaa erikseen oikeudet näin haluttaessa.

[![](

*Reporting groups* tarkoittaa raportointiryhmiä. Raportointiryhmillä dimensioita voidaan niputtaa yhteen ja raportoida yhtenä. Käyttäjälle halutaan antaa oikeus lukea ja luoda raportointiryhmiä.

*Report Schemes* liittyy raporttimalleihin, jotka ovat raportoinnin perusta. Siksi käyttäjälle tulee antaa oikeus lukea raporttimalleja. Muut oikeudet häneltä voi poistaa.

*Reporting tags* liittyy raporttien tageihin. Käyttäjälle halutaan antaa oikeus lukea ja luoda tageja.

*Rolling rule templates* liittyy vyörytyssääntöihin. Nämä oikeudet jätetään roolille.

*Role Management* liittyy roolien hallintaan. Tämän voi poistaa kokonaan kyseiseltä roolilta, koska hänen ei tarvitse päästä käsittelemään roooleja.

Lopuksi listassa on vielä *User Management*, joka liittyy käyttöoikeuksiin ja *Vouchers*, joka liittyy tositteisiin. Molemmat oikeudet voidaan poistaa ko. käyttäjältä kokonaan. Käyttäjän ei tarvitse käsitellä käyttäjätunnuksia eikä tositteita.

Roolin oikeudet näyttävät nyt oheiselta:

[![](

# Mitä ko. roolilla nyt näkee ja pystyy tekemään?

Roolilla pystyy tarkastelemaan kaikkia hänelle jaettuja raportteja. Raportteihin nousee ainoastaan dimension "USA" luvut. Hän pystyy myös muodostamaan itse raportteja aivan kuten kaikki muutkin käyttäjät - mutta hänelle nousee raportteihin ainoastaan dimension "USA" luvut.

Jos lukuja on kohdistettu usealle dimensiolle, kuten vaikkapa yhdistelmälle "USA" sekä "Sweden", ei käyttäjä näe näitä lukuja. Jos tällaisten lukujen halutaan näkyvän hänelle, tulee hänelle antaa oikeus myös dimensioon "Sweden".

Käyttäjä pystyy myös katselemaan yrityksen budjettia 221-100; tässäkin hänelle näkyy vain dimension "USA" luvut. Käyttäjä pystyy lisäksi budjetoimaan osabudjetille "Sales budget". Budjetoidessa hän pystyy budjetoimaan vain dimensiolle "USA". Käyttäjä pystyy tarvittaessa myös muokkaamaan "sales budget" osabudjetin rakenteita.

[![](

*Budjetti -näkymässä käyttäjälle, jolla on rajattu oikeuksia dimensioihin, aukeaa ns. "tyhjä" budjetti -näkymä. Budjetin rivit tulevat näkyviin kun käyttäjä valitsee jonkin dimension oikeaan yläkulmaan, mihin hänelle on oikeudet.*

System tasoisesta Finazillan tuottamasta dashboardista tällaiselle käyttäjälle ei näy mitään, koska data näihin haetaan kaikkien dimensioarvojen summana. käyttäjälle näiden dashboardien raportit näkyy näin:

[![](

# Lisätietoja

[Mikä merkitys eri rooleilla on Finazillassa?](

[Roolien kautta määritellään yritystasoisen käyttäjän käyttöoikeudet Finazillassa](



artikkelin osoite on https://intercom.help/finazilla/fi/articles/4476547-esimerkki-roolin-luominen-annetaan-kayttajalle-oikeudet-vain-yhteen-dimensioon

