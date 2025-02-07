## Kuluvan kuukauden raportointi

Olemme kuvanneet months from dynamic date -valinnan avulla tehtäviä raportteja artikkelissamme ["lukituspäivän käyttäminen mahdollistaa raportoinnin siihen saakka, mihin kirjanpito on valmistunut"]( Tässä artikkelissa neuvomme, miten dynaamisia valintoja voidaan hyödyntää siten, että muodostetaan raportti, joka raportoi aina automaattisesti kuluvaa kuukautta.

Kyseinen raportti voidaan muodostaa useammalla eri tavalla. Esittelemme vaihtoehtoista tyypillisimmän tavan.

# Kuluvan kuukauden raportointi

Uusi raportti muodostetaan normaalisti "reports" valikon kautta painikkeella "new report". Raportille annetaan kuvaava nimi ja valitaan haluttu raporttimalli.

[![](

Kun raportille on lisätty raporttimalli, lisää Finazilla raporttiin automaattisesti tietolähteen ja nimeää sen oletusnimellä. Seuraavaksi lähdetään tekemään valitulle tietolähteelle määrittelyitä. Finazillan raporteilla on aina oletusvalinta, että raporttia tehdään kuluvasta tilikaudesta. Tämä valinta on tässä esimerkissä oikea, mutta raportin dynaamisia alku- ja loppuaikoja tulee muuttaa.

[![](

Nyt kyseinen raportti raportoi aina kuluvan tilikauden kuluvaa kuukautta. Raportti päivittyy sitä mukaa, kun kuukaudet vaihtuvat.

[![](

*Kuluvaa kuukautta voi raportoida myös käyttämällä "months from dynamic date" valikon kautta siten, että number of dynamic months -kenttään ei syötetä mitään arvoa.*

*Kuluvan kuukauden saa raportoitua myös "months from dynamic date" valikon kautta syöttämällä number of dynamic months" kenttään arvon 1, sekä valitsemalla "include dynamic start" valinnan päälle.* 

[![](

*Yrityksen aktiivinen tilikausi on vuosi 2024 ja artikkelin kirjoitushetkellä on toukokuu (eli kuluva kuukausi on toukokuu). Jos raportin asetuksissa määritellään accounting period kohtaan "previous period", muodostuu kyseinen raportti aikaväliltä 5/2023 ja vastaavasti taas valinta "next period" tuottaa raportin aikaväliltä 5/2025 (mikäli ko. kaudella olisi lukuja mitä raportoida, kuten esimerkiksi budjettia raportoitaessa).* 

*Jos tilikaudella ei olisi ollenkaan kuluvaa kuukautta (eli tässä tapauksessa tilikaudella ei olisi yhtään toukokuuta) näytetään koko tilikausi. Tällainen tilanne voi tulla vastaan yrityksillä, joilla on alimittainen tilikausi.* 



artikkelin osoite on https://intercom.help/finazilla/fi/articles/5294167-esimerkki-luodaan-raportti-jossa-raportoidaan-aina-kuluvaa-kuukautta

