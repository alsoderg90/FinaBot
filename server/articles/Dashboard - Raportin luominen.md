## Raportin luominen

[![](

*Versiopäivityksessä 24.10.2023 tuotu parannus. Parannus mahdollistaa tavoitetilan asettamisen tunnusluvulle -ja tavoitteen täyttymisen seuraamisen*

Artikkelissamme ["tunnuslukujen kiinnittäminen Dashboardille"]( kuvataan, miten yksittäisiä tunnuslukuja luodaan Dashboard -näkymään. Tässä artikkelissa kerromme, miten tunnusluvulle voidaan asettaa tavoitetila ja raportoida tavoitetilan täyttymistä.

# Raportin luominen

Luodaan raportti reports -valikossa. Tässä esimerkissä luodaan raportti käyttämällä system -tasoista raporttimallia "tuloslaskelma". Luodaan raportille yksi tietolähde, jonka nimeksi annetaan "kuluva" ja kyseiselle tietolähteelle haetaan dataa valinnalla "current period". Tallennetaan raportti.

# Raportin kiinnittäminen Dashboardille

Kun laadittu raportti halutaan kiinnittää ko. yrityksen Dashboardille, mennään ensin Dashboard -näkymään. Dashboard laitetaan muokkaus -tilaan "actions valikon takaa kohdasta "edit". Tässä kohdin voidaan luoda joko kokonaan uusi Dashboard tai valita jokin olemassa olevista Dashboardeista. Uutta sisältöä lisätään add widget -painikkeen kautta. Valitaan vaihtoehto "key figures".

Kun tunnusluvusta halutaan tehdä tavoitetilaa indikoiva, valitaan vaihtoehto "use traffic lights instead".

[![](

## Tavoitetilan, eli nk. liikennevalon, asettaminen

Kun widgetin luonti -ikkunassa on valittu vaihtoehto "use traffic lights instead", aukeaa käyttäjälle automaattisesti optional settings -valikko. Valikossa voidaan asettaa tavoitetilat.

Limit to use negative color -kentässä kerrotaan arvo, joka esitetään punaisena. Limit to use positive color kenttään asetetaan arvo, joka esitetään vihreänä.

[![](

**Havainnollistava esimerkki:** 

Yrityksen A liikevaihtotavoite on 15 000 000,00 euroa. Huonona tuloksena pidetään, jos liikevaihto jää 12 000 000,00 euroon. Tunnusluku widgetille annetaan tavoitearvot kuvatun mukaisesti.

[![](

# Tunnusluvun näkyminen Dashboardilla

Tunnusluku tulee Dashboardille siten, että valittu tunnusluku (esimerkin tapauksessa liikevaihto) tuodaan annettujen tavoitetilojen värien mukaisesti. Yrityksen A liikevaihto on ollut kausilla 1-8/2023 yhteensä 12 132 740,00€. Liikevaihto ylittää "limit to use negative color" kenttään asetetun minimitavoitteen (12 000 000,00€), mutta alittaa "limit to use positive color" tavoitetilan (15 000 000,00€), jolloin arvo esitetään neutraalilla värityksellä (keltainen).

[![](

[![](

*Finazilla tuo automaattisesti negatiiviseksi väriksi punaisen, neutraaliksi keltaisen ja positiiviseksi vihreän. Värejä voi haluttaessa myös vaihtaa klikkaamalla värikoodi -kentässä. Värin voi valita joko aukeavasta väripaletista, tai syöttää värikoodin.* 

*Tunnusluku widgettiä luotaessa tavoitearvot voi kirjoittaa description kenttään, jolloin ne näkyvät dashboardilla widgetin yläkulman i -painikkeen kautta pop up -ikkunassa.* 

[![](

artikkelin osoite on https://intercom.help/finazilla/fi/articles/8508340-tunnusluvulle-tavoitteen-asettaminen-kayttaen-key-figures-toimintoa

