## Rajapinnan kytkeminen päälle Finazillassa

Tässä ohjeessa kuvaamme, miten API -rajapinta voidaan kytkeä päälle Finazillassa. Ennen kytkentää lähdejärjestelmässä on pitänyt luoda lähdejärjestelmäkohtaisen ohjeen mukaisesti API -rajapintatunnukset.

Tätä ohjetta voidaan hyödyntää kaikkien olemassa olevien API -rajapintojen kytkemiseen, eli sama ohje toimii mm. Procountor, Netvisor, Lemonsoft, Fivaldi jne integraatioihin.

# Rajapinnan kytkeminen päälle Finazillassa

Lähtökohtaisesti Finazillan käyttöönotosta vastaava henkilö huolehti integraation kytkemisestä päälle, mutta tilitoimistoasiakkailla on mahdollisuus kytkeä integraatio itse päälle.

Integraatio kytkentään päälle valikossa Company > settings. Valikossa on oma välilehti nimeltä "integrations". Uusi integraatio luodaan painikkeesta "create".

[![](

Tämän jälkeen alasvetovalikosta valitaan oikea lähdejärjestelmä (esim. Procountor) ja painetaan uudelleen "create". Finazillaan ilmestyy oheinen näkymä. Integraation perässä on painike "edit", josta päästään syöttämään API -avaimet.

[![](

Näkymä aukeaa oheisesti. Integraatio -järjestelmän käyttäjätunnus syötetään username kenttään ja API -avain, eli salasana, syötetään password -kenttään. Tietojen syöttämisen jälkeen painetaan update, jolloin tiedot tallennetaan ja rajapinta on käytettävissä.

[![](

[![](

*Joissain harvinaisemmissa integraatiossa näkymä voi poiketa edellisestä ja täytettäviä kenttiä on enemmän. Epäselvissä tilanteissa pyydämme olemaan yhteydessä asiakaspalveluumme ([asiakaspalvelu@finazilla.fi](mailto:asiakaspalvelu@finazilla.fi))*

### Datojen ajaminen kytkemisen jälkeen

Kun rajapinta aukaistaan, tulee avauksen jälkeen ajaa datat Finazillaan sisään. Jos yrityksen datat halutaan vaikkapa kahdelta edeltävältä vuodelta, tulee Finazillan tilikausiin (company --> accounting periods) perustaa kaksi edeltävää tilikautta ja sen jälkeen tositteet tulee ajaa sisään kahden edeltävän vuoden ajalta. Suosittelemme ajamista tilikausi kerrallaan.

Datojen ajamista olemme kuvanneet tarkemmin [täällä.]( 

Kun datat on ajettu sisään, suosittelemme täsmäyttämään lähdejärjestelmän tuloslaskelman ja taseen Finazillan tuloslaskelman ja taseen osalta. Näin voidaan varmistua tietojen oikeellisuudesta.

# Rajapinnan muokkaaminen

Kun lähdejärjestelmä on aukaistu muokattavaksi, on näkymässä välilehti "advanced settings". Lisäasetuksissa voidaan muokata kyseistä integraatiota muutamin eri tavoin.

[![](

Valikossa näkyvä ***number of days to include in scheduled run*** tarkoittaa, montako päivää taakse päin datat synkronoidaan joka yö. Oletusvalinta on 100 päivää. Emme suosittele jatkuvassa integraatiossa merkittävästi suurempaa arvoa, mutta päivää voi rajata alaspäin.

***Transfer schedule as cron*** liittyy siihen, miten usein datat haetaan rajapinnan kautta. Lähtökohtaisesti käyttäjän ei tarvitse koskea kenttään, vaan datat haetaan joka yö.

***Material types*** -kentässä voidaan rajata, mitä dataa integraatiossa siirretään. Mikäli esimerkiksi Procountorista, Netvisorista tai Lemonsoftista ei haluta tuoda myyntilaskuja. voidaan oheisen kentän avulla rajata, että vain kirjanpidon tositteet (vouchers) tuodaan.

***Exclude accounting dimensions*** ja ***exclude operative dimensions*** liittyvät dimensioiden rajaamiseen. Aihetta on kuvattu tarkemmin [täällä.]( 

Haluttujen muokkausten jälkeen tulee painaa "update", jotta muutokset astuvat voimaan.



artikkelin osoite on https://intercom.help/finazilla/fi/articles/9572860-api-rajapinnan-kytkeminen-paalle-ja-integraation-muokkaaminen

