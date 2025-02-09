## Esimerkki 1

Olemme aikaisemmassa artikkelissamme ["raporttimallin avulla dimensioiden filtteröinti"]( kuvanneet, miten raporttimallilla voidaan rajata raportilla näytettävää talousdataa koskettamaan jotakin tiettyä dimensiota -tai dimensioita. Toiminto on käytettävissä myös operatiivisella datalla, eli raporttimallin rivillä, joka raportoi operatiivista dataa.

Tässä artikkelissa havainnollistamme asiaa esimerkin avulla. Artikkelin ymmärtämistä helpottaa, jos käyttäjä osaa luoda perinteisiä raporttimalleja, sekä ymmärtää, mitä operatiivinen data on ja miten sitä voidaan hyödyntää Finazillassa.

# Esimerkki 1

Yrityksellä on 4 tehdasta, joissa valmistetaan tuotteita, kuten holkki, mäntä, akseli ja ruuvi. Tuotemyyntejä seurataan tehdaskohtaisesti sekä kappalemäärin, että myydyin euroin.

Tuotemyynnit on tuotu Finazillaan sisään csv -tiedostona. (Ohje tietojen sisäänlukuun löytyy [tästä]( Tämän jälkeen tuotemyyntejä halutaan raportoida tehtaittain siten, että kunkin tehdaan tuotteiden myyntimäärät (kpl) raportoidaan kappaleittain tuotekohtaisesti.

## Raporttimallin rakentaminen

Uudet yritystasoiset raporttimallit luodaan valikossa company, kohdassa report scheme. Luotavalle raporttimallille annetaan kuvaava nimi ja raporttimalli tallennetaan.

[![](

Seuraavaksi luodulle raporttimallille aletaan rakentamaan ns. raporttipuuta. Tässä esimerkissä raporttipuuta on lähdetty rakentamaan siten, että raportilla on kukin tehdas omana hierarkisena kokonaisuutenaan ja kunkin tehtaan alla on omina riveinään yrityksen tuotteet.

Kullekin riville kerrotaan rivin nimi, mistä data groupista tieto poimitaan ja onko poimittava määre tyypiltään "quantity" vai "amount". Lopuksi dataa rajataan valitsemalla halutut dimensiovaluet kohtaan "filter data by dimensions".

[![](

Samalla logiikalla luodaan kaikki halutut rivit raporttimallin raporttipuuhun. Alla on esimekki tehdas 1 raporttipuusta otsikkotasolla.

[![](

Seuraavaksi raporttimallille lisätään tehtaat 2-4 samalla logiikalla ja niiden alle kaikki tuotteet.

[![](

## Luodulla raporttimallilla raportoiminen

Kun koko raporttimallin raporttipuu on rakennettu, voidaan raporttimallilla lähteä raportoimaan normaalisti reports -valikossa.

[![](

Luodaan uusi raportti "new report" painikkeen kautta, valitaan raporttimalliksi luotu raporttimalli ja tehdään muut tarvittavat määrittelyt (mm. ajanjakso valinnat). Raportin muodostaminen ei poikkea tavallisesta raportin muodostamisesta.

Raportti kyseisellä mallilla raportoituna näyttää oheiselta. Riveille nousevat valitusta operatiivisesta datasta (data group) ne määreet (quantity) ja arvot (operatiiviset dimensiot) mitä raporttimallille on valittu.

[![](

[![](

*Raporttipuun voi rakentaa täysin haluamallaa tavalla ja halutuin otsikoin. Yllä esitetty esimerkki on vain yksi havainnollistava esimerkki. Raporttimallissa voidaan yhdistää myös operatiiviseen dataan talousdataa.* 

# Esimerkki 2

Tässä esimerkissä jatkojalostamme esimerkin 1 aineistoa. Yrityksellä on edelleen samat 4 tehdasta ja samat tuotteet. Yrityksen tuotemyynnit kohdistetaan aikaisemman lisäksi myyjille, jotka muodostavat oman dimensionsa.

Raportoinnissa käytetään edelleen samaa, aikaisemmin luotua raporttimallia, jossa ovat siis yrityksen 4 tehdasta hierarkisessa rakenteessa. Tarpeena on saada samasta raportista myyjäkohtainen raportti, jossa voidaan tarkastella tietyn myyjän myymiä tuotemääriä.

## Luodulla raporttimallilla raportointi

Luodaan edelleen uusi raportti reports -valikossa toiminnolla "new report". Valitaan raporttimalliksi esimerkkki 1 yhteydessä luotu raporttimalli "tuotemyynti tehtaittain". Tämän lisäksi valitaan kohdassa operative dimensions dimensio "myyjä".

[![](

Tämän jälkeen raporttia voi pivotoida haluamallaan tavalla. Dimension "myyjä" voi asettaa vaikkapa raportin filtteriksi, joilloin voi filtteröidä tietyn myyjän myynnit helposti esiin.

[![](

[![](

[![](

*Finazillan logiikka on, että jos raportilla yhdistetään filtteröintiä raporttivalinnoissa ja raporttimallilla, niin ensin datasta otetaan raporttivalintojen filtteriä vastaava data. Seuraavaksi filtteröidystä datasta otetaan raporttimallin filtteriä vastaava data kyseiselle riville.*

# Lisätietoja

[Raporttimallin avulla dimensioiden filtteröinti](

[Esimerkki: liikevaihto raporttimallin luominen käyttämällä dimensiofiltteriä](

[Operatiivisen datan tuominen Finazillaan vakiomuotoisella csv -siirtotiedostolla](

[Operatiivista dataa ja kirjanpidon dataa yhdistävän raporttimallin luominen](



artikkelin osoite on https://intercom.help/finazilla/fi/articles/5440927-esimerkki-raporttimallin-avulla-dimensioiden-filtterointi-yhdistelma-raporteissa

