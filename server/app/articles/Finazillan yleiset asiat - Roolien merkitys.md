## Roolien merkitys

# Roolien merkitys

Rooleilla on suuri merkitys tietojen näkemisen ja muokkaamisen näkökulmasta. Roolien merkitys korostuu silloin kun on tarvetta rajata jonkin käyttäjän näkymää johonkin tiettyyn dataan tai halutaan antaa käyttäjälle näkymä vain yhden yrityksen dataan.

Roolien avulla voidaan yksilöidä hyvinkin tarkasti, mikä tietty käyttäjä (tai vaikkapa käyttäjäryhmä) näkee ja voi tehdä. Rooleja voidaan siis ajatella oikeuksien antamisena dataan. Oikeudet on Finazillassa rajattu kolmeen kategoriaan; lukuoikeus, muokkausoikeus ja oikeus poistaa dataa.

Kun ajankohtaiseksi tulee eri roolien ja käyttöoikeuksien miettiminen ja laatiminen Finazillaan, voidaan pohdinnan avuksi ottaa oheiset kysymykset:

* Kuka pystyy muokkaamaan raporttimalleja ja toisaalta, kenen on syytä päästä näkemään raporttimallien rakenne?
* Kenellä on oikeudet budjetointiin ja osabudjettien muokkaamiseen ja kenellä vain katseluoikeus? Saako käyttäjä nähdä kaikki kaikki budjetit ja osabudjetit vai vain tietyn budjetin tietyt osabudjetit?
* Onko mahdollisesti dimensioita, joiden näkyvyys tietyille käyttäjille pitää estää?
* Kuka saa muokata yrityksen taustalla olevia perusasetuksia, kuten tilikarttaa, tilejä, käyttöoikeuksia jne. ?
# **Koko asiakkuuden pääkäyttäjätunnus**

Kun asiakkuus luodaan Finazillaan, perustetaan asiakkuudelle Customer -tason pääkäyttäjätunnus. Customer -tasoinen pääkäyttäjätunnus on koko asiakkuuden pääkäyttäjätunnus. Tämä tunnus luovutetaan asiakkaan pääkäyttäjälle.

# **Uusien käyttäjätunnusten luominen**

Pääkäyttäjätunnuksella uusia käyttäjätunnuksia voi luoda sekä Customer – että Company –tasoilla. Customer -tasolla (Customer –valikon alla) annetaan pääkäyttäjäoikeus koko asiakkuudelle. Tämä tarkoittaa, että käyttäjä pääsee näkemään ja muokkaamaan kaikkien asiakkuuden alla olevien yhtiöiden dataa sekä Finazillan toimintoja.

Uusille customer –tasoisille pääkäyttäjille tulee automaattisesti rooliksi CustomerUser. Tällaista tunnusta ei tarvitse erikseen liittää rooliin, eikä samaa käyttäjätunnusta tarvitse luoda enää erikseen Company -tasolle.

Kun käyttäjälle halutaan antaa oikeuksia vain tiettyyn yritykseen / yrityksiin, suositellaan tämä tehtäväksi Company –tasolla (Company –valikon alla, jossa on omat toiminnot tunnusten luontiin ja roolien muokkaamiseen). Uusille company -tasoisille käyttäjille tulee automaattisesti rooliksi CompanyUser.

*Company –tason tunnukset pitää aina **l**iittää johonkin rooliin*, ennen kuin mitään toimintoja pystyy näkemään tai käyttämään Finazillassa. Ilman kiinnitettyä roolia company user ei pysty tekemään mitään muuta kuin kirjautumaan sisään Finazillaan.

# **Roolit**

Finazillassa on valmiiksi luotuna Company -tasoiset roolit "CompanySuperUser" ja "CompanyUser". CompanySuperUser rooli on ikään kuin yritystasoinen pääkäyttäjärooli kun taas CompanyUser -roolilla käyttäjä pääse pelkästään kirjautumaan Finazillaan sisään. Jälkimmäinen rooli tarvitsee aina jonkin lisäroolin, missä käyttäjän oikeudet on määritelty.

Erilaisia rooleja voi määritellä kattavasti Finazillassa. Suosittelemmekin yrityksille, joissa on paljon eri käyttäjiä, suunnittelemaan tarkkaan, minkälaisia oikeuksia käyttäjille halutaan antaa. Oikeudet Finazillaan toimintoihin myönnetään roolien avulla. Samalla käyttäjällä voi olla useisiin asiakkuuden yrityksiin erilaisia rooleja.

Alla olemme vielä kuvanneet eri rooleja Finazillassa

[![](

[![](

*Käyttäjätunnusten valvonta ja hallinta on asiakkaan vastuulla, eikä Finazilla pidä rekisteriä käyttäjätunnuksista.* 

# Lisätietoja

[Roolien kautta määritellään yritystasoisen käyttäjän käyttöoikeudet Finazillassa](

[Yrityksen käyttäjätunnusten hallinnoiminen](



artikkelin osoite on https://intercom.help/finazilla/fi/articles/4163868-mika-merkitys-eri-rooleilla-on-finazillassa

