## Raportin lukujen muokkaus

Versiopäivityksessä 10.4.2024 tuotu kokonaan uusi toiminto. Toiminto mahdollistaa suoraan raportilla lukujen muokkaamisen.

Finazillan raportoinnissa on mahdollista raportoida joko toteumadataa (actuals), budjettidataa (budget) tai jotakin laskennallista dataa (formula). Toteumadataa raportoitaessa käyttäjien ei ole ollut mahdollista vaikuttaa mitenkään ketterästi raportoitaviin lukuihin. Budjetin kautta raportoitaviin lukuihin muutos on pitänyt tehdä budjetille - jonka jälkeen muutos on uinut raporttiin.

Jatkossa käyttäjät voivat muokata raporttien lukuja suoraan raportin kautta. Toimintoa voidaan käyttää esimerkiksi nopeisiin mallinnuksiin, joissa halutaan nähdä miltä raportin luvut näyttävät, jos vaikkapa liikevaihto muuttuu.

Raportin kautta lukujen muokkausta voidaan tehdä yksittäisiin soluihin, laajempiin alueisiin (maalaamalla haluttu alue), operatiivisen datan raportteihin (amount ja quantity), sekä taseraportteihin. Taseen osalta tulee huomioida, että mikäli käyttäjä muokkaa vaikkapa pankkitilin saldoa, ei Finazilla tee automaattisesti taseen toiselle puolelle kirjausta. Yksipuolisen muokkauksen seurauksena tase ei mene siis tasan. Käyttäjän tulee tehdä muokkaus taseen molemmille puolille, jotta tase menee tasan.

# Raportin lukujen muokkaus

Kun käyttäjällä on auki Finazilla -raportti, voidaan yksittäisen solun lukua muokata painamalla halutussa solussa (kuvan esimerkissä tili 3000 ja kausi 2023/01) hiiren oikeaa painiketta. Painikkeen kautta aukeaa vaihtoehto "add value".

