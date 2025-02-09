## Data aggregate valinta

Tämä artikkeli on kohdennettu edistyneemmille käyttäjille, joilla on tarve luoda hieman monimutkaisempia raporttimalleja, missä on erilaista laskentaa taustalla. Artikkelin ymmärtämistä helpottaa, jos käyttäjä osaa jo luoda raporttimalleja.

Raporttimallia luodessa käyttäjälle tulee vastaan kaavan, eli formulan, luominen. Tässä yhteydessä on hyvä tietää mitä "Data aggregate" kohdassa mainitut toiminnot tekevät.

# **Data aggregate valinta**

Data aggregate valinnalla on merkitys silloin kun raportille on tehty valinta "total reporting period" eli koko raportointiaika yhdessä sarakkeessa. Kyseinen valinta tehdään raportin tietolähteissä kohdassa "period presentation type".

Oletusvalinta SUM on hyvä useimmissa käyttötapauksissa, joten yleensä tätä ei ole tarvetta muuttaa. Käytännössä SUM tarkoittaa sitä, että Total sarakkeessa (silloin kun raportin valinnoissa on laitettu ruksi kohtaan ”Show Grand Total”) raportilla näkyvä summa on yhteenlasku kausilta.

## **Milloin Data aggregate valintaa kannattaa käyttää**

Joskus on kuitenkin tarve siihen, että raportin rivi raportoi "yhteensä" sarakkeessa jotain muuta kuin sarakkeiden yhteissummaa. Tällöin agregaattivalinnoilla voidaan määrittää raporttimallilla eri laskentajärjestys kyseiselle kaavariville.

Yhteisumman voidaan määrittää olevan kauden ensimmäisen tai viimeisen kuukauden saldo, kausien keskiarvo tai kahden eri laskentatekijän yhteissummien jako tai kertolaskun tulos (NON). Tällainen tilanne voi olla usein esimerkiksi jakolaskuissa.

Tyypillisiä käyttötapauksia voivat olla esimerkiksi tilanteet, joissa halutaan laskea koko vuoden keskiarvoa, halutaan saada käyttökate koko vuodelta prosentuaalisena tai muu vastaava luku, joka perustuu toisen rivin yhteissumman jakamiseen toisen rivin yhteissummalla sen sijaan, että ko. riviltä lasketaan luvut yhteen, kuten grand total -valinta normaalisti tekee.

# **Time aggregate valinnat**

```
Sum of values = lyhenne kaavassa on SUM  

```
```
No aggregate = lyhenne kaavassa on NON  

```
```
Average of values = lyhenne kaavassa on AVG  

```
```
Only first value = lyhenne kaavassa FIRST  

```
```
Only last value = lyhenne kaavassa LAST  

```
```
Sum of values from all dimensions = lyhenne kaavassa DIMTOTSUM *   

```
```
Average of values from all dimensions = lyhenne kaavassa DIMTOTAVG *
```

 *\* liittyy vanhoihin operatiivisiin raportteihin. Emme käsittele näitä aggregaatteja sen tarkemmin tässä artikkelissa, koska niiden käyttö on erittäin harvinaista*.

Näistä raporttien laskentaan käytettän SUM ja AVG aggregaatteja. Näillä käyttäjä voi kertoa millä tavalla hän haluaa, että laskenta suoritetaan, silloin kun raportti yhdistää laskennassaan kuukausia yhteen; esimerkiksi tilikausikohtaisessa raportissa.

Havainnollistamme aggregaattien käyttöä esimerkin avulla. Alla on kaavaan valittu vain yksi raporttimallin rivi (myynti) ja annettu tälle riville eri aggregaatit testimielessä.

Varsinaisessa raportoinnissa on tehty period presentation type - kohdassa valinta "Total reporting period", jotta nähdään agrekaattien toiminta.

[![](

**Selvennös yllä olevaan kuvaa:** 

Myynti SUM = yhdellä laskentatekijällä summaa kaudet.

Myynti NON = yhdellä laskentatekijällä summaa kaudet

Myynti AVG = laskee kausien keskiarvon. Kausien summa / 12 = 2500.

Myynti FIRST = total sarakkeessa on ensimmäisen sarakkeen luku

Myynti LAST = total sarakkeessa on viimeisen sarakkeen luku

# **Kahdella eri laskentatekijällä laskeminen**

Lisätään kaavaan laskentavakio eli nyt kaava sisältää 2 eri laskentatekijää, joille molemmille voidaan erikseen määritellä aggregaatti (kaava = laskentavakio jaettuna myynnillä).

[![](

**Selvennös yllä olevaan kuvaa:** 

Myynti SUM + Laskentavakio SUM= Raporttimallin kaavarivi laskee ensin summan riviltä myynti, sitten summan riviltä laskentavakio ja lopuksi jakaa myynnin summan laskentavakion summalla (30 000/530 = 56,60)

Myynti NON + Laskentavakio NON = Raporttimallin kaavarivi laskee ensin jakolaskun jokaiselta kaudelta eli 2019 / 1 = 1000/50 = 20 ja lopuksi laskee yhteen näiden jakolaskujen tulokset = 770,48

Myynti AVG + Laskentavakio SUM = Raporttimallin kaavarivi laskee ensin myynnin keskiarvon = 2500 ja sen jälkeen jakaa sen laskentavakion summalla = 530 --> 2500/530 = 4,72

Myynti SUM + Laskentavakio AVG = Tässä laskenta tehdään päinvastoin kuin yllä eli myynti yhteensä = 30 000 jaetaan laskentavakion keskiarvolla = 44,17 --> 30 000/44,17 = 679,25

# Lisätietoja

[Raporttimallien rivityyppien sekä rivien balance data ja formula tarkemmat määrittelyt avattuna](

[Kaavarivit budjetoinnissa](

[Budjettien kaavoihin liityvien koodien tai lyhenteiden avaaminen](



artikkelin osoite on https://intercom.help/finazilla/fi/articles/4279898-kaavojen-kirjoittaminen-raporttimalleille

