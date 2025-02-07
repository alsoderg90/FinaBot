## Laskentavakion luominen

Laskentavakiot (calculation constants) ovat budjetoinnin ja raportoinnin aputyökaluja, joiden avulla samaa kiinteä arvoa voidaan käyttää eri budjeteissa -ja arvoa päivittämällä, päivittää arvo kerralla kaikkialle missä laskentavakiota on käytetty. Tämän artikkelin ymmärtämistä helpottaa, jos käyttäjä tietää jo peruspiirteittäin mitä laskentavakiot ovat sekä osaa luoda erilaisia kaavarivejä osabudjeteille.

Laskentavakioiden käyttöä olemme opastaneet aikasemmissa artikkeleissamme ja aiheeseen liittyvät artikkelit löytyvät myös tämän artikkelin lopusta. Tämä artikkeli opastaa, kuinka luodaan *yrityskohtainen* *prosentuaalinen* laskentavakio. Havainnollistamme asiaa esimerkin avulla.

**Esimerkki**

Yrityksessä on käytössä myyntikomissio siten, että myyjälle maksetaan prosentuaalinen myyntikomissio tekemistään kaupoista. Sovittu myyntikomissio on 1.1.2020 lähtien 8% suuruinen. Komissio muuttuu pitkin vuotta. Myyntikomissio käsitellään Finazillassa osabudjetin kautta käyttämällä laskentavakiota hyväksi laskennassa.

# **Laskentavakion luominen**

Luodaan yrityskohtainen laskentavakio myyntikomissiolle menemällä Company -valikossa kohtaan "Calculation Constants". Näkymään tulee kaikki yrityksen laskentavakiot. Uusi laskentavakio luodaan "new calculation constants" -painikkeesta.

Luotavalle laskentavakiolle annetaan nimi, symbol -kenttään jokin lyhyt nimi mistä laskentavakion tunnistaa budjetti -näkymässä sekä tehdään valinta "percentage", koska luotava laskentavakio on prosenttimuotoinen. Create calculation constants -painike luo laskentavakion ja se ilmestyy tämän jälkeen listaan.

[![](

Kun luotu laskentavakio löytyy listasta, klikataan sen nimeä. Laskentavakionäkymä on ns. "tyhjä", koska laskentavakiolle ei ole vielä kiinnitetty yhtään arvoa. Uusi arvo luodaan "New Value" painikkeesta.

[![](

Kun laskentavakiolle syötetään arvoa, valitaan ensimmäisenä päivä mistä lähtien arvo on voimassa. Value -kenttään syötetään arvo prosentteina. Create Calculation Constant Value -painike luo arvon.

# **Laskentavakion arvojen päivittäminen**

Yhdelle laskentavakiolle voi antaa lukuisia arvoja. Tällöin uutta arvoa määriteltäessä valitaan vain aina päivämäärä, mistä lähtien kyseinen arvo on voimassa. Edeltävä arvo päivittyy päättymään automaattisesti edelliseen päivään.

Alla olevassa esimerkissä laskentavakiolle on luotu ensimmäiseksi arvo 7%, joka on alkanut 1.1.2019. Tämän jälkeen samalle laskentavakiolle on käyty luomassa uusi arvo new value -painikkeesta. Arvoksi on laitettu 8% ja alkupäiväksi on valittu 1.1.2020. Finazilla päättää alkuperäisen arvon 7% automaattisesti päättymään 31.12.2019, sillä uusi arvo tulee voimaan 1.1.2020.

[![](

# **Laskentavakion käyttäminen osabudjetissa**

Luotua laskentavakiota käytetään yrityksen myyntibudjetissa siten, että budjetissa ensimmäisenä syöttörivi myynti (pce), johon syötetään myytyjä kappaleita. Seuraava rivi on syöttörivi, joka on myynti (eur), johon syötetään myytihintoja.

Osabudjetin kolmas rivi on kaavarivi, jossa lasketaan myynti yhteensä. Neljäs osabudjetin rivi on kaavarivi, jossa kaavana on pelkkä laskentavakio (myyntikomissio). Näin saadaan prosenttiluku budjetille näkyviin. Lopuksi budjetissa on vielä myyntikomissio yhteensä -rivi, jossa lasketaan kaavalla maksettavaa myyntikomissiota.

[![](

Yllä oleva esimerkki on vain yksi lukuisista tavoista käyttää laskentavakioita hyväksi budjetoinnissa.

## Lisätietoja

[Mitä laskentavakiot ovat ja miten niitä käytetään?](

[Laskentavakiot ovat yksi budjetoinnin ja raportoinnin työkaluista](

[Yrityskohtaisten laskentavakioiden luominen ja päivittäminen sekä niiden käyttäminen kaavassa](

[Budjettikohtaisten laskentavakioiden luominen ja päivittäminen](

[Asiakastasoiset uudet toiminnot osa 2: laskentavakio](



artikkelin osoite on https://intercom.help/finazilla/fi/articles/4706480-esimerkki-prosentuaalisen-laskentavakion-luominen

