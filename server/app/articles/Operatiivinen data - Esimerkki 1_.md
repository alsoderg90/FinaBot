## Esimerkki 1:

Olemme aikaisemmassa artikkelissamme ["Esimerkki: dimensiokohdistuksen valuttaminen lapsiriveille"]( kertoneet, miten dimensioita voidaan valuttaa hierarkisessa rakenteessa alempana oleville lapsiriveille. Tämä artikkeli on jatkumoa aikaisemmalle artikkelillemme. Tässä artikkelissa kerromme, miten voidaan kopioida (duplicate) rivejä. Havainnollistamme asiaa kahden esimerkin avulla.

# Esimerkki 1:

Yrityksellä on edelleen 3 tehdasta ja näissä kaikissa valmistetaan yrityksen tuotteita holkki, mäntä, akseli ja ruuvi. Budjetointia tehdään tehdaskohtaisesti siten, että budjetoidaan myytävien tuotteiden kpl määrää. Budjettia seurataan kahdella dimensiokohdistuksella, jotka ovat tehdas + tuote.

Yrityksellä on luotuna hierarkinen budjettipohja tehtaalle 1 oheisesti. Kullekin tuotteelle on käyty tekemässä data group kiinnitys, kerrottu budjetoidaanko quantity vai amount määrettä sekä käyty kiinnittämässä oikea tuote dimensio.

[![](

## Rakenteen kopiointi

Yritys haluaa luoda vastaavat hierarkiset rakenteet tehtaille 2 ja 3. Sen sijaan, että lähdettäisiin luomaan rakennetta käsin, voidaan oheinen rakenne kopioida. Tällöin otetaan esimerkin mukaisessa tapauksessa rivin "tehdas 1" takaa auki rivikohtaiset työkalut ja valitaan vaihtoehto "create duplicates"

[![](

Tämän jälkeen käyttäjälle aukeaa oheinen ikkuna

[![](

Esimerkin tapauksessa halutaan luoda seuraava hierarkinen rakenne, joka kohdistetaan tehtaalle 2. Tällöin valitaan duplication mode -kohtaan oletusvalinta "copy for dimension values", joka mahdollistaa sen, että kopioitavaan rakenteeseen voidaan kertoa uudeksi dimensiokohdistukseksi "tehdas 2". Valinta "single copy" tuottaisi täysin identtisen kopion. Kenttään "generate new row for dimension value", valitaan dimension arvo "tehdas 2".

[![](

Tämän jälkeen Finazillaan syntyy identtinen hierarkinen rakenne tehtaalle 2, jossa on dimensio kiinnitykset oikein.

[![](

[![](

*Tuoteriveille tulee asettaa tehdas 1 rakenteessa rivin asetuksissa operatiivinen dimensio -kohdistus, jotta seuraavissa rakenteissa sama kohdistus tulee muihinkin rakenteisiin*

# Esimerkki 2:

Yrityksellä on edelleen 3 tehdasta ja näissä kaikissa valmistetaan yrityksen tuotteita holkki, mäntä, akseli ja ruuvi. Budjetointia tehdään tehdaskohtaisesti siten, että budjetoidaan tuotteiden myyntejä ja ostoja euroissa. Budjettia seurataan yhdellä dimensio kohdistuksella, joka on tehdas.

Yrityksellä on luotuna hierarkinen budjettipohja tehtaalle 1 + yhdelle tuotteelle oheisesti.

[![](

Nyt budjettipohjaan halutaan tuoda loputkin yrityksen tuotteet samaan hierarkiseen rakenteeseen mukaan. Sen sijaan, että lähdettäisiin luomaan rivejä yksitellen käsin, luodaan rivit käyttämällä "create duplicates" toimintoa.

Kopiointia lähdetään tekemään tuote -riviltä, sillä budjettiin halutaan kopioida loput puuttuvat tuotteet.

[![](

Seuraavaksi valitaan kaikki halutut tuotteet kerralla kohtaan "generate new row for dimension values". Näin toimien voidaan luoda massana isokin määrä uusia rivejä.

[![](

Tämän jälkeen toiminto "duplicate row" generoi uudet rivit osabudjettiin.

[![](



artikkelin osoite on https://intercom.help/finazilla/fi/articles/5447799-esimerkki-hierarkisen-rakenteen-kopioiminen-dimensio-kohdistuksin

