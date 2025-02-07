## Finazillaan luodut oletusasetukset budjettien generointiin

Olemme kertoneet aikaisemmissa artikkeleissamme Finazillan kehittämästä budjetin generointi menetelmästä. Ominaisuuteen löytyvät ohjeet löytyvät [täältä.]( Tässä artikkelissa kuvaamme tarkemmin luotuja oletusasetuksia.

[![](

*Kaikki Finazillan asiakkaat, joiden tilikartta noudattelee liikekirjurin tilikarttaa, saavat oletusasetukset automaattisesti. Käyttöönotosta vastaava Finazillan asiantuntija osaa neuvoa asiassa, mikäli et ole varma, onko asetukset yrityksessänne käytössä.* 

# Finazillaan luodut oletusasetukset budjettien generointiin

Finazillan tilikarttamalli (template) nimeltään "Tilikartta, liikekirjuri (tämän takana generointiasetukset)" sisältää yksityiskohtaiset asetukset budjetointiin, jotka on suunniteltu helpottamaan ja automatisoimaan tuloslaskelman ja taseen luomista. Alla on yhteenveto tilikarttamallin (template) oletusasetuksista.

# 

# TULOSLASKELMA

## Yleinen asetus

Kaikilla kyseisen tilikarttamallin tileillä käytetään oletuksena fit a line, linear -menetelmää, joka tarkoittaa regressiosuoran sovittamista historiallisiin data-arvoihin. Fit a line, linear -menetelmä on helpoin hahmottaa graafisen kuvaajan avulla. Tämä menetelmä tarkoittaa käytännössä sitä, että piirretään viiva, jonka etäisyys on mahdollisimman pieni pisteisiin nähden. Alla olevassa esimerkissä sininen viiva on yrityksen toteumaluvut. Punainen viiva kuvaa samaa yrityksen dataa, kun se on generoitu budjetille käyttämällä fit a line linear -valintaa.

[![](

## Tuloslaskelman poikkeukset

**Henkilöstökulut**

Tähän ryhmään kuuluvat tilit käyttävät oletuksena "latest same calendar month" asetusta, mikä tarkoittaa, että edellisen vuoden vastaavan kuukauden saldo otetaan käyttöön. Kyseinen valinta auttaa huomioimaan kausivaihtelut, kuten esimerkiksi lomakaudet.

**Poistot ja arvonalentumiset**

Tähän ryhmään kuuluvat tilit käyttävät oletuksena "average" asetusta, jossa valitun ajanjakson yhteissumma jaetaan tasaisesti kuukausille. Valinta tasaa poistojen vaikutusta kuukausittain.  
​  
​

# TASE

## Perusperiaatteet taseen täsmäytys- sekä erikoistilien takana

Täsmäytys- ja erikoistilit määritellään käyttöönoton yhteydessä valmiiksi asiakkaalle Finazillan toimesta. Alla kuvaamme tarkemmin erikoistilejä.

**Tili 1910 Rahat ja pankkisaamiset, sekä tili 2370 Tilikauden voitto/tappio**

Taseen budjetoinnissa Finazilla laskee automaattisesti tilikauden tulosta ja täsmäyttää sen omaan pääomaan ja rahavaroihin. Tämän vuoksi edellä mainitut tilit tulee olla määriteltynä yhtiön tilikartalla. Tämä tehdään aina käyttöönoton yhteydessä valmiiksi asiakkaalle Finazillan toimesta.

Tilikauden voitto 2370 on erikoistili. Kun esimerkiksi tulosbudjetti näyttää tilikauden tulokseksi 40 000€, tekee Finazilla automaattisesti kirjauksen taseeseen omaan pääomaan, sekä vastakirjauksen rahavaroihin. Näin toimien tase menee tasan.

**Tili 2251 Edellisten tilikausien voitto**

Edellisen tilikauden voitto -tili on oletuksena erikoistili. Tili hakee tilikauden vaihteessa edellisen tilikauden tuloksen ja siirtää sen kyseiselle tilille.   
​  
Mikäli tarpeena on budjetoida ko. tiliä koko tilikaudelle, tulee tilin rivityyppi vaihtaa Input-muotoon. Tämän jälkeen kyseiselle tilille pystyy syöttämään budjetille tilin kokonaissaldon, eikä budjetille noudeta esitettäväksi vain esimerkiksi kauden 12/2023 budjetoitua tulosta.

# VASTAAVAA

## Yleinen asetus

Taseen vastaavaa puolella kaikilla tileillä on oletuksena latest. Kyseinen asetus hakee lukituspäivän mukaisen viimeisen tilinsaldon jokaiselle kuukaudelle.

## VASTAAVAA puolen poikkeukset

**Pysyvät vastaavat - Budjetoidut poistot**

Finazillaan on perustettu generointia varten uusi tiliryhmä budjetoidut poistot. Kyseiseen ryhmään on ohjattu oletuksena tili 149999. Kyseisen tilin takana on generointiasetuksena kaava, joka hakee tuloslaskelman poistot ja arvonalentumiset -merkkisenä ja kumuloi kyseistä saldoa tälle tilille. Näin saadaan laskettua taseelle myös pysyvien vastaavien vähennykset poistojen osalta.

Havainnollistamme asiaa esimerkillä. Alla olevassa esimerkissä tuloslaskelmalla on poistoja jokaisella kuukaudella 2500 €. Taseen tilille 149999 haetaan tätä kyseistä saldoa kumuloiden. Pysyvät vastaavat pienenevät siis joka kuukausi poistojen verran, jos oletetaan, että taseeseen ei tule uusia investointeja.

[![](

**Vaihtuvat vastaavat – Myyntisaamiset**

Myyntisaamiset nollataan oletuksena kokonaan. Kyseisen tiliryhmän takana on kaava, joka kertoo myyntisaamiset nollalla. Näin oletuksena tähän tiliryhmään ei tule lukuja. Myyntisaamiset lasketaan myöhemmin uuteen tiliryhmään.

**Vaihtuvat vastaavat – Budjetoidut myyntisaamiset**

Finazillaan on perustettu generointia varten uusi tiliryhmä budjetoidut myyntisaamiset. Kyseiseen ryhmään on ohjattu oletuksena tili 172999. Kyseisen tilin takana on generointi asetuksena kaava, joka hakee tuloslaskelman yleiset myyntitilit ja lisää siihen 24 %. Näin myyntisaamisissa on aina oletuksena kyseisen kuun liikevaihto arvonlisäverolla lisättynä.

[![](

# VASTATTAVAA

## Yleinen asetus

Taseen vastattavaa puolella kaikilla tileillä on oletuksena latest. Kyseinen asetus hakee lukituspäivän mukaisen viimeisen tilinsaldon jokaiselle kuukaudelle.

## **VASTATTAVAA puolen poikkeukset**

**Lyhytaikainen vieras pääoma – Siirtovelat – Lomapalkkavelka tili 2962**

Lomapalkkavelan takana on oletuksena asetus latest same calendar month. Tämä oletusasetus hakee saldoksi edellisen vuoden vastaavan kuukauden saldon. Näin saadaan lomapalkkavelat generoitumaan edellisen vuoden mukaan, jolloin saldo kasvaa tilikauden aikana ja pienenee yleensä kesäkuukausina, kun työtekijät ovat lomalla.

**Lyhytaikainen vieras pääoma – Budjetoidut lainanlyhennykset**

Finazillaan on perustettu generointia varten uusi tiliryhmä budjetoidut lainanlyhennykset. Kyseiseen ryhmään on ohjattu oletuksena tilit 299997-299999. Tilin 299997 budjetoidut lainanlyhennykset syöttötili takana on oletusasetuksena skip account. Kyseinen tili toimii lainanlyhennysten syöttötilinä Finazillassa. Tälle tilille syötetään lyhennys aina kyseisen kuukauden kohdalla, jolloin lyhennys maksetaan. Tilille ei kuulu generoitua saldoa missään vaiheessa.

Tilin 299998 budjetoidut lainanlyhennykset vastatili takana on oletuksena kaava, joka kääntää 299997 tilille syötetyt luvut negatiiviseksi, sekä kumoaa syötetyt summat lopullisessa laskennassa, jotta ryhmään ei tule tuplasaldoa.

Tilin 299999 budjetoidut lainanlyhennykset kumulatiivinen takana on generointi asetuksena kaava, joka hakee tilin 299998 saldon ja kumuloi kyseistä saldoa tälle tilille. Näin saadaan laskettua taseelle myös lainan lyhennykset tilikaudelle.

Havainnollistamme asiaa yhden esimerkin kautta. Alla olevassa esimerkissä lainoja lyhennetään tilikauden aikana yhteensä 12 000 €. Lyhennykset maksetaan kvartaaleittain tilikauden aikana; 3/24, 6/24, 9/24 ja 12/24. Tilille 299997 on syötetty 3000 € näille kuukausille ja tämän jälkeen tiliryhmä on generoitu. Budjetoidut lainanlyhennykset ryhmän saldo muuttuu aina näiden maksuerien mukaan ja lyhytaikainen vieraspääoma pienenee lyhennysten verran, jos oletetaan, että taseeseen ei tule uutta vierasta lyhytaikaista pääomaa.

[![](



artikkelin osoite on https://intercom.help/finazilla/fi/articles/8879246-finazillaan-luodut-oletusasetukset-budjettien-generointiin

