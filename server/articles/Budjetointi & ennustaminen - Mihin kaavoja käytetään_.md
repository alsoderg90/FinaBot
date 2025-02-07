## Mihin kaavoja käytetään?

Tässä artikkelissa käydään läpi kaavarivien luomista. Laskentavakioiden ja tagien käyttö budjetilla tapahtuu myös kaavarivien kautta, joten myös nämä toiminnot liittyvät budjetin kaavoihin - nämä on tosin käsitelty omissa artikkeleissaan, joihin löytyy linkkejä artikkelin lopusta.

Tämän artikkelin toimintojen ymmärtämisen edellytys on, että käyttäjä osaa jo vähintään laatia budjetin ja osabudjetin.

# **Mihin kaavoja käytetään?**

Kaavarivejä käytetään budjetoitaessa osabudjetilla. Toiminto mahdollistaa esimerkiksi vaikkapa sellaisen laskennan, että osabudjetille luodaan rivit myyntikappaleille, kappalekohtainen hinta ja näistä lasketaan liikevaihto, joka ohjataan pääbudjetin halutulle tilille.

Kaavoja voi muodostaa kaikista mahdollisista osabudjetin riveistä sekä kaikista mahdollisista kiinteistä arvoista, joita voidaan tuoda osaksi kaavaa esimerkiksi laskentavakion kautta. Käyttötapoja on siis lukemattomia.

# **Kaavan muodostaminen**

Kaavan muodostaminen alkaa siitä, että luodaan haluttu osabudjetti ja sinne luodaan rivejä. Kaavarivi päästään muodostamaan muuttamalla rivin tyyppi kaavariviksi, eli tyypiksi "Formula". Rivin tyyppiä päästään muokkaamaan rivikohtaisista työkaluista kohdasta "Settings".

Kaava muodostetaan kaavaeditorissa, joka aukeaa Formula –laatikosta. Kaavaeditorissa muodostettu kaava näkyy Formula –rivillä.

[![](

## **Kaavan kirjoittaminen**

Kaava aletaan kirjoittamaan kaavaeditorissa kenttään "Formula:(edit pos. 0).

Kaavaan haetaan tietoja kaavaeditorin yläosasta joko budjettiriveistä, laskentavakioista, fixed data -kentästä, tageista sekä tietenkin operators -kentän alla olevista kertoimista ja jakomerkeistä jne.

Alla on kuvattuna kaavaeditorin toiminnot tarkemmin:

[![](

Kun kaava aletaan kirjoittamaan kenttään "Formula:(edit pos. 0), tulee sen alla olevaan kenttään "selkokielinen" kaava näkyviin samaan tahtiin.

***Esimerkki*** 

Havainnollistamme asiaa vielä esimerkin kautta. Yritykselle on luotu osabudjetti, jossa on kolme riviä. Rivillä 1 on myyntikappaleet, jotka syötetään osabudjettiin käsin; rivin tyyppi on siis input. Toinen rivi osabudjetilla on myyntihinta per kpl ja myös tämä rivi on input tyyppinen, jolloin myyntihinta syötetään käsin. Kolmas rivi on tyypiltään kaavarivi ja tällä rivillä lasketaan kyseisten myyntien liikevaihto kertomalla myyntikappaleet ja myyntihinta.

Kaavaa aletaan kirjoittamaan siis kolmannelle osabudjetin riville. Rivin tyypiksi valitaan Formula, jolloin päästään kaavaeditoriin. Mennään hakemaan kentästä "Budget rows" kaavaan ensimmäisenä myyntimäärä. Kaavaeditori näyttää nyt tältä:

[![](

Seuraavaksi lisätään kaavaan kertomerkki tai haetaan se "Operators" valikosta. Sen jälkeen haetaan jälleen "Budget rows" kentästä kaavaan myyntihinta per kpl. Kaavareditori on nyt tämän näköinen:

[![](

Painikkeesta "Accept" luotu kaava tallennetaan. Tämän jälkeen näkymä palaa rivin asetukset -näkymään, jossa luotu kaavarivi voidaan ohjata pääbudjetille halutulle tilille kohdassa "Transfer to account". Update -painike tallentaa muutoksen.

Osabudjetin rivi 3 on nyt muuttunut siniseksi, mikä kertoo, että kyseinen rivi on kaavarivi ja sille ei voi syöttää manuaalisesti lukuja. Luotua kaavaa kannattaa testata syöttämällä osabudjetin riveille 1 ja 2 lukuja ja tarkistamalla, että kaava laskee oikein sekä oikeat luvut ohjautuvat pääbudjetille sinne minne kuulukin.

[![](

# Lisätietoja

[Yleistä budjetoinnista](

[Budjetoinnin aloittaminen sekä budjetointinäkymän painikkeiden ja toimintojen esittely](

[Osabudjetit osana yrityksen budjetointiprosessia](

[Uuden osabudjetin luominen tai osabudjetin kopioiminen toiselta asiakkuuden yritykseltä](

[Mitä laskentavakiot ovat ja miten niitä käytetään?](

[Yrityskohtaisten laskentavakioiden luominen ja päivittäminen sekä niiden käyttäminen kaavassa](

[Budjettikohtaisten laskentavakioiden luominen ja päivittäminen](

[Budjettien kaavoihin liityvien koodien tai lyhenteiden avaaminen](



artikkelin osoite on https://intercom.help/finazilla/fi/articles/4430034-kaavarivit-budjetoinnissa

