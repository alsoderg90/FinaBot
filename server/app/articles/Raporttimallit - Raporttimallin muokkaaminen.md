## Raporttimallin muokkaaminen

Joskus voi olla miellekästä saada raporttiin näkyviin, mitä mikin luku on % osuuksina. Tällöin voidaan käyttää nk. select percentage target -toimintoa. Tässä esimerkissä näytämme, kuinka luodaan tuloslaskelmasta versio, mihin nousee % -osuus liikevaihdosta.

# **Raporttimallin muokkaaminen**

Ensimmäisenä käydään kopioimassa Customer - Report Scheme -valikossa tuloslaskelma raporttimalli ja annetaan kopiolle uusi nimi. Näin toimien saadaan vanha pohjalle otettu raporttimalli pysymään ennallaan.

Tämän jälkeen mennään muokkaamaan luotua kopiota klikkaamalla raporttimallin nimeä listasta. Raporttimallin raporttipuu aukeaa näkyviin. Valitaan yläosasta "settings", jonka takaa löytyy valinta "select percentage target".

[![](

Tämän jälkeen aukeaa select target account -kohdasta aukeaa alasvetovalikko, jossa on valittavissa kaikki raporttimallilla olevat rivit, joihin tulee summia.

[![](

Tässä esimerkissä halutaan laskea % -osuuksia liikevaihdosta, joten raporttimallille valitaan vaihtoehto "liikevaihto".

Tämän jälkeen raporttimallilla voidaan raportoida normaalisti reports -valikossa. Raportti näkyy oheisesti, kun valintana on tilikausi siten, että koko tilikausi näytetään yhdessä sarakkeessa.

[![](

[![](

*Toiminto ei sovellu käytettäväksi silloin kun %- osuus halutaan laskea yksittäisestä arvosta. Tällöin oikea toimintamalli on muodostaa raporttimallille erillinen rivi, johon lasketaan kyseinen % arvo. Tästä hyvänä esimerkkinä toimii myyntikate %.* 

Toimia ei voida käyttää yhdessä raporttien kanssa, joissa on valinta dimensio/column

[![](

*Muista system -tasoiset valmiit raporttimallit, joista löytyy mm. "tuloslaskelma sis. myynti- ja käyttökatteen % liikevaihdosta"*



artikkelin osoite on https://intercom.help/finazilla/fi/articles/4957031-esimerkki-tuloslaskelma-raporttiin-liikevaihdosta-sarakkeen-lisaaminen

