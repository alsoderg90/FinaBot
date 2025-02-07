## Päivämäärien eri muodot

Raporttia luodessa tulee käyttäjälle valittavaksi muunmuassa vaihtoehto "date format", joka tarkoittaa sitä, miten päivämäärät tulevat raporttiin näkyväksi. Oletusvalintana on "year and month", mikä on useisiin raportteihin hyvä lähtökohta. Valinta löytyy raportilta otsikon advanced settings alta ja valinta on yleinen, koko raporttia koskettava esitystapavalinta.

[![](

# Päivämäärien eri muodot

Date format vaikuttaa siis siihen, missä päivämäärämuodossa data näytetään raportin pivotoinnissa. Alla on kuvattuna kukin vaihtoehto sekä niiden keskeinen sisältö:

```
Year And Month = vuosi ja kuukausi  

```
```
Month And Year = kuukausi ja vuosi  

```
```
Month = kuukausi  

```
```
Year, Month and Day = vuosi, kuukausi ja päivä  
Käytettävissä vain operatiivisessa datassa
```

Alla näytämme, miltä kullakin valinnalla tehty raportti näyttää. Ensimmäinen raportti on tehty valinnalla year and month, seuraava on tehty valinnalla month and year ja kolmas raportti on tehty valinnalla month.

[![](

Valintaa tehdessä tulee kiinnittää huomiota myös raportin muihin aikaväliä koskeviin valintoihin, joita tehdään advanced settings valikon lisäksi raportin tietolähteellä/tietolähteillä. Tietolähteellä vaikutetaan vain ja ainoastaan kyseisen tietolähteen esitystapaan ja valintoihin ja eri tietolähteillä voi olla toisistaan poikkeavat valinnat.

Jos käyttäjä haluaa raportoida esimerkiksi päivämäärätasoisesti dataa, mutta ei valitse advanced settings valikossa kohtaan date format -kohtaan "Year, Month and Day" vaihtoehtoa (ainoa vaihtoehto missä on päivä mukana) ei hän saa päiväkohtaista raporttia - vaikka kuinka valitsisi raportin tietolähteissä alempana kohdassa "Period presentation type" vaihtoehdon "Day per column".

Päiväkohtaista raportointia voi tehdä vain operatiivisella datalla. Kirjanpidon dataa ei siis pysty raportoimaan päiväkohtaisesti, eikä päivä -valinta tule edes näkyville talousraporteilla.

[![](

*Month valinnalla raportoitaessa raportille tulee aina oletuksena 12 kuukautta, vaikka käytettäisiin esimerkiksi valintana accounting periodia ja yrityksen tilikausi olisikin esimerkiksi 14 kuukautta.* 

*Kuukaudet saa esiin pivotoimalla raporttia siten, että valitsee dates -valikosta esiin year vaihtoehdon ja ottaa sen mukaan raportin aikamääreisiin datasource vaihtoehdon alle.* 



artikkelin osoite on https://intercom.help/finazilla/fi/articles/4290898-date-format-valinta-maarittelee-missa-muodossa-aikavali-tulee-raportille

