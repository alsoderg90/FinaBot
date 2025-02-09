## Toteumalukujen tuominen

Osabudjeteille voidaan tuoda lukuja usealla eri tavalla. Kuvaamme tässä artikkelissa eri vaihtoehtoja datan tuomiseen.

# Toteumalukujen tuominen

Osabudjeteille toteuman tuominen noudattelee samaa peruslogiikkaa kuin pääbudjetin puolelle toteumalukujen tuontikin noudattelee. Osabudjetin puolella keskeinen tekijä toteumien tuomisessa on riville tehty tilikiinnitys. Tilikiinnitys määrää sen, mistä tililtä toteumat tuodaan - ja mille riville osabudjetilla ne tuodaan. Tämän lisäksi tuontia voidaan rikastaa hyödyntämällä mahdollisuutta tuoda haluttujen dimensioiden (tai dimensioyhdistelmien eli nk. matriisien) toteumia.

Itse tuonti voidaan tehdä aivan samoista painikkeista kuin pääbudjetin puolellakin. Yläosan import -painike tuo toteumat kerralla koko osabudjettiin (eli kaikille osabudjetin riveille, missä on tilikiinnitys). Jos tuonti tehdään yksittäisen rivin perästä olevan rivityökalun kautta, tuodaan toteuma vain kyseiselle riville.

Toiminnallisuutta on kuvattu laajemmin artikkelissamme [täällä.]( 

# Tietojen tuominen suoraan excelistä

Osabudjeteille voi tuoda lukuja esimerkiksi Excelistä. Tämä tapahtuu siten, että excel –tiedostossa on luvut budjetoituna. Kopioidaan haluttu alue excelissä ja liitetään se Finazillan budjettiin valitsemalla alue, jolle luvut halutaan liittää.

Excel kopioinnissa tulee huomioida, että lukujen tulee olla excelissä vierekkäisissä sarakkeissa ja/tai allekkaisilla riveillä. Lisäksi luvuissa ei saa olla tuhaterottimia.

[![](

Finazillassa kyseisellä yrityksellä on osabudjetti nimeltä "sales budget", missä on vastaavat rivit

[![](

Tämän jälkeen excel -tiedostosta otetaan kopio luvuista, jotka halutaan liittää osabudjetille (esim. Ctrl + C).

[![](

Seuraavaksi mennään osabudjettiin, mihin tiedot halutaan liittää. Maalataan osabudjetista sama alue kuin mikä kopioitiin excelistä. Liitetään data (esim. Ctrl + V).

# Tietojen tuominen vanhasta budjetista CSV -tiedoston avulla

Osabudjetista voi ottaa CSV -tiedoston ulos ja sitten tuoda datan uudelleen sisään käyttäen edellä mainittua excelin copy - paste -toimintoa.

Tässä yhteydessä tulee huomioida, että toimenpide pitää tehdä dimensiokohtaisesti - jos dimensioita on käytetty.

Ensimmäisenä viedään osabudjetilta tiedot export budget to CSV -toiminnolla ulos. Tämä tapahtuu kuvanmukaisesta painikkeesta.

[![](

Exportattu data tulee vasempaan alakulmaan, josta sen saa auki kuvakkeen päällä klikkaamalla.

[![](

Tämän jälkeen tiedostoa voidaan muokata, dataa korjata ja poistaa. Kun dataa viedään sisään uudelleen uudelle osabudjetille, toimenpidettä helpottaa, jos uusi osabudjetti on samanmuotoinen rakenteeltaan kuin Finazillan osabudjetti.

Tiedot viedään sisään noudattaen alussa ollutta ohjetta tietojen kopioimisesta excelistä.

[![](

*Jos luvut eivät muutu vuosien kesken, on yksi vaihtoehto tuoda luvut "könttänä" toteumana pääbudjetille. Tällöin menetetään toki osabudjettien kautta saavutettu seurattavuus sen suhteen, mistä luvut ovat tulleet.* 

# Lisätietoja

[Toteumadatan tuominen budjetille pohjatiedoksi](

[Lukujen kopiointi Excelistä Finazillan budjetille pohjatiedoksi](

[Lukujen tuonti CSV -tiedostolla Finazillan budjetille pohjatiedoksi](

[Dimensioille, eli seurantakohteille, budjetointi](

[Osabudjetit osana yrityksen budjetointiprosessia](

[Uuden osabudjetin luominen tai osabudjetin kopioiminen toiselta asiakkuuden yritykseltä](



artikkelin osoite on https://intercom.help/finazilla/fi/articles/4472382-osabudjetille-datan-tuominen

