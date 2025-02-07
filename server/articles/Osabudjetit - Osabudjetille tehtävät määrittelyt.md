## Osabudjetille tehtävät määrittelyt

[![](

*Versiopäivityksessä 24.3.2023 tuotu kokonaan uusi toiminto. Toiminto mahdollistaa osabudjeteille toteumalukujen tuomisen*

Osabudjeteille toteuman tuominen noudattelee samaa peruslogiikkaa kuin pääbudjetin puolelle toteumalukujen tuontikin noudattelee. Ominaisuutta on kuvattu laajemmin artikkelissamme ["Toteumadatan tuominen budjetille pohjatiedoksi"]( sekä yksityiskohtaisemmassa artikkelissamme ["Esimerkki: tuodaan toteumaa budjetille pohjatiedoksi"](

# Osabudjetille tehtävät määrittelyt

Osabudjetin puolella keskeinen tekijä toteumien tuomisessa on riville tehty tilikiinnitys. Tilikiinnitys määrää sen, mistä tililtä toteumat tuodaan - ja mille riville osabudjetilla ne tuodaan. Tämän lisäksi tuontia voidaan rikastaa hyödyntämällä mahdollisuutta tuoda haluttujen dimensioiden (tai dimensioyhdistelmien eli nk. matriisien) toteumia.

# Toteuman tuonti

Itse tuonti voidaan tehdä aivan samoista painikkeista kuin pääbudjetin puolellakin. Yläosan import -painike tuo toteumat kerralla koko osabudjettiin (eli kaikille osabudjetin riveille, missä on tilikiinnitys). Jos tuonti tehdään yksittäisen rivin perästä olevan rivityökalun kautta, tuodaan toteuma vain kyseiselle riville. Rivikohtaisessa tuonnissa on myös mahdollisuus importissa valita erikseen, että tuonti tehdäänkin joltain toiselta tililtä, kuin mihin rivi on kiinnitetty. Tuonti voidaan tehdä myös hierarkisen rakenteen ylimmältä riviltä, jolloin toteumat tuodaan kaikille rakenteen riveille, missä on tilikiinnitys.

[![](

Käytössä on myös pääbudjetin puolelta tutut kertoimet (multiplier) sekä euromääräinen lisäys (static addition). Tuonnissa voidaan valita myös vapaasti ajanjakso miltä toteumat tuodaan -ja minne ne osabudjetille tuodaan.

# Ominaisuudessa huomioitavaa

* Toteuman tuonti ylikirjoittaa osabudjetille budjetoidut luvut
* Kaavariveille ei voi tuoda toteumalukuja. Mikäli koko osabudjetille tuodaan toteumia, hypätään kaavarivien ohi ja ja ne jäävät nollaksi
* Käytettävissä on kaikki pääbudjetin puolellakin olevat mahdollisuudet liittyen dimensiotasoisuuteen (tuodaan vain tietyn dimension luvut, summataan kaikki jne)
* Voidaan käyttää myös riveillä missä on lisäkohdistus
* Voidaan käyttää yhdessä multiplier ja static addition -valintojen kanssa (nk. prosenttikerroin tai euromääräinen muutos)
* Jos osabudjetilla on vain yksi dimensiokohdistus ja toteumaa tuodaan valinnalla current dimension values, tuodaan vain luvut, jotka kohdistuvat tähän yhteen dimensioarvoon. Jos kyseinen dimensionarvo esiintyy matriisikohdistuksessa, ei näitä lukuja tuoda tällä valinnalla
* Matriisiluvut saadaan tuotua, kunhan osabudjetilla on jollain tavalla kohdistettuna sama matriisi, mitä halutaan tuoda
* Rivikohtaisessa tuonnissa on mahdollisuus tuoda vaikkapa riville missä on tiliohjaus tilille 3010 tilin 3000 toteumat
* Toiminto on käytettävissä myös ennustebudjeteilla olevissa osabudjeteissa (forecast budget)

Tarkempia esimerkkejä toteuman tuomisesta erilaisille osabudjeteille löytyy artikkelistamme alta

# Lisätietoja

[Esimerkkejä toteuman tuomisesta osabudjetille](



artikkelin osoite on https://intercom.help/finazilla/fi/articles/7109183-toteumien-tuominen-osabudjetille

