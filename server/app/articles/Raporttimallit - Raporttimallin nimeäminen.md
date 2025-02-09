## Raporttimallin nimeäminen

# Raporttimallin nimeäminen

Raporttimallin luominen aloitetaan valitsemalla joko Customer –taso tai Company -taso (riippuen siitä, halutaanko raporttimalli luoda customer- vai company tasolle) ja sen jälkeen mennään valikkoon "Report Scheme" ja painetaan ”New Report Scheme” -painiketta. Tämän jälkeen aukeaa oheinen täyttölomake.

[![](

Raporttimallille annetaan nimi kentässä "Name". Nimeämiseen kannattaa kiinnittää huomiota. Suosittelemme, että Customer –tason alle luodun raporttimallin nimeen laitetaan tunnisteeksi alkuun kolminumeroinen asiakkuuden tunnus ja Company –tason alle luodun raporttimallin tunnisteeksi kuusinumeroinen yrityksen tunnus.

Myös varsinaisten raporttien nimeämisessä suositellaan käytettävän samaa logiikkaa.

Kohdassa "Description" voidaan tarkentaa raporttimallin tarkoitusta jne. Kentän voi jättää myös tyhjäksi.

Kun raporttimallia luodaan tyhjästä, eikä pohjalle valita mitään valmista raporttimallia, tulee "from template" kohtaan oletusvaihtoehto "Empty". Tämä tarkoittaa, että mitään valmista mallia ei käytetä apuna. Mikäli pohjalle halutaan ottaa tilikartta, valitaan vaihtoehto "account scheme". Valinta account scheme template tarkoittaa tilikarttatemplaattia.

Painamalla ”Create Report Scheme”, raporttimallin nimi ilmestyy listalle.

# Raporttipuun, eli rakenteen, luominen

Seuraavaksi on vuorossa varsinaisen "raporttipuun" luominen. Tämä alkaa klikkaamalla raporttimallin nimeä raporttimallilistassa, jolloin avautuu raportin rakenne eli ”raporttipuu”. Tässä esimerkissä luomme raporttimallin, jossa on seuraavat rivit:

• Liikevaihto

• Käyttökate EUR

• Käyttökate %

• Tilikauden tulos

# Rivien lisääminen

Raporttimallin nimeä klikatessa avautuva näkymä on tyhjä, sillä mitään valmista pohjaa ei ole käytetty. Raporttimallin rakentaminen alkaa klikkaamalla ”New Row” –painiketta.

[![](

1. Rivin tyypiksi valitaan ”Header”, joka tarkoittaa ns. otsikkoa. Käytännössä tämä on ensimmäinen rivi, joka tulee näkyviin valmiille raportille. Nimetään rivi ”Liikevaihto” ja ”visible” kohtaan laitetaan ruksi, koska haluamme, että rivi Liikevaihto näkyy itse raportilla.

Rivin luomisen jälkeen näkymä on seuraava:

[![](

Raportilla halutaan esittää tietoa juuri luodulla "Liikevaihto" rivillä, joten raporttimallille lisätään uusi ”Child row”eli ns. lapsirivi klikkaamalla painiketta "New Child Row" -painiketta juuri luodun liikevaihto rivin perästä. Käyttäjälle aukeaa tämän jälkeen uuden rivin syöttöikkuna.

[![](

Luodun "lapsirivin" tyypiksi valitaan ”Balance data”, joka tarkoittaa sitä, että tietoa tällä rivillä esitetään kirjanpidon datasta. ”

# Tilivälin valitseminen (start account, end)

Seuraavaksi valitaan tiliväli, josta rivin halutaan laskevan saldot yhteen. Kyseisessä raporttimallin rivissä ollaan laskemassa liikevaihtoa, joten tässä tapauksessa rajaus on tilistä 3000 tiliin 3599.

*HUOM! Riippuen yhtiöstä ja käytettävistä tileistä, välille saattaa kuulua myös liiketoiminnan muiden tuottojen tilejä; asiakas vastaa aina itse rakennettujen raporttimallien raportoinnin oikeellisuudesta itse.* 

## Row factor -valinta

”Row Factor” kohdassa valitaan joko vaihtoehto "Credit" tai "Debit". Liikevaihtotilien luvut ovat kirjanpidossa credit- eli miinusmerkkisiä kun taas raportoinnissa tuottoluvut yleensä halutaan esittää positiivisena, joten tässä käytetään kertojana miinusta. Näin ollen lopputulos on positiivinen.

Visible” kohtaan tulee oletuksena ruksi, koska luvun halutaan näkyvän raportilla.

## **Saldojen summautumisen valinnat**

”Sum account range to parent” valinta tarkoittaa sitä, että saldojen summa näkyy parent rivillä (joka on tässä tapauksessa ensimmäiseksi luotu liikevaihtorivi). Valitaan kyseinen vaihtoehto, sillä haluamme tilien saldojen summan näkyvän liikevaihtorivillä.

Jos valinta jätettäisiin tekemättä, raportilla olisi seuraava esitystapa:

[![](

"Filter data by dimensions" kohta voidaan jättää tyhjäksi peruskäytössä. Toiminto on tarkoitettu datan filtteröintiin pääosin tilanteissa, missä raportin kautta rajaaminen ei ole riittävä.

”Balance type” , ”Previous month count” ja ”previous month balance type” kohtiin jätetään oletusvalinnat.

Kun rivi tallennettu, raporttirakenne näyttä seuraavalta (huomaa, että liikevaihto-otsikon edessä olevasta nuolesta tiedot saa auki):

[![](

Seuraavaksi luodaan Käyttökate EUR –rivi. Uusi rivi luodaan ”New Row” painikkeella alla olevasta kuvaan merkitystä kohdasta. Jos uusi rivi lisätään raporttimallin otsikon alla näkyvästä painikkeesta, Finazilla lisää rivin ylimmäiseksi raporttipuuhun.

Uusi rivi luodaan muutoin vastaavalla logiikalla kuin aikaisemmin luotu "liikevaihto" rivi. Luodaan siis otsikkorivi (eli header -tyyppinen rivi), joka nimetään ”Käyttökate EUR”.

[![](

Seuraavaksi luodaan 2 "lapsiriviä" (eli ns. *”Child Row”* –riviä). Valittua tiliväliä lukuun ottamatta lomakevalinnat tehdään vastaavasti kuin tehtiin aikaisemmin liikevaihdon osalta.

Logiikka tilien valintaan on sama kuin luvun alussa esitetyssä esimerkissä. Raporttipuussa tulee jälleen huomioida, että kun tehdään toista Child Rowta, valitaan ylemmän Child Row:n painikerivistä ”New Row”, jotta toinen lapsirivi tulee oikeaan paikkaan raporttipuussa.

Rivien lisäämisen jälkeen raporttirakenne näyttää seuraavalta:

[![](

# **Prosenttirivin lisääminen kaavan avulla**

Seuraavaksi raporttimallille luodaan rivi, jolla käyttökate esitetään prosentteina. Valitaan Käyttökate EUR-riviltä ”New Row” ja valitaan rivin rivin tyypiksi vaihtoehto "Formula", joka tarkoittaa kaavaa. Kaava on oikea rivityyppi, sillä käyttökate % saadaan jakamalla käyttökate liikevaihdolla. Name -kenttään tulee syöttää haluttu nimi.

[![](

”Report Scheme Rows” –ikkuna toimii alasvetovalikkona. Alasvetovalikosta voi valita kaavaan jo raporttirakenteessa olevia rivejä. Tässä tapauksessa valitaan ensin Käyttökate EUR –rivi klikkaamalla riviä ja Finazilla lisää tämän jälkeen rivin kaavaan.

Kaava alkaa kirjaantumaan alaosan "Formula" kenttään sitä mukaa, kun kaavaa kirjoitetaan. Kun kaavaan halutaan lisätä jakomerkki (tai mikä tahansa muu merkki), mennään hiirellä klikkaamalla Formula -kenttään ja kirjoitetaan jakomerkki kaavan loppuun. Tämän jälkeen haetaan Report Scheme Rows -alasvetovalikosta jakajaksi liikevaihto. Tämän jälkeen mennään taas hiirellä klikkaamalla takaisin Formula kenttään ja kirjoitetaan kertomerkki kaavan loppuun, jotta saadaan luvusta prosentteja.

[![](

Lopuksi raporttimallille lisätään vielä rivi tulos -rivi samoin kun aluksi lisätiin rivi Liikevaihto. Valmis raporttirakenne näyttää seuraavalta:

[![](

Raportti, joka luodaan esimerkissä luodun raporttimallin pohjalta, näyttää seuraavalta:

[![](

# Raporttimallilla rivin siirtäminen

Raporttimallille luotujen rivien paikkaa voi tarvittaessa myös siirtää. Jos esimerkiksi yllä kuvatussa raporttimallissa haluttaisiin, että tulos -rivi esitettäisiin raportilla ensimmäisenä, voitaisiin sen paikkaa siirtää.

Rivin siirtäminen tehdään kyseisen rivin perässä olevan move -painikkeen kautta.

[![](

Seuraavaksi raporttimallilla navigoidaan siihen kohtaan, mihin valittu rivi halutaan siirtää. Käyttäjälle ilmestyy valikko, josta voidaan valita siirretäänkö rivi "tulos" liikevaihto rivin yläpuolelle (before), alapuolelle (after) vai kyseisen rakenteen sisälle lapsiriviksi (inside)

[![](

Rivien siirto toimii yksittäisissä tiliväleissä tai hierarkisissa kokonaisuuksissa.

# Raporttimallilla rivin kopioiminen

Raporttimallilla rivejä voi myös kopioida copy -painikkeen kautta. Kopioinnin toimintalogiikka on vastaava kuin siirtämisen - ensin valitaan kopioitava rivi ja sen jälkeen paikka, mihin rivi halutaan kopioida.

[![](

[![](

*Kaavoihin voidaan lisätä myös valmiita laskentavakioita. Tästä löytyy lisätietoa artikkeleistamme, jotka löytyvät hakusanalla "laskentavakio".*



artikkelin osoite on https://intercom.help/finazilla/fi/articles/4341885-raporttimallin-rakentaminen-alusta-saakka

