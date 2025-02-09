## Usean tietolähteen määrittely

[![](

*Versiopäivityksessä 8.6.2023 tuotu kokonaan uusi toiminto. Toiminto mahdollistaa toisen saman asiakkuuden yrityksen lukujen tuomisen yrityksen budjetille siten, että samalla tuonnilla voidaan tuoda lukuja budjetista ja toteumasta. Toimintoa on laajennettu 26.2.2024 osalla 5.* 

Tuotu ominaisuus on osa laajempaa kokonaisuutta. Tässä artikkelissa esitelty ominaisuus on osa 2, joka keskittyy nimenomaan usean tietolähteen yhtäaikaisesta tuonnista Tuotavia osia on yhteensä 5. Toimintoon liittyy myös seuraavat ominaisuudet:

[Budjetin import, osa 1: toiselta yritykseltä lukujen tuominen](

[Budjetin import, osa 3: lukujen siirtäminen dimensionarvolta toiselle](

[Budjetin import, osa 4: usealta dimensiolta tuominen](

[Budjetin import, osa 5: osabudjetilta toiselle lukujen tuominen](

Olemme aikaisemmassa osassa 1 kuvanneet, kuinka budjetille voidaan tuodaa toteumaa ja/tai budjettidataa import balances -työkalulla. Tässä artikkelissa kuvaamme, miten yhdellä tuonnilla voidaan tuoda useaa eri dataa; eli esimerkiksi toteumaa ja budjettia samanaikaisesti.

# Usean tietolähteen määrittely

Import balances -näkymässä on oikeassa reunassa datasource -kohta. Lomakkeelta voi painaa + ja - nappeja, joista tulee lisää tai poistuu tietolähteitä.

[![](

Import -lomakkeeseen on alla olevassa esimerkissä lisätty oikean reunan plus -painikkeesta yksi uusi tietolähde. Aina kun lisätään uusi tietolähde, tulee myös vasempaan reunaan uusi "from" laatikko.

Ensimmäisellä tietolähteellä on määritelty, että yrityksen 2 budjetille halutaan tuoda lukuja yrityksen 1 budjetilta. Budjetti on kiinnitetty valitsemalla se alasvetovalikosta.

Toisella tietolähteellä on määritelty, että samalla tuonnilla tuodaan yrityksen 2 budjetille yrityksen 1 toteumaluvut. Import actuals -valinta viittaa nimenomaan toteumaan.

[![](

# Aikavälin valitseminen

Import -toiminnossa on edelleen tarkistus siitä, että To ja From päivämäärät ovat yhtä pitkät. Tarkistus on kaikissa tuonneissa, mutta tässä yhteydessä from ja to -aikaväleihin tulee kiinnittää erityistä huomiota. From - valitsimia on yhtä monta kuin on tietolähteitäkin, kun taas to -valitsimia on aina vain yksi.

Useamman tietolähteen importissa tarkistus yhtä pitkästä aikavälistä toimii siten, että sisääntulevassa datassa (from) tulee olla aikaisimman tietolähteen päivä ja to -kohdassa on myöhäisin päivä.

Jos esimerkiksi importtia ollaan tekemässä vuoden 2023 budjetille siten, että ensimmäiset 6 kuukautta halutaan tuoda toteumista ja loput 6 kuukautta budjetista, niin aikavalitsin 01-06/2023 toteumaa ja 06-12/2023 budjettia on validi.

[![](

Vastaavasti taas 01/2022-12/2022 toteumia ja 01/2023-12/2023 ei ole validi, koska silloin sisään tuleva datan on 2 vuoden jakso, jota tuodaan 1 vuoden mittaiselle jaksolle. From ja To eivät ole silloin yhtä pitkät. Tällöin Finazilla ilmoittaa virheestä aikajaksoissa.

[![](

# Lukujen summaantuminen

Jos importissa on usea tietolähde (kuten alla), niin luvut summataan siten, että jos samalla kuulla on lukuja useasta tietolähteestä, niin budjetille tuodaan näiden yhteenlaskettu summa. Alla olevassa esimerkissä kaudelle 6/2023 ollaan tuomassa lukuja sekä toteumista, että budjetista, jolloin kaudelle 6 tulee näiden yhteenlaskettu summa.

[![](

# Havainnollistavat esimerkit

Havainnollistamme asiaa esimerkillä.

**Esimerkki 1:**

Yrityksellä 1 on tilillä 3000 myyntiä 428€ dimensionarvolla "Jyväskylä". Lisäksi yritys 1 on budjetoinut myyntiä 10 000€ tilille 3000 dimensionarvolle "Jyväskylä".

Yritys haluaa tuoda budjetille tilille 3000 näiden kahden luvun summan. Tämä voidaan tehdä lisäämällä datasource -kohtaan toinen tietolähde. Toisella tietolähteellä tuodaan budjetin luvut ja toisella toteuman. Kummassakin tapauksessa valintana on single target ja dimensionarvo "Jyväskylä".

[![](

Yllä olevassa tapauksessa budjetille oikeaan yläkulmaan valittu dimensionarvo määrää sen, millä dimensionarvolla luvut esitetään. Mikäli ei valita mitään, esitetään luvut "blank" arvolla (= dimensioimaton, kohdistamaton).

[![](

*Myös kertoimella tuonnit (multiplier) sekä tasamääräiset muutokset (static addition) ovat mahdollisia*



artikkelin osoite on https://intercom.help/finazilla/fi/articles/7941675-budjetin-import-osa-2-usealta-tietolahteelta-lukujen-tuominen

