## DISTRIBUTION - TYYPPINEN VYÖRYTYSSÄÄNTÖ

Vyörytyssääntöihin tutustuessa kannattaa lukea ensimmäisenä artikkelimme ["mitä vyörytyssäänöt ovat ja miten niitä voidaan käyttää Finazillassa?"](

Vyörytyssääntöjä on kahdenlaisia; "distribution" ja "distribution to siblings". Distribution -sääntö jakaa valitun dimension sisällä dimensiovalueille halutussa % suhteessa. Distribution to siblings -sääntö taasen jakaa valitulta dimensiovaluelta halutuille muille dimensiovalueille halutussa % osuudessa.

Käytännössä vyörytyksen tekeminen on kummassakin vaihtoehdossa 2 –vaiheinen:

1. Ensin luodaan sääntö vyörytykselle yrityksen taakse Company -valikossa
2. Luotua sääntöä käytetään budjetilla halutussa kohtaa
# DISTRIBUTION - TYYPPINEN VYÖRYTYSSÄÄNTÖ

**Taustaa**

Yrityksellä on dimensio nimeltä maa/alue. Dimension alla on dimensiovaluet Ranska, Puola ja Saksa. Vyörytyssäännössä voidaan valita, mikä prosentuaalinen osuus kohdistuu kullekin dimensiovaluelle. Kohdistetaan esimerkiksi Ranskalle 35%, Puolalle 40% ja Saksalle 25%.

Alkuperäinen kirjaus tehdään tässä vaihtoehdossa ns. yritystasolle eli Finazillassa arvolle "blank" budjetin puolella.

## Vyörytyssäännön luominen (distribution)

Valitaan vasemman yläkulman Company -valikosta rolling rule templates -toiminto. Vyörytyssääntö luodaan oikeasta yläkulmasta painikkeesta "create rolling rule".

Vyörytyssäännölle annetaan kuvaava nimi, jotta jatkossa on helppoa valita oikea vyörytyssääntö budjetoidessa. Esimerkki hyvästä vyörytyssäännön nimestä voisi olla vaikka ”Hallintokulujen jakaminen kustannuspaikoille”.

Tämän jälkeen valitaan type -kentään vaihtoehto "distribution" ja kenttään "dimension" se dimensio, missä vyörytystä halutaan tehdä. Total Amount to share -kohdassa määritellään kuinka suuri % -osuus halutaan vyöryttää. Jos ko. dimensiolta halutaan vyöryttää esimerkiksi 100%, valitaan kenttään 100. Jos taas kenttään valitaan vaikkapa 60, tekee vyörytyssääntö 60% osalta vyörytyksen ja jättää loput 40% ennalleen. Create -painike luo vyörytyssäännön.

Tämän jälkeen valitaan luotu vyörytyssääntö listasta sen nimeä klikkaamalla, jolloin avautuu oheinen syöttöikkuna, johon syötetään kullekin dimensiovaluelle haluttu prosenttiosuus.

[![](

# DISTRIBUTION TO SIBLINGS - TYYPPINEN VYÖRYTYSSÄÄNTÖ

​**Taustaa**

Yrityksellä on edelleen dimensio nimeltä maa/alue, jossa on dimensiovaluet Ranska, Puola ja Saksa. Valitaan, että dimensiovaluelta Ranska kohdistetaan 75% dimensiovaluelle Puola ja 25% kohdistetaan dimensiovaluelle Saksa.

Alkuperäinen kirjaus tehdään tässä vaihtoehdossa dimensioarvolle "Ranska" budjetin puolella.

## Vyörytyssäännön luominen (distribution to siblings)

Valitaan vasemman yläkulman Company -valikosta rolling rule templates -toiminto. Vyörytyssääntö luodaan oikeasta yläkulmasta painikkeesta "create rolling rule".

Vyörytyssäännölle annetaan kuvaava nimi, jotta jatkossa on helppoa valita oikea vyörytyssääntö budjetoidessa. Esimerkki hyvästä vyörytyssäännön nimestä voisi olla vaikka ”Hallintokulujen jakaminen kustannuspaikoille”. Tämän jälkeen valitaan type -kentään vaihtoehto "distribution to siblings" ja kenttään "dimension value" se dimensiovalue, missä vyörytystä halutaan tehdä. Create -painike luo vyörytyssäännön.

Tämän jälkeen valitaan luotu vyörytyssääntö listasta sen nimeä klikkaamalla, jolloin avautuu oheinen syöttöikkuna, johon syötetään kullekin dimensiovaluelle haluttu prosenttiosuus.

Alla on esimerkki yhdestä vyörytyssäännöstä.

Oheinen sääntö tarkoittaa käytännössä sitä, että jos kyseinen vyörytyssääntö olisi kiinnitetty vaikkapa hallintokuluihin, niin kaikista dimensiovaluelle "Ranska" kohdistuneista hallintokuluista 15 % jäisi dimensiovaluelle Ranska, ja loput kohdistuisivat siten, että 50 % menisi dimensiovaluelle "Puola", 25 % dimensiovaluelle "Kiina" ja 10 % dimensiovaluelle "Intia".

[![](

Vyörytyssääntöjä voi luoda niin paljon kuin on tarpeen ja luotuja vyörytyssääntöjä voi käydä päivittämässä.

[![](

*Dimensiokombinaatioille syötettyjä lukuja ei voi vyöryttää. Lisäksi lukuja, joilla on jo jokin dimensiokohdistus ei voi vyöryttää.* 

# Lisätietoja

[Mitä vyörytyssäännöt ovat ja mihin niitä käytetään?](

[Yleistä budjetoinnista](

[Vyörytyssääntöjen käyttäminen budjetilla](



artikkelin osoite on https://intercom.help/finazilla/fi/articles/4175022-vyorytyssaannon-luominen-yrityksellle

