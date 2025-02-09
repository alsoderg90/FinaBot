## Uuden raporttimallin luominen

Tässä esimerkissä neuvomme vaihe vaiheelta, miten luodaan uusi raporttimalli. Artikkelin ymmärtäminen edellyttää, että käyttäjä tietää jo mitä raporttimallit ovat ja ymmärtää hieman raporttimallien logiikkaa. Artikkeli täydentää aikaisempia raporttimalleja käsitteleviä artikkeleitamme.

Esimerkissä luotavalla raporttimallilla halutaan raportoida yrityksen liikevaihto, myyntikate ja myyntikate%.

# Uuden raporttimallin luominen

Raporttimallin luominen tehdään Customer -tasolla, koska raporttimallin halutaan olla kaikkien asiakkuuden yritysten käytettävissä. Mennään valikkoon Customer ja siellä kohtaan "report scheme". Uusi raporttimalli luodaan yläkulman "new report scheme" painikkeen kautta.

[![](

Tämän jälkeen käyttäjälle aukeaa syöttöikkuna, jossa annetaan raporttimallille nimi. Raporttimallille ei valita mitään templatea, sillä malli rakennetaan alusta saakka itse eikä kopioida mitään valmista mallia.

[![](

# **Rivien lisääminen raporttimallille eli nk. raporttipuun laatiminen**

Tämän jälkeen aletaan rakentamaan raporttimallille rivejä eli nk. raporttipuuta. Luodaan ensimmäiseksi riviksi otsikkorivi eli nk. header -rivi, jonka nimi on "liikevaihto". Riville tehdään lapsirivi (child row), joka on tyypiltään "balance data" -tyyppinen ja kerää luvut tiliväliltä 3000 - 3599. Luvut summataan otsikkoriviin. Tästä löytyy esimerkki ohjeestamme [täältä.](#h_12b51dca51) 

Seuraavaksi raporttipuuhun luodaan rivi "myyntikate", joka luodaan luomalla ensin otsikkorivi "myyntikate" ja luomalla tämän alle lapsirivi, joka on jälleen tyypiltään balance -tyyppinen. Rivi kerää luvut tiliväliltä 3000 - 4999 ja summaa ja otsikkoriviin.

Kolmanneksi raporttimallille luodaan myyntikate % rivi. Luodaan rivi, jonka tyyppinä on kaava (formula). Kirjoitetaan riville kaava, joka on tässä tapauksessa myyntikate jaettuna liikavaihdolla ja kerrottuna sadalla.

Raporttimallin raporttipuu on nyt tämän näköinen:

[![](

Raporttimalli on tämän jälkeen valmis käytettäväksi ja sillä voi lähteä raportoimaan.



artikkelin osoite on https://intercom.help/finazilla/fi/articles/4560465-esimerkki-uuden-raporttimallin-luominen-raportoidaan-liikevaihto-myyntikate-ja-myyntikate

