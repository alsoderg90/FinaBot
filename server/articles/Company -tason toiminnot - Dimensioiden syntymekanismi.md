## Dimensioiden syntymekanismi

[![](

*Versiopäivityksessä 25.5.2023 tuotu kokonaan uusi toiminto. Toiminto mahdollistaa haluttujen dimensioiden arvojen uudelleen nimeämisen massana muotoon koodi + nimi*

Tämä artikkeli koskettaa vain niitä asiakkaita, jotka haluavat dimensioidensa arvojen olevan Finazillassa muotoa dimension arvon koodi + nimi, eikä pelkkä dimension arvon nimi. Koodien tuominen nimeen helpottaa mm. raporttien filtteröinnissä.

# Dimensioiden syntymekanismi

Finazillaan syntyy dimensiot lähdejärjestelmistä siten, että dimension nimi sekä koodi tulevat omiin kenttiinsä. Koodi tulee asiakkaan lähdejärjestelmästä. Dimension sisällä myös yksittäiset dimension arvot (dimension value codes) syntyvät siten, että niillä on nimi sekä koodi.

Asiakkaat ovat tähänkin saakka voineet "uudelleen nimetä" dimensioita ja dimension arvoja käyttämällä "name to display in Finazilla" kenttää. Muutos on kuitenkin pitänyt tehdä jokaiselle dimensiolle ja dimension arvolle yksitellen.

[![](

# Massana nimien muuttaminen

Jatkossa käyttäjät voivat uudelleen nimetä dimensionarvoja siten, että niiden uudeksi nimeksi tulee koodi + nimi -yhdistelmä. Muutos tehdään valitsemalla haluttu dimensio valikossa company kohdassa "dimensions". Haluttua dimensiota klikataan, jolloin kyseisen dimension asetukset aukeavat. Valita tehdään ruksittamalla kohta "generate value display names".

[![](

Käytännössä muutos tarkoittaa sitä, että jos ennen muutosta asiakkaalla on ollut dimensio nimeltä Projekti ja sen alla dimensionarvo nimeltä Projekti A, jonka koodi (code) on ollut 1234, on muutoksen jälkeen kyseisen dimensionarvon uusi nimi "1234 Projekti A". Dimensionarvo esiintyy kaikkialla Finazillassa uudella nimellä.

# Massamuutoksen peruminen

Täpän "generate value display names" voi käydä ottamassa myös pois, jolloin dimension arvojen nimet palautuvat alkuperäiseen tilanteeseen. Tällöin tulee huomioida, että mahdolliset jo tehdyt ja pivotoidut raportit saattavat muuttua ei haluttuun suuntaan.

[![](

 *Dimension nimet eivät muutu, vain dimensionarvot uudelleen nimetään*



artikkelin osoite on https://intercom.help/finazilla/fi/articles/7931801-dimension-arvojen-uudelleen-nimeaminen-massana

