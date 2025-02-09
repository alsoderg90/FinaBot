## Tiedostopohjainen integraatio

Mikäli käytössä on sellainen lähdejärjestelmä, mistä ei ole olemassa valmista rajapintaa Finazillaan, tuodaan tieto Finazillaan joko tiedostopohjaisella integraatiolla, tai manuaalisesti drop- in tuontina. Tämä artikkeli käsittelee nimenomaan tiedostopohjaista integraatiota, joka hyödyntää SFTP -palvelinta.

# Tiedostopohjainen integraatio

Tiedostopohjaiset integraatiot, jotka hyödyntävät tiedostojen noutoa SFTP -palvelimelta, synkronoivat tiedot Finazillaan noutopaikasta noin 1 - 20 minuutin välein. Tiedot voi tarvittaessa päivittää Finazillaan myös kesken päivän. Synkronointitiheyttä voidaan säätää tarpeen mukaan myös esimerkiksi siten, että nouto tapahtuukin vain kerran päivässä.

## Prosessin kulku

Käytännössä tiedostopohjainen integraatio edellyttää, että asiakkaalla on olemassa SFTP -palvelin. Finazilla noutaa palvelimelta asiakkaan muodostaman aineiston ja sisään ajaa sen Finazillaan. Tiedostolle on käyttöönoton yhteydessä sovittu yhteinen muotovaade, jossa tiedoston tulee olla.

Onnistuneet tiedostot siirretään tyypillisesti siirron jälkeen automaattisesti omaan kansioonsa ja epäonnistuneet tiedostot omaan kansioonsa.

Sisään ajon jälkeen datat ovat välittömästi päivittyneet Finazillaan.

## Manuaalinen päivittäminen kesken päivän

Manuaalinen tietojen päivittäminen tapahtuu valikosta "Company Settings". Näkymässä on hieman alempana kohta "Integration file drop-in", jossa valitaan tuotavan datan tyyppi.

Finazilla käynnistää automaattisen saldojen lasketuksen (recalculate balances). Lasketuksen etenemistä voi seurata yläpalkin notifikaatioiden kautta.

[![](

# Lisätietoja

[Tietojen päivittäminen Finazillaan kesken päivän](



artikkelin osoite on https://intercom.help/finazilla/fi/articles/4126614-tiedostopohjainen-tositteiden-tuonti-tiedostopohjaisella-integraatiolla-sftp

