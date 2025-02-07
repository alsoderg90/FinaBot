## Miksi käyttää lukituspäivää eli lock date -toimintoa?

# Miksi käyttää lukituspäivää eli lock date -toimintoa?

Asiakkaan voi olla mielekästä lukita Finazillassa aina se kuukausi mihin saakka kirjanpito on tehty valmiiksi ja lukittu lähdejärjestelmässä. Tämä mahdollistaa sekä raportoinnin hyödyntämisen lock date - valinnan kautta, että myöskin auttaa hahmottamaan mikä data on vahvistettua ja muuttumatonta - ja mihin taas vastaavasti voi tulla vielä muutoksia.

Lock Date -toiminto mahdollistaa dynaamisesti päivittyvät raportit ja ennusteet, eikä se vaikuta millään tavalla aineiston noutoon. Näin ollen Lock Date -toiminnon käyttäminen ei tarkoita sitä, että mikäli kirjanpitoon tehtäisiinkin vielä muutoksia, etteivätkö ne päivittyisi oikein Finazillaan oikeille kuukausille.

# Lukituspäivän (eli lock date:n) asettaminen

Lock Date -toiminnon asettaminen tehdään valikossa Company - Accounting Periods kohdassa "Lock Date". Update Accounting Lock Date -painike tallentaa muutoksen. Lukituspäivän voi asettaa ainoastaan yrityksen aktiiviselle tilikaudelle. Mikäli aktiivinen tilikausi vaihdetaan, ja lukituspäivä on jollain muulla kaudella, ehdottaa Finazilla lukituspäiväksi tilikauden ensimmäistä kuukautta.

[![](

# Lukituspäivän hyödyntäminen raportoinnissa

Raportoinnissa on vaihtoehto dynamic end date, mikä tarkoittaa, että raportille tuodaan dataa Lock Date päivään saakka. Kun seuraavan kuukauden kirjanpito valmistuu ja Lock Date käydään päivittämässä - raportti päivittyy automaattisesti raportoimaan uuteen valmistuneeseen kuukauteen saakka.

Näin toimien käyttäjällä on aina ajantasainen raportti vahvistettuun kirjanpidon dataan saakka. Raportille ei tarvitse tehdä mitään muutoksia, vaan raportti päivittyy itsestään raportoimaan Lock Date päivään saakka.

# **Havainnollistavat esimerkit**

Havainnollistamme asiaa muutaman esimerkin kautta.

**Esimerkki 1**

Yrityksen Lock Date päiväksi on asetettu 30.5.2024. Tämän jälkeen mennään muodostamaan raportti, jossa dynamic start date valintana on "Start date of accounting peridod ja valintana dynamic end date kohdassa on "Lock date of accounting period". Saadaan raportti, jossa on yritykset luvut kausilta 1-5/2024. Raportin esitystapa riippuu muista raportilla tehdyistä valinnoista.

**Esimerkki 2**

Yrityksen Lock Date päiväksi on asetettu 30.5.2024. Tämän jälkeen mennään muodostamaan raportti, jossa valintana dynamic start date kohdassa on "locked month" ja dynamic end date kohdassa on "Lock date of accounting period". Saadaan raportti, jossa on luvut kaudelta 5/2024. Raportin esitystapa riippuu muista raportilla tehdyistä valinnoista.

# Lock date yhdessä months from dynamic date -toiminnon kanssa

Lock Date -toimintoa voidaan käyttää raportoinnissa yhdessä myös "Months from Dynamic date" -toiminnon kanssa. Tämä toiminto tuo raportointiin uudenlaisia mahdollisuuksia, sillä toiminnon avulla voidaan luoda raportteja haluttu kuukausimäärä eteen- tai taaksepäin lukitusta kuukaudesta laskien.

[![](

Tämän jälkeen valitaan valikkoon "Dynamic start date" vaihtoehto "Locked month". Seuraavaksi raportille tulee määritellä dynaamisten kuukausien määrä joko eteen- tai taaksepäin. Näin voidaan valita vapaasti mikä aikaväli raportille tulee. Valitsemalla kuvan osoittamaan kenttään luvuksi 4, saadaan aikaan raportti, jossa on 4 kuukautta eteenpäin lukitusta kuukaudesta. Esimerkissämme lukituspäivänä on 30.5.2024, jolloin kyseiselle raportille tulee luvut kausille 6-9/2024.

[![](

Raportille voi määritellä dynaamisen luvun myös taaksepäin syöttämällä luvun eteen miinus -merkin. Näin ollen raportille tulee luvut syötetyn lukumäärän mukaisesti taaksepäin.

[![](

Kolmannen ulottuvuuden kyseiseen raporttiin tuo valinta "Include dynamic start" -toiminto, jolla voidaan määritellä lasketaanko lukittu kuukausi mukaan kuukausia laskettaessa vai ei. Aikaisemmissa esimerkeissämme valinta ei ole ollut päällä.

[![](

# Lisätietoja

[Yrityksen tilikausien määritteleminen](



artikkelin osoite on https://intercom.help/finazilla/fi/articles/4100120-lukituspaivan-kayttaminen-mahdollistaa-raportoinnin-siihen-saakka-mihin-kirjanpito-on-valmistunut

