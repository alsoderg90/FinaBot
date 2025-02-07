## Taustaa

Artikkelimme "[uuden käyttäjätunnuksen luominen](" kuvaa, kuinka Finazillaan luodaan uusia käyttäjätunnuksia. Tässä artikkelissa esittelemme, kuinka luodaan käyttäjätunnuksia useampaan asiakkuuden yritykseen, silloin kun tarpeena on myös rajata käyttäjän näkemää dataa. Ohje on erityisen tarpeellinen mm. konserniyrityksille.

Tämän artikkelin ymmärtämisen edellytyksenä on, että käyttäjä osaa jo luoda käyttäjätunnuksia ja ymmärtää mikä ero on customer ja company -tasoisilla käyttäjätunnuksilla. Lisäksi käyttäjä ymmärtää roolien merkityksen.

# Taustaa

Finazillassa on asiakkuus nimeltä Filmmaker Group Oy. Asiakkuudessa on kolme yritystä; Filmmaker Group, Movies Ltd ja Series Ltd. Käyttäjälle halutaan antaa oikeus yrityksiin Filmmaker group sekä movies ltd.

[![](

# Käyttäjätunnuksen luominen

Käyttäjälle luodaan company -tasoinen käyttäjätunnus yritykseen Filmmaker Group. Company -tasoinen käyttäjätunnus saa aina oletuksena roolin "company user", jonka lisäksi käyttäjälle tulee antaa varsinainen muu haluttu rooli. Tässä tapauksessa käyttäjälle halutaan antaa ns. pääkäyttäjyys yritykseen Filmmaker Group, joten käyttäjätunnukseen kiinnitetään rooli CompanySuperUser.

[![](

# Seuraavan yrityksen kiinnittäminen jo olemassa olevaan käyttäjätunnukseen

Seuraavaksi käyttäjätunnukselle halutaan antaa oikeus toiseen asiakkuuden yritykseen; yritykseen Movies Ltd. Uutta kiinnitystä lähdetään tekemään samasta valikosta kuin missä äsken luotiin käyttäjätunnus. Oikeassa yläkulmassa on painike "add user to role", jolla lähdetään kiinnittämään uutta roolia käyttäjätunnukselle.

[![](

Käyttäjätunnukselle lisätään ensimmäisenä kirjautumisen mahdollista roolitus yritykseen Movies Ltd. Tämä rooli on nimeltään "company user".

Alasvetovalikoista voidaan valita minkä tasoinen tunnus ollaan luomassa (customer vs company), role kenttään kerrotaan haluttu rooli (koskettaa vain company -tasoisia käyttäjätunnuksia) ja company -valikosta löytyvät kaikki asiakkuuden yritykset.

[![](

Lopuksi käyttäjälle tulee vielä antaa rooli, mikä määrittelee mitä käyttäjä saa nähdä ja tehdä Finazillassa yrityksessä Movies Ltd. Tähän yritykseen käyttäjän oikeuksia halutaan rajata, jolloin käyttäjälle kiinnitetään rajoitettu rooli.

Uusi rooli lisätään jälleen "add user to role" painikkeen takaa. Käyttäjälle kiinnitetään aikaisemmin luotu rooli nimeltä "budjetointirooli".

[![](

Käyttäjätunnus näyttäytyy nyt oheisesti:

[![](

# Mitä käyttäjä näkee?

Kyseinen käyttäjä pääsee nyt näkemään Finazillassa yritykset Filmmaker Group sekä Movies Ltd. Jälkimmäisen osalta hänen oikeuksiaan on rajoitettu erillisellä budjetointiroolilla kun taas Filmmaker Groupin osalta hän pystyy näkemään kaiken ja tekemään kaikkea.

[![](

*Mikäli käyttäjä saa nähdä kaiken mahdollisen datan kaikista yhtiön yrityksistä, sekä muokata vapaasti kaikkea, on kyseessä customer -tasoinen pääkäyttäjätunnus. Tällöin riittää kun käyttäjälle luodaan customer -tasolle käyttäjätunnus. Tunnusta ei tarvitse erikseen kytkeä mihinkään rooliin eikä asiakkuuden yrityksiin.* 

# Lisätietoja

[Pääkäyttäjätunnuksella pääsee näkemään ja muokkaamaan kaikkien yhtiöiden dataa sekä toimintoja](



artikkelin osoite on https://intercom.help/finazilla/fi/articles/5639574-esimerkki-kuinka-luodaan-kayttajatunnus-useampaan-asiakkuuden-yritykseen

