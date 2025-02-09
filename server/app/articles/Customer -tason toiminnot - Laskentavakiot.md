## Laskentavakiot

​*Versiopäivityksessä 9.9.2022 tuotu kokonaan uusi toiminto. Toiminto on **vaihtoehtoinen** tapa aikaisemmille yrityskohtaisille toiminnoille. Tuotava kokonaisuus koskettaa siis vain asiakkaita, joilla on enemmän kuin yksi yritys omassa asiakkuudessaan*

# Laskentavakiot

Calculation Constants, eli laskentavakiot, ovat yksi budjetoinnin ja raportoinnin keskeisistä työkaluista. Yleisimmin laskentavakioita käytetään budjetoinnissa, kun on tarve käyttää samaa arvoa useassa eri budjetissa ja/tai osabudjetissa sekä päivittää tätä arvoa. Laskentavakion päivityksellä saadaan siis arvo päivittymään kerralla kaikkiin osabudjetteihin ja budjetteihin, joissa laskentavakiota on käytetty.

Laskentavakioita on aikaisemmin ollut mahdollisuus luoda yrityskohtaisena tai budjettikohtaisena. Tämän lisäksi laskentavakioita on ollut Finazillan hallinnoimina nk. system -tasoisina. Nyt valikoimaan tuodaan mukaan myös asiakastasoinen laskentavakio.

Tämän artikkelin ymmärtämistä helpottaa, mikäli käyttäjä tietää mitä laskentavakiot ovat, miten niitä luodaan ja käytetään.

# Asiakastasoisen laskentavakion luominen

Asiakastasoinen laskentavakio luodaan customer -valikossa kohdassa "calculation constants".

[![](

Calculation constants -näkymässä näkyy kaikki laskentavakiot, mitä asiakkuudessa on olemassa. Listassa näkyy siis system -tasoiset Finazillan luomat laskentavakiot, sekä mahdolliset asiakastasoiset laskentavakiot. Yrityskohtaiset laskentavakiot eivät näy täällä, vaan ne löytyvät company -valikosta kohdasta calculation constants.

Uusi laskentavakio luodaan ihan samalla tavalla kuin yrityskohtainen laskentavakio. Ohje luomiseen löytyy mm. [täältä.](

[![](

Kun luotu laskentavakio löytyy listasta, käydään sille määrittelemässä arvo tai arvot, sekä ajankohta, mistä alkaen laskentavakio on voimassa.

Kun laskentavakio on luotu customer -tasolle, se näkyy jokaisessa asiakkuuden yrityksessä (company -calculation constants). Laskentavakiota voidaan myös käyttää jokaisessa asiakkuuden yrityksessä.

# Asiakastasoisen laskentavakion poistaminen

Mikäli laskentavakiota on käytetty jossain asiakkuuden yrityksen budjetissa ja/tai osabudjetissa tai raporttimallilla, ei laskentavakiota voi poistaa. Muussa tapauksessa laskentavakion voi poistaa delete -painikkeella näkymässä, missä se on luotukin.

# Asiakastasoisen laskentavakion ottaminen käyttöön

Asiakastasoisen laskentavakion käyttöönottaminen ei eroa millään tavalla yritystasoisen laskentavakion käyttämisestä.

Luotuja laskentavakioita voidaan hakea esimerkiksi osabudjetin kaavoihin tai raporttimallin kaavoihin kaavageneraattorissa. Kaavarivissä käytetty laskentavakio näkyy laskentavakion tunnuksella.

[![](

# Asiakastasoisen laskentavakion ylikirjoittaminen

Kun asiakastasoinen laskentavakio on luotu ja luodulle laskentavakiolle on annettu symbol -kohdassa "nimi", voidaan asiakaskohtainen laskentavakio ylikirjoittaa luomalla yrityskohtainen laskentavakio, jolla on sama symbol.

Tässä artikkelissa esittelimme esimerkkiä, missä luotiin oheinen asiakastasoinen laskentavakio.

[![](

Mikäli jollekin asiakkuuden yritykselle käytäisiin luomassa uusi yritystasoinen laskentavakio samalla symbolilla, korvaisi se asiakastasoisen laskentavakion.

[![](

Tämä mahdollistaa sen, että jos asiakkuudessa on 10 yritystä, voi yhdeksällä näistä olla käytössään asiakastasoinen laskentavakio ja yhdellä jokin oma yrityskohtainen laskentavakio.

Uusi asiakastasoisten toimintojen kokonaisuus muodostuu useammasta erillisestä toiminnosta, jotka käsittelemme kunkin omissa artikkeleissaan. Linkit muihin osioihin löytyvät alta.

# Lisätietoja

[Osa 1: Raportointi](

[Osa 3: Dashboard](



artikkelin osoite on https://intercom.help/finazilla/fi/articles/6544908-asiakastasoiset-toiminnot-osa-2-laskentavakio

