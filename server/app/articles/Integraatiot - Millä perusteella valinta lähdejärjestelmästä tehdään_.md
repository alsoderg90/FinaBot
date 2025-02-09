## Millä perusteella valinta lähdejärjestelmästä tehdään?

Mikäli käytössä on sellainen lähdejärjestelmä, mistä ei ole olemassa valmista rajapintaa Finazillaan, tuodaan tieto Finazillaan joko tiedostopohjaisella integraatiolla, tai manuaalisesti drop- in tuontina. Tämä artikkeli käsittelee nimenomaan manuaalista drop -in tuontia. Tiedostopohjaista rajapintaa olemme kuvanneet ohjeessamme [täällä.]( 

Finazillassa on useita eri lähdejärjestelmiä, jotka tukevat manuaalista drop-in tuontia. Asiakkaan ei tarvitse itse tietää, mikä on hänelle oikea soveltuva lähdejärjestelmä kun hän tuo dataa drop-in metodilla, vaan valinnan on tehnyt Finazillan käyttöönottaja. Valinta tehdään sen mukaan, että asiakkaan dataa tarvitsisi muokata manuaalisesti mahdollisimman vähän.

# **Millä perusteella valinta lähdejärjestelmästä tehdään?**

Keskeisin vaikuttava tekijä, mikä vaikuttaa lähdejärjestelmän valintaan, on taseen saldojen käyttäytyminen asiakkaan tositeaineistossa. Taseen osalta tulee olla selvillä, miten taseen avaava saldo esiintyy tositteissa. Taseen avaavista saldoista tulee tietää alla mainituista vaihtoehdoista oikea:

* Jokaisen kuukauden alkusaldoissa mukana
* Jokaisen tilikauden ensimmäisen kuukauden saldoissa mukana
* Historiassa olevassa ensimmäisessä tiedostossa ensimmäisessä kuukaudessa mukana (eikä koskaan enää sen jälkeen)

Kun taseen avaavien saldojen logiikka on tiedossa, tiedetään, mikä on Finazillassa oikea laskentalogiikka. Tämän lisäksi toinen valintaan vaikuttava tekijä on se, minkä näköisenä data saadaan ulos lähdejärjestelmästä. Eri lähdejärjestelmillä tuotava drop-in tiedosto on eri näköinen. Valinta pyritään tekemään niin, että tiedostoa pitäisi muokata mahdollisimman vähän manuaalisesti.

## **MSNAV**

Kirjauspäivissä käsitellään päivämääriä. Sarakkeessa D ja E on dimensioita. Nämä voi luonnollisesti jättää pois, mikäli tositteeseen ei kohdistu dimensiota. Rivillä 1 oleva nimi tulee dimension nimeksi ja tositeriveillä olevat dimensioiden nimet/koodit ovat yksittäisten dimensionarvojen nimiä.

Tässä mallissa tasetta kumuloidaan loputtomasti.

Valmis siirtotiedostopohja löytyy [täältä]( Pohjassa on valmiina otsikot ja se on tallennettu csv -muotoon. Huomaa, että pohja vaatii muokkaamista dimensioiden osalta, sillä valmiissa pohjassa on vain otsikot, jotka tulee korvata varsinaisilla dimensioilla ja dimensionarvoilla.

[![](

## **GENERIC**

Kirjauspäivissä käsitellään edellisestä poiketen vuosia ja kuukausia. Genericissä päivämäärän muoto on siis erilainen. Sarakkeessa E on dimension nimi ja sarakkeessa F on kyseisen dimension arvon nimi. Seuraava dimensio voidaan laittaa sarakkeeseen G ja sen arvo sarakkeeseen H jne. Dimensiot voi luonnollisesti jättää pois, mikäli tositteeseen ei kohdistu dimensiota.

Genericin valmis siirtotiedostopohja löytyy [täältä.]( Pohjassa on valmiina otsikot ja se on tallennettu csv -muotoon. Huomaa, että pohja vaatii muokkaamista dimensioiden osalta, sillä valmiissa pohjassa on vain otsikot, jotka tulee korvata varsinaisilla dimensioilla ja dimensionarvoilla.

[![](

[![](

*Genericistä on useampi eri toteutus liittyen erilaisiin vaihtoehtoihin taseen kumulointiin. Aihetta on kuvattu tarkemmin artikkelissamme [täällä.]( 

## **ETBALANCE**

Kun asiakkaalla on käytössä ns. ET Balance Import integraationa niin tämä tarkoittaa käytännössä sitä, että saldoaineisto muodostetaan lähdejärjestelmästä esimerkkitiedoston muotoon (csv). Tämän jälkeen integraatio siirtää tilisaldot Finazillaan Finazillan Dropbox-tiedonsiirtotyökalulla.

Alla on kuvattuna esimerkki siitä, minkälainen aineiston tulee olla, mikäli käytössä on dimensiot.

[![](

Mikäli aineistossa ei ole lainkaan dimensioita, muodostetaan aineisto muutoin samanlaiseksi kuin yllä olevassa esimerkissä, mutta sarakkeet E-J voi jättää kokonaan pois.

# **Aineiston tuominen Finazillaan**

Kun tositeaineisto on muodostettu (exceliin), tulee aineisto tallentaa csv -muotoon. Finazillan valmiit pohjat ovat valmiiksi jo csv -mudossa. Suosittelemme nimeämään tiedoston kuvaavasti, esimerkiksi "tositeaineisto 2023" tai "tositeaineisto 042024" tyyppisesti.

Tämän jälkeen mennään Finazillassa valikkoon "company" ja siellä kohtaan settings. Valikossa on kohta "integration file drop-in", johon tiedosto raahataan ja tipautetaan (tai haetaan klikkaamalla ruudussa). Oikeaan reunaan tulee valita vaihtoehto data type "vouchers".

[![](

Sisään luvun jälkeen file upload history näkymä (samassa ikkunassa alempana) kertoo, onko sisään luku ollut onnistunut. Ikkunasta näkee viimeisimmät sisään luvut.

[![](



artikkelin osoite on https://intercom.help/finazilla/fi/articles/6816819-tiedostopohjainen-eli-manuaalinen-tositteiden-tuonti-drop-in-vaihtoehdolla

