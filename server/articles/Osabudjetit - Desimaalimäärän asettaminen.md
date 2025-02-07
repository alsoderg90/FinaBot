## Desimaalimäärän asettaminen

[![](

*Versiopäivityksessä 12.10.2022 tuotu parannus, jolla voidaan vapaasti määrittää osabudjettikohtaisesti, millä tavalla desimaalit halutaan esittää kyseisellä osabudjetilla*

Finazillan osabudjetteja voidaan kutsua eräänlaisiksi ”apulaskelmiksi”, jotka syötettävien perustietojen pohjalta laskevat budjetoitavia lukuja. Halutut luvut ohjataan osabudjetilta pääbudjetille tiliohjausten avulla. Osabudjetteja voi olla hyvin monenlaisia ja niiden tietosisältö voi vaihdella laidasta laitaan. Tästä johtuen myös syötettävien lukujen tarkkuus ja niiden haluttu tarkastelutaso voi vaihdella hyvinkin paljon.

# Desimaalimäärän asettaminen

Kun budjetille luodaan uusia osabudjetteja, voidaan jokaiselle osabudjetille määrittää decimals to display -kentässä, että esitetäänkö kyseisessä osabudjetissa desimaaleja - ja jos esitetään, kuinka monta desimaalia.

[![](

Desimaalien näyttämisessä Finazillassa on logiikka, että turhia nollia ei näytetä, vaikka budjetille olisi niitä syötetty. Osabudjetilla esitetään valittu määrä desimaaleja vain, jos niillä on merkitystä. Mikäli syötetyssä luvussa on enemmän desimaaleja kuin osabudjetille on valittu esitettäväksi, pyöristää Finazilla luvun seuraavaan lukuun. Logiikka on avattu alla vielä enemmän muutaman esimerkin avulla.

**Esimerkki 1: syötetään osabudjetille luku 1,76**

[![](

**Esimerkki 2: syötetään osabudjetille luku 100,0**

[![](

Osabudjeteille valittavien desimaalien maksimimäärä on 5 desimaalia. Kaikilla vanhoilla osabudjeteilla on oletusarvoisesti päällä valinta 0 desimaalia, mutta valintaa voi muuttaa halutessaan osabudjetin editin kautta.

[![](

*Laskenta käyttää aina taustalla tarkkoja lukuja huolimatta siitä montako desimaalia osabudjetille on valittu näytettäväksi. Desimaalimäärän valitsimen vaikutus on siis puhtaasti osabudjetin haluttuun katselutarkkuuteen*



artikkelin osoite on https://intercom.help/finazilla/fi/articles/6636350-desimaalien-maara-osabudjeteilla

