## Toiminto lyhyesti kuvattuna

[![](

*Versiopäivityksessä 21.4.2023 tuotu kokonaan uusi toiminto.*

*Toiminto mahdollistaa budjetille lukuja importatessa sen, että tuotavia lukuja voi tuoda käyttämällä tilikartalle tallennettuja generointimenetelmiä hyödyntämällä. Ominaisuutta on parannettu 12.1.2024 päivityksessä.* 

Finazillan budjetille voidaan saada lukuja hyvin monella tavalla. Lukuja voidaan syöttää manuaalisesti, hyödyntää erilaisia copy-paste toimintoja, tuoda lukuja csv -tiedostoista tai rakentaa erilaisia kaavoja, joiden perusteella luvut tulevat. Tämän lisäksi budjetille voidaan tuoda lukuja nk. import -toiminnolla. Näistä tyypillisin tilanne on se, että budjetille halutaan tuoda vaikkapa edellisen vuoden toteumat pohjatiedoksi, ja lähteä niiden perusteella budjetoimaan tulevaa.

Finazillan käyttäjät voivat jatkossa hyödyntää myös budjetin generointimenetelmää, joka perustuu siihen, että yrityksen tilikartalle voidaan asettaa erilaisia generointimenetelmiä, miten jokin tietty tili tai tiliryhmä halutaan generoida. Tällöin import suoritetaan siten, että jokaiselle tilille käytetään sitä menetelmää, mikä on tilikartalla määritelty.

# **Toiminto lyhyesti kuvattuna**

* Generointimenetelmät asetetaan yrityksen tilikartalle
* Generointimenetelmiä voi asettaa tiliryhmille ja/tai yksittäisille tileille
* Luodaan uusi budjetti normaalisti
* Generointimenetelmää käytetään painikkeesta, mistä toteumaluvut tuodaan budjetille eli budjetin yläosan työkalurivin painikkeesta "import budget or actuals"
* Toteumien tuonnissa tulee valita erikseen metodiksi, että tuonnissa käytetään nimenomaan tilikartan asetuksia, eikä normaalia toteumien tuontia
* Import tuottaa budjetille luvut tilikartan menetelmien mukaisesti
* Toimintoa voidaan käyttää myös silloin, kun lukuja tuodaan joltain toiselta budjetilta
* Eri aikajaksot mistä dataa tuodaan, ovat käytettävissä
* Eri dimensiovalinnat ovat myöskin käytettävissä
* Tuonnin voi tehdä myös tilikohtaisesti tai tiliryhmäkohtaisesti

Tuotu ominaisuus on osa laajempaa kokonaisuutta. Tässä artikkelissa esitelty ominaisuus on osa 1, joka keskittyy nimenomaan asetusten laittamiseen tilikartalle. Tuotavia osia on yhteensä 3. Toimintoon liittyy myös seuraava ominaisuus

[Budjetin generointimenetelmä, osa 2: toteumien tuonti](

[Budjetin generointimenetelmä, osa 3: budjetin luominen esivalinnoilla](

# **Asetusten laittaminen tilikartalle**

Toiminto on uusi, joten olemassa oleville asiakkaille tämä tarkoittaa sitä, että generointiasetukset tulee käydä merkitsemässä itse yrityksen tilikartalle. Tilikartalla asetusten merkitseminen ei vielä automaattisesti tarkoita, että ne olisivat budjetoinnissa käytössä. Tämä on optio, joten käyttäjä ei voi siis vahingossa käyttää näitä valintoja. Generointiasetukset voi siis hyvin asettaa yrityksen olemassa olevalle tilikartalle, eikä tätä varten ole pakko luoda uutta tilikarttaa.

Tilikartan asetukset tehdään company -valikosta kohdasta account schemes. Valikosta löytyy kaikki yrityksen tilikartat. Tyypillisimmin yritykselle on vain yksi tilikartta. Tilikartan saa auki sen nimeä klikkaamalla. Tilin/tiliryhmän perässä oleva edit -painike aukaisee alla olevan näkymän, josta löytyy kohta "Default forecasting method".

[![](

Budjetin generointimetodi voidaan asettaa tiliryhmälle tai yksittäiselle tilille. Ns. Parentille merkitty generointimenetelmä valuu sen alapuolella oleville lapsiriveille. Vastaavasti taas lapsiriville asetettu generointimenetelmä ylikirjoittaa parentin asetukset.

[![](

# **Eri generointimenetelmät**

Budjetin generointimenetelmiä on useita. Esittelemme alla jokaisen menetelmän.

## ***Inherit from parent = nykyinen vakioasetus***

Oletusarvoisesti Finazillan tilikartalla on jokaisella tilikartan tilillä asetus "Inherit from parent". Tämä tarkoittaa käytännössä sitä, että tilin käyttäytyminen määräytyy sen yläpuolisen rakenteen mukaan. Inherit from parent on ns. vanha nykyinen toteutus, joka on tilikartalla aina oletusasetuksena. Valinta mahdollistaa sen, että tiliryhmän parentille voidaan antaa jokin muu vaihtoehto, joka "valuu lapsiriveille" tämän jälkeen.

## ***Skip account = tilin ohittaminen***

Skip account -valinta tarkoittaa, että kyseinen tili halutaan ohittaa tyystin generoinnissa. Tämä valinta ohittaa generointimenetelmän ja pitää nykyisen arvon kyseisellä tilillä.

*Esimerkki 1:*

Tilillä 3000 ei ole mitään budjetoituna. Budjetille generoidaan liikevaihto. Tili 3000 pysyy nollana, sillä se ohitetaan.

*Esimerkki 2:*

Tilillä 3000 on budjetoituna 10 000€ myyntiä jokaiselle kuukaudelle. Budjetille generoidaan liikevaihto. Tili 3000 pysyy samassa 10 000€/kk, sillä se ohitetaan generoinnissa.

*Esimerkki 3:*

Tilillä 3000 on budjetoituna 10 000€ myyntiä siten, että myyntiä ei ole kohdistettu dimension arvoille. Tämän lisäksi on budjetoitu dimension arvolle "hallinto" myyntiä 3 000€. Budjetille generoidaan liikevaihto. Budjetoidut myynnit pysyvät, kuten ne olivat. Kokonaismyynti on 13 000€.

## ***Fit a line, linear = lineaarinen***

Fit a line, linear menetelmä on helpoin hahmottaa graafisen kuvaajan avulla. Tämä menetelmä tarkoittaa käytännössä sitä, että piirretään viiva, jonka etäisyys on mahdollisimman pieni pisteisiin nähden. Alla olevassa esimerkissä ensimmäinen viiva on yrityksen A toteumaluvut. Jälkimmäinen viiva kuvaa samaa yrityksen A dataa kun se on generoitu budjetille käyttämällä fit a line linear -valintaa. Menetelmää voisi verrata siihen, että laitetaan viivoitin pisteiden päälle ja piirretään suora viiva kaikkien pisteiden kautta.

[![](

Fit a line valinnoissa valinta tehdään alla olevan mukaisesti. Forecasting method -kohtaan valitaan vaihtoehto "Fit a line" ja tämän lisäksi kenttään "Growth type" valitaan vaihtoehto "Linear".

Valinnoista löytyy kohta "Include zero values in forecasting", joka on tarpeellinen silloin kun toteumien välissä on ns. nollakuukausia - eli esimerkiksi kuukausia missä ei ole ollut lainkaan tapahtumia. Jos välissä on nollakuukausia, eikä valintaa ole täpätty, ohitetaan nollakuukaudet kokonaan, eivätkä ne vaikuta budjettiin. Mikäli valinta on täpätty, nollakuukaudet käsitellään nollana.

[![](

## ***Fit a line, exponential = exponentiaalinen***

Fit a line (exponential) on toinen nk. matemaattisista ennnustamismenetelmistä. Eksponentiaalinen tarkoittaa kasvua, joka on suoraan verannollinen kulloiseenkin arvoon. Mitä suurempi arvo on kyseessä, sitä nopeammin se kasvaa (tai vastaavasti pienenee).

Valinnoista löytyy myös tässä vaihtoehdossa kohta "Include zero values in forecasting", joka on tarpeellinen silloin kun toteumien välissä on ns. nollakuukausia - eli esimerkiksi kuukausia missä ei ole ollut lainkaan tapahtumia. Jos välissä on nollakuukausia, eikä valintaa ole täpätty, ohitetaan nollakuukaudet kokonaan, eivätkä ne vaikuta budjettiin. Mikäli valinta on täpätty, nollakuukaudet käsitellään nollana.

[![](

## ***Average = keskiarvo***

Finazilla generoi valinnalla budjetin luvut siten, että niistä lasketaan keskiarvo ja saatu keskiarvo tulee jokaiselle budjetin kuukaudelle.

[![](

*Esimerkki 1:*

Yrityksen sähkökulut vaihtelevat vuoden sisällä rajusti. Talvella sähkökulut ovat huomattavasti korkeammat kuin kesällä. Kokonaiskulut ovat vuodessa 32 000€. Tällä valinnalla sähkökulut tuodaan budjetille 2666,66€/kuukausi arvolla.

## ***Latest = viimeisin arvo***

Budjetin generointimenetelmä latest tarkoittaa sitä, että kyseiselle tilille otetaan viimeisin arvo siltä kaudelta, miltä toteumia tuodaan.

Jos esimerkiksi osakepääoma on ollut kaudella 12/2022 2500€, ja budjetti luodaan vuodelle 2023 siten, että tilille osakepääoma generoidaan luvut tilikauden 2022 pohjalta, tulee jokaiselle vuoden 2023 kuukaudelle arvoksi 2500€.

[![](

## ***Formula = kaava***

Generointimenetelmä "formula" tarkoittaa kaavaa. Kaavoja voidaan rakentaa tilikartalle joko yksittäisten tilien kohdalle, tai tiliryhmätasoisesti. Kaava määrää sen, miten/mistä arvo syntyy budjetille.

Itse kaavan luominen mukailee mm. raporttimallin kaavan luomista. Näkymä on hyvin samankaltainen. Hiiren kursori tulee olla "forecasting formula" kentässä kun kaavaa kirjoitetaan. Kaavan komponentteja, eli tilejä tai tiliryhmiä, voidaan hakea "account scheme template row" valikosta.

[![](

Kaavoihin voidaan hakea mukaan myös laskentavakioita. Laskentavakiot löytyvät valikosta "calculation constants". Valikossa näkyy kaikki system, customer ja company -tasoiset laskentavakiot.

Offset valikossa voidaan viitata esimerkiksi edellisiin kuukausiin. Jos kenttään syötetään -1, tarkoittaa tämä viittausta yhteen edelliseen kuukauteen. Ensin valitaan offset ja sen jälkeen kaavan muut koponentit.

[![](

**Esimerkki 1:**

Yrityksellä A on tilillä 3000 myyntiä oheisesti:

1/2023 10 000€

2/2023 15 000€

3/2023 20 000€

Yrityksen tilikartalle on asetettu liiketoiminnan muihin tuotttoihin kaava tili 3000 ja offset -1.

Kun budjetille tuodaan lukuja käyttämällä tilikartan asetuksia, tulee budjetille luvut seuraavasti:

1/2023 0€

2/2023 10 000€

3/2023 15 000€

4/2023 20 000€

**Esimerkki 2:**

Yrityksellä A on tilillä 3000 myyntiä oheisesti:

1/2023 10 000€

2/2023 15 000€

3/2023 20 000€

4/2023 25 000€

5/2023 30 000€

Yrityksen tilikartalle on asetettu liiketoiminnan muihin tuotttoihin kaava tili 3000 ja offset +2.

Kun budjetille tuodaan lukuja käyttämällä tilikartan asetuksia, tulee budjetille luvut seuraavasti:

1/2023 20 000€

2/2023 25 000€

3/2023 30 000€

Kaavoja luotaessa valikossa on myös lisävalinta "add formula value to current value cumulatively". Tämä valinta vaikuttaa lukujen kumuloitumiseen. Sen tulee olla aina päällä silloin kun kaavoja rakennetaan taseen puolella. Vastaavasti tuloslaskelmassa tätä ei tule käyttää.

[![](

## ***Latest same calendar month = viimeisin sama kuukausi***

Kyseessä on ennustemenetelmä, joka tuo kaikille kuukausille uusimman löytämänsä saman kuukauden arvon lähtödatasta. Kuukauden arvo tuodaan lähtökohtaisesti ottamalla lähtödatasta generoitava kuukausi edeltävältä vuodelta. Jos budjettia ollaan siis tekemässä vuodelle 2024, tarkoittaa tämä sitä, että kaudelle 1/2024 generoitaisiin kauden 1/2023 luvut, kaudelle 2/2024 generoitaisiin kauden 2/2023 luvut ja niin edelleen.

Esimerkki 1:

Yrityksellä A on myyntiä tilillä 3200 oheisesti

1/2023 15 000€

2/2023 33 000€

3/2023 48 000€

Vuoden 2024 budjetille tuodaan toteumat käyttämällä valintaa "latest same calendar month". Budjettiin tulee luvut oheisesti:

[![](

Esimerkki 2:

Yrityksellä A on myyntiä tilillä 3200 oheisesti edellisen esimerkin mukaisesti. Sen lisäksi kaudella 1/2023 on myyntiä 5 000€, joka kohdistuu dimensionarvolle "Helsinki".

Vuoden 2024 budjetille voi tuoda toteumia kahdella tapaa; joko voidaan tuoda vain valitun dimension toteumat (current dimension target) tai voidaan tuoda kaikki toteumat (all dimension target). Jälkimmäinen tuonti toisi kaudelle 1/2024 myynniksi yhteensä 20 000€.

[![](

*Jos kuukautta ei löydy ollenkaan lähtödatasta, niin generoidaan siihen viimeisin luku, joka lähtödatasta löytyy. Tällöin budjetille tuodaan viimeisin luku riippumatta siitä, että mikä on sen kuukausi. Jos esimerkiksi vuoden 2024 budjettiin generoidaan lukuja tilanteessa, missä joulukuun 2023 dataa ei ole olemassa, niin joulukuulle 2024 tuodaan marraskuun 2023 luvut.* 

*Mikäli generointia tehdään käynnissä olevan vuoden vuoden osalta, niin budjettiin tuodaan loppupäähän budjettia viimeisin tilillä oleva luku/luvut. Jos generointia tehdään marraskuussa 2023 budjettiin, joka on vuodelle 2023, tarkoittaa tämä sitä, että kausille 1-11/2023 tuodaan datat vastaavilta kuukausilta vuosilta 2022 ja kaudelle 12/2023 tuodaan viimeisin lähtödatassa oleva arvo, eli 11/2023.* 

​



artikkelin osoite on https://intercom.help/finazilla/fi/articles/8753438-budjetin-generointimenetelma-osa-1-asetusten-laittaminen-tilikartalle

