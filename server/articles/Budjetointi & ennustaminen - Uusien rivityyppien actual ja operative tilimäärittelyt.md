## Uusien rivityyppien actual ja operative tilimäärittelyt

[![](

Versiopäivityksessä 5.5.2023 tuotu uusi toiminto. Toiminto mahdollistaa osabudjetille rivien luonnin siten, että niihin haetaan aina toteutuneet luvut. Toiminto on suunniteltu erityisesti ennustebudjetteja varten.

Tuotu ominaisuus on osa laajempaa kokonaisuutta. Tässä artikkelissa esitelty ominaisuus on osa 2/2. Toimintoon liittyy myös seuraavat ominaisuudet:

* [Automaattisesti päivittyvä osabudjetti, osa 1: rivityypit actual ja operative](

Aikaisemmin osabudjeteilla oli olemassa 4 vaihtoehtoa, minkälaisia rivejä osabudjetille voi luoda. Rivityypit olivat syöttörivi (input), otsikko (header), kaava (formula) ja prosenttirivi (percentage). Nyt rivityyppeihin on tuotu näiden lisäksi kaksi uutta rivityyppiä, jotka ovat actual ja operative.

# **Uusien rivityyppien actual ja operative tilimäärittelyt**

Mikäli osabudjetille on luotu rivejä, joiden tyyppi on joko actual tai operative, tuodaan näissä tilanteissa kyseisille riveille dataa ennustebudjetin real balance end date -päivään saakka. Tuotu data on toteumadataa ja se tuodaan sellaisenaan siltä tililtä, mikä kyseiselle riville on kiinnitetty lähtötiliksi.

Lähtötili (eli tili mistä toteumadataa tuodaan) asetetaan kohtaan "from account". Tilikiinnitys tehdään kohtaan "transfer to account" -kuten ennenkin. Nämä määrittelyt määrävät sen, mistä tililtä toteumat tuodaan ja minne ne pääbudjetilla ohjataan. Real balance end date:n jälkeisen ajan käyttäjä voi budjetoida itse käsin, aivan kuten ennenkin.

# **Uusien rivityyppien actual ja operative dimensiomäärittelyt**

Jos toteumadata kohdistuu dimensiolle/dimensioille, tuodaan data osabudjetin kohdistuksien mukaisesti. Luvut voivat näyttäytyä osabudjetilla hyvin monella tavalla riippuen siitä, mitä valintoja osabudjetille on tehty suhteessa dimensioihin.

# Havainnollistavat esimerkit

Havainnollistamme asiaa muutamalla esimerkillä.

Yrityksellä A on myyntiä tilillä 3000 kaudella 1/2023 oheisesti:

* 10 000€. Tämä myynti ei kohdistu millekään dimensionarvolle, eli se on nk. dimensioimaton/kohdistamaton myynti
* 3000 € kohdistuu dimensionarvolle Kerta-asiakkaat
* 5000€ kohdistuu dimensionarvolle Kerta-asiakkaat + Jyväskylä (nk. matriisidimensio)

***Esimerkki 1: "perinteinen dimensiokohdistus"***

Perinteisellä dimensiokohdistuksella tarkoitetaan dimensiokohdistuksen tekemistä käyttämällä oikean yläkulman select dimensions- valintaa. Mikäli oikeassa yläkulmassa ei ole valittuna mitään, näkyy osabudjetin rivillä myynti 10 000€ (nk. blank). Jos oikeaan yläkulmaan valitaan dimensionarvo "kerta-asiakkaat", näkyy summana 3000€.

***Esimerkki 2: lisäkohdistus (additional dimension target)***

Osabudjetin riville voidaan antaa nk. lisäkohdistus, joka tarkoittaa käytännössä katsoen dimensiokohdistuksen tekemistä. Lisäkohdistuksen tekeminen on yksi monista vaihtoehtoisista tavoista tehdä dimensiokohdistusta osabudjetilla. Lisäkohdistus tehdään rivikohtaisissa asetuksissa (settings) kohdassa "additional dimension values".

Kyseiselle myynti -riville on kerrottu lisäkohdistukseksi dimensionarvo "kerta-asiakkaat". Tämä tarkoittaa, että kyseiselle riville haetaan tililtä 3000 toteutuneita myyntejä niiden myyntien osalta, mitkä kohdistuvat vain ja ainoastaan dimensionarvolle "kerta-asiakkaat".

[![](

Osabudjetin rivillä näkyy tässä tapauksessa kerta-asiakas dimension myynti, eli 3000€.

***Esimerkki 3: perinteinen dimensiokohdistus + lisäkohdistus (additional dimension target)***

Matriisikohdistuksen tekeminen osabudjetilla voidaan toteuttaa siten, että riville valitaan lisäkohdistus ja tämän lisäksi valitaan osabudjetin oikeaan yläkulmaan matriisin toinen osapuoli.

Jos siis edellä kuvatussa tapauksessa riviasetuksissa on asetettuna dimensionarvo kerta-asiakas, ja osabudjetin oikeaan yläkulmaan valintaan dimensionarvo "Jyväskylä", näkyy osabudjetin rivillä arvona 5000€.

***Esimerkki 4: Dimensiokiinnitetty osabudjetti***

Dimensiokiinnitetty osabudjetti on automaattisesti kohdistettu valitulle dimensionarvolle. Tämä vastaa siis dimensiokohdistuksen tekemistä. Mikäli luodaan osabudjetti, joka on kiinnitetty dimensionarvolle kerta-asiakas, esitetään osabudjetin rivillä myyntinä 3000€. Jos riville käytäisiin tekemässä vielä lisäkohdistus dimensionarvoon Jyväskylä, esitetään osabudjetin rivillä myyntinä 5000€.

***Esimerkki 5: Vyörytyssääntö***

Vyörytyssääntö tarkoittaa dimensiokohdistamista tietyllä prosenttijakaumalla. Mikäli osabudjetin riviin kohdistuu vyörytyssääntö, tarkoittaa tämä käytännössä sitä, että osabudjetin alusta real balance end date;n saakka toteuma tulee sellaisenaan, mutta loppuosa kohdistuu dimensionarvoille vyörytyssäännön jakosuhteessa.



artikkelin osoite on https://intercom.help/finazilla/fi/articles/7858448-automaattisesti-paivittyva-osabudjetti-osa-2-dimensiokohdistukset-actual-ja-operative-riveilla

