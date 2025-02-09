## System Dashboardin kopioiminen

[![](

*Versiopäivityksessä 30.11.2024 tuotu merkittävä parannus. Ominaisuus mahdollistaa sen, että käyttäjät voivat kopioida Finazillan luomia system -tasoisia Dashboardeja ja tämän jälkeen muokata niitä itse. Kopiointi ulottuu myös asiakkuustasoisiin Dashboardeihin.*

Olemme kuvanneet kokoelmassa "[Finazillan luomat valmiit Dashboardit](" minkälaisia Dashboardeja asiakkaillemme näkyy. Aikaisemmin käyttäjät eivät ole voineet vaikuttaa Dashboardeihin muutoin, kuin joko piilottamalla ne kokonaan, tai pitämällä ne näkyvillä kokonaan. Tämän lisäksi Dashboardeja on voinut jatkojalostaa erilaisin sisäänajotiedostoin.

***Jatkossa käyttäjillä on mahdollisuus ottaa Finazillan luomat Dashboardit käyttöön ja lähteä personoimaan niitä haluttuun suuntaan.*** Mikäli Dashboardilla on esimerkiksi raportteja/widgettejä, mitkä eivät ole tarpeellisia, voidaan tällaiset poistaa. Mikäli jossain raporteissa on vaikkapa ei halutut muotoilut, voidaan tilalle tehdä juuri sellaiset muotoilut kun halutaan. Myös kielisyys voidaan vaihtaa tekemällä kiinnittämällä raportteihin suomenkieliset raporttimallit.

Muutoksen taustalla on kantava ajatus siitä, että asiakas saa mahdollisimman paljon valmiina, mutta voi kuitenkin helposti ja vaivattomasti muokata valmiiksi saamaansa haluttuun suuntaan. Alla kerromme, kuinka tämä tehdään.

# System Dashboardin kopioiminen

Finazillan luoman valmiin system -tasoisen Dashboardin voi kopioida navigoimalla sille Dashboardille, mikä halutaan kopioida. Dashboardin oikeassa yläkulmassa on actions -painike, jonka takaa löytyy vaihtoehto "copy".

![](

Copy -valinnan jälkeen käyttäjän tulee antaa uudelle Dashboardille jokin oma nimi. Nimen tulee olla yksilöllinen. Create painike luo kopion ja käyttäjä ohjataan suoraan uudelle Dashboardille.

# Dashboardin käyttämän raportin kopioiminen

Dashboardin kopioiminen ei kopioi taustalla olevia raportteja käyttäjälle, vaan pelkästään itse Dashboardin. Jos siis jotakin raporttia ja sen dataa on tarpeena muokata, tulee itse raporttikin kopioida.

Raportti kopioidaan hyödyntämällä Dashboardin widgetin url -linkkia. Dashboardilla oltaessa raportin otsikkoa klikkaamalla käyttäjä ohjataan linkin avulla varsinaiselle raportille.

[![](

Raportilla oltaessa raportin oikeassa yläkulmassa on vaihtoehto "save as a copy", jonka avulla system tasoinen raportti voidaan kopioida. Raportti nimetään automaattisesti lisäämällä raportin alkuperäisen nimen perään sana copy. Käyttäjä voi itse nimetä raportin uudelleen haluamallaan tavalla. Raportin nimen tulee olla yksilöllinen.

System -tasoisen raportin kopioiminen tekee uudesta raportista käyttäjän omistaman raportin, eli raportti käyttäytyy aivan kuten käyttäjä olisi sen luonut alun alkaenkin itse. Käyttäjällä on raporttiin kaikki muokkausoikeudet. Reports -näkymässä raportti näkyy aivan samalla tavalla kuin muutkin käyttäjän itsensä tekemät raportit.

# Kopioidun Dashboardin muokkaaminen

Huomaa, että kun käyttäjä kopioi vaikkapa system tasoisen Dashboardin, niin Dashboard on nyt kontekstiltaan aivan kuin se olisi käyttäjän itsensä tekemä. Tämä tarkoittaa, että kyseisellä käyttäjällä on Dashboardiin muokkausoikeudet kaikilta osin.

Mikäli jotain Dashboardilla olevaa raporttia halutaan muokata jollakin tavalla (esimerkiksi tietosisältö, ajanjaksot, muotoilut), tulee käyttäjän ensin kopioida system raportti itselleen, tehdä kopioituun raporttiin halutut muutokset ja sen jälkeen vaihtaa kyseinen widget Dashboardilla omaan raporttiin. Käyttäjä voi toki myös toki tehdä suoraan itse jonkin oman raportin ja kiinnittää sen Dashboardille. Mikään pakko ei ole siis tehdä raporttia kopioimalla system -raportti, mutta mikäli muutokset ovat pieniä, säästää tällä aikaa ja vaivaa.

# Asiakkuustasoisten Dashboardien kopiointi

Tässä artikkelissa kuvatut ominaisuudet toimivat vastaavalla logiikalla myös asiakkuustason Dashboardeissa. Asiakastasoisia Dashboardeja olemme kuvanneet ohjeissamme [täällä]( tarkemmin.

Jos asiakkuuteen on tehty customer -tason Dashboardeja, voidaan navigoida asiakkuustason Dashboardille ja kopioida se tässä ohjeessa kuvatulla tavalla. Myös asiakkuustason raportit voidaan kopioida ohjeessa kuvatulla tavalla. Kopioista tulee tavallisia yritystasoisia käyttäjän omistamia Dashboardeja ja raportteja.

# Ominaisuudessa huomioitavaa

* Dashboardin kopiointi ei kopioi automaattisesti Dashboardilla olevia raportteja
* Mikäli Dashboardin raporttien tietosisältöön tai muotoiluun halutaan tehdä muutoksia, tulee käyttäjän tehdä oma raportti (joko kopioimalla ja alusta saakka) ja "korvata" Dashboardin widget käyttämään omaa raporttia
* Kopioista tulee aina käyttäjän omia Dashboardeja/raportteja
* Kopio tulee muistaa jakaa muille käyttäjille, mikäli sen halutaan näkyvän muille käyttäjille. Jako pitää muistaa tehdä sekä Dashboardille, että raporteille
* System Dashboardeja ja raportteja voi kopioida asiakkuuden pääkäyttäjä, yrityksen pääkäyttäjä ja rajoitetun roolin omaava käyttäjä
* Mikäli käyttäjällä on rajoitettu rooli ja oikeus vain osaan datasta, saa hän kopioihinsa myös vain omia oikeuksiaan vastaavat datat
* Asiakkuustasoisia Dashboardeja voi kopioida asiakkuuden pääkäyttäjä. Yrityksen pääkäyttäjä ja rajoitetun roolin omaava käyttäjä voivat kopioida myös, mikäli heille näkyy asiakkuustason Dashboardeja. Näkyvyys riippuu siitä, onko kyseisiin yrityksiin sellaisia luotu


artikkelin osoite on https://intercom.help/finazilla/fi/articles/10174619-system-ja-asiakkuustasoisten-dashboardien-kopiointi