[![](

## Prosentuaalinen muokkaus

Lukujen muokkaamista voidaan tehdä joko numeerisesti (number) tai prosentuaalisesti (percentage). Numeerista muokkaamista olemme kuvanneet ohjeessamme [täällä](

Value type määrittelee, kummasta tavasta on kyse. Kun value type kenttään on valittuna prosentuaalinen vaihtoehto, syötetään haluttu muokkaus "percentage" kenttään. Huomaa, että percentage -kenttään voi syöttää vain kokonaisia prosentteja. Desimaaleja ei toistaiseksi voi käyttää. Description -kenttään voidaan kirjoittaa tapahtumalle haluttu kuvaus. Submit -painike tekee muutoksen raporttiin.

[![](

*Dimension Values kenttä näkyy vain, jos raportti on luotu dimension/column valinnalla. Yritystasoisissa raporteissa kenttää ei näy.* 

[![](

Kun käyttäjä on tehnyt raporttiin jonkin muutoksen, näytetään muokattu solu violetilla pohjavärillä. Lisäksi raportin yläkulmaan raportin nimen perään ilmestyy painike "re-calculate report". Painikkeen avulla raportti "lasketaan" uusiksi ja muutos ilmestyy raporttiin.

[![](

# Raportin näkyminen muokkauksen jälkeen

Kun raportti on lasketettu uudelleen, päivittyy kyseisen solun arvo. Samalla päivitetään myös kaikki muut tiliryhmät, joihin muutos vaikuttaa. Kaikki kohdat raportissa, joihin muutos vaikuttaa, esitetään harmaalla pohjavärillä.

[![](

Koska aiemmassa esimerkissä tehtiin muutos tilin 3000 lukuun kaudella 2023/01, vaikuttaa tehty muutos useaan tiliryhmään / otsikkoon raportissa. Muutos vaikuttaa liikevaihdon lisäksi bruttotulokseen, liikevoitto/tappio summaan sekä tulokseen ennen tilinpäätössiirtoja ja veroja ja tilikauden voitto/tappio riviin. Tästä syystä jokainen näistä otsikoista esitetään harmaalla pohjavärillä.

Muutos tehtiin pelkästään kauden 2023/01 lukuihin, mistä syystä väritystä ei ole muilla kausilla. Muutos koskettaa myös raportin ensimmäistä saraketta, joka laskee tilikauden luvut yhteensä. Tästä syystä väritys esitetään myös siinä sarakkeessa.

[![](

[![](

*Jos raporttimallilla on kaavarivejä, niin kaavariveihin väritys on ulotu. Jos esimerkiksi tilikauden voitto/tappio rivi olisi toteutettu kaavana, eikä tilivälein, ei rivillä olisi harmaata pohjaväriä.* 

## Tositeporautuminen muokkauksen jälkeen

Raportilta voidaan porautua halutun solun tositteisiin. Tositeporautuminen tehdään tuplaklikkaamalla haluttua solua (esimerkiksi tili 3000, kausi 01/2023). Porautuminen aukaisee käyttäjälle tositelistauksen, missä näkyy jokainen solun tosite tietoineen. Käsin lisätyt tositteet näkyvät listauksessa myös.

Porautumisessa on hyvä huomata, että käsin tehty 5% lisäys näyttää lisäyksen euroina, sillä prosentin syöttäminen on vain ns. aputyökalu eurojen laskentaan. Mikäli käyttäjä ei ole kirjoittanut mihinkään selitteeseen, että paljonko prosentuaalisesti on muokattu, ei tätä näe mistään jälkikäteen.

[![](

[![](

*Ainoastaan raportin omistaja pystyy muokkaamaan raporttia. Muokkaus on myöskin estetty Customer tasoisilta raporteilta.* 

*Erikoisempia aikajaksoa käyttävien raporttien (mm. Kvartaali ja Tertiili) tapauksessa solua muokatessa, laitetaan muokkaukset ajanjakson viimeiselle kuukaudelle. Tämä esiintyy käyttäjille vain tilanteissa, missä vaihdellaan raportin päivämäärän esitystapaa*

## Operatiivisten raporttien muokkaaminen

Tässä artikkelissa kuvattu raportin lukujen muokkaaminen koskettaa myös operatiivisen datan raportteja ja toimii samalla tavalla kuin perinteinen talousraporttikin.

Operatiivisessa datassa on kaksi "määrettä"; amount ja quantity. Amount tarkoittaa euromäärää ja quantity vastaavasti mitä tahansa muuta määrettä (tunteja, senttejä, millejä, kiloja, kappaleita, tunteja jne). Raportin lukujen muokkaaminen ulottuu kumpaankin määreeseen, eli käyttäjä voi muokata kumpaa tahansa vaihtoehtoa.

Operatiivisen datan raporteissa muokkaamisen yhteydessä tulee valita data type (amount tai quantity) sekä datagroup, mitä muokataan. Finazilla osaa valita data type valinnan rivin perusteella.

[![](

# Muokkausten katsominen, muokkaaminen ja poistaminen

Raporteilla, jotka sisältävät muokattua dataa, on oikeassa yläkulmassa yksi lisäpainike nimeltä "edits". Edits -näkymästä päästään tarkastelemaan kaikkia kyseisen raportin muokkauksia.

[![](

## Muokkausten poistaminen

Edits -näkymä aukeaa siten, että kaikki raportin muokkaukset näkyvät yhdessä näkymässä. Näkymästä voidaan poistaa haluttu muokkaus delete -painikkeella tai käyttää delete all -painiketta, joka poistaa kerralla kaikki tehdyt muokkaukset.

[![](

## Muokkausten editointi

Tässä artikkelissa tehtiin muokkaus siten, että kaudelle 1/2023 syötettiin tilille 3000 lisää myyntiä 5%. Raportin oikean yläkulman edits -painikkeella muokkaus saadaan näkyviin. Muokkauksen perässä olevalla "edit" painikkeella syötettyä muokkausta päästään uudelleen muokkaamaan.

[![](

Editin kautta aukeaa ikkuna, jossa tehtyä muokkausta voidaan muuttaa. Näkymässä voidaan vaihtaa summaa, kuvausta, tiliä mihin muokkaus kohdistuu, dimensio kohdistusta (mikäli raporttia on dimensiotasoinen) ja päiväystä.

[![](

[![](

*Uudelleen muokkausta ei voi tehdä prosenteissa, vaan se tulee tehdä jatkossa euroissa. Mikäli lukua halutaan muokata prosentteina, on järkevintä poistaa kokonaan aiempi muokkaus ja tehdä kokonaan uusi muokkaus uuden prosentin mukaisesti.* 

Mikäli edit -näkymässä tehdään muutoksia, ilmoittaa raportti käyttäjälle, että raportti tulee uudelleen laskettaa, jotta muutokset päivittyvät.

[![](

# Massamuokkaus

Raportin solujen summia voidaan muokata myös massana maalaamalla jokin isompi alue kerralla ja tekemällä muokkaus kerralla koko maalattuun alueeseen. Jos käyttäjä esimerkiksi maalaa kaudet 1-5/2023 tilin 3000 osalta ja muokkaa lukuja syöttämällä 10%, lisätään kullekin kaudelle sama 10% lisäys lähtösaldoon.

[![](

*Muokkaukset koskettavat vain ainoastaan sitä raporttia, mihin muokkaus on tehty. Muokkaus on siis raporttikohtainen*



artikkelin osoite on https://intercom.help/finazilla/fi/articles/9076165-raportin-lukujen-muokkaaminen-suoraan-raportilla-osa-2-prosentuaalinen-muokkaus

