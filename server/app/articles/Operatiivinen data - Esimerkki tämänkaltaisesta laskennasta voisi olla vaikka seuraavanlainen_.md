## Esimerkki tämänkaltaisesta laskennasta voisi olla vaikka seuraavanlainen:

Tässä artikkelissa kuvaamme yhden esimerkkitapauksen siitä, miten operatiivista dataa voidaan raportoida omalla raporttimallilla kirjanpidon dimensiota vasten. Artikkeli on suunnattu edistyneemmille käyttäjille, joille operatiivisen datan käyttäminen Finazillassa on jo tuttua. Varsinaista operatiivisen datan perusraportointia olemme käsitelleet aikaisemmassa artikkelissamme ["Operatiivisen datan raportointi".](

Joskus käyttäjälle voi tulla eteen tilanne, että raportille filtteröidään jokin tietty kirjanpidon dimensio ja halutaan sen jälkeen laskea operatiivisia tunnuslukuja tehtyä valintaa vasten. Kyseinen käyttötapa on erityistapaus, eikä siten tule vastaan ihan jokaisella käyttäjällä.

# Esimerkki tämänkaltaisesta laskennasta voisi olla vaikka seuraavanlainen:

yrityksen myynnit tulevat kirjanpidosta. Myynnit on kohdistettu dimensioille, jotka ovat yrityksen kolme kauppaa, jotka sijaitsevat Tampereella, Jyväskylässä ja Helsingissä. Tämä on esimerkin kirjanpidon data.

​

Yrityksellä on lisäksi operatiivista dataa, joista yhtenä on valmistustunnit. Yrityksen tuotteita ovat muki, pannu ja hella. Nämä ovat operatiivisia dimensioita. Yrityksen valmistustunnit on kohdistettu valmistettaville tuotteille siten, että mukin tekemiseen menee 5 tuntia, pannun tekemiseen 1 tunti ja hellan tekemiseen 2 tuntia. Tämä kokonaisuus on yksi yrityksen operatiivinen data. Finazillassa kyseinen data on ns. DataGroup".  
​

Yritys haluaa näiden kahden tiedon perusteella laskea Finazillan avulla operatiivista tuotekohtaista tehokkuutta, sekä kirjanpidon tehokkuutta kauppakohtaisesti. Kyseinen toiminto mahdollista tämänkaltaisen laskennan.

Esimerkin hahmottamiseen saattaa auttaa asian purkaminen sellaiseen muotoon, miten se Excel -taulukossa voitaisiin laskea. Alla on tästä esimerkki.

[![](

Finazillassa on toimintalogiikkana, että kun valitaan raportille "Dimensions / column" valinta niin laskenta tehdään dimensiokohdistuksen sisällä. Tämä tarkoittaa sitä, että jos on [Myynti] - [Kulut] niin tämä aukeaa "Dimensions / column" valinnalla useaksi laskuoperaatioksi, jotka suomentuvat esimerkiksi kaupungeittain otetussa raportissa seuraaviksi [Tampereen myynti] - [Tampereen kulut], [Jyväskylän myynti] - [Jyväskylän kulut], [Helsingin myynti] - [Helsingin kulut].

Kuvattu logiikka ei toimi tässä esimerkissä, sillä laskentakaavan tekijät eivät ole samoilla dimensioilla; toinen on operatiivisilla dimensioilla ja toinen kirjanpidon dimensioilla.

Kun halutaan tunnuslukuja, jotka lasketaan kirjanpidon datan kokonaisarvosta jaoteltuna operatiivisten dimensioiden suhtaan, ei tällaista "aukeavaa" laskentaa tarvitse saada tehtyä. Tällöin voidaan määritellä raporttimallilla, että halutaankin `DIMTOTSUM([Myynti])-[KULUT]`. Kyseinen valinta aukeaa edellisen kaltaisessa kaupungittaisessa raportissa seuraaviksi operaatioiksi:

* `[myynti] - [Tampereen kulut]`
* `[myynti] - [Jyväskylän kulut]`
* `[myynti] - [Helsingin kulut]`

Alla lisäesimerkkejä toiminnon kuvaamiseksi.

## Esimerkki 1: Hybridi laskenta filterillä

Alla olevassa datassa on operatiivinen kappalemääräinen myynti ja kirjanpidosta otettu euromääräinen myynti. Tarve on raportoida tietyn kirjanpidon dimension ja operatiivisen dimension suhdetta toisiinsa.

[![](

## Esimerkki 2: Operatiivinen kustannuslaskenta

Operatiivisena datana tässä esimerkissä on postikulut kaupungeittain, sekä toimitetut paketit kaupungeittain ja tuotteittain. Postikulujen kustannusperuste on prosenttiosuus kokonaistoimituksien suhteen.

[![](

.



artikkelin osoite on https://intercom.help/finazilla/fi/articles/4294086-esimerkki-kirjanpidon-dimension-filtterointi-seka-operatiivisten-tunnuslukujen-laskenta-tehtya-valintaa-vasten

