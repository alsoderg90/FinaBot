## Hierarkisen raportointiryhmän luominen

Tämän artikkelin ymmärtämistä helpottaa, jos käyttäjä tietää jo mitä raportointiryhmät ovat, osaa luoda raportointiryhmiä sekä käyttää niitä raporteilla.

Raportointiryhmän tarkoitus on nivoa yhteen eri dimensiovalueita, jolloin niitä voidaan raportoida helposti ja nopeasti. Hierarkinen raportointiryhmä taasen nivoo yhteen toisia *raportointiryhmiä ( ja niihin kiinnitettyjä dimensiovalueita).* 

# Hierarkisen raportointiryhmän luominen

Hierarkinen raportointiryhmä luodaan siten, että ensin luodaan raportointiryhmä, jolle annetaan nimi. Tässä kohdin raportointiryhmään ei kiinnitetä mitään dimension arvoja.

[![](

Seuraavaksi luodaan kyseiselle raportointiryhmälle alisteinen lapsiryhmä eli "new child group". Alisteiselle "lapsiryhmälle" annetaan nimi ja kiinnitetään halutut dimension arvot.

[![](

Tarvittaessa uusia lapsiryhmiä voi lisätä new child row painikkeesta. Hierarkinen raportointiryhmä näyttää oheiselta, kun ryhmään on kiinnitetty dimensionarvo Finland sekä Company A. Ryhmässä on siis kaksi hierarkista "lapsiryhmää".

[![](

Kun yllä mainitulla raportointiryhmällä raportoidaan, nousee raporttiin vain ne luvut, jotka kohdistuvat kombinaatiolle Finland + Company A.

**Esimerkki 1:**

Yrityksellä on myyntiä tilillä 3000. Myynti jakaantuu seuraavasti:

* 10 000€ myynti kohdistuu dimensionarvolle Finland
* 5000€ myynti kohdistuu dimensionarvoille Finland + Company A
* 500€ myynti kohdistuu dimensionarvoille Finland + Company B
* 700€ myynti kohdistuu dimensionarvoille Sweden + Company A

Yllä mainitulla raportointiryhmällä raportoitaessa raporttiin nousee 5000€ myynti, sillä se on ainoa myynti, joka kohdistuu yhdistelmälle Finland + Company A.

# Hierarkisella raportointiryhmällä raportointi

Raportointi tehdään kuten mikä tahansa muukin raportti. Raportille valitaan luotu hierarkinen raportointiryhmä kohtaan "Reporting groups".

[![](

Raportille nousee nyt kaikki ne luvut, mitkä ovat kyseisillä dimensioyhdistelmillä.

Havainnollistamme asiaa vielä budjetin kautta lisää.

**Esimerkki 2:**

Yrityksellä on dimensio maa sekä asiakas. Näissä on kussakin lukuisia dimension arvoja. Yritys budjetoi myyntiään kyseisille dimensioille. Budjetoitaessa luvut syötetään dimensioyhdistelmille, eli nk. matriisidimensioille.

Budjetoidaan kuukausittaista myyntiä seuraaville dimensioyhdistelmille:

Norja + Kerta-asiakkat 300€/kk.

Norja + Kuukausisopimukset 17 000€/kk.

Suomi + Kerta-asiakkaat 55€/kk.

Suomi + Kuukausisopimukset 44€ /kk

USA + Kerta-asiakkaat 1350€/kk

USA + Kuukausisopimukset 10 500€/kk

Yritys luo hierarkisen raportointiryhmän oheisesti. Ryhmässä on mukana asiakas sekä maa.

[![](

Tämän jälkeen otetaan raportti, missä raportoidaan kyseistä budjettia. Valitaan luotu hierarkinen raportointiryhmä raportin määrityksiin ja Finazilla tuotaa oheisen raportin.

Huomaa, että raporttia on pivotoitu selvyyden vuoksi ottamalla raportti valinnalla dimension per column ja pivotoitu dimensiot näkyviin ja poistettu date -valinta.

[![](

[![](

*Jos yllä mainitussa esimerkissä budjetille syötettäisiin myyntiä dimensiovaluelle "Suomi" niin kyseinen luku ei nousisi raporttiin hierarkisella raportointiryhmällä raportoitaessa, sillä luku ei kohdistu dimensioyhdistelmään vaan yksittäiseen dimensiovalueen.* 

# Lisätietoja

[Mitä raportointiryhmät ovat ja miten niitä käytetään?](

[Raportointiryhmän luominen](

[Dimensioiden ja raportointiryhmien käyttäminen yhdessä raportilla](



artikkelin osoite on https://intercom.help/finazilla/fi/articles/4145540-hierarkinen-raportointiryhma-nivoo-yhteen-eri-dimensiovalueita

