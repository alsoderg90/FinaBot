## Kertoimet ja staattinen lisäys

Tässä artikkelissa kerromme pääpiirteittäin budjetille toteuma -ja/tai budjettidatan tuomisesta budjetin taustatiedoiksi. Artikkelin lopussa on linkki artikkeliimme, missä kuvaamme toimintoa laajemmin erilaisin esimerkein.

Edellisenvuoden luvut, tai myös luvut toisesta budjetista, voidaan tuoda budjettiin koko tuloslaskelman, taseen tai tilinpäätöksen tasolla tai sitten erä tai tilitasolla.

Jos toteumadataa halutaan tuoda budjettiin siten, että tuodaan toteuma kerralla koko budjetille, tulee budjetilla mennä välilehdelle "all". Tuonnin logiikka on se, että dataa tuodaan vain sille välilehdelle, missä kulloinkin ollaan toimintoa tehtäessä.

[![](

Tuontiin liittyvät painikkeet löytyvät budjetilta kahdesta eri paikasta, riippuen millä tasolla dataa halutaan tuoda. Rivikohtainen tuonti -painike löytyy rivin asetuksista kun taas yläosan painikkeella voidaan tuoda koko näkymään kerralla.

[![](

"Import balances" painikkeesta avautuu oheinen lomake riippumatta siitä, mistä valikosta tuonti aloitetaan.

[![](

## Lukujen tuonti suhteessa dimensioihin

Import mode -valinta määrittelee sen, ***mihin*** budjetilla ollaan tuomassa dataa. Valinta ei ota kantaa siihen, mistä luvut tulevat, vaan nimenomaan siihen, mihin ne taustalla auki olevassa budjetissa haetaan. Current dimension target valinta tarkoittaa, että lukuja tuodaan budjetille sille dimensionarvolle, mikä on valittuna budjetin oikeaan yläkulmaan ennen kuin navigoidaan import budget balances -näkymään. Mikäli mitään dimensionarvoa ei ole valittuna, tuodaan luvut blank -tunnisteelle. Blank tarkoittaa kohdistamatonta/dimensioimatonta.

All dimension targets -valinta tuo datat kaikille dimensiokohdistuksille siten, miten ne esiintyvät lähtödatassakin.

Luvut on myös mahdollista tuoda siten, että niiden kohdistusta siirretään dimension arvolta toiselle. Tätä olemme kuvanneet tarkemmin artikkelissamme [täällä.]( 

[![](

Seuraavaksi määritellään kausi, jolta lukuja halutaan tuoda (from), sekä kausi, mihin lukuja tuodaan (to). Valikossa data source valitaan tuodaanko toteumaa (actuals) vai dataa toisesta budjetista. Oletusvalintana on aina toteumadata.

[![](

# Kertoimet ja staattinen lisäys

Tämän lisäksi lomakkeella voidaan vielä määritellä tuodaanko luvut sellaisenaan vai jollain kertoimella. Kerroin voidaan määrittää kohdassa multiplier siten, että kerroin 1.1 tarkoittaa 10% kasvua kun taas kerroin 0.8 tarkoittaa 20% laskua.

Staattinen lisäys kohdassa "static addition" lisää lukuihin kenttään syötetyn staattisen luvun. Jos kenttään syötetään 1000, tekee Finazilla automaattisen +1000 lisäyksen tuotaviin lukuihin.

Kohdassa "import data transformation method" oleva oletusvalinta "import data as is" on nk. oletusvalinta, ja se tarkoittaa, että luvut tuodaan sellaisenaan.

[![](

Klikkaamalla valintojen jälkeen alaosan painiketta ”import”, luvut ilmestyvät budjetointinäkymän niille riveille, joille ne on valittu tuotavaksi. Lukuja voidaan myös esikatsella ennen tuontia preview -painikkeen kautta (ei käytettävissä tuonnissa, missä tuodaan data dimensioille eriteltynä)

[![](

*Lukuja pystyy tuomaan pääbudjetille sekä osabudjeteille. Suositeltavaa on, että edellisen vuoden toteumalukuja tuotaessa ei tuoda lukuja koko budjettiin kerralla, vaan erä tai rivi tasolla. Mikäli tuot lukuja dimensioittain eriteltynä ja dimensioita ja/tai näiden arvoja on paljon, tuominen saattaa kestää jonkin aikaa.*

[![](

*Esimerkiksi liiketoiminnan muut kulut -tiliryhmä on usein selllainen, mihin halutaan tuoda edellisen vuoden toteumat ja arvioida kertoimen avulla kulujen kasvu. Import balance -toiminto toimii tässä hyvin yhdessä multiplier -ominaisuuden kanssa.*

# Lisätietoja

[Esimerkki: toteuman tuominen budjetille pohjatiedoksi](



artikkelin osoite on https://intercom.help/finazilla/fi/articles/4418371-toteumadatan-tuominen-budjetille-pohjatiedoksi

