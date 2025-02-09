## Esimerkki operatiivisille dimensioille budjetoinnista:

Aikaisemmassa artikkelissamme ["Operatiivisen datan budjetointi osa 1"]( kerroimme, kuinka operatiivista dataa voidaan budjetoida siten, että kyseistä operatiivista budjetointia voi hyödyntää kirjanpidon budjetin laskennassa.

Tässä artikkelissa keskitymme siihen, kuinka operatiivista dataa voidaan budjetoida siten, että saadaan raportoitua operatiivisesta datasta ja kirjanpidon datasta matriisidimensioiden lukuja.

# Esimerkki operatiivisille dimensioille budjetoinnista:

Yrityksellä on operatiivinen dimensio nimeltä tuote, jonka alle kuuluvat dimensiovaluet, jotka ovat yrityksen tuotteet: akseli, holkki ja mäntä. Operatiivinen data on tuotu Finazillaan operative datagroup indentifier -kohdassa "tuotevalmistus" nimellä.   
​

Lisäksi yrityksellä on kirjanpidon dimensiona tehdas, jonka alla ovat dimensiovalueina yrityksen kolme eri tehdasta, eli tehdas 1, tehdas 2 ja tehdas 3.

​

Yritys haluaa budjetoida operatiivista dataa, eli tuotteita, mahdollisimman tarkasti. Tarve on kohdistaa lukuja ns. matriisidimensioille eli tehdas x + tuote y -tyyppisesti. Tämä mahdollistaa kyseisessä esimerkkitapauksessa mm. sen, että valmistusta voidaan pivotoida raportoinnissa sekä tuotteittain, että tehtaittain - sekä molempia yhtäaikaa.   
​

# Budjetin sekä osabudjetin luominen

Budjetointi alkaa sillä, että käyttäjä luo budjetin sekä osabudjetin. Operatiivinen data budjetoidaan osabudjetin kautta. Osabudjetille luodaan kolme riviä, joille kaikille laitetaan kohtaan Transfer to datagroup -kohtaan "Tuotevalmistus".

[![](

*Kun "Transfer to datagroup" -valinta tehdään alasvetovalikosta valitsemalla siellä oleva vaihtoehto "tuotevalmistus", kohdistuu data juuri sille datagroupille, millä operatiivinen data on alkuperäisestikin tuotu Finazillaan. Jos käyttäjä tässä kohdin kirjoittaisi uuden haluamansa datagroupin, kohdistuisi tiedot tälle uudelle datagroupille.*  
​

Ensimmäinen rivi, mikä budjetille luodaan, on yrityksen ensimmäinen tuote eli "akseli". Operative dimension target -kohtaan tulee "tuotevalmistus". Toinen rivi on yrityksen toinen tuote eli "holkki". Operative dimension target -kohtaan tulee "tuotevalmistus". Kolmas rivi on yrityksen kolmas tuote eli "mäntä". Operative dimension target -kohtaan tulee "tuotevalmistus".   
​

# Budjetointi

Budjetointi alkaa siitä, että osabudjetilla valitaan oikeaan yläkulmaan haluttu tehdas -vaikkapa tehdas 1. Tämän jälkeen syötetään halutut arvot jokaiselle kolmelle tuotteelle. Sama toistetaan kaikille tehtaille ja kaikille tuotteille.   
​  
Syötetyt luvut kohdistuvat nyt kaikki aikaisemmin mainituille matriisidimensioille eli tehdas x + tuote y, joka muodostuu riville syötetyn operative dimension target -valinnan, sekä kirjanpidon dimensiovalinnan summasta.   
​

# Budjetin raportointi

Tehtyä budjettia voidaan tämän jälkeen raportoida halutulla raporttimallilla (esimerkiksi system tasoisella system operative data -raporttimallilla) ja pivotoida raporttia halutunlaiseksi.   
​

[![](



artikkelin osoite on https://intercom.help/finazilla/fi/articles/4311833-operatiivisen-datan-budjetointi-osa-2-matriisidimensiot

