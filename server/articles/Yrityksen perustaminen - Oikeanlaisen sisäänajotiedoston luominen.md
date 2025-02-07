## Oikeanlaisen sisäänajotiedoston luominen

Artikkelimme ["raportointikoodi apuna konserniyritysten raportoinnissa"]( kuvaa yleisellä tasolla, miten raportointikoodia voidaan hyödyntää sellaisten konserniyritysten avaustoimissa, joilla on käytössään jokin muu tilikartta kuin liikekirjurin tilikartta.

Tässä artikkelissa näytämme konkreettisesti, miten raportointikoodit voidaan tuoda massana Finazillaan samalla, kun yrityksen tilit luetaan sisään Finazillaan.

**Esimerkki**

Yrityksen tilikartassa on tili 5200 Toimitilavuokrat. Liikekirjurin tilikartassa toimitilavuokrat ovat kuitenkin tilillä 7230.

# **Oikeanlaisen sisäänajotiedoston luominen**

Tilien tuomista olemme kuvanneet tarkemmin artikkelissamme ["Yrityksen kirjanpidon tilien tuominen"]( Yrityksen tilejä sisääntuotaessa tiedostossa kerrotaan, että kyseiselle tilille 5200 asetetaan raportointikoodiksi 7230. Sisäänajotiedosto näyttää siis oheiselta:

[![](

 otiedosto

## Tiedon vaatimukset

* Sarake A = tilin numero
* Sarake B = tilin nimi
* Sarake C = raportointikoodi, mikäli sellainen halutaan tuoda
* Tallennetaan unicode.txt muotoon

Tämän jälkeen yrityksen tilit voidaan lukea sisään valikossa company -accounts käyttämällä yläosan painiketta "import accounts". Kyseinen tili tulee Finazillaan sisään siten, että sen raportointikoodi tulee mukana ja näkyy kentässä "reporting code".

[![](

Tilit voidaan tuoda tarpeen mukaan sisään uudelleen, mikäli jotakin raportointikoodeja halutaan korjata. Yksittäisen koodin voi myös korjata manuaalisesti valikossa "company" kohdassa "accounts" ja avaamalla halutun tilin edit -tilaan.

[![](



artikkelin osoite on https://intercom.help/finazilla/fi/articles/5570907-esimerkki-tilien-tuominen-raportointikoodia-kayttamalla

