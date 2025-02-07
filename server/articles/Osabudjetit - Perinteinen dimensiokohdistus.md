## Perinteinen dimensiokohdistus

[![](

*Versiopäivityksessä 10.3.2022 tuotu kokonaan uusi toiminto, jossa voidaan valita osabudjetille eri riveille eri dimensionarvot käyttämällä ns. lisäkohdistusta*

Tuotu ominaisuus on osa laajempaa kokonaisuutta. Tässä artikkelissa esitelty ominaisuus on osa 1. Tuotavia osia on yhteensä 4.

Tässä artikkelissa esittelemme, kuinka osabudjetilla voidaan tehdä yhden osabudjetin sisällä eri dimension arvoille helposti kohdistuksia. Kyseessä on siis *vaihtoehtoinen* tapa kohdistaa arvoja dimensioille.

# Perinteinen dimensiokohdistus

"Tyypillinen tapa" tehdä dimensio-kohdistus osabudjetille on valita budjetointi -näkymässä oikeaan yläkulmaan haluttu dimension arvo. Tämän jälkeen kaikki syötetyt luvut kohdistuvat kyseiselle arvolle. Sen jälkeen kun halutaan vaihtaa kohdistusta, otetaan oikeasta yläkulmasta sinne valittu arvo pois, ja tilalle valitaan toinen. Tässä artikkelissa esittelemme tälle tavalla vaihtoehdon.

[![](

# Lisäkohdistuksen käyttäminen osabudjetilla

Kun osabudjetilla halutaan käyttää lisäkohdistusta, ei dimensiota valita lainkaan oikeaan yläkulmaan, kuten yllä. Dimensiovalinta tehdään tällaisessa tapauksessa osabudjetin riviasetuksista rivikohtaisesti.

[![](

Riviasetuksissa on kenttä nimeltä "additional dimension values", joka tarkoittaa nimenomaan dimensio -kohdistusta (nk. lisäkohdistus). Valinta näkyy kaikilla rivityypeillä (otsikko, syöttörivi, kaavarivi sekä prosenttirivi). Laittamalla kenttään jonkin dimension arvon, kohdistuu kyseinen rivi kyseiselle dimensionarvolle.

[![](

​

**Esimerkki 1:**

Lisäkohdistusta voidaan käyttää hyödyksi siten, että osabudjetin eri riveillä on eri lisäkohdistukset, jolloin osabudjetin rivi 1 kohdistuu dimensionarvolle A, rivi 2 kohdistuu dimensionarvolle B jne.

Alla on osabudjetti nimeltä "sales", jossa on kolme riviä. Jokaisella rivillä on tiliohjaus pääbudjetin tilille 3000. Ensimmäiselle riville on kiinnitetty dimensionarvo "Finland", toiselle riville dimensionarvo "Sweden" ja kolmannelle riville dimensionarvo "USA".

[![](

Nyt kun asiaa tarkastellaan pääbudjetin kautta monitor -näkymässä, nähdään, että tilille 3000 ohjautuu koko myynti eli yhteensä myyntiä on 3 005 000,00€. Sen lisäksi nähdään, että kaikki myynti tulee osabudjetilta, jonka nimi on "sales". Tämän alta nähdään, että myynnistä 1 200 000,00€ kohdistuu dimensionarvolle "Finland", 925 000€ kohdistuu dimensionarvolle "Sweden" ja 880 000,00€ kohdistuu dimensionarvolle "USA".

[![](

**Esimerkki 2:**

Alla olevassa esimerkissä osabudjetille on luotu hierarkinen rakenne. Osabudjetille on luotu ensimmäisenä otsikkorivi "Project 2022T1" ja sen alle on luotu lapsirivejä. Viimeinen rivi on kaavarivi, joka ohjaa laskennan lopputuloksen pääbudjetille.

Mikäli lisäkohdistus tehdään hierarkisessa osabudjetin rakenteessa hierarkisen rakenteen ylimmälle oksalle, valuu kohdistus lapsiriveille. Tässä tapauksessa siis kun dimensionarvo kiinnitetään riville "Project 2022T1", valuu kohdistus myös riveille sales €, purchases € ja total €.

[![](

Otsikkoriville on tässä esimerkissä kiinnitetty dimensionarvo "Finland".

[![](

Tämän jälkeen dimensiokohdistus näyttäytyy eri riveillä siten, että sillä rivillä mihin kiinnitys tehtiin, se näkyy edelleen kentässä "additional dimension value" ja lapsiriveillä, mihin kohdistus "valuu", se näkyy kentässä "inherited additional values"

[![](

**Esimerkki 3:**

Osabudjetilla voi olla myös useita hierarkisia rakenteita ja lisäkohdistusta voidaan käyttää siten, että kullakin hierarkisella rakenteella on oma erillinen dimensiokohdituksensa. Jokainen hierarkinen rakenne valuttaa lisäkohdistuksen "omille" lapsiriveilleen.

[![](

# Lisätietoja

[Lisäkohdistuksen käyttäminen osabudjetilla, osa 2: matriisikohdistus](

[Lisäkohdistuksen käyttäminen osabudjetilla, osa 3: lisäkohdistuksen periytyminen ja rivien kopiointi](

Lisäkohdistuksen käyttäminen osabudjetilla, osa 4: tagit ja kaavat. \*\*HUOM: superuserin ominaisuus, artikkeli tulossa\*\*



artikkelin osoite on https://intercom.help/finazilla/fi/articles/6677642-lisakohdistuksen-kayttaminen-osabudjetilla-osa-1

