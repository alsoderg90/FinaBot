## Syöttörivin luominen osabudjetille

Tämä artikkeli täydentää aikaisempia artikkeleitamme budjetointiin, osabudjetteihin ja kaavoihin liittyen. Tämän artikkelin ymmärtämistä helpottaa, jos käyttäjä tuntee jo Finazillan budjetoinnin, osaa luoda uuden osabudjetin ja sinne erilaisia perusrivejä.

Tase on tyypillisin esimerkki kumuloivasta laskennasta, jossa otetaan aina pohjalle edellisen kuukauden saldo sekä lisätään siihen muutos. Vastaavia kumulatiivisia laskentoja voi käyttää hyödykseen myös mm. osabudjetilla.

Tässä esimerkissä näytämme, miten rakennetaan kaava, jossa kumuloidaan saldoa.

# Syöttörivin luominen osabudjetille

Luodaan ensin uusi osabudjetti, jolle luodaan input -tyyppinen syöttörivi. Rivi luodaan plus merkin takaa valikosta "add new row". Rivin tyypiksi valitaan "input". Kun rivi on luotu, riville voidaan syöttää tässä kohdin jo arvoja.

[![](

# Kaavarivin luominen osabudjetille

Seuraavaksi luodaan osabudjetille kaavarivi, jossa kaavana on kumuloiva kaava ensimmäiseen riviin liittyen. Luodaan siis jälleen uusi rivi "add new row" toiminnolla. Rivin tyypiksi valitaan "formula". Mennään kaavaeditoriin ja luodaan oheinen kaava valitsemalla luotu rivi budget rows -valikosta.

[![](

# 

# Kaavan kirjoittaminen osabudjetille vaiheittain

Tässä kohdin tulee huomata, että kaavaeditoriin kaava syötetään siten, että ensin haetaan "budget rows" kentästä kaavaan "syöttörivi", sen jälkeen valitaan operaattoreista plus -merkki. Seuraavaksi valitaan "column ref." kenttään miinus 1 (joka viittaa siis edelliseen soluun) ja haetaan lopuksi "budget rows" valikosta kaavaan rivi "kumuloiva rivi, joka on budjetille luotu 2. rivi).



artikkelin osoite on https://intercom.help/finazilla/fi/articles/4604752-esimerkki-osabudjetille-kumuloivan-rivin-rakentaminen

