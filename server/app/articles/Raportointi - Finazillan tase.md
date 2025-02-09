## Finazillan tase

[![](

*Versiopäivityksessä 30.11.2024 tuotu muutos, joka mahdollistaa muutoksen valitsemisen massatoimintona raporttimallille*

# Finazillan tase

Finazillan tase on aina lähtökohtaisesti kumulatiivinen ja raportoi kunkin kuukauden loppusaldoa - ei muutosta. Joskus voi olla kuitenkin tarvetta tarkastella tasetta nimenomaan muutoksen näkökulmasta. Tämä vaatii Finazillassa uuden raporttimallin luomisen.

Alkuun heti vinkki; raporttimalli kannattaa tehdä Customer tasolle jos sitä halutaan käyttää kaikille asiakkuuden yrityksille joko nyt tai kenties tulevaisuudessa. Company tasolle tehty raporttimalli on käytettävissä nimittäin vain kyseiselle yritykselle.

Muutossaldoinen raporttimalli voidaan tehdä kahdella tavoin. Kuvaamme kummankin vaihtoehdon alla.

# Vaihtoehto 1: massatoiminnon avulla muutossaldoisen raporttimallin tekeminen

Massatoiminnon hyödyntäminen on paras vaihtoehto tilanteissa, missä halutaan tehdä esimerkiksi koko tilikarttaan perustuvasta taseesta muutossaldoinen. Tällöin raportilla on paljon dataa ja massatyökalulla saadaan raporttimalli tehtyä kerralla. Toiminto on uusi ja se on tuotu päivityksessä 30.11.2024.

Uusi raporttimalli luodaan report scheme valikossa valitsemalla new report scheme. Raporttimalli luodaan käyttämällä tilikarttaa, eli valinta from template tulee olla account scheme template. Account group type valinta balance tarkoittaa tasetta. Viimeinen valinta balance type change tarkoittaa, että taseraporttimallista tehdään nimenomaan muutossaldoinen, eikä kumulatiivinen. Create report scheme -painike tekee raporttimallin. Huomaa, että raporttimallille tulee antaa nimi.

[![](

Tämän jälkeen raporttimalli ilmestyy report scheme listaukseen, josta sitä voidaan muokata tai siirtyä suoraan raportointiin raportoimaan mallilla.

# Vaihtoehto 2: tilivälikohtaisesti asetuksen muuttaminen

Uuden raporttimallin voi luoda kokonaan tyhjästä tai jos valmiina on hyvä tasemalli millä raportoidaan, niin tästä voidaan ottaa kopio ja säästää näin ylimääräistä aikaa ja vaivaa. Kopion voi nimetä esimerkiksi ”tase muutos kuukausittain” tai muulla halutulla kuvaavalla nimellä.

Tämän jälkeen tulee käydä muuttamassa kyseisen raportin asetuksissa balance type valinta siten, että raportoidaan muutosta eikä loppusaldoa. Täppä vaihdetaan siis kohtaan ”change”. Tämä muutos pitää tehdä raporttimallin kaikille riveille yksitellen, koska muutoin tase raportoi loppusaldoa.

Raporttimallit löytyvät Customer -valikosta kohdasta Report Schemes. Raporttimallin saa kopioitua nimen perässä olevasta "Copy" painikkeesta. Itse raporttimalli aukeaa raporttimallin nimeä painamalla. Muutos tehdään nimenomaan sille riville, missä on tiliväli mikä raporttiin tulee.

[![](

Muokkaustilassa aukeaa näkymä kyseisen raporttimallin asetuksista. Asetuksissa tulee käydä muuttamassa "Balance Type" kohtaan vaihtoehto "Change". Muutos tallennetaan "Update Balance Data Row" painikkeella.

[![](



artikkelin osoite on https://intercom.help/finazilla/fi/articles/4131115-taseraportti-raportoimaan-muutosta-per-kuukausi-kumulatiivisen-sijasta

