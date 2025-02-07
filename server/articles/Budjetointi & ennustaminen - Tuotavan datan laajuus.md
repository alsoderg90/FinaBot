## Tuotavan datan laajuus

[![](

*Versiopäivityksessä 20.10.2021 tuotu uudistus. Toiminto parantaa merkittävästi aikaisempaa toteumadatan tuomista budjetin pohjatiedoksi.* 

Budjetille on mahdollista tuoda pohjatiedoksi toteumadataa -kuten olemme aikaisemmassa artikkelissamme ["toteumadatan tuominen budjetille pohjatiedoksi](" kertoneet. Tässä artikkelissa kerromme käytännön esimerkkien kautta, miten eri tavoin toteumadataa voidaan tuoda budjetille.

# **Tuotavan datan laajuus**

* Yksittäiselle tilille
* Tiliryhmälle
* Kokonaiselle tiliosiolle
* Koko budjettiin kerralla
# **Datan sisällön rajaamisen mahdollisuudet**

* Valitulle dimensionarvolle tuominen
* Kaikki dimesionarvot dimensiotasoisesti eriteltynä
* Kaikki dimensionarvot yhteenlaskettuna
* Dimension arvolta toiselle tuominen /siirtäminen
# **Ominaisuudessa huomioitavaa**

* Ei tuo lukuja tileille, joissa on joko kaavoja tai tiliohjaus osabudjetilta
* Dimensiotasoisen toteuman tuominen koko budjettiin kerralla saattaa kestää hetken aikaa - varsinkin yrityksillä, joilla on paljon dimensioita tai dimension arvoja. Suurilla massoilla emme suosittele toimintoa käytettävän kuvatusti
* Toiminnolla mahdollistetaan lukujen tuonti massana myös sellaisiin aika- ja dimensioulottuvuuksiin, joilla on jo mahdollisesti jotain budjetoituja lukuja
* Rajatun roolin käyttäjä voi tuoda vain roolinsa rajoissa toteumaa

**Esimerkki 1:**

Yritys on luonut budjetin tilikaudelle 2024. Budjettiin halutaan tuoda edellisen tilikauden (tilikausi 2023) toteumat pohjatiedoksi. Toteumat halutaan tuoda kaikki dimensionarvot yhteenlaskettuna. Yritys ei siis budjetoi dimensioille. Toteumat halutaan tuoda kerralla koko profit and loss -näkymään (eli kaikille tuloslaskelman tileille kerralla).

Toteumien tuonti tehdään yläosan palkista painikkeen "import budget or actuals" takaa.

[![](

Seuraavaksi valitaan mistä aikajaksosta dataa tuodaan ja minne. Valinnat tehdään kohdasta from ja to. Import mode -valintaan ei tarvitse tässä kohdin koskea.

Datasource kohtaan valitaan yrityksen alle (esimerkissä yritys on nimeltään T-Company) valinta multiple targets ja jälkimmäinen kenttä jätetään tyhjäksi. Tämä valinta tarkoittaa, että kaikki luvut tuodaan budjetille ja ne esitetään budjetilla dimensioimattomana.

[![](

**Esimerkki 2:**

Yritys on luonut budjetin tilikaudelle 2024. Budjettiin halutaan tuoda edellisen tilikauden (tilikausi 2023) toteumat pohjatiedoksi. Toteumat halutaan tuoda käyttämällä samoja dimensiokohdistuksia, kuin mihin toteumat ovat kohdistuneet. Yrityksen budjetointia tehdään dimensioittain. Toteumat halutaan tuoda kerralla koko profit and loss -näkymään (eli kaikille tuloslaskelman tileille kerralla).

Toteumien tuonti tehdään yläosan palkista painikkeen "import budget or actuals" takaa.

[![](

Jälleen tehdään ajanjaksojen valinnat sekä kerrotaan, miten dimensiot halutaan tuotavan.

[![](

**Esimerkki 3:**

Yritys on luonut budjetin tilikaudelle 2024. Budjettiin halutaan tuoda edellisen tilikauden (tilikausi 2023) toteumat pohjatiedoksi vain tiliryhmälle "liikevaihto". Toteumat halutaan tuoda lisäksi vain yrityksen dimensionarvolle "hallinto" siten, että toteumat tuodaan vain kausilta 1-9/2023 kausille 1-9/2024.

Tässä tapauksessa kun toteumaa halutaan tuoda vain tietylle dimension arvolle, tulee ensimmäisenä valita budjetin oikeaan yläkulmaan kyseinen dimension arvo.

[![](

Tässä esimerkissä halutaan lisäksi toteumaa tuoda vain tietylle osiolle budjetista, joten tehdään toteuman tuominen kyseisen rivin rivityökaluista eikä yläosan painikkeesta.

[![](

Seuraavaksi valitaan jälleen aikajaksot mistä tuodaan ja minne tuodaan. Esimerkissä haluttiin tuoda vain 9 kuukauden jaksolta toteumaa, joten aikaväli on kummassakin kohdassa 9 kuukauden mittainen. Valinta current dimension target viittaa siihen, että tuodaan vain dimensioarvon "hallinto" toteumat. Hallinto -dimension arvo kiinnittyy myös automaattisesti oikeaan reunaan kohtaan datasource-.

[![](

[![](

Rajatun roolin käyttäjälle (mikäli oikeuksia dimensioihin on rajoitettu) toteumien tuonti on mahdollista vain yksi dimensiovalue kerrallaan ja vain niille dimension arvoille, mihin käyttäjällä on oikeus

Tuotava data ylikirjoittaa aina kaikki budjetilla olevat luvut, joten kehoitamme huolellisuuteen toteumaa tuotaessa



artikkelin osoite on https://intercom.help/finazilla/fi/articles/5660268-esimerkki-tuodaan-toteumaa-budjetille-pohjatiedoksi

