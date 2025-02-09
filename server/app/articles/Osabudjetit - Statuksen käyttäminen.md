## Statuksen käyttäminen

[![](

*Versiopäivityksessä 4.3.2023 tuotu kokonaan uusi toiminto. Toiminto mahdollistaa osabudjetille statuksen asettamisen.*

# Statuksen käyttäminen

Osabudjetin statuksen määritteleminen helpottaa budjetointia organisaatioissa, missä budjetointityöhön osallistuu useampi henkilö. Erilaisilla statuksilla voidaan merkitä esimerkiksi se, että mitkä osiot on budjetoitu ja pääkäyttäjän toimesta tarkistettu, ja mikä odottaa jotakin seuraavaa vaihetta. Toiminto on suunniteltu helpottamaan siis erityisesti pääkäyttäjän kokonaiskuvan saamista.

# Status kentän vaihtoehdot

* In progress = prosessissa/kesken
* Needs rework = vaatii työtä
* Done = Valmis
* Approved = Hyväksytty

  + ko. statuksen omaavaa osabudjettia ei saa/voi enää muokata

    - Rivien & rakenteiden muokkaaminen ei ole enää mahdollista
    - Lukujen import ei ole enää mahdollinen
* Not started = Ei aloitettu
* No status (Ei näytetä listauksessa mitään) = Ei statusta
* Oma custom status (voidaan siis vapaasti kirjoittaa mitä tahansa statukseen)

  ​
# Osabudjetin statuksia voidaan asettaa kolmessa ei paikassa

* Osabudjettia luotaessa
* Osabudjettilistauksen kautta edit -painikkeen kautta
* Osabudjetin työkalun valikon kautta (nk. modaalin kautta)

Kerran asetettu status näkyy muissakin paikoissa, missä status voidaan asettaa. Jos osabudjetille on siis asetettu status "not started" osabudjettia luotaessa, näkyy tämä status editin kautta, sekä työkaluvalikon kautta statusta tarkasteltaessa. Statuksia voidaan asettaa kolmessa eri paikassa sen vuoksi, että erilaisin käyttöoikeuksin varustetut henkilöt voivat asettaa tarvittavia statuksia ja pääkäyttäjä pystyy hallinnoimaan kokonaisuutta.

## Osabudjettilistauksen kautta edit -painikkeen kautta asetettava status

Osabudjetit löytyvät budjetin takaa valikosta sub budgets. Valikossa näkyy kaikki kyseisen budjetin osabudjetit. Osabudjettlistassa näkyy edit -painike kunkin osabudjetin perässä. Aukeavassa näkymässä on kenttä "Select sub budget Status".

[![](

## Työkaluvalikon kautta tehtävä statuksen asettaminen

Kun osabudjetti on aukaistu, löytyy status -painike työkalupalkista aivan oikeasta reunasta.

[![](

Yllä olevan kuvan mukaisesta painikkesta päästään asettamaan ko. statukset.

[![](

**Esimerkki1:**

Kolme osabudjettia, joista yhdelle ei ole asetettu statusta. Yhden osabudjetin status on not started ja toisen osabudjetin status on done.

[![](

# Statuksen asettaminen ja käyttäjän rooli/oikeudet

Statuksen asettaminen on sidottu tietyiltä osin käyttäjän oikeuksiin. Tällä halutaan varmistaa, että pääkäyttäjälle jää sellaiset toimenpiteet, joiden voidaan ajatella olevan nimenomaan pääkäyttäjän vastuulle/oikeuksiin kuuluvia asioita.

Pääkäyttäjät, eli käyttäjät, joilla on kaikki oikeudet, voivat päivittää osabudjetin statuksia kaikkialla (osabudjettia luotaessa, edit -painikkeen kautta ja osabudjetin työkaluvalikon kautta).

Budjetteihin liittyen Finazillassa on olemassa edit -oikeus. Tällä oikeudella voi syötellä ja muutella rakenteita ja tehdä kaikkea. Tämä on vanha oikeus, joka ei ole muuttunut millään tavalla. Kaikki vanhat käyttäjät joilla on edit -oikeus, saavat automaattisesti myös uuden tässä yhteydessä luodun input -oikeuden. Tämä oikeus ei käytännössä muuta heidän oikeuksiaan millään tavalla.

Osabudjetin statuksen yhteydessä budjetteihin on tuotu uusi oikeus nimeltä input. Tällä oikeudella käyttäjä pääsee syöttämään lukuja, mutta ei voi muokata mitään kaavoja/rakenteita jne. Tällä roolilla osabudjetin saa laittaa tilaan in progress tai done; ei muualle. Input oikeudella osabudjetin statuksen voi asettaa vain osabudjetin kautta; ei siis osabudjettilistauksen puolelta.

[![](

*Uutta osabudjettia luotaessa statukseksi voi asettaa "not started". Kun osabudjetin rakennetta ollaan työstämässä, voi status olla esimerkiksi "In progress". Jos osabudjettia budjetoi vaikkapa myyntijohtaja, voi hän vaihtaa statukseksi "done". Tämän jälkeen pääkäyttäjä voi käydä validoimassa osabudjetin ja vaihtaa statukseksi "approved" tai "needs rework".* 



artikkelin osoite on https://intercom.help/finazilla/fi/articles/6967112-osabudjetin-status-valinta

