## Integraation avaaminen

Tässä artikkelissa kerromme integraation avaamisesta yleisellä tasolla sekä kerromme myös datan siirtymisestä Finazillaan ns. tiedostopohjaisena vientinä. Asiat on kuvattu samassa artikkelissa, sillä asiakkailla, joilla on käyttössään integraatio, on myös optio tuoda dataa drop-in toiminnon avulla.

Kun yrityksen perustaminen on siinä vaiheessa, että yritykselle voidaan kytkeä integraatio päälle, tarvitaan avauksen tueksi käyttöönottolomaketta, joka on toimitettu uusille asiakkaille asiakkuuden alkuvaiheessa. Käyttöönottolomakkeessa kysytään mm. integroitava järjestelmä ja muita avaamiseen liittyviä tietoja, sekä tilikaudet, joista tiedot tullaan siirtämään.

# **Integraation avaaminen**

Integraation avaaminen alkaa sillä, että asiakkaan lähdejärjestelmässä täytyy käydä sallimassa rajapinnan käyttö. Tämän jälkeen lähdejärjestelmässä luodaan rajapintatunnukset, jotka toimitetaan Finazillalle käyttöönottolomakkeella. Näistä vastaa aina asiakas.

[![](

*Finazilla toimittaa rajapinnan käyttöön ja tunnusten luomiseen liittyen asiakkaalle lähdejärjestelmäkohtaisen asiakasohjeen avuksi, jota noudattamalla rajapinta saadaan avattua oikeaoppisesti. Ohjetta tulee noudattaa täsmällisesti.* 

# **Integraation avaamisen jälkeen datan siirtyminen**

Finazilla hoitaa ensimmäisen tiedonsiirroon ja samalla varmistaa ensimmäisen tiedonsiirron yhteydessä, että siirtyvät tiedot täsmäävät asiakkaan lähdejärjestelmästä toimittamaan tuloslaskelmaan ja taseeseen. Näin toimien voidaan varmistua, että alkutilanne on oikea.

Tämän jälkeen data siirtyy ajastetusti joka yö Finazillaan ja päivittyy automaattisesti olemassa oleville raporteille.

# **Tiedostopohjaisen siirron aloittaminen**

Mikäli käytössä ei ole integraatiota, kyse on tiedostopohjaisesta siirrosta.

Tiedostopohjainen siirto jakautuu kahdenlaisiin vaihtoehtoihin; sellaisiin, jotka hyödyntävät tiedotojen noutoa SFTP -palvelimelta ja sellaisiin, joissa tiedosto tuodaan aina manuaalisesti haluttaessa Finazillaan.

Tiedostopohjaiset integraatiot, jotka hyödyntävät tiedostojen noutoa SFTP -palvelimelta, synkronoivat tiedot Finazillaan noutopaikasta noin 1 - 20 minuutin välein - riippuen siitä, miten asiasta on sovittu. Tämä tarkoittaa sitä, että asiakkaan vastuulla on huolehtia sovitunlainen tiedosto sovittuun paikkaan, josta Finazilla noutaa sen ja vie sen Finazillaan. Tiedostojen viennin Dropboxiin voi aloittaa kun yritys on luotu ja sille on tuotu kirjanpidon tilit, määritetty tilikaudet sekä tilikartta.

Mikäli tiedostot tuodaan aina itse manuaalisesti tarpeen mukaan Finazillaan, vastaa tästä työstä asiakas. Ohje toimintoon löytyy [tästä.](

# **Ylimääräiset datan päivittämiset kesken päivän**

Kummassakin yllä kuvatussa vaihtoehdossa tiedot voi *lisäksi* aina tarvittaessa päivittää Finazillaan myös kesken päivän. Tämä tapahtuu siten, että käydään tipauttamassa siirtotiedosto itse Finazillaan silloin, kun halutaan siirtää dataa lähdejärjestelmästä Finazillaan. Asiakkailla, joilla on käytössään integraatio, datan ajamisen voi vain käynnistää kesken päivän.



artikkelin osoite on https://intercom.help/finazilla/fi/articles/4283425-integraation-avaaminen-osana-yrityksen-perustamista

