## Raporttimallin tekeminen

[![](

*Versiopäivityksessä 4.10.2024 tuotu kokonaan uusi toiminto. Toiminto helpottaa mm. tilanteissa, missä halutaan raportoida esimerkiksi lukuja "tietty dimensio, paitsi joku"*

Tässä artikkelissa kerromme, kuinka raporttimallin kautta voidaan lähteä rajaamaan raportille nostettavia dimensioita hieman uudella tavalla. Artikkelin ymmärtämistä helpottaa, jos käyttäjä osaa jo tehdä raporttimalleja Finazillassa, ymmärtää mitä dimensiot ovat, sekä ymmärtää myös mitä matriisidimensiot tarkoittavat.

# Raporttimallin tekeminen

Ominaisuutta käytetään raporttimallin kautta (report scheme). Raporttimallien dimensio -rajausta on kuvattu tarkemmin ohjeessamme [täällä.](

Kun raporttimallilla on balance data tyyppinen rivi (rivi jossa kerrotaan raportoitava tili/tiliväli), niin rivin asetuksissa voidaan vaikuttaa siihen, minkä dimensioiden lukuja riville nostetaan. Valikosta löytyy yritystason blank (vihreällä merkitty), kunkin dimension blank (keltaisella merkitty) sekä kaikki varsinaiset muut dimensiot ja dimensionarvot. Keltaisella merkityt dimensiotasoiset "blankit" ovat uusi ominaisuus.

[![](

Kuvaamme raporttimallin kautta tehtäviä dimensiorajauksia alla erilaisin esimerkein. Osa esimerkeistä on sellaisia, että ne ovat onnistuneet jo aikaisemmin, kun taas osa on uusia mahdollisuuksia.

# Havainnollistavat esimerkit erilaisista dimensio -rajauksista

#### Taustatietoa

Yrityksellä on kaksi dimensiota; kaupunki ja kustannuspaikka. Dimensiossa kaupunki on kolme arvoa: Jyväskylä, Tampere ja Helsinki. Dimensio kustannuspaikka sisältää kaksi arvoa: hallinto ja markkinointi.

Yrityksellä on myyntiä tilillä 3000 kaudella 1/2024 ***yhteensä 47 5000€.*** Myynti jakautuu oheisesti:

* Tampere: 5 500€ ***(kaupunki)***
* Jyväskylä 17 000€ ***(kaupunki)***
* Myynti ilman mitään kohdistusta: 2 000€ ***(yritystason blank)***
* Tampere + Hallinto: 6 000€ ***(kaupunki + kustannuspaikka)***
* Jyväskylä + Hallinto: 4 000€ ***(kaupunki + kustannuspaikka)***
* Hallinto: 1 000€ ***(kustannuspaikka)***
* Markkinointi 12 000€ ***(kustannuspaikka)***
## Esimerkki 1: halutaan raportoida luvut, joissa ei ole mitään kohdistusta

Raporttimallille asetetaan dimensio -rajaukseen yllä olevassa kuvassa oleva yritystason blank -valinta, joka on yllä olevassa kuvassa vihreällä merkittynä.

[![](

Raporttiin nousee myyntiä 2 000€, eli vain se myynti, jolla ei ole mitään kohdistusta missään (nk. yritystason blank).

Kyseisen valinnan on voinut tehdä aikaisemminkin Finazillan raportoinnissa. Saman lopputuloksen saa myös raportoimalla myyntiä ilman dimensiorajausta raportilla ja valitsemalla require exact dimension selection -valinnan päälle.

## Esimerkki 2: halutaan raportoida myynnit, joissa on hallinto -kohdistus

Raporttimallille asetetaan dimensio -rajaukseen hallinto -dimensio. Raporttiin nousee tällöin kaikki luvut, joissa on hallinto -dimensio jollain tapaa osallisena. Huomaa, että tällä valinnalla raporttiin nousee siis luvut, jotka ovat jollain matriisilla, kuten vaikkapa Hallinto + Tampere yhdistelmällä oleva 6000€ myynti.

[![](

Raporttiin nousee myyntiä yhteensä 11 000€. Myynteihin lasketaan 6000€ (Tampere + hallinto) + 4000€ (Jyväskylä + hallinto) + 1000€ (hallinto).

Kyseisen valinnan on voinut tehdä aikaisemminkin Finazillan raportoinnissa. Saman lopputuloksen saa myös raportoimalla myyntiä ja valitsemalla dimension -rajaukseen valinnan hallinto.

## Esimerkki 3: halutaan raportoida myynnit, joissa ei ole mitään kaupunkia

Raporttimallille asetetaan dimensio -rajaukseen kaupunki -dimension alla oleva blank.

[![](

Raporttiin nousee myyntiä yhteensä 15 000€, joka tulee: myynti ilman mitään kohdistusta 2000€ + hallinto 1000€ + markkinointi 12 000€. Raporttiin nousee siis luvut, joissa ei esiinny mitään kaupunki -kohdistusta.

Kyseistä valintaa ei ole voinut tehdä aikaisemmin Finazillan raportoinnissa. Raportoimalla Finazillassa käyttämällä kaupunki dimensiota rajaavana tekijänä, saa raportin, jonka lopputulos on 32 500€. Luku muodostuu kaikista luvuista, missä kaupunki esiintyy joko yksin, tai toisen osapuolen kanssa. 32 500€ muodostuu 5500€ + 17000€ + 6000€ + 4000€. Kyseessä on siis kaksi erilaista tapaa raportoida ja siten niiden lopputuloksetkin eroavat toisistaan.

Mikäli kaupunki dimensio -rajauksessa laittaa päälle valinnan "require exact dimension selection", tuottaa Finazilla raportin, jonka lopputulos on 0€, sillä missään ei esiinny kohdistusta pelkälle kaupunki -dimensiolle, vaan kohdistukset ovat dimensionarvoilla. Tämän lisäksi yksittäisiä kaupunkeja on pystynyt raportoimaan joko ilman require exact dimension selection -valintaa, tai sen kanssa.

## Esimerkki 4: halutaan raportoida myynnit, joissa on kustannuspaikka, mutta ei kaupunkia

Raporttimallille asetetaan dimensio -rajaukseen valinta kustannuspaikka, sekä kaupunki -dimension alla oleva blank.

[![](

Raportille nousee myyntiä yhteensä 13 000€, joka tulee markkinoinnille kohdistetusta myynnistä 12 000€+ hallinnolle kohdistetusta myynnistä 1000€. Kyseistä valintaa ei ole voinut tehdä aikaisemmin Finazillan raportoinnissa. Raporttiin nousee siis luvut, joilla on joku kustannuspaikka ja ei mitään kaupunkia.

## Esimerkki 5: halutaan raportoida Jyväskylän myynnit niiden myyntien osalta, jossa ei ole kustannuspaikkaa

Raporttimallille asetetaan dimensio -rajaukseen kaupunki Jyväskylä, sekä kustannuspaikan alla oleva blank.

[![](

Raportille nousee myyntiä 17000€, joka on Jyväskylälle kohdistuva myynti ilman mitään muuta kohdistusta. Huomaa, että matriisille Jyväskylä + Hallinto kohdistuva 4000€ myynti ei nouse raporttiin tällä valinnalla.

## 



artikkelin osoite on https://intercom.help/finazilla/fi/articles/9564679-raporttimallin-riville-mahdollisuus-sisallyttaa-arvo-jota-ei-ole-kohdistettu-tietylle-dimensiolle

