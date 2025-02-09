## Import actuals from accounting lock date to balance sheet

Tuotu ominaisuus on osa laajempaa kokonaisuutta. Tässä artikkelissa esitelty ominaisuus on osa 3, joka keskittyy siihen, kuinka osissa 1 ja 2 tuotuja ominaisuuksia voidaan hyödyntää mm. siihen, että taseeseen saadaan tuotua lähtösaldoksi lukituspäivän tiedot. Lisäksi toimintoja voidaan hyödyntää mm. siihen, että tuloslaskelman perusteella tehdään tasebudjetti.

Toimintoon liittyy myös seuraavat ominaisuudet:

[Budjetin generointimenetelmä, osa 1: asetusten laittaminen tilikartalle](

[Budjetin generointimenetelmä, osa 2: toteumien tuonti](

Kun käyttäjä luo uutta budjettia Finazillassa, on näkyvillä uusi valikko nimeltä "Generate Initial Values".

[![](

# **Import actuals from accounting lock date to balance sheet**

Kyseinen valinta tarkoittaa käytännössä sitä, että luotavan uuden budjetin taseeseen voidaan generoida automaattisesti lukituspäivän mukaiset saldot. Generointi tehdään koko taseeseen *yritystasoisesti.* Taseen lukuja ei siis kohdisteta dimensioille.

Jos esimerkiksi yrityksen A lukituspäivä (lock date) on 28.2.2023 ja taseen pysyvät vastaavat on tuolloin 6 172 060,00€ tuo Finazilla tämän saldon automaattisesti budjetin jokaiselle kuukaudelle. Jos budjetti on siis luotu vuodelle 2024, on kausilla 1-12/2024 pysyvät vastaavat 6 172 060,00€

[![](

Tuonti tapahtuu yllä olevassa esimerkissä tilitasoisesti sen mukaan, millä tileillä on kirjanpidossakin ollut tapahtumia lukituskuukaudella. Toiminnosta on hyvä tiedostaa se, että lukituspäivän muuttaminen sen jälkeen kun budjetille on generoitu taseen luvut, ei vaikuta mitenkään jo luotuun budjettiin. Luvut eivät siis päivity budjetille lukituspäivän kautta jälkikäteen.

[![](

*Import actuals from accounting lock date to balance sheet -toiminto ei ole suoraan kytköksissä tilikartta-asetuksiin, eli sitä voi hyvin käyttää hyödykseen, vaikka ei olisi tehnyt tilikartalle mitään asetuksia*

# **Generate initial values from actuals using accountscheme defaults**

Jälkimmäinen vaihtoehto nojaa osissa 1 ja 2 kuvattuun toimintamalliin, jossa tilikartalle on tehty generointimenelmävalintoja - ja näitä valintoja halutaan käyttää budjetin luomisessa hyödyksi.

Toiminto käyttää hyödykseen yrityksen lukituspäivää, ja hakee toteumaluvut 12 kuukautta ennen lukituspäivää. Kuukausien määrää voi itse säätää oikean reunan "months of source data" kentän kautta. Oletuksena kentässä on 12 kuukautta.

Month of source data kohdasta on hyvä ymmärtää, että mitä isompi luku kenttään laitetaan, sen parempi tämä on ennustettavuuden kannalta (pitkän ajan trendi). Minimi on nolla ja maksimi on 48. Toiminto on parhaimmillaan yrityksissä, missä toiminta on kohtuullisen stabiilia.

[![](

[![](

*Toimintoa voi käyttää myös siten, että sen avulla generoidaan ensin tuloslaskelma, johon tehdään halutut muutokset. Tämän jälkeen voidaan generoida tase aikaisemmin generoidun tuloslaskelman pohjalta (import budjetista).* 

*Tämän voi tehdä myös kerralla alla olevin valinnoin, jolloin budjetille syntyy tuloslaskelma annettujen menetelmien mukaan, tilikauden voitto/tappio lasketaan tulosbudjetille alimmaksi ja siirretään taseeseen omaan pääomaan ja pankkivaroihin. Muut taseen erät generoidaan lukituspäivän saldojen mukaisesti.* 

[![](



artikkelin osoite on https://intercom.help/finazilla/fi/articles/7206978-budjetin-generointimenetelma-osa-3-budjetin-luominen-esivalinnoilla

