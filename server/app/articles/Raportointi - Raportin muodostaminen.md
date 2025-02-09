## Raportin muodostaminen

# Raportin muodostaminen

Raportin muodostaminen aloitetaan menemällä "Reports" -toimintoihin ja klikkaamalla siellä ”New Report” –painiketta. Raportille annetaan nimi kohdassa "Name".

Seuraavana valintaikkunassa on raporttimallin valinta (Report Scheme). Alasvetovalikosta valitaan raporttimalli nimeltä (System) Tuloslaskelma. Raporttimalli on valmiina valikossa (ellei system -tasoisia raporttimalleja ole erikseen piilotettu).

[![](

## Tietolähteiden valitseminen

Seuraavaksi raportille syntyy automaattisesti ensimmäinen tietolähde. Tietolähde saa oletusnimen ja oletusvalinnat, joita päästään muokkaamaan. Tietolähde voidaan uudelleen nimetä halutulla tavalla. Tässä esimerkissä tietolähde on nimetty nimellä "Toteuma".

## Datatyypin valitseminen

Seuraavaksi valitaan kohtaan "Datasource", mitä dataa valitulla tietolähteellä halutaan raportoida. Tässä tapauksessa oletusvalinta "Actual" on oikea, koska halutaan raportoida toteumadataa.

Kaikki muut Finazillan oletusvalinnat ovat tässä tapauksessa hyviä, joten muita valintoja ei ole tarpeen tehdä. Alla on vielä kuva tehdyistä valinnoista. Valintoihin ei tehty mitään muutoksia.

[![](

Dimensioihin liittyvät valinnat löytyvät tietolähteeltä keskiosasta, oman välilehden "dimensions" takaa. Valitaan vaihtoehto "include dimensions". Valinta tarkoittaa, että raportilla on dimensiot käytössä.

[![](

Seuraavaksi raportin voi esikatsella alaosan "preview" painikkeesta, jonka jälkeen raportti aukeaa automaattisesti. Tämän jälkeen raporttia voi pivotoida halutusti. Raportti tulee muistaa tallentaa oikean yläkulman "save" painikkeen kautta, jotta se jää talteen.

[![](

*Dimensiot ilmestyvät raportille automaattisesti kyseisellä valinnalla filters -kenttään. Raporttia voi pivotoida haluttuun suuntaan.* 

# Raportin pivotointi

Raportin pivotointi aloitetaan menemällä raportilla oltaessa oikeasta yläkulmasta "fields" valikkoon. Sen jälkeen käyttäjälle aukeaa ns. pivotointi näkymä, josta dimensiotieto löytyy vasemmasta report filters kentästä.

[![](

Haluttu dimensio/dimensiot, voidaan raahata raportilla esitettäväksi haluttuun paikkaan, kuten esimerkiksi sarakkeille (Columns).

[![](

Apply -painikkeella tehdään luotu muutos raportille ja palataan katselemaan raporttia tehtyjen muutosten kera.

[![](

[![](

*Yllä esitetty pivotointi on vain yksi monista vaihtoehdoista, eli ei suinkaan ainoa tapa esittää dimensiot raportilla*



artikkelin osoite on https://intercom.help/finazilla/fi/articles/4538963-esimerkki-kuinka-saan-luotua-toteumadatasta-dimensiokohtaisen-raportin

