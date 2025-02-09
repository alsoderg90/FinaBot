## Asiakastasoisen raportin luominen

Tässä artikkelissa neuvomme asiakastasoisen raportin luomista yhden esimerkin avulla. Tämä artikkeli koskettaa vain asiakkuuksia, joissa on enemmän kuin yksi yritys.

Artikkelin ymmärtämisen edellytys on, että käyttäjä osaa jo luoda tavanomaisia raportteja ja pivotoida niitä. Aiheesta voi lukea lisää kokoelmasta "Raportointi".

# **Asiakastasoisen raportin luominen**

Kun Finazillaan halutaan luoda asiakastasoinen raportti, tehdään tämä settings -valikon alta valikossa "customer" ja sieltä kohdassa "customer reports".

[![](

Uusi raportti luodaan oikean yläkulman "new report" painikkeesta. Raportin luomisikkuna on täysin samanlainen kuin Finazillan muussakin raportoinnissa - sillä erotuksella, että lomakkeessa ei ole erikseen mainintaa yrityksestä. Kentät eivät siis muutoin poikkea mitenkään reports -näkymässä tehtävästä raportista.

[![](

Ensimmäisenä luotavalle raportille valitaan käytetty raporttimalli (report scheme). Asiakaskohtaisessa raportissa on tärkeää hahmottaa se, onko kaikilla asiakkuuden yrityksillä yhtenevä tilikarttarakenne vai onko tarvetta muuttaa jonkin yrityksen tilien ohjautumista esimerkiksi raportointikoodein. Aihetta on kuvattu laajemmin mm. [täällä.](

Seuraavaksi raportille annetaan nimi. Nimeämisessä tulee muistaa, että raportin nimi näkyy samanlaisena jokaisen asiakkuuden yrityksen alla reports -listalla.

Seuraavaksi raportille luodaan uusi tietolähde/tietolähteet "new datasource" painikkeella. Tässä esimerkissä raportille luodaan kaksi tietolähdettä: toiseen tulee toteuma ja toiseen budjetti. Ensimmäisenä luodaan toteuma.

[![](

Kun asiakastasoiselle raportille luodaan budjetti -tietolähde, ei raportointi -ikkunassa voida valita, että mistä budjetista on kyse. Tämä siksi, että budjetit ovat kunkin asiakkuuden yrityksen alla.

[![](

# **Oletusbudjetin kiinnittäminen**

Jotta asiakastasoisella raportilla voidaan raportoida budjettia, tulee kunkin yrityksen "budget" näkymässä käydä määrittelemässä yrityksen oletusbudjetti. Tämä tehdään "set as default" painikkeella (löytyy budjetin perästä). Oletusbudjetteja voi olla vain yksi.

[![](

# **Raportin avaaminen**

Tämän jälkeen raportti voidaan tallentaa ja avata "save and open" painikkeesta. Aukeavaa raporttia voi tämän jälkeen pivotoida haluttuun suntaan. Pivotoinnin jälkeen raportin muotoilut tulee tallentaa save -painikkeen kautta.

Raportti voidaan myös kiinnittää asiakastasoiselle Dashboardille, jolloin Dashboard löytyy asiakkuuden yritysten Dashboard listasta ja raporttiin nousee aina sen yrityksen luvut, mistä raportti aukaistaan.



artikkelin osoite on https://intercom.help/finazilla/fi/articles/6544926-esimerkki-asiakastasoinen-raportti-jossa-raportoidaan-budjettia-ja-toteumaa

