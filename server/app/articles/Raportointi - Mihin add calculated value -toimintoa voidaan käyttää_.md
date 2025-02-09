## Mihin add calculated value -toimintoa voidaan käyttää?

Olemme kertoneet artikkelissamme ["Raportoinnin pivotointi -painikkeet"]( erilaisista toiminnoista, joilla voidaan pivotoida raportteja. Yksi artikkelissa esitelty toiminto on "add calculated value" -toiminto.

# Mihin add calculated value -toimintoa voidaan käyttää?

Toiminnolla voidaan lisätä raportille uusi tietolähde hyödyntämällä raportilla jo olevia tietoja. Esimerkki tällaisesta käyttötavasta voisi olla vaikkapa sellainen, että raportilla on jo tietolähteinä edellisen vuoden toteuma (tietolähteenä toteumadata eli actual ja periodi -valinta previous accounting period) sekä kuluvan vuoden toteuma (tietolähteenä toteumadata eli actual ja periodi -valintana current accounting period) ja näistä haluttaisiin laskea erotusta.

Toinen käyttötapa voisi olla vaikkapa sellainen, että raportilla on jo tietolähteinä toteuma (tietolähteenä totemadata eli actual) ja ennuste (tietolähteenä budjetti ja kiinnitettynä haluttu yrityksen budjetti). Add calculated value -toiminnolla voitaisiin tässä tapauksessa laskea toteuman ja ennusteen erotus raportille.

[![](

Add Calculated value -toiminto mahdollistaa esimerkiksi kahden tietolähteen välillä prosentuaalisen erotuksen laskemisen. Tietueen saa muutettua prosenttimuotoon "format" toiminnon kautta.

# Calculated valuen lisääminen olemassa olevalle raportille

Calculated value päästään lisäämään raportille silloin, kun raportti on aukaistuna ja kaikki työkalupainikkeet näkyvät raportin yläosassa. Painike löytyy "Fields" valikon alta.

[![](

Add calculated value -painike löytyy valikosta kuvan osoittamasta kohdasta

[![](

# Kaavan luominen add calculated valuen avulla

Tämän jälkeen käyttäjälle aukeaa ns. kaavaikkuna, jossa voidaan lähteä luomaan haluttua kaavaa. Kaavalle annetaan nimi kaavaikkunan yläosassa. Varsinaisen kaavan perusteena voidaan käyttää kaikkia tietolähteitä, mitä kyseisellä raportilla on jo entuudestaan.

Kaava rakennetaan siten, että tietolähteitä raahataan alaosan kaavaeditori -laatikkoon. Tämän jälkeen laitetaan halutut operaattorit (kertomerkki, miinus, plussa jne) ja raahataan aina seuraava tietolähde. Kun haluttu kaava on valmis, painetaan "apply" painiketta, jolloin calculated value tulee raportille.

[![](

Tämän jälkeen luotu calculated value käyttäytyy kuten mikä tahansa muukin tietolähde. Raporttia täytyy usein pivotoida Add Calculated Valuen lisäämisen jälkeen, jotta saavutetaan haluttu lopputulos.

[![](

*Yllä olevassa esimerkissä lisätään raportille Add Calculated Value -toiminnolla kolmatta tietuetta, joka on laskentakaava. Jotta raportti näyttäytyy oikein, tulee raporttia pivotoida tämän jälkeen. Laskennoissa datalähteet tulee olla aina values -kentässä ja date -valinta otetaan pois, koska luvut eivät ole samalta vuodelta.* 

[![](

[![](

*Add calculated value -toiminto on vastaava kuin kokonaan uuden tietolähteen lisääminen raportille. Vaihtoehtoinen tapa toteuttaa asia on siis kuvattu artikkelissamme "Esimerkki: raportti, jossa raportoidaan edellistä vuotta, kuluvaa vuotta ja näiden erotusta". Käyttäjä voi valita soveltuvimman tavan.* 



artikkelin osoite on https://intercom.help/finazilla/fi/articles/4656366-calculated-valuen-kayttaminen-raportilla

