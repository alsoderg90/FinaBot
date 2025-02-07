## Taustaa

Tässä esimerkissä neuvomme, miten myyntisaamiset voidaan laskettaa tasebudjettiin hyödyntämällä tulosbudjettia sekä kaavaa. Artikkelin ymmärtämisen edellytyksenä on, että käyttäjä osaa Finazillan budjetoinnin perusperiaatteet, sekä osaa luoda kaavarivejä.

# **Taustaa**

Yrityksen myynti on kotimaan myyntiä, jolloin kaikessa myynnissä on alv -kantana 24% alv. Lisäksi yrityksen laskutus tehdään aina kunkin kuun lopussa ja laskuilla on 14 päivän maksuaika. Näin ollen myyntisaatavat kotiutuvat aina oletusarvoisesti seuraavassa kuussa.

Budjetilla myynnit on budjetoitu kuvan osoittamaan kokonaisuuteen, eli otsikon "myyntituotot" alle.

[![](

Tasebudjetilta myyntisaatavat löytyvät välilehden "assets" alta

[![](

Tässä esimerkissä myyntisaamiset lasketaan yhdelle tilille, joka on tili 1700 myyntisaamiset.

[![](

# **Kaavan kirjoittaminen**

Oletuksena tili "1700 Myyntisaamiset" on input -tyyppinen syöttörivi. Kun kyseiseen riviin halutaan rakentaa laskentakaava, tulee rivin tyypiksi vaihtaa "formula" eli kaavarivi.

[![](

Kun rivin tyypiksi vaihdetaan vaihtoehto "formula", aukeaa käyttäjälle nk. kaavaeditori -näkymä. Kaavaa päästään kirjoittamaan kuvan osoittaman painikkeen takaa.

Aukeava syöttöikkuna on oheinen. Kaavaa kirjoitetaan aina "formula" kenttään valitsemalla "budget rows" valikosta haluttuja määreitä kaavaan.

[![](

Kun kaavaa lähdetään kirjoittamaan, tulee ensin mieltää, mitä kaavaan ollaan laskemassa. Esimerkin tapauksessa todettiin, että myyntisaamiset maksetaan aina seuraavassa kuussa kuin milloin varsinainen laskutus on tapahtunut. Näin ollen esimerkiksi budjetilla kaudella 1/2021 olevat myynnit maksetaan kaudella 2/2021. Myyntisaamisiin kirjaus kohdistuu siis kaudella 1/2021 ja pankkitilille ko. summa tuloutuu kaudella 2/2021.

Ensimmäiseksi kaavaan otetaan mukaan myynnit. Esimerkin tapauksessa myynnit olivat ryhmän "myyntotuotot" alla. Tällöin kaava on järkevää rakentaa käyttämällä koko tiliryhmää, eikä summata yksittäisiä tilejä kaavaan mukaan.

[![](

Kun kaavaan lisätään mukaan budjettirivi "myyntituotot", on kaavarivi oheinen.

[![](

## Arvonlisävero kaavassa

Myyntituotot tiliryhmän saldo ei sisällä kuitenkaan lähtökohtaisesti arvonlisäveroa, joka halutaan laskea myyntisaataviin kuitenkin mukaan. Tällöin kaavassa tulee vielä huomioida arvonlisävero 24%.

Arvonlisävero saadaan summaan mukaan kertomalla myyntituotot 1,24:lla. Kaavaan lisätään siis vielä kyseinen laskenta. Tässä yhteydessä tulee lisäksi huomioida, että myyntitilit ovat Finazillassa tyypiltään "credit" tyyppisiä tilejä, jolloin kaavassa käytettään kertojana -1,24:aa.

[![](

Tämän jälkeen myyntisaamiset laskettuvat tasebudjetille automaattisesti oheisesti;

jos myynti on kaudella 1/2021 vaikkapa 1000€, kirjaa Finazilla kaudelle 1/2021 tilille 1700 Myyntisaamiset 1240€ (eli myynnin sisältäen alv:n osuuden).

[![](

*Yllä oleva esimerkki perustuu oletukseen, että kaikki myynti on alv 24% alaista.*



artikkelin osoite on https://intercom.help/finazilla/fi/articles/5313648-tasebudjetointi-myyntisaatavien-laskettaminen-myyntien-perusteella

