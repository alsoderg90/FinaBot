## Alkuperäinen henkilöstöbudjetti

Artikkelin ymmärtämistä helpottaa, jos käyttäjä tuntee ja tietää jo, mitä osabudjetit ovat Finazillassa ja kuinka niitä voidaan käyttää budjetoinnissa apuna. Lisäksi auttaa, jos käyttäjä tuntee jo Finazillan henkilöstöbudjetin logiikan.

Tässä artikkelissa opastamme, miten henkilöstöbudjetti -nimistä osabudjettia muokataan siten, että lomarahat maksetaan kerran vuodessa, eikä silloin, kun työntekijä on lomalla. Sama muokkaus pätee myös tapauksissa, missä lomaraha maksetaan kahdesti vuodessa tiettyinä kuukausina. Muokkauksella on merkitystä kassavirtaan.

# Alkuperäinen henkilöstöbudjetti

Alla on esimerkki siitä, miltä henkilöstöbudjetti näyttää alkuperäisesti, ilman tiliohjauksia.

[![](

# 

[![](

*Kaikki osabudjetin rivit, joissa on rivin nimen edessä tähtisymboli (\*), kaipaavat tiliohjauksen taakseen. Tiliohjaus ohjaa kyseisen rivin saldot pääbudjetille kyseiselle tilille tulokseen tai taseeseen.*

# Valmiiseen osabudjettiin tehtävät muutokset

Valmis osabudjetti on rakennettu siten, että kun osabudjettiin syötetään pidettäviä lomapäiviä, laskee Finazilla automaattisesti kyseiselle kuukaudelle loma-ajan palkan sekä lomarahan. Oletus on siis, että kun työntekijä lomailee, maksetaan hänelle mahdollinen normaali työajanpalkka (niiltä osin kuin työntekijä on kaudella töissä) + loma-ajan palkka sekä lomaraha.

Silloin kun lomaraha maksetaankin tiettynä kuukautena (tai kuukausina) huolimatta siitä, milloin varsinainen loma pidetään, tulee osabudjettia muokata. Osabudjettiin tulee lisätä yksi uusi rivi, jonka nimi voi olla vaikka "maksettavat lomarahapäivät". Rivi on tyypiltään syöttörivi (input). Rivin voi sijoittaa osabudjetilla esimerkiksi pidettävien lomapäivien syöttörivin jälkeen.

Seuraavaksi osabudjetilla olevaa "lomarahat" riviä tulee käydä muuttamassa kaavan osalta. Alkuperäisessä osabudjetissa kaava on "loma-ajan palkka \*0,5". Kaavaa tulee muuttaa siten, että kaava lasketaan varsinaisesta palkasta johtaen ja hyödynnetään kaavassa luotua "maksettavat lomarahapäivät" riviä. Alla on esimerkki kaavasta.

[![](

# Esimerkki uuden osabudjetin käyttämisestä

Kun muokkaukset on tehty osabudjettipohjaan, voidaan osabudjettia käyttää palkkojen budjetointiin.

Havainnollistamme asiaa vielä yhdellä esimerkillä. Budjetoidaan yhden henkilön palkka siten, että työntekijän kuukausipalkka on 3 500€ kuukaudessa. Työntekijällä on täydet lomat (30 päivää), joista talviloman (6 päivää) hän pitää helmikuussa ja kesäloman (24 päivää) heinäkuussa. Pidettävät lomapäivät syötetään normaalisti riville "Lomat: Pidettävät lomapäivät".

Yrityksen lomarahat on sovittu maksettavaksi kahdesti vuodessa. Talviloman osalta lomaraha maksetaan kaikille tammikuussa ja kesäloman osalta kesäkuussa. Syötetään maksettavat päivät osabudjettiin luodulle riville "maksettavat lomarahapäivät".

Finazilla laskee nyt automaattisesti kyseiselle henkilölle talvilomakaudelle normaalin työajan palkan työssäolon ajalta, loma-ajan palkan loman osalta mutta lomarahan Finazilla laskee tammikuulle; huolimatta siitä, että työntekijä lomailee vasta helmikuussa. Sama logiikka pätee myös kesäloman osalta.

[![](

Jos lomarahat maksettaisiin yrityksessä kerran vuodessa, vaikkapa joulukuussa, syötettäisiin maksettavat päivät (30 päivää) osabudjettiin luodulle riville "maksettavat lomarahapäivät".

# Osabudjettiin tehtävät muutokset tiivistetysti

* Tehdään tilikiinnitykset kaikille \* symbolin riveille
* Lisätään osabudjetille yksi uusi syöttörivi (input) nimeltä maksettavat lomarahapäivät
* Syötetään yllä mainitulle riville maksettavat päivät sille kuukaudelle, tai kuukausille, milloin lomarahat maksetaan
* Muutetaan osabudjetilla olevaa "lomarahat "riviä kaavan osalta. Vanha kaava on loma-ajan palkka \*0,5. Tämän tilalle tehdään kaava (esim. kuukausipalkka /25 \*0,5\*maksettavat lomapäivät). Kaavassa käytetään siis varsinaista palkkaa eikä loma-ajan palkkaa.
# Lisätietoja

[Osabudjetit osana yrityksen budjetointiprosessia](

[Esimerkki: henkilöstöbudjetin laatiminen kuukausipalkkaisille ja tuntipalkkaisille](



artikkelin osoite on https://intercom.help/finazilla/fi/articles/4648039-esimerkki-henkilostobudjetin-muokkaaminen-kun-lomarahat-maksetaan-kaikille-tiettyna-kuukautena

