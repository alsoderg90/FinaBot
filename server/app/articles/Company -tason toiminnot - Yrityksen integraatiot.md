## Yrityksen integraatiot

Asiakkailla, joilla on käytössään API-rajapinta (kuten mm. Procountor, Netvisor, Lemonsoft jne), Finazillaan siirtyy automaattisesti joka yö kaikki uudet dimensiot ja dimension arvot. Joskus voi olla kuitenkin tilanne, että kaikkia dimensioita ei tarvita Finazillassa. Tällöin suosittelemme rajaamaan turhat dimensiot pois integraatiosta.

# Yrityksen integraatiot

Yrityksen asetuksien kautta valikossa company, kohdassa settings, nähdään mitä integraatioita kyseisellä yrityksellä on käytössä. Integraatiot löytyvät omalta välilehdeltään "integrations". Mikäli yrityksellä on useita integraatiota, näkyy jokainen lähdejärjestelmä omana rivinään allekkain.

[![](

# Integraation muokkaaminen

Integraatiota voidaan lähteä muokkaamaan lähdejärjestelmän perässä olevan edit -painikkeen kautta (kts. ylempi kuva). Edit aukaisee kyseisen integraation määrittelylomakkeen.

Määrittelylomakkeesta löytyy painike "Advanced settings", josta päästään tarkempaan määrittelyyn.

[![](

## Kirjanpidon dimension/dimensioiden blokkaaminen integraatiosta

Advanced settings -valikon alta löytyy erillinen kenttä, missä voidaan määritellä, että mitä dimensiota ei haluta siirtää integraatiossa. Exclude accounting dimensions -kenttä (kuvassa korostettu keltaisella) on tarkoitettu kirjanpidon dimension/dimensioiden blokkaamiseen ja exclude operative dimensions -kenttä (kuvassa korostettu vihreällä) on tarkoitettu operatiivisten dimensioiden blokkaamiseen.

[![](

Kenttiä käytetään siten, että niihin kirjoitetaan sen dimension nimi, mitä ei haluta enää siirtää. Nimi tulee kirjoittaa täysin samalla tavalla kuin se esiintyy lähdejärjestelmässä. Kuvan esimerkissä ollaan blokkaamassa dimensiota nimeltä "Kustannuspaikka". Klikkaamalla kohtaa "Exclude: Kustannuspaikka, dimensio kiinnittyy kenttään ja tulee valituksi. Update -painike päivittää muutoksen integraatiolle.

[![](

Mikäli integraatiosta halutaan poistaa useampi dimensio, kirjoitetaan ne yksitellen edellä mainitulla tavalla. Kenttään kiinnittyy tällöin useita dimensioita.

[![](

## Operatiivisen datan dimension/dimensioiden blokkaaminen integraatiosta

Operatiivisia dimensioita syntyy API -rajapintaa käyttäville asiakkaille automaattisesti sekä myyntilaskuista, että ostolaskuista. Olemme kuvanneet kyseisiä dimensioita tarkemmin kunkin lähdejärjestelmän omassa ohjeessa. API -rajapinnan ohjeet löytyvät kokoelmasta [täältä.]( 

Operatiivisia dimensioita voi olla tarpeen blokata integraatiosta, sillä välttämättä kaikki rajapinnan kautta siirtyvät dimensiot eivät ole kaikille asiakkaille tarpeellisia. Alla olevassa esimerkissä on haluttu blokata laskun numero. Laskun numero on operatiivinen dimensio, joka syntyy myynti/ostolaskudatasta. Kyseiselle yritykselle ei enää siirry laskunnumeroa dimensioksi.

Varsinainen blokkaaminen tehdään samoin kuin kirjanpidon dimensioiden blokkaaminen tehdään.

[![](



artikkelin osoite on https://intercom.help/finazilla/fi/articles/8708026-dimensioiden-rajaaminen-integraatiosta-pois

