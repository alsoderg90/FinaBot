## Uuden osabudjetin luominen

Osabudjetin rakentamista avataan tässä artikkelissa vielä rakentamalla osabudjetti askel kerrallaan. Tämä artikkeli on edistyneemmille käyttäjille, joilla on jo hyvä perustietämys budjetoinnista ja osabudjeteista.

Tässä artikkelissa esimerkkinä rakennettava osabudjettipohja on investointien poistoihin liittyvä tasapoisto malliosabudjetti. Investointien seurantaan ja poistoihin tarvitaan tietoja hankintamenosta, tasearvosta, tilikauden lisäyksistä ja vähennyksistä sekä poistoista, jotta voidaan budjetoida poistojen vaikutus tuloslaskelmaan ja tasebudjettiin.

# Uuden osabudjetin luominen

Aloitetaan valitsemalla osabudjettivälilehdellä ”New Sub Budget”. Budjetti nimetään, mutta koska rakentaminen aloitetaan alusta, Sub Budget Template -valinta jätetään tyhjäksi. Osabudjetti tehdään nyt yritystasolla, joten kohdistusta seurantakohteelle ei tehdä.

Aloitetaan esimerkkibudjetin rakentaminen lisäämällä pääotsikkorivi ”Investointi 1”. Tällä rivillä ei ole kaavoja tai lukuja, osabudjetissa tämä näkyy vain otsikkona.

[![](

Seuraava rivi eli alaotsikko ”Tasearvot” tulee investointirivin alle, joten se lisätään investointirivillä olevasta Plus -painikkeesta ja jälleen avautuvasta plussasta. Vastaavasti tehdään tämän rivin alle ”Tasearvo tilikauden alussa” -rivi sillä erotuksella, että rivin tyyppi on ”input”. Tälle kolmanneksi luotavalle riville syötetään nyt siis lukuja; rivi näkyy siten pohjassa vihreänä.

# Luodun rakenteen kopioiminen

Luotava puurakenne mahdollistaa sen, että luotava rakenne on kopioitavissa kokonaan. Kopiointi tehdään Copy -toiminnon kautta kopioimalla rivi ”Investointi 1” ja nimetään se esimerkiksi ”Investointi 2”. Näin toimien koko luotu rakenne laskukaavoineen kopioituu.

[![](

Seuraavaksi ”Tasearvo tilikauden alussa” -rivin alapuolelle samaan tasoon lisätään vielä rivit ”Tilikauden lisäykset” ja ”Tilikauden vähennykset”.

Rivit on nimetty tässä tapauksessa mahdollisimman kuvaavasti, esim. ”Syötä vähennykset – merkkisenä” ohjaa budjetoijaa syöttämään luvun negatiivisena, jotta taustalla olevat laskentakaavat laskevat oikein.

[![](

Seuraavaksi lisätään seuraava ”ryhmä” rakenteeseen eli poistot. Tämä alaotsikko luodaan taas vastaavasti kuin edellä Hankintameno -otsikko. Koska rivin halutaan tulevan pääotsikon ”investoinnit” alle, tulee rivi lisätä rivin ”Investoinnit 1” plussasta.

[![](

Toistetaan vielä läpikäytyjä vaiheita, eli luodaan alla näkyvät rivit vielä ryhmän ”Poistot” alle ja lopuksi luodaan vielä 3.ryhmä ”Taustalaskennat”, jonka alle lisätään edelleen rivit. Nyt rakenne näyttää seuraavalta:

[![](

Vielä ennen kuin kaavoja aletaan luomaan, on hyvä ymmärtää, mihin kaavojen luomisella pyritään. Tämän investointibudjetin tarkoitus on ensinnäkin seurata investointia, mutta tätä kautta luvut budjetoituvat myös tulos -ja tasebudjetteihin. Sen vuoksi osabudjetti laskee:

* Tilikauden poistot (rivi kuukausipoistot), jotka on tiliohjauksella ohjattu tuloslaskelmalle
* Tasearvo tilikauden lopussa (rivi tasearvo), joka on tiliohjauksella ohjattu taseelle

Muut rivit toimivat apulaskentariveinä, jota syötettyjen tietojen pohjalta pystytään laskemaan nämä luvut.

Syöttöriveille syötettävät tiedot eli tiedot, jotka investoinnista pitää olla tiedossa, ovat seuraavat:

* Tasearvo tilikauden alussa + tilikauden aikaset lisäykset (tässä tapauksessa tasearvo kaudella 1/2018 on 20 000€. Kaudella 4/2018 tehdään investoinnille 4 000€ lisäys.

* Jäljellä oleva poistoaika (tässä tapauksessa on käytössä tasapoisto, jonka poistokuukausia on tilikauden alussa vielä 20 kuukautta jäljellä. Poisto kuukaudessa on 1 000€ tilikauden alussa).

* Poistojen aloituskuukausi on tässä tapauksessa tekninen rivi, jota käytetään kaavoissa apuna. Riville syötetään kaudelle 1/2018 luku 1, koska tilikauden poisto tehdään tällä kaudella 1 kertaa, seuraavalle kaudelle syötetään luku 2 jne.
# Kaavojen luominen

Lopuksi avaamme vielä hieman lukujen syötön kautta luotuja kaavoja. Seuraavaksi luodaan siis kaavat.

Nyt muut kuin otsikkorivit ovat vihreitä, eli syöttörivejä. Luodaan seuraavaksi kaavarivit. Tässä yhteydessä on hyvä palautella mieliin kaavaeditorin toiminnot:

[![](

Nyt luodaan rivi "Poistamaton arvo" Muutetaan ensin luotavan rivin tyypiksi Formula, eikä input, ja tämän jälkeen avataan kaavageneraattori.

[![](

[![](

Seuraavaksi luodaan kaavarivi "Kum. Kertyneet poistot". Rivin tyypiksi vaihdetaan jälleen formula ja avataan kaavageneraattori.

[![](

Luodaan rivi "Kum. kirjatut poistot"'

[![](

Luodaan kaavarivi "kuukausipoistot"

[![](

Luodaan kaavarivi "tasearvo"

[![](

Nyt kaikki tarvittavat kaavarivit on luotu. Seuraavaksi tarkastellaan lukujen syöttämisen vaikutuksia, joka avaa juuri luotujen kaavojen merkitystä.

[![](

Yllä esitelty esimerkki tasapoistosta ei ole yksinkertaisimmasta päästä oleva esimerkki osabudjettien luontia silmälläpitäen, mutta antaa kuvan siitä, mitä kaikkea osabudjettien rakentamisessa voidaan tehdä laskukaavoja ja apurivejä käyttämällä.

Artikkelin tarkoitus on ohjata osabudjettien rakentamista ja kaavojen luomista ja tulkintaa. Tältä pohjalta voi myös muita Finazillassa valmiiksi luotuja osabudjetteja ja niiden taustalla olevia kaavoja ja näin saada ideoita ja ohjeita omien osabudjettien rakentamiseen.

[![](

*Finazillan luomassa tasapoistojen osabudjetissa kaikki osabudjetin rivit, joissa on rivin nimen edessä tähtisymboli (\*), kaipaavat tiliohjauksen taakseen. Tiliohjaus ohjaa kyseisen rivin saldot pääbudjetille kyseiselle tilille tulokseen tai taseeseen.* 



artikkelin osoite on https://intercom.help/finazilla/fi/articles/4436976-esimerkki-kuinka-tasapoistojen-osabudjetti-on-rakennettu

