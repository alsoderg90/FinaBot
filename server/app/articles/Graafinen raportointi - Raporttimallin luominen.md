## Raporttimallin luominen

Tässä artikkelissa esittelemme, miten voidaan muodostaa raporttimalli, joka soveltuu hyvin pylväsdiagrammin esitysasuun yhdessä viivan kanssa. Artikkelin ymmärtämistä auttaa, jos käyttäjä tietää jo mitä raporttimallit ovat ja miten uusia raporttimalleja muodostetaan. Lisäksi käyttäjän on hyvä ymmärtää raportoinnin perusperiaatteet.

# Raporttimallin luominen

Tarpeena on muodostaa raportti, jossa yrityksen myyntikate ilmoitetaan sekä euroissa että prosenteissa.

Tehdään raporttimalli, jossa kukin raportille haluttu tieto on oma rivinsä raporttimallilla. Luodaan ensimmäisenä raporttimallille kaikki kolme otsikkoriviä; myyntikate eur, liikevaihto ja myyntikate %. Liikevaihto rivi tarvitaan raporttimallille mukaan, sillä se on taustalaskennassa tarvittava tieto. Näistä otsikoista liikevaihto on piilotettuna, kaikki muut otsikkorivit ovat näkyvissä. Liikevaihto -rivi piilotetaan, koska se on ainoastaan taustalaskennassa tarvittava rivi, jota ei haluta esittää lopullisella raportilla.

[![](

Seuraavaksi luodaan "Myyntikate EUR". Otsikon alle lapsiriveinä tilivälit, jotka muodostavat myyntikatteen. Tilivälit summataan "parenttiin" jotta ne näkyisivät lopullisella raportilla oikein.

[![](

Seuraavaksi mennään luomaan otsikkorivin "liikevaihto" alle "lapsiriveinä" halutut tilivälit. Liikevaihto on piilotettu siksi, että sen ei haluta näkyvän varsinaisella raportilla. Tietoa kuitenkin tarvitaan myyntikate % laskennan taustalla, joten siksi se tulee ottaa raporttimallille mukaan.

[![](

Viimeisenä käydään muokkaamassa riviä "myyntikate %" siten, että muutetaan rivin tyypiksi kaava (formula) ja kirjoitetaan rivin taakse laskentakaava myyntikate EUR / Liikevaihto \* 100.

[![](

# Luodulla raporttimallilla raportoiminen

Tämän jälkeen raporttimalli on valmis ja sillä voidaan raportoida. Mennään Reports -valikkoon ja muodostetaan luodulla raporttimallilla raportti, jossa raportoidaan kuluvaa tilikautta kuukausittain. Raporttia muodostettaessa tulee huomioida, että valinta "row measures" tulee asettaa päälle, jotta dataa voidaan pivotoida myöhemmässä vaiheessa halutusti.

[![](

# Raportin pivotointi

Kun raportti aukeaa, täytyy raporttia käydä ensimmäisenä pivotoimassa. Pivointi tapahtuu oikeasta yläkulmasta "fields" painikkeen takaa. Pivotoidaan "Data row" otsikon alta löytyvät "myyntikate eur" sekä "myyntikate %" raportin "values" laatikkoon. Samalla otetaan values -laatikosta siellä ollut "amount" valinta pois tuplaklikkaamalla sitä. Rows -kenttään jätetään pelkästään arvot (values).

Näkymä kun pivotointi suoritettu halutusti:

[![](

Pivotoinnin jälkeen raportti näyttää oheiselta

[![](

# Numeerisen raportin muuttaminen graafiseen muotoon

Viimeisenä käydään vielä muodostamassa raportista graafinen raportti. Graafiset raporttivalinnat löytyvät yläosan työkalupalkista "charts" valikon alta. Valitaan vaihtoehto "column/line", joka on haluttu muoto.

Raportti näyttää nyt oheiselta. Visuaaliseen ulkoasuun tehdyt muutokset tulee muistaa tallentaa työkaluvalikon "save" painikkeesta.

[![](



artikkelin osoite on https://intercom.help/finazilla/fi/articles/4934097-graafinen-raportti-pylvas-ja-viiva

