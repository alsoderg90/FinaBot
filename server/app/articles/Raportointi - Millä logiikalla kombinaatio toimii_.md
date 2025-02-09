## Millä logiikalla kombinaatio toimii?

Olemme aikaisemmassa artikkelissamme ["Dimensioiden valitseminen raportille](" kuvanneet, miten tietystä / tietyistä dimensioista voidaan muodostaa raportti. Artikkelimme ["Raportointiryhmän luominen"]( taasen kuvaa tilannetta, missä raportti muodostetaan käyttämällä raportointiryhmää. Tässä artikkelissamme kerromme, miten nämä kaksi vaihtoehtoa voidaan tarvittaessa yhdistää.

# Millä logiikalla kombinaatio toimii?

Raportin voi muodostaa siten, että rajauksissa käytetään sekä dimensiota että raportointiryhmää. Näin toimien haetaan siis dimensioiden *yhdistelmää* eli niin kutsuttua matriisivalintaa. Toiminto voi olla tarpeellinen yrityksille, jotka haluavat raportoida säännönmukaisesti tiettyjen dimensioiden yhdistelmiä.

Valinnalla raportointiryhmä + joku dimensio Finazilla tuottaa siis raportin, missä on mukana raportointiryhmään valitut dimensiot ja hakua *täsmennetään* dimensions -kentässä valitulla dimensiolla. Havainnollistamme asiaa esimerkillä.

***Esimerkki***

Yrityksellä on dimensio nimeltä "Asiakasryhmä", jossa on neljä dimensiovalueta. Dimensiovaluet ovat "kuukausiasiakkaat", "kerta-asiakkaat", "konserniyhtiöt" ja "konsultointiprojektit".

Yritys on luonut raportointiryhmän, johon on valittu dimensiovaluet "kuukausisopimukset" ja "kerta-asiakkaat".

[![](

Tämän lisäksi yrityksellä on dimensio nimeltä "Maa / alue", jossa on lukuisia eri maita dimensiovalueina (mm. Ruotsi, Norja, Usa jne).

Tarpeena on muodostaa raportti, jossa on mainittuna jokin raportointiryhmän dimensiovalueista, eli joko kuukausisopimukset tai kerta-asiakkaat, sekä lisänä dimensiovalue "Norja".

Yhdistelmällä raportointiryhmä, sekä dimensio Norja, saadaan tositteet, jossa on mainittu jokin ryhmän asiakasryhmistä ja Norja. Kyseinen raportti tuottaa siis tositteet, jotka on kohdistettu joko "Kuukausisopimukset" ja "Norja" dimensioille TAI "Kerta-asiakkaat" ja "Norja" dimensioille.

[![](

*Raporttiin ei nouse lukuja, mitkä on kohdistetty pelkästään dimensiolle kuukausisopimukset, kerta-asiakkaat tai Norja.* 

# Raportin muodostaminen

Muodostetaan haluttu raportti normaalisti. Valitaan dimensions -kenttään dimensiovalue Norja, sekä reporting groups -kenttään luotu raportointiryhmä.

[![](

Nyt saadaan raportti, jossa on dimensioiden Norja + Kuukausisopimukset sekä Norja + Kerta-asiakkaat luvut. Raportin esitystapa riippuu luonnollisesti raportin muista valinnoista. Alla oleva esimerkkiraportti on otettu valinnoin include dimensions, sekä accounting period / column. Raporttia voi pivotoida aivan kuten mitä tahansa muutakin raporttia. Esimerkin raporttia on pivotoitu siten, että dimensiot ovat sarakkeilla.

[![](

[![](

*Muistutamme vielä, että raportin luvut ovat nimenomaan **matriisidimensioiden lukuja.** Esimerkkitapauksessamme saman aikavälin dimension "kerta-asiakkaat" myynti on kokonaisuudessaan 1 019 871,77€. Tästä luvusta 114 453,84€ on kohdistettu kerta-asiakkaat dimension lisäksi dimensiolle Norja, mistä syystä se nousee raporttiin esimerkkimme valinnoin.* 

# Lisätietoja

[Mitä dimensiot ovat ja miten niitä käytetään?](

[Dimensioiden valitseminen raportille](

[Mitä raportointiryhmät ovat ja miten niitä käytetään?](

[Raportointiryhmän luominen](



artikkelin osoite on https://intercom.help/finazilla/fi/articles/5049597-dimensioiden-ja-raportointiryhmien-kayttaminen-yhdessa-raportilla

