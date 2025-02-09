## Prosentuaalisen tunnusluvun haasteet, jos raportissa on useita dimensioita

Raporttimallit mahdollistavat monenlaista laskentaa ja usein raporttimalleille halutaankin lisätä erilaisia prosentuaalisia tunnuslukuja hyödyntämällä kaavariviä. Yksi tällainen tunnusluku on kateprosentti.

Tässä artikkelissa kerromme, minkälaisia haasteita raporttimallien kanssa voi tulla vastaan, mikäli tarpeena on raportoida erilaisia prosentuaalisia tunnuslukuja käyttämällä useita dimensioita tai raportointiryhmiä. Lisäksi kerromme, miten esiin tulevat haasteet voidaan ratkaista.

# Prosentuaalisen tunnusluvun haasteet, jos raportissa on useita dimensioita

Raportilla, missä lasketaan esimerkiksi kateprosenttia, ja raportin valinnoissa on tavalla tai toisella valittuna useita dimensioita, raportin kateprosentti laskettuu kokonaisuutena oikein, mutta tätä tietoa ei voi lähteä pivotoimaan auki. Auki pivotoituna kateprosentti summaantuu yhteen.

Tämä on kuitenkin ratkaistavissa muuttamalla raportin muodostamisen logiikkaa. Alla kuvattu tapa mahdollistaa raportin auki pivotoimisen siten, että prosentuaalinen tunnusluku laskettuu oikein.

# Kuinka luoda raportti, missä on prosentuaalinen tunnusluku sekä useita dimension arvoja?

Mikäli tarpeena on luoda raportti, missä raportoidaan kateprosenttia useammasta dimensiosta joko siten, että dimension arvoja on valittu dimensions -valikosta tai käyttämällä raportointiryhmää, tulee raportti luoda siten, että raportille luodaan eri tietolähteet eri dimensioille.

Käytännössä tämä tarkoittaa sitä, että jos halutaan raportoida kahta dimension arvoa, luodaan kaksi datalähdettä, joissa toisessa on dimension arvo A ja toisessa B. Jos raportti halutaan tehdä käyttämällä raportointiryhmiä, luodaan kullekin raportointiryhmälle oma tietolähde.

[![](

*Ohje pätee kaikkiin prosentuaalisiin tunnuslukuihin*



artikkelin osoite on https://intercom.help/finazilla/fi/articles/5352276-esimerkki-prosentuaalisen-tunnusluvun-laskenta-kun-raportoidaan-useita-dimensioita

