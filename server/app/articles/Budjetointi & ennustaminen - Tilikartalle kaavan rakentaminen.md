## Tilikartalle kaavan rakentaminen

Tämä artikkeli on suunnattu edistyneemmille Finazilla käyttäjille, joilla on jo osaamista budjetin kaavojen luomiseen. Artikkelin ymmärtämisen edellytys on lisäksi se, että käyttäjä ymmärtää taseen toimintalogiikkaa.

Tässä artikkelissa neuvotaan, miten käyttäjä voi luoda tilikartalle kaavoja ja sen jälkeen hyödyntää tehtyjä kaavoja budjetoinnin puolella. Toiminto mahdollistaa mm. sellaisen, että myyntisaamiset voidaan laskettaa saman budjetin tuloslaskelmalta taseeseen ja saada saldot kumuloitumaan oikein. Toimintoa voidaan käyttää muidenkin kaavojen rakentamiseen; tässä neuvottu on vain yksi esimerkki.

# **Tilikartalle kaavan rakentaminen**

Yrityksen tilikartta/tilikartat löytyy company -valikosta kohdasta account schemes. Tilikartta saadaan auki sen nimeä klikkaamalla.

Tässä esimerkissä halutaan rakentaa kaava myyntisaamisiin, joten tilikartasta etsitään kyseinen rivi. Rivin asetukset saa auki rivin perässä olevasta edit -painikkeesta. Tämän jälkeen kerrotaan tilikartalle kaava, eli vaikkapa niin, että myyntisaamiset (tili 1700) generoidaan myyntien (tili 3000) perusteella. Kaavassa on huomioitava merkkisyysasiat, eli kun myyntisaamiset halutaan budjetille positiviisena saldona, pitää kaavassa on miinusmerkki. Valinta "add formula value to current value cumulatively" tarkoittaa, että arvoa kumuloidaan.

[![](

# **Budjetin luominen**

Seuraavaksi siirrytään luomaan budjetti ja budjetoidaan tuloslaskelman puoli halutulla tavalla. Tässä esimerkissä riittää, että tili 3000 on budjetoitu, sillä se on ainoa tili, mitä halutaan hyödyntää taseen luomisessa kaavojen kautta.

# **Taseen luominen tulosbudjetin perusteella**

Seuraavaksi mennään budjetilla vastaavaa -välilehdelle (assets). Nyt kun vastaavaa puolella oleva myyntisaamisten tili (1700) halutaan tehdä siten, että siinä hyödynnetään saman budjetin tilillä 3000 olevia lukuja sekä luotua kaavaa, hyödynnetään tässä ominaisuutta nimeltä toteumien tuonti.

Seuraavaksi toteumat voidaan tuoda pelkästään riville 1700 myyntisaamiset. Työkalu löytyy kyseisen rivin perästä kolmen pisteen takaa (nk. rivityökalut).

[![](

Seuraavaksi määritellään, että mistä toteumat tuodaan. Määrittelyssä on tärkeää, että datasource -kenttään kerrotaan se budjetti, missä ollaan. Luvut tuodaan siis taseeseen siitä samasta budjetista, missä myynnitkin on budjetoitu. Toiminto mahdollistaa lukujen tuomisen toki jostain muustakin budjetista.

Lisäksi on tärkeää valita import data transformation method -kohtaan valinta "account scheme default forecasting method". Tämä valinta nimenomaan määrittelee sen, että tuonnissa käytetään nyt taustalla tilikartalle rakennettua kaavaa.

[![](

Tämän jälkeen tilillä 1700 on laskentakaavan mukaiset myynnit, joissa hyödynnetään budjetoituja myyntejä tililtä 3000.

**Esimerkki 1:**

Myyntejä on budjetoitu tilille 3000 jokaiselle kuukaudelle 10 000€. Laskentakaavaan tilille 1700 on kerrottu, että sinne tuodaan aina 50% myynneistä. Näin ollen tammikuulla on myyntejä 5000€, helmikuulla 10 000€, maaliskuulla 15 000€ jne.

**Esimerkki 2:**

Myyntejä on budjetoitu tilille 3000 siten, että tammikuulla on 10 000€, helmikuulla on 5000€ ja maaliskuulla on 7000€. Laskentakaavaan tilille 1700 on kerrottu, että sinne tuodaan aina 50% myynneistä. Näin ollen tammikuulla on myyntiä 5000€, helmikuulla 7500€, maaliskuulla on 11 500€.

**Esimerkki 3**:

Myyntejä on budjetoitu tilille 1000€/kk. Myyntisaamisiin on syötetty jokaiselle kuukaudelle lähtöarvoksi 3000€. Laskentakaavaan tilille 1700 on kerrottu, että sinne tuodaan aina 50% myynneistä. Näin ollen tammikuulla on myyntiä 3500€, helmikuulla 4000€, maaliskuulla 4500€ jne.

Alkusaldon voi joko:

1. Tuoda importtaamalla käyttäen vaikkapa latest menetelmää siten että lähtödatan loppupäivä on siinä kuukaudessa mistä halutaan tuoda alkusaldot.
2. Tuomalla ne käyttäen budettia luodessa täppää "tuo alkusaldot"
3. Syöttämällä kyseiselle tilille käsin alkusaldon ennen importtia
[![](

Tilikartalle tallennetut metodit on kaikki suunniteltu siten, että niillä voi tuoda esimerkiksi 2019-2022 luvut 2023 vuoden budjetille.  
Tämä on sitä varten, että generointi on luotettavampi mitä pidemmän aikavälin datasta se suoritetaan.

# Helpoin tapa luoda tase tuloksen perusteella

Uutta budjettia luotaessa voidaan myös tehdä edellä kuvatut valinnat suoraan budget -näkymästä. Valinnat on kuvattu alla. Tämä valinta tekee ensin tuloslaskelman ja sen jälkeen taseen. Yllä kuvattu komponentti on tämän *taustalla* oleva toiminto.

[![](

[![](

Jos taseen "importtaamisen" jälkeen tekee muutoksia tuloslaskelman puolelle, ei muutokset ui taseeseen automaattisesti, vaan import pitää tehdä uudelleen.



artikkelin osoite on https://intercom.help/finazilla/fi/articles/7055202-esimerkki-taseen-tekeminen-tuloslaskelman-perusteella

