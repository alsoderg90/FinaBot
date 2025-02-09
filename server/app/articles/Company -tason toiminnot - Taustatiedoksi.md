## Taustatiedoksi

Dimensiot löytyvät valikosta "Company" ja sieltä kohta "Dimensions". Käyttäjälle avautuu lista yrityksellä käytössä olevista dimensioista.

# Taustatiedoksi

Esimerkin yrityksellä on dimensio nimeltä "Movies", jonka alla on kaksi dimensiovalueta; "Movie X" sekä "LA studio". Tässä esimerkissä luodaan hierarkinen dimensiorakenne siten, että dimensio "LA studios" on alisteinen dimensiolle "movie X".

# Hierarkisen dimensiorakententeen luominen

Valitaan dimension "LA studios" klikkaamalla dimension nimeä. Käyttäjälle aukeaa dimension muokkausikkuna. Käydään valitsemassa kohtaan "Parent" se dimensio, jolle kyseisestä dimensiosta halutaan tehdä alisteinen. Muutos tallennetaan painikkeesta "Edit dimension".

[![](

Tämän jälkeen käydään lisäämässä dimensioille niin kutsutut dimensiovaluet eli arvot.

Dimensiovalue luodaan klikkaamalla dimension nimeä. Yläosaan aukeaa kohta "create new dimension value". Luodaan uusi dimensiovalue.

Selkein tapa toimia on aloittaa ylimmän tason valueista ja työskennellä siitä hierarkisesti alaspäin. Ylimmän tason dimensiovaluelle ei tulee Parenttia, mutta seuraavalla tasolla kyseisen dimensiovaluen parentiksi tulee edellinen ylemmän tason dimensiovalue.

# Hierarkisen dimensiorakenteen erottaminen

Hierarkinen dimensiorakenne näkyy käyttäjälle Dimensions -listauksessa siten, että kyseisen dimension "Parent" kentässä näkyy mille dimensiolle kyseinen dimensio on alisteinen.

Hierarkinen rakenne näkyy käyttäjälle myös klikkaamalla sitä dimension nimeä, mikä on hierarkisen rakenteen ylin dimensio. Tässä tapauksessa se on dimensio Movies.

[![](

[![](

*Dimension parent-arvoa ei voi poistaa, jos dimension arvoille on asetettu jokin parent-arvo. Näissä tilanteissa täytyy ensin poistaa dimension parent arvo ja sen jälkeen pääsee poistamaan dimension arvojen parent -kiinnitykset*



artikkelin osoite on https://intercom.help/finazilla/fi/articles/4134158-hierarkisen-dimensiorakenteen-luominen-silloin-kun-joku-dimensio-on-toiselle-dimensiolle-alisteinen

