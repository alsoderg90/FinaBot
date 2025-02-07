## Raportin luominen

Tässä esimerkissä kerromme, miten voidaan luoda raportti, jossa esitetään esimerkiksi koko vuoden budjetti yhteenlaskettuna, koko vuoden toteuma yhteenlaskettuna, budjetti kuukausitasoisena sekä toteuma kuukausitasoisena.

Tämän artikkelin ymmärtämisen edellytyksenä on, että käyttäjä osaa tehdä raportteja ja tietää raportoinnin perusvalinnat, sillä tässä artikkelissa emme erikseen kuvaa jokaista tehtävää valintaa syvällisesti.

# Raportin luominen

Tässä esimerkissä raportti luodaan käyttämällä valmista system- tasoista raporttimallia "tuloslaskelma". Raportille valitaan date -format kohtaan oheinen valinta.

[![](

Raportti luodaan 4. tietolähteen raporttina siten, että tietolähteet ovat oheiset:

1. Budjetti yhteensä
2. Toteuma yhteensä
3. Budjetti kuukausittain
4. Toteuma kuukausittain

Tietolähteet 1 ja 2 tehdään kumpikin valinnalla "accounting period per column", tai "total reporting period" jolloin saadaan raportille vain yhteenlaskettu saldo.

[![](

Seuraavissa kahdessa tietolähteessä vastaava valinta on "month/column", sillä näissä halutaan raportoida kuukausittaista dataa.

# Raportin pivotointi

Avautuva raportti ei ole vielä parhaassa mahdollisessa muodossa, vaan raporttia on syytä pivotoida. Pivotoinnissa käännetään datasourcen ja daten paikkaa, eli laitetaan date ensin columns -laatikkoon.

[![](

Raportin pivotoinnin jälkeen raportilla on ensimmäisenä vuotuiset yhteenlasketut arvot ja sen jälkeen kuukausittaiset arvot sekä toteumasta, että budjetista

[![](



artikkelin osoite on https://intercom.help/finazilla/fi/articles/5990943-esimerkki-luodaan-raportti-jossa-on-vuositasoista-seka-kuukausitasoista-dataa

