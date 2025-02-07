## Havainnollistava esimerkki

[![](

Versiopäivityksessä 21.4.2023 tuotu kokonaan uusi toiminto. Toiminto mahdollistaa sen, että tietyissä raporteissa tietty tili eliminoituu ja toisessa raportissa se ei eliminoidu.

Tämä artikkeli koskettaa vain konserniyrityksiä. Artikkelin ymmärtämisen edellytys on, että käyttäjä tietää miten yrityksen eliminoitavat tilit merkitään tileihin ja kuinka Finazillassa tehdään konserniraportteja, joissa keskinäiset tapahtumat eliminoidaan.

Tässä artikkelissa kuvattu toiminnallisuus on suunniteltu erityisesti sellaisille konserneille, joissa on tarvetta raportoida nk. alakonserneja. Toiminto mahdollistaa sen, että koko konsernia raportoitaessa kaikki eliminointitilit huomioidaan raportilla ja vastaavasti taas silloin kun raportoidaan vaikkapa vain kahta konsernin yrityksistä, eliminoidaan vain ne tilit, joiden yrityksetkin ovat raportilla.

# Havainnollistava esimerkki

Havainnollistamme asiaa esimerkin avulla.

Esimerkki 1:

Finazillassa on asiakkuus, missä on 3 yritystä. Nämä 3 yritykset A, B ja C muodostavat konsernin. Lisäksi yritykset A ja C muodostavat nk. alakonsernin.

Jokaisella kolmella yrityksellä on tilit:   
3001 = Myynti yritykselle A  
3002 = Myynti yritykselle B  
3003 = Myynti yritykselle C

Kun koko konsernista halutaan raportti, toimii tämä ongelmitta. Näissä tilanteissa Finazillan raportointi eliminoi kaikki kolme tiliä. Kyseessä on normaali Finazillan konserniraportti, jota olemme kuvannneet mm. artikkelissamme [täällä.]( 

Tässä kuvattu uusi ominaisuus tulee vastaan tilanteessa, missä halutaankin raportoida yritys A ja C. Tässä raportissa halutaan eliminoida vain tilit 3001 ja 3003, sillä tili 3002 koskee yrityksen B tapahtumia, eikä niitä haluta eliminoida alakonsernin raportista. Yritykselle B kohdistuva myynti on tämän raportin näkökulmasta ulkopuolelle menevä tapahtuma ja sen tulisi käyttäytyä näissä tilanteissa kuten minkä tahansa muunkin ei-eliminoitavan tilin.

# Tilin määrittely

Konsernitilit merkitään yrityksen tililistaan valikossa company ja kohdassa "accounts". Tilin nimen perässä olevasta edit -painikkeesta tiliä pääsee muokkaamaan. Kohdassa "consolidated account" voidaan kertoa, että kyseessä on eliminoitava tili. Tämä tarkoittaa, että kyseinen tili eliminoidaan aina.

Kohta "consolidated transaction target" on uusi ja tässä kentässä voidaan nimenomaan kertoa, että tämä kyseinen tili halutaan elimoida vain silloin, kun kyseisellä raportilla esiintyy siihen valittu yritys.

[![](

Konsernitilit näkyvät yrityksen tililistassa siten, että "consolidation" otsikon alla kerrotaan onko tili eliminoitava, ja jos on, mistä se eliminoidaan. Always tarkoittaa, että se eliminoidaan aina ja kaikkialta. Ilman merkintää olevat tilit ovat "tavallisia" tilejä.

[![](

# Raportointi

Mikäli Finazillalla raportoidaan yritykset A, B ja C, niin Finazilla eliminoi kaikki aiemmin kerrotut tiit.

Mikäli Finazillassa tehdään raportti, jossa on mukana vain yritykset A ja C, eliminoi Finazilla vain yritysten A ja C tilit. Yrityksen B tili tulee normaalisti myynteihin.



artikkelin osoite on https://intercom.help/finazilla/fi/articles/7439535-tilin-eliminointi-riippuvaiseksi-raportin-yrityksesta

