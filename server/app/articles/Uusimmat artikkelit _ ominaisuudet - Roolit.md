## Roolit

Ominaisuutta parannettu versiopäivityksessä 9.1.2025. Muutoksessa roolinäkymä on tuotu puurakenteeseen sekä samalla Finazillan vakioroolien nimiä on selkiytetty. Samassa yhteydessä käyttäjän muut asetukset on viety oman settings -välilehden taakse. Muutos on osa laajempaa kehitystämme liittyen rooleihin ja käyttäjien luomiseen ja muutoksella haetaan selkeämpää näkymää.

# Roolit

Finazillan käyttäjänäkymässä *(**settings > customer > users*** tai ***settings > company > users***) käyttäjätunnusta klikkaamalla aukeaa näkymä siitä, mitä oikeuksia käyttäjällä on ja mihin yritykseen/yrityksiin oikeudet on annettu. Näkymässä käyttäjätunnus näkyy yläosassa ja alaosassa näkyy kyseisen käyttäjän roolit. Näkymä on puurakenteessa.

## Vakioroolit

Finazillan vakioroolien nimityksiä on selkiytetty ja yhdenmukaistettu. Uudet vakioroolit ovat seuraavat:

Customer Admin (entinen CustomerUser)

Company Admin (entinen CompanySuperUser)

Default Member (entinen CompanyUser)

Report Reader (ei muutosta)

[![](

*Kuva: Roolinäkymässä kerrotaan erillisellä info -ikkunalla vanhan roolin nimi.*

## Roolien muokkaaminen

Lähtökohtaisesti *pääkäyttäjän (customer Admin)* tapauksessa yritysten kohdalla olevaa edit roles -painiketta tarvitaan vain tilanteissa, missä käyttäjän käyttöoikeus halutaan muuttaa pääkäyttäjästä rajoitetuksi rooliksi ja käyttäjälle kiinnitetään jokin yritystason rooli. Huomaa, että yritystason rooli tulee kiinnittää ensin - vasta sen jälkeen customer admin roolin voi poistaa.

[![](

Yritystasoisen käyttäjän rooleja voidaan hallinnoida ***company > users*** -näkymässä. Alla on hallituksen jäsenen näkymä. Käyttäjällä ei ole asiakkuustasolla oikeuksia, vaan hänellä on oikeudet vain asiakkuuden kolmesta yrityksestä yhteen.

[![](

*Kuva: Oikeuksien muokkaaminen.*

Rooleja voidaan hakea yläosan search -kentän avulla, jolloin aukeaa valikko kaikista asiakkuuden yrityksistä ja niiden rooleista.

[![](

 *Kuva: Roolin hakeminen.* 

Havainnollistamme alla erilaisten käyttäjäoikeuksien näkymistä Finazillassa.

## Asiakkuuden pääkäyttäjä

Asiakkuuden pääkäyttäjän rooli näyttää oheiselta. Käyttäjällä on asiakkuuteen 1th Filmmaker Ltd Customer Admin -rooli. Tämä rooli antaa käyttäjälle automaattisesti kaikki oikeudet jokaiseen asiakkuuden yritykseen.

[![](
## Yritystasoinen pääkäyttäjä

Kun käyttäjälle on annettu oikeus asiakkuuden yhteen yritykseen siten, että käyttäjällä on yritystasoinen pääkäyttäjäoikeus, on roolin nimi Company Admin. Roolipuu näyttää oheiselta.

[![](
## Rajoitettu rooli

Alla olevassa esimerkkikuvassa käyttäjällä on pelkästään yhteen yritykseen oikeus. Käyttäjän oikeus on personoitu eli yrityksen pääkäyttäjä on luonut Finazillaan personoidun roolin nimeltä "sales manager" ja rooli on annettu kyseiselle käyttäjälle. Käyttäjällä näkyvä Default Member on Finazillan vakiorooli, joka tulee aina automaattisesti kun käyttäjä luodaan. Rooli antaa pääsyn kyseiseen yritykseen.

[![](
## Rajoitettu rooli sekä yritystason pääkäyttäjä rooli

Alla olevassa esimerkissä kyseisellä käyttäjällä on *yritystasoinen pääkäyttäjyys* yritykseen Filmmaker Group, sekä rajoitettu rooli nimeltä budjetointirooli. Tämä rooli on yrityksen itsensä luoma. Default member on Finazillan vakiorooli, joka antaa pääsyn ko. yritykseen.

[![](

*Kuva: Kyseisellä käyttäjällä on kaksi Finazillan vakioroolia, sekä yksi itse tehty rooli. Yhteen yritykseen käyttäjällä ei ole lainkaan oikeuksia.* 

HUOM! Käyttäjätunnusta klikattaessa aukeaa aina oletuksena roles -välilehti. Mikäli käyttäjätunnuksen voimassaoloaikaa, tai muita asetuksia halutaan muuttaa, löytyvät nämä erilliseltä settings -välilehdeltä.



artikkelin osoite on https://intercom.help/finazilla/fi/articles/10204570-kayttajan-asetukset-roolinakyma

