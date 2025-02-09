## Tositteen luominen Finazillaan

Artikkelimme ["kirjaustositteiden tekeminen kirjanpidon ulkopuolella"]( kuvaa sitä, kuinka Finazillassa voidaan luoda tositteita. Tässä artikkelissa kuvaamme vaihtoehtoisen tavan luoda tositteita hyödyntämällä Exceliä.

# Tositteen luominen Finazillaan

Tositteen luominen lähtee liikkelle siitä, että Finazillassa navigoidaan valikkoon company ja sieltä kohtaan "vouchers". Valikossa painetaan painiketta "create new voucher" ja tämän jälkeen valitaan vaihtoehto "import voucherlines".

[![](

Tämän jälkeen käyttäjälle aukeaa ikkuna, mihin voidaan "copy pastettaa" halutut tositerivit kerralla.

[![](

Excel, mistä tiedot tuodaan kopioimalla, voi olla hyvin monenlainen ja näköinen. Excelille ei sinällään ole tarkkaa muotovaadetta, eikä tietojen tarvitse olla Excelissä missään tietyssä järjestyksessä. Tietoja voidaan erikseen vielä määritellä, lisätä ja muokata.

# Havainnollistavat esimerkit

Havainnollistamme asiaa tarkemmin muutamalla esimerkillä.

## Esimerkki 1: tositerivit ilman dimensioita

Tositteen tiedot ovat Excelissä oheisesti. Excel sisältää sekä myyntiä, että ostoa. Tiedostossa on kirjanpidon tili, summa sekä selite.

[![](

Seuraavaksi Excelissä maalataan haluttu alue (eli kaikki rivit mitkä halutaan tuoda tositteelle) ja valitaan Ctrl + C. Tämän jälkeen navigoidaan Finazillaan ja mennään "voucher" näkymässä kohtaan create new voucher ja valitaan päivä mille tosite halutaan tehdä sekä kirjoitetaan tositteelle selite kohtaan "description". Seuraavaksi valitaan vaihtoehto "import voucherline". Tiedot liitetään tyhjään kenttään painikkeella Ctrl + V.

[![](

Näkymässä voidaan määritellä, että mitä mikin Excelistä tuotava tieto on klikkaamalla näkymässä olevia otsikoita.

[![](

Kun tiedot on tarkistettu ja määritelty halutusti, painike "generate voucher" luo tositteen esikatselun/manuaalisen syöttöikkunan. Tositetta voidaan vielä tässä kohdin täydentää tai muuttaa. Painamalla "create voucher" tosite luodaan ja tallennetaan.

[![](

## Esimerkki 2: tositerivit yhdellä dimensioilla

Tositteen tiedot ovat Excelissä oheisesti. Excel sisältää sekä myyntiä, että ostoa. Tiedostossa on kirjanpidon tili, summa sekä selite. Tiedostossa oleva osto kohdistuu yrityksen dimension arvolle "hallinto" (sarake D).

[![](

Seuraavaksi Excelissä maalataan haluttu alue (eli kaikki rivit mitkä halutaan tuoda tositteelle) ja valitaan Ctrl + C. Tämän jälkeen navigoidaan Finazillaan ja mennään "voucher" näkymässä kohtaan create new voucher ja valitaan päivä mille tosite halutaan tehdä sekä kirjoitetaan tositteelle selite kohtaan "description". Seuraavaksi valitaan vaihtoehto "import voucherline". Tiedot liitetään tyhjään kenttään painikkeella Ctrl + V.

[![](

Näkymässä voidaan määritellä, että mitä mikin Excelistä tuotava tieto on klikkaamalla näkymässä olevia otsikoita. Erityisesti mikäli aineisto sisältää dimensioita, tulee määritellä mistä dimensiosta on kyse. Kyseisessä esimerkissä oleva "hallinto" on dimension "maa/alue" arvo, jolloin valikosta valitaan vaihtoehto "maa/alue".

[![](

Kun tiedot on tarkistettu ja määritelty halutusti, painike "generate voucher" luo tositteen esikatselun/manuaalisen syöttöikkunan. Tositetta voidaan vielä tässä kohdin täydentää tai muuttaa. Painamalla "create voucher" tosite luodaan ja tallennetaan.

[![](

## Esimerkki 3: tositerivit usealla eri dimensioilla

Tositteen tiedot ovat Excelissä oheisesti. Excel sisältää sekä myyntiä, että ostoa. Tiedostossa on kirjanpidon tili, summa sekä selite. Tiedostossa oleva myynti kohdistuu yrityksen dimension arvolle "kuukausisopimukset" (sarake D) ja osto kohdistuu yrityksen dimension arvolle "hallinto" (sarake E).

Huomaa, että koska tiedosto sisältää kahta eri dimensiota, tulee nämä laittaa Excelissä eri sarakkeisiin, jotta ne voidaan myöhemmässä vaiheessa määritellä omikseen.

[![](

Seuraavaksi Excelissä maalataan haluttu alue (eli kaikki rivit mitkä halutaan tuoda tositteelle) ja valitaan Ctrl + C. Tämän jälkeen navigoidaan Finazillaan ja mennään "voucher" näkymässä kohtaan create new voucher ja valitaan päivä mille tosite halutaan tehdä sekä kirjoitetaan tositteelle selite kohtaan "description". Seuraavaksi valitaan vaihtoehto "import voucherline". Tiedot liitetään tyhjään kenttään painikkeella Ctrl + V.

[![](

Näkymässä voidaan määritellä, että mitä mikin Excelistä tuotava tieto on klikkaamalla näkymässä olevia otsikoita. Erityisesti mikäli aineisto sisältää dimensioita, tulee määritellä mistä dimensiosta on kyse. Kyseisessä esimerkissä oleva "hallinto" on dimension "maa/alue" arvo, jolloin valikosta valitaan vaihtoehto "maa/alue". Vastaavasti taas dimensionarvo "kuukausisopimukset" on dimension "asiakasryhmä" arvo.

[![](

Kun tiedot on tarkistettu ja määritelty halutusti, painike "generate voucher" luo tositteen esikatselun/manuaalisen syöttöikkunan. Tositetta voidaan vielä tässä kohdin täydentää tai muuttaa. Painamalla "create voucher" tosite luodaan ja tallennetaan.

[![](

## Esimerkki 4: tositerivit matriisidimensiolla

Tositteen tiedot ovat Excelissä oheisesti. Excel sisältää sekä myyntiä, että ostoa. Tiedostossa on kirjanpidon tili, summa sekä selite. Tiedostossa oleva myynti kohdistuu yrityksen dimension arvolle "kuukausisopimukset" (sarake D) sekä dimension arvolle "hallinto" (sarake E). Kyseessä on nk. matriisidimensio.

Huomaa, että koska tiedosto sisältää kahta eri dimensiota, tulee nämä laittaa Excelissä eri sarakkeisiin, jotta ne voidaan myöhemmässä vaiheessa määritellä omikseen.

[![](

Seuraavaksi Excelissä maalataan haluttu alue (eli kaikki rivit mitkä halutaan tuoda tositteelle) ja valitaan Ctrl + C. Tämän jälkeen navigoidaan Finazillaan ja mennään "voucher" näkymässä kohtaan create new voucher ja valitaan päivä mille tosite halutaan tehdä sekä kirjoitetaan tositteelle selite kohtaan "description". Seuraavaksi valitaan vaihtoehto "import voucherline". Tiedot liitetään tyhjään kenttään painikkeella Ctrl + V.

[![](

Näkymässä voidaan määritellä, että mitä mikin Excelistä tuotava tieto on klikkaamalla näkymässä olevia otsikoita. Erityisesti mikäli aineisto sisältää dimensioita, tulee määritellä mistä dimensiosta on kyse. Kyseisessä esimerkissä oleva dimensionarvo "kuukausisopimukset" on dimension "asiakasryhmä" arvo. Vastaavasti taas

"hallinto" on dimension "maa/alue" arvo, jolloin valikosta valitaan vaihtoehto "maa/alue".

[![](

Kun tiedot on tarkistettu ja määritelty halutusti, painike "generate voucher" luo tositteen esikatselun/manuaalisen syöttöikkunan. Matriisi kohdistuksen tiedot näkyvät nyt yhdessä kentässä kohdassa "dimensions". Tositetta voidaan vielä tässä kohdin täydentää tai muuttaa. Painamalla "create voucher" tosite luodaan ja tallennetaan.

[![](



artikkelin osoite on https://intercom.help/finazilla/fi/articles/8255242-tositteiden-luominen-kopioimalla-excelista

