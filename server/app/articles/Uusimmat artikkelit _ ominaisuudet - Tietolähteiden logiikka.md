## Tietolähteiden logiikka

[![](

*Versiopäivityksessä 3.7.2024 tuotu kokonaan uusi toiminto. Toiminto mahdollistaa tietolähteiden paremman järjestelyn raportilla. Uusi toiminto on mahdollinen vain uudessa beta -versiossa*

# Tietolähteiden logiikka

Finazillan raporteilla tulee olla aina vähintään yksi tietolähde (datasource), mutta tietolähteitä voi olla useita. Useita tietolähteitä tarvitaan esimerkiksi raporteilla, missä halutaan raportoida kuluvaa tilikautta ja edellistä tilikautta. Kuluva tilikausi, edellinen tilikausi ja näiden välinen erotus tarkoittaa raporttia, missä on jo kolme tietolähdettä. Finazillan raportointi toimii logiikalla, missä tietolähteet järjestellään aukeavaan raporttiin aakkosjärjestyksessä tietolähteen nimen mukaan.

## Aikaisemmat vaihtoehdot tietolähteiden järjestelemiseen

## Numerointi tai aakkostus

Käyttäjät ovat voineet vaikuttaa järjestymistapaan aikaisemmin muutamin eri konstein, kuten esimerkiksi käyttämällä tietolähteen nimen edessä numeroa tai kirjainta (esim. 1. Kuluva tilikausi, 2. Edellinen tilikausi).

## AZ ja ZA -järjestely

Toinen vaikutusmahdollisuus on löytynyt raportin kautta tietolähteen AZ to ZA valinnasta. Valinnan rajoitteena on kuitenkin ollut se, että esimerkiksi kolmen tietolähteen raporteissa ei ole aina saatu haluttua valintaa aikaan.

[![](

## Kaavoja ja/tai calculated values -tietoja sisältävien raporttien muokkaaminen pivotoinnin kautta

Kolmas vaihtoehto tietolähteiden järjestelyyn on pivotointi -näkymän kautta tehtävä järjestely. Tämä vaihtoehto on toimiva silloin, kun raportilla on mukana kaavoja tai calculated values -toiminnon kautta laskettuja asioita.

Näissä tilanteissa tietolähteet löytyvät pivotointi -näkymän values kentästä, jossa niitä voidaan uudelleenjärjestellä raahaamalla.

[![](

## Tietolähteiden järjestely raahaamalla \*uusi ominaisuus\*

Raportin oikeasta yläkulmasta löytyy painike nimeltä "format". Valikosta löytyy uusi vaihtoehto, nimeltä "reorder". Kyseinen valikko toimii tilanteissa, missä raportilla ei ole mukana kaava -tietolähteitä tai calculated values -toiminnon kautta tehtyjä laskettuja arvoja. Mikäli tarpeena on järjestellä tietolähteitä tällaisilla raportoilla, löytyy siihen ohjeet edeltävästä kappaleesta.

[![](

Aukeavassa ikkunassa näkyy kyseisen raportin tietolähteet vasemmassa reunassa ja oikeassa reunassa kerrotaan, mikä/mitkä yritykset raportilla ovat. Tietolähteitä voidaan raahata kentässä haluttuun järjestykseen ja tämän jälkeen painike "apply" tekee järjestelyn raportille.

[![](

## Eri tavat järjestellä raporttien tietolähteitä lyhyesti kuvattuna

Olemme kuvanneet alle vielä kaikki eri tavat järjestellä raportin tietolähteitä, sekä kunkin tavan rajoitteet ja mahdollisuudet.

* Tietolähteiden nimien edessä käytettävät numerot tai kirjaimet

  + Hyvää: toimiva vaihtoehto kaikissa raporteissa
  + Huonoa: ei haluttu tapa silloin, kun numero/kirjain häiritsee visuaalisesti
* Datasourcen kautta tehtävä AZ tai ZA järjestely

  + Hyvää: toimii aina raporteissa missä on kaksi tietolähdettä
  + Huonoa: Useimmiten ei toimi raporteissa missä on kolme tai enemmän tietolähdettä. Joskus voi niissäkin tuottaa halutun järjestyksen
* Kaavoja/laskettuja arvoja sisältävien raporttien järjesteleminen pivotoinnin kautta

  + Hyvää: toimii aina raporteissa, missä on mukana laskettuja arvoja (formula, calculated value)
  + Huonoa: Ei toimi helposti raporteissa, missä ei ole laskennallisia elementtejä
* Uusi reorder vaihtoehto

  + Hyvää: toimii aina kaikissa raporteissa, missä ei ole formula -tietolähdettä ja/tai calculated value:ta
  + Huonoa: ei toimi raporteissa, missä on kaavoja ja/tai calculated value:ta
[![](

*Toiminto mahdollistaa konserniyrityksillä konsolidoitujen raporttien tietolähteiden järjestelyn toiseen järjestykseen*



artikkelin osoite on https://intercom.help/finazilla/fi/articles/9560950-tietolahteiden-jarjestely-raportilla

