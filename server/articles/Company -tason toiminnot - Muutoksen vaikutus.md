## Muutoksen vaikutus

[![](

*Versiopäivityksessä 12.10.2023 tuotu optimointi muutos. Toiminto näyttäytyy ainoastaan niille yrityksille, joilla on yli 2000 dimension arvoa.* 

Finazillan logiikkaa on muutettu vastaamaan paremmin niiden yritysten tarpeisiin, joilla on poikkeuksellisen suuret dimensiomäärät. Tehty muutos logiikassa parantaa Finazillan suorituskykyä merkittävästi. Muutos näkyy ainoastaan yrityksille, joilla on yli 2000 dimension arvoa.

# Muutoksen vaikutus

Tehty muutos näyttäytyy kaikkialla, missä dimensioita käytetään. Muutos tarkoittaa käytännössä sitä, että Finazillassa latautuu aina oletusarvoisesti 2000 ensimmäistä dimension arvoa kustakin dimensiosta. Mikäli jossakin dimensiossa on yli 2000 arvoa, saa käyttäjä kyseisen dimension arvon valittua käyttämällä hakukenttää.

Tehty muutos näkyy mm. dimensions -listauksessa, budjetti näkymässä dimensioille budjetoitaessa, osabudjeteilla, raportin valinnoissa sekä aputyökaluissa, kuten mm. raportointiryhmien luomisessa ja vyörytyssäännöissä.

Mikäli jollekin käyttäjälle on annettu roolilla oikeuksia dimension arvoihin, jotka menevät tuon 2000 ulkopuolelle, näkyy rooleissa kuitenkin aina se dimension arvo, mihin käyttäjällä on oikeus. Tällöin dimension arvo ei jää ns. piiloon.



artikkelin osoite on https://intercom.help/finazilla/fi/articles/4984843-dimensioiden-optimointi-kun-kaytossa-on-yli-2000-dimension-arvoa

