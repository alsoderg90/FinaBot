## Taustaa

*Tämä ohje koskettaa vain asiakkaita, joilla on joko Procountor tai Netvisor integraatio ja laskudata tulee siten automaattisesti Finazillaan.*

Tämän artikkelin ymmärtämistä helpottaa, jos käyttäjä tietää mitä raporttimallit ovat ja osaa luoda raporttimalleja. Lisäksi ymmärtämistä helpottaa, mikäli operatiivinen data on jossain määrin tuttua. Lukijan tulee myös tietää, miten raportteja muodostetaan ja pivotoidaan.

# Taustaa

Prcountor ja Netvisor asiakkailla siirtyy aina oletusarvoisesti Finazillaan myyntilaskut sekä ostolaskut. Laskudataa hyödynnetään kyseisillä asiakkailla mm. lyhyen ajan kassavirrassa (cash flow).

Myynti- ja ostolaskut ovat Finazillassa ns. operatiivista dataa ja laskudatassa tulevat kohdistukset eli dimensiot, ovat ns. operatiivisia dimensioita. Myynti- ja ostolaskuista syntyy dimensioita, kuten esimerkiksi asiakas (customer), myyjä (seller), tuote (product), toimittaja (supplier) ja ostaja (buyer).

Procountor ja Netvisor asiakkailla laskudatan tuleminen Finazillaan mahdollistaa sen, että kyseistä dataa voidaan raportoida Finazillalla. Tässä esimerkissä näytämme, miten voidaan raportoidaan myyntiä asiakkaittain euroissa kuukausikohtaisesti.

# Raporttimallin luominen

Operatiivisen datan raportoiminen edellyttää, että asiakkaalla on luotuna raporttimalli halutun datan raportoimiseen.

Raporttimalli luodaan company -valikossa kohdassa report schemes painikkeesta "new report scheme". Raporttimallille annetaan kuvaava nimi ja raporttimalli tallennetaan.

[![](

Kun raporttimalli on luotu, ilmestyy se report scheme listaan sille annetulla nimellä. Raporttimalli saadaan auki sen nimeä klikkaamalla. Tämän jälkeen raporttimallille päästään luomaan ns. raporttipuuta.

Kun raporttimallille halutaan nostaa operatiivista dataa, valitaan row type -kohtaan valinta "operative data (new)". Name kenttään kirjoitetaan se otsikko, minkä raportilla halutaan näkyvän.

Operative data group -kenttään valitaan, mitä tietovirtaa raportoidaan. Kun raportoidaan myyntidataa, on tietovirtana "salesinvoice". Amount -valinta kertoo, että halutaan raportoida myyntien euroja (quantity taasen raportoisi myyntilaskujen kpl määrää).

[![](

# Raportointi

Sen jälkeen kun raporttimalli on luotu, tehdyllä raporttimallilla voi lähteä raportoimaan normaalisti. Mikäli myynnit halutaan raportoida asiakkaittain, tulee raportoinnissa muistaa valita dimensio/column valinta, joka mahdollistaa dimensioiden pivotoinnin raportille.

[![](

Mikäli raportille halutaan asiakkaat näkyviin, täytyy raportille pivotoida customer -dimensio.

[![](

Customer -dimension voi raahata esimerkiksi rows -laatikkoon, jolloin asiakkaat esitetään riveillä.

[![](

Pivotoitu raportti näyttää tämän jälkeen oheiselta. Asiakkaat esitetään riveillä ja kuukaudet sarakkeilla.

[![](

[![](

Raporttia voi luonnollisesti pivotoida myös muutoin, kuin yllä kuvatulla tavalla. Yllä kuvattu esimerkki on vain yksi vaihtoehto. Customer -dimension voi laittaa vaikkapa filtteriksi (report filters), jolloin voidaan helposti filtterin kautta katsoa tietyn asiakkaan myynnit.

Raportista voi myös piirtää vaikkapa graafisen raportin piirakka -muotoon, jolloin voidaan tarkastella kunkin asiakkaan myyntejä graafisessa esitysasussa.



artikkelin osoite on https://intercom.help/finazilla/fi/articles/5882439-esimerkki-myyntien-raportoiminen

