## Palkkojen budjetoinnista

Tämä artikkeli täydentää aikaisempia artikkeleitamme, joissa olemme käsitellet osabudjetteja ja budjetointia. Artikkelin ymmärtäminen edellyttää, että käyttäjä tuntee Finazillan budjetointityökalua jossain määrin sekä ymmärtää palkkojen laskennan. Artikkelin lopussa olemme havainnollistaneet lisäksi Finazillan taseen kirjausten logiikkaa palkkoihin liittyen. Artikkelin ymmärtämistä helpottaa siis myös taseen tunteminen.

# Palkkojen budjetoinnista

Iso osa asiakkaistamme päätyy budjetoimaan henkilöstökulut osabudjetin kautta. Finazillassa on valmiina osabudjetti nimeltä "henkilöstöbudjetti", millä pääsee hyvin alkuun budjetoinnissa. Valmista pohjaa voi muokata oman yrityksen tarpeisiin sopivaksi.

Osa yrityksistä haluaa budjetoida henkilöstökulut yhtenä eränä, kun taas joku toinen yritys haluaa budjetoida ihan henkilötasolla. Tässä esimerkissä rakennamme osabudjetin, jossa budjetoidaan kuukausipalkat yhtenä eränä ja tuntipalkat toisena eränä. Palkat viedään tiliohjauksin pääbudjetille.

# Budjetointi Finazillassa

Mennään budgets -toimintoihin ja haetaan haluttu yrityksen budjetti. Osabudjetit löytyvät "sub budgets" välilehden takaa. Valitaan Finazillan valmiiksi luoma osabudjetti nimeltä "henkilöstöbudjetti". Osabudjetti näyttää tältä:

[![](

[![](

*Kaikki osabudjetin rivit, joissa on rivin nimen edessä tähtisymboli (\*), kaipaavat tiliohjauksen taakseen. Tiliohjaus ohjaa kyseisen rivin saldot pääbudjetille kyseiselle tilille tulokseen tai taseeseen.*

Ensimmäisenä käydään tekemässä riveille tiliohjaukset kuntoon ja muutetaan rivin otsikoksi (työntekijä 1 tilalle) kuukausipalkkaiset. Sen jälkeen koko kuukausipalkkaiset rakenne kopioidaan. Kopioidulle rakenteelle annetaan nimeksi Tuntipalkkaiset. Tämän jälkeen osabudjetilla on kaksi identtistä rakennetta: kuukausipalkkaiset ja tuntipalkkaiset. Jos palkat on ohjattu kirjanpidossa eri tileille, korjataan tiliohjaukset tässä kohdin oikeaksi toisen ryhmän osalta.

Rakenne on nyt oheinen:

[![](

Kun tarvittava pohja on luotu, voidaan alkaa syöttämään varsinaisia lukuja. Ensimmäisenä syötetään lomapalkkavelan lähtösaldo. Esimerkin kuvassa on syötetty alkusaldoksi 15 000€ kaudelle 1/2024. Syöttö tehdään vihreälle input -riville. Finazilla juoksuttaa saldoa eteenpäin muille kausille.

[![](

Seuraavaksi syötetään palkkakulut kuukausipalkkaisille, sekä arvioidaan lomien pitämisajankohtaa. Kuvan esimerkissä kuukausipalkat ovat yhteensä 15 000€ joka kuukausi. Kuukausipalkkaiset pitävät kaikki talvilomaa (6 päivää) helmikuussa ja kesälomaa (24 päivää) heinäkuussa. Finazilla laskee palkkojen jaksotukset automaattisesti.

Mahdolliset luontoisedut syötetään niille varatulle riville, mikäli sellaisia on. Finazilla laskee sivukulut myös luontoiseduista.

Tässä kohdin tulee huomata, että kun budjetointia tehdään työntekijäryhmittäin, syötetään lomapäivien määrä ryhmätasolla eli 30 lomapäivää tarkoittaa koko palkansaajaryhmää.

[![](

Seuraavaksi syötetään tuntipalkkaisten tiedot. Tuntipalkkaisten palkkakulut ovat 22 000€ joka kuukausi. Tuntipalkkalaiset lomailevat vuoroissa; puolet pitää talvilomansa helmikuussa ja puolet maaliskuussa. Näin ollen lomapäiviin syötetään kummallekin kaudelle 3 päivää, eli puolet (yhteensä 6 päivää). Myös kesälomat pidetään vuoroissa; puolet pitää kesälomaa kesäkuussa ja puolet heinäkuussa, joten budjettiin syötetään kummallekin kaudelle 12 lomapäivää (yhteensä 24 päivää).

[![](

[![](

*Tuntipalkkaisten palkat voi laskea myös muokkaamalla pohjaa siten, että pohjassa on esimerkiksi tehdyt työtunnit ja tuntipalkka ja palkkasumma lasketaan kaavan kautta. Tuntipalkan voi tällöin toteuttaa halutessaan laskentavakion kautta.* 

Kun kaikki luvut on syötetty, Finazilla laskee siniset rivit automaattisesti ja siirtää ne rivit, joissa on tiliohjaus pääbudjettinäkymään. Lomapalkkavelka siirtyy taseeseen, jossa se näkyy oheisesti.

Lomapalkkavelkaan lasketaan taseeseen aina alkusaldo (esimerkissä manuaalisesti syötetty 15 000€) sekä kyseisen kauden uusi kertymä, joka on tässä esimerkissä kaudella 1/2024 kuukausipalkkaisten 2812,50€ sekä tuntipalkkaisten 4125€. Näiden summa (21 937,50€) siirtyy taseeseen (liabilities) lyhytaikaisiin velkoihin. Finazilla täsmäyttää taseen käyttämällä pankkitiliä lyhytaikaisten velkojen vastatilinä.

[![](

[![](

*Henkilöstöbudjetissa on oletuksena Finazillan luomat system -tasoiset laskentavakiot palkkojen sivukuluille. Käyttäjä voi halutessaan luoda omia Customer -tasoisia laskentavakioita ja käydä vaihtamassa ne henkilöstöbudjetille, sillä esimerkiksi tapaturmavakuutus on hyvin yrityskohtainen.* 

*Mahdolliset muutokset kannattaa tehdä ensimmäisenä, ennen kuin rakennetta kopioi. Näin korjaukset siirtyvät uusiin kopioihin kerralla.*

*Muista myös mahdollisuus toteumalukujen tuontiin osabudjetille*

# Lisätietoja

[Esimerkki: henkilöstöbudjetin vaikutukset taseeseen](



artikkelin osoite on https://intercom.help/finazilla/fi/articles/4560317-esimerkki-henkilostobudjetin-laatiminen-kuukausipalkkaisille-ja-tuntipalkkaisille

