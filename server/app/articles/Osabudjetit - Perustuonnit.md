## Perustuonnit

[![](

*Versiopäivityksessä 24.3.2023 tuotu kokonaan uusi toiminto. Toiminto mahdollistaa osabudjeteille toteumalukujen tuomisen*

Olemme kertoneet toteumien tuomisesta osabudjetille yleisellä tasolla artikkelissamme [täällä]( Suosittelemme kyseisen artikkelin lukemista riittävän pohjatiedon saamiseksi. Tässä artikkelissa keskitymme esittelemme toimintoa tarkemmin erilaisin esimerkein.

Artikkelin alusta löytyy nk. helpoimmat "perustuonnit". Tämän jälkeen esittelemme miten tuonti toimii, jos käytössä on lisäkohdistus. Artikkelin lopussa on vaativampia esimerkkejä tilanteissa, missä osabudjetilla on käytössä matriisidimensiot sekä vyörytyssäännöt.

# Perustuonnit

**Esimerkki 1:**

Osabudjetilla on yksi vihreä input rivi ja rivillä on tilikiinnitys tiliin 3000.

[![](

Seuraavaksi riville lähdetään tuodaan toteumalukuja joko rivityökalujen kautta tai yläosan import -painikkeen kautta. Jos toteumat tuodaan rivityökalujen kautta yksittäiselle riville, mahdollistaa tämä tuonnin myös joltain toiselta tililtä kuin tililtä 3000, mihin kyseinen osabudjetin rivi on kiinnitetty. Yläosan import -tuonti ei mahdollista tätä.

Tuonnissa valitaan, että miltä ajanjaksolta myynnit halutaan tuoda ja mille ajanjaksolle budjetilla ne halutaan tuoda. Kuvan esimerkissä tuodaan vuoden 2023 myynnit budjetille vuodelle vuodelle 2024. Import mode on tässä esimerkissä current dimension target.

Jos tuonti haluttaisiin tuoda joltain muulta tililtä kuin tililtä 3000, valittaisiin haluttu tili kohtaan "From Account".

[![](

Tällä toimenpiteellä osabudjetille tuodaan tilin 3000 tapahtumat vuodelta 2023 vuodelle 2024 siten, että vain kohdistamattomat (blank) luvut tuodaan. Tämä johtuu siitä, että valinta on "current dimension target", eikä mitään dimensiota ole valittu minnekään osabudjetilla.

Jos "From Account" kohtaan olisi valittu vaikkapa tili 3010, tuotaisiin tilin 3010 tapahtumat vuodelta 2023 vuodelle 2024 siten, että vain blank luvut tuotaisiin. Luvut tulisivat osabudjetin riville, missä on tilikiinnitys tilille 3000, jolloin luvut olisivat budjetilla tilillä 3000.

**Esimerkki 2:**

Taustalla on edelleen esimerkin 1 osabudjetti. Osabudjetin oikeaan yläkulmaan valitaan haluttu dimensionarvo (eli tehdään dimensiokohdistus). Tässä esimerkissä dimensionarvo on nimeltään "d-company". Tuodaan toteumat valinnalla "current dimension target". Osabudjetille tulee vain dimensionarvon "d-company" myynnit (eli samat myynnit, mitkä saataisiin, jos raportoitaisiin dimensionarvoa d-company valinnalla require exact dimension selection).

**Esimerkki 3:**

Taustalla on edelleen esimerkissä 1 kerrottu osabudjetti, missä on tilikiinnitys. Budjetille tuodaan totumat vuodelta 2023 vuodelle 2023. Tuonnissa käytetäänkin valintaa "all dimension targets". Budjetille tulee kaikki tilin 3000 myynnit siten, että ne kohdistuvat kaikille samoille dimensioille kuin lähdejärjestelmässäkin. Data on siis dimensiotasoista.

**Esimerkki 4:**

Edelleen käyttäjällä on esimerkin 1 mukainen osabudjetti. Osabudjetin oikeaan yläreunaan valitaan dimensionrvo "d-company". Tämän jälkeen osabudjetille tuodaan toteumat vuodelta 2023 vuodelle 2024 ja valintana käytetään vaihtoehtoa "sum of all dimensions to current". Toteumat tulevat osabujetille siten, että kaikki myynnit tililtä 3000 tuodaan huolimatta siitä, mille dimensionarvolle/arvoille ne kohdistuvat. Myynnit summataan dimensionarvolle d-company. Jos siis ennen myyntiä oli usealla dimensionarvolla, niin nyt ne kaikki ovat yhteenlaskettuna dimensionarvolla "d-company".

**Esimerkki 5:**

Käyttäjällä on osabudjetti, missä on useampia erilaisia rivejä; otsikkorivi, syöttörivejä sekä kaavarivi. Kahdella osabudjetin syöttörivillä on tilikiinnitys. Tilikiinnitykset ovat tileihin 3000 ja 3003.

[![](

Toteuman tuontia voidaan tässä tapauksessa lähteä tekemään useaa eri kautta, riippuen siitä, minne kaikkialle toteumaa halutaan tuoda. Tässä esimerkissä toteuma tuodaan yläosan import -painikkeen kautta, jolloin toteumat tuodaan kerralla sekä tilille 3000, että tilille 3003.

Toteumat tuodaan tässä esimerkissä siten, että kauden 12/2023 myynnit halutaan tuoda kaudelle 1/2024. Tuodaan siis vain yksi kuukausi. Lisäksi toteumat halutaan tuoda 20% kertoimella, joten multiplier -kentässä on kerroin 1.2. Toteumat tuodaan valinnalla "All dimension targets", jolloin data on dimensiotasoista.

[![](

# Osabudjetit, missä on käytetty lisäkohdistusta (Additional dimension target)

**Esimerkki 6:**

Finazillassa on oheinen osabudjetti. Osabudjetin ensimmäisellä vihreällä syöttörivillä on käytetty rivikohtaista dimensiokiinnitystä eli nk. additional dimension target kohdistusta. Kohdistus on tehty dimensionarvolle "D-company".

[![](

Toteumat tuodaan osabudjetin yläosan import -painikkeen kautta valinnalla "current dimension target". Tämä tarkoittaa käytännössä sitä, että ensimmäiselle vihreälle riville tuodaan tilin 3000 tapahtumat, jotka kohdistuvat dimensionarvolle "D-company", ja jälkimmäiselle vihreälle riville tuodaan tilin 3003 tapahtumat, jotka eivät kohdistu millekään dimensionarvolle (blank).

Mikäli jälkimmäiselle riville kiinnitettäisiin jokin dimensionarvo, tuotaisiin edellä kuvatulla tuonnilla myös tälle riville kyseisen dimensionarvon toteumat tililtä 3003.

**Esimerkki 7:**

alla olevassa esimerkissä ylimmälle riville (otsikkorivi) on kiinnitetty lisäkohdistus (additional dimension target) dimensionarvolle "d-company". Kohdistus valuu koko alapuoliselle rakenteelle. Vihreillä syöttöriveillä on tilikohdistus, joten näille riveille voidaan tuoda kyseisten tilien toteutuneet myynnit, jotka kohdistuvat dimensionarvolle "d-company".

[![](

**Esimerkki 8:**

Alla olevassa osabudjetissa Asiakas A syöttöriveillä on lisäkohdistus dimensionarvolle "kerta-asiakas". Asiakkaalla B lisäkohdistus on "kuukausisopimukset".

[![](

Kun osabudjetille tuodaan toteumaa valinnalla current dimension values, tuodaan ylempään rakenteeseen toteumat tileiltä 3000 ja 3003 niiden lukujen osalta, jotka kohdistuvat dimensionarvolle "kerta-asiakas". Alempaan tuodaan luvut tileiltä 3000 ja 3003 niiden lukujen osalta, joissa kohdistus on dimensionarvolle "kuukausisopimus".

#### 

# Osabudjetit, missä on käytetty matriisikohdistusta

**Esimerkki 9:**

Edelleen käytössä on ylemmän esimerkin kaltainen osabudjetti. Edellä kuvatun lisäksi osabudjetin oikeaan reunaan valitaan dimensionarvo "D-company". Kun osabudjetille tuodaan nyt toteuma valinnalla current dimension values, tuodaan ylempään rakenteeseen (Asiakas A) tilin 3000 toteumat niiltä osin, missä kohdistus on matriisille kerta-asiakas + D-company. Sama koskee tiliä 3003.

Alempaan rakenteeseen (Asiakas B) tuodaan toteutuneet myynnit tililtä 3000, niiltä osin, missä myynti kohdistuu matriisille kuukausisopimukset + D-company. Samoin tapahtuu tilin 3003 osalta.

[![](

*Matriisikohdistus, missä kumpikin matriisin osapuoli on samassa dimensiossa, ei ole sallittu. Tällaiselle kombinaatiolle ei täten voi myöskään tuoda toteumaa. Mikäli toteumaa yrittää tuoda, tulee osabudjetille arvoksi pelkkä 0.* 

[![](

*All dimension targets -valinnalla tehty tuonti tuo kaikki mahdolliset kohdistukset, missä osabudjettiin kiinnitetyt dimensionarvot esiintyvät joko yksistään, tai yhdessä jonkin toisen dimensionarvon kanssa. Jos siis osabudjetille on kiinnitetty dimensioarvo "asiakas A", ja osabudjetille tuodaan toteumat, tuodaan osabudjetille luvut jotka kohdistuvat pelkästään asiakkaalle A, asiakas A + projekti 1, asiakas A + projekti 2, asiakas A + projekti 1 + Jyväskylä jne... Toimintalogiikka vastaa pääbudjetin puolella olevaa vastaavaa toimintoa.* 

# Dimensiokiinnitetyt osabudjetit

Toiminto on käytettävissä myös osabudjeteilla, mitkä on kiinnitetty tietylle dimensionarvolle. Tällöin tulee huomioida, että kiinnitetty dimensionarvo on osa määrittelyä. Jos siis esimerkiksi osabudjetti on kiinnitetty dimensionarvolle hallinto, ja osabudjetille tuodaan toteumaa valinnalla current dimension values, tuodaan luvut jotka kohdistuvat dimensionarvolle hallinto.

Huomaa, että dimensiokiinnitetylle osabudjetille ei voi tuoda toteumaa valinnalla "All dimension targets", sillä osabudjetin kiinnittäminen tarkoittaa, että osabudjetille voi budjetoida vain kyseiselle dimensionarvolle.

# Toteumien tuominen jos käytössä on vyörytyssääntöjä

Toiminto on käytettävissä myöskin osabudjeteilla, missä käytetään distribution tyyppisiä vyörytyssääntöjä. Tässä yhteydessä on huomioitava, että tämä tuo käyttöön hieman kompleksisuutta ja käyttäjän tulee itse ymmärtää, mitä toteumia hän on tuomassa ja mistä - ja minne niitä edelleen vyörytetään. Tässä yhtälössä täytyy siis huomioida osabudjetin määrittelyt suhteessa dimensioihin ja tileihin, toteuman tuontiin liittyvät dimensiotasoisuudet (import mode) sekä vyörytyssäännöt.

#### 

# Toteumien tuominen ennustebudjetille (forecast budget)

Toteumia voi tuoda yhtä lailla myös sellaiselle osabudjetille, mikä on ennustebudjetin takana, eli budjetti on tyypiltään forecast budget. Jos esimerkiksi ennustebudjetilla olisi myyntien ennustamiseen tehty osabudjetti, niin toteumia voidaan tuoda import -työkalulla osabudjetille ja vastaavasti pääbudjetin monitor -näkymä näyttää kokonaismyynnit siten, että toteumana tulee ne luvut mikä on asetettu ennusteelle real balance end date:ksi ja loput luvut tulevat osabudjetilta.

# Lisätietoja

[Lisäkohdistuksen käyttäminen osabudjetilla; osa 1](

[Lisäkohdistuksen käyttäminen osabudjetilla, osa 2: matriisikohdistus](

[Lisäkohdistuksen käyttäminen osabudjetilla, osa 3: lisäkohdistuksen periytyminen ja rivien kopiointi](



artikkelin osoite on https://intercom.help/finazilla/fi/articles/7154997-esimerkkeja-toteuman-tuomisesta-osabudjetille

