## Havainnollistavat esimerkit

Olemme kertoneet versiotiedotteessamme 21.4.2023 uudesta mahdollisuudesta generoida budjetti hyödyntämällä erilaisia tilikartan asetuksia. Tässä artikkelissa kerromme, kuinka tätä ominaisuutta voidaan hyödyntää tilanteissa, missä budjetille halutaan tuoda menneiden vuosien keskiarvot pohjatiedoksi.

Käyttäjä voi hyödyntää 21.4.2023 tuotua budjetin generointimenetelmää myös siten, että *yrityksen tilikartalle ei ole pakko asettaa asetuksia, vaan uusia asetuksia hyödynnetään pelkästään importissa*. Tämä mahdollistaa sen, että esimerkiksi vuoden 2023 budjetille saadaan vuosien 2019 - 2023 keskiarvot pohjatiedoksi. Toimintoa, ja sen ominaisuuksia, voi siis hyödyntää myös pelkästään toteumalukujen/budjettilukujen tuonnissa. Itse generointimenetelmää laajemmin, olemme kuvanneet mm. artikkelissamme [täällä.]( 

# Havainnollistavat esimerkit

Havainnollistamme asiaa esimerkin avulla.

**Esimerkki:**

Yrityksellä A on tilillä 3000 myyntiä kaudesta 1/2019 alkaen. Myynti aikavälillä 1/2019 - 12/2023 on yhteensä 22 614 273,44 euroa.

Yritys haluaisi luoda budjetin, missä hyödynnetään kyseisen myynnin (22 614 273,44€) keskiarvoa pohjatietona.

Ensimmäisenä tulee luoda Finazillaan budjetti halutulle aikajaksolle. Tämän jälkeen hyödynnetään budjetin import balance -työkalua. Koska toteuma halutaan tuoda vain yhdelle tilille, mennään työkaluun kyseisen rivin rivityökalujen kautta.

[![](

Seuraavaksi aukeaa ns. määrittelyikkuna, jossa kerrotaan "From" kohdassa, mistä aikavälistä toteuma halutaan tuoda. Tässä tapauksessa haluttiin tuoda aikavälin 1/2019 - 12/2023 toteumat. "To" kohtaan tulee oletuksena aina se aikaväli, mille budjetti on luotu. Tämä määrää sen, miten pitkälle aikajaksolle luvut tuodaan.

[![](

*To ja From aikajaksojen ei ole pakko olla yhtä pitkät silloin kun käytetään jotain muuta valintaa kuin perinteistä "import as is" -menetelmää*

Tässä esimerkissä haluttiin tuoda toteumat keskiarvoina, joten "import data transformation method" kohtaan valitaan vaihtoehto "average".

Yläosan "Import mode" kohdassa voidaan määritellä, miten toteumat tuodaan suhteessa dimensioihin. Tässä esimerkissä dimensiot summataan yhteen.

[![](

Import -painikkeella tuonti tehdään. Budjetille tulee kausille 1-12/2023 keskiarvoinen myynti tililtä 3000. Keskiarvo lasketaan myynti (22 614 273,44€) jaettuna kuukausien määrällä. Jos myyntiä oli siis vuosilla 2019-2023, on kausia yhteensä 60 (12 kuukautta \* vuosien määrä). Näin ollen keskiarvoinen myynti on 22 614 273,44€ / 60 = 376 904,55€.

Finazilla tuo myynnin budjetille kausille 1-12. Rivi käyttäytyy tämän jälkeen tavallisen syöttörivin tavoin.

[![](

[![](

*Huomaa myös muut transformation method kohdassa olevat vaihtoehdot. Tätä ohjetta voidaan hyödyntää myös muiden valintojen kanssa (mm. latest)*



artikkelin osoite on https://intercom.help/finazilla/fi/articles/7801796-esimerkki-budjetille-pohjatiedoksi-menneiden-vuosien-keskiarvot

