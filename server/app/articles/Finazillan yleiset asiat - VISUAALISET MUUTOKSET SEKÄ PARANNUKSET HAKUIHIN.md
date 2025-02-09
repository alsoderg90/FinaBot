## VISUAALISET MUUTOKSET SEKÄ PARANNUKSET HAKUIHIN

[![](

*Versiopäivityksessä 8.6.2023 tuotu parannus Finazillan ulkoasuun. Parannuksella pyritään yhtenäistämään eri näkymiä sekä parantamaan erilaisia haku- sekä järjestelytoimintoja.* 

Olemme tuoneet Finazilla -ohjelmistoon kaikkien näkymien kattavan tyylimuutoksen. Muutoksen tarkoituksena on yhdenmukaistaa erilaisten valikoiden näkymää - ja toimintatapaa. Olemme samalla tuoneet myös pieniä uudistuksia, jotka helpottavat asioiden löytämistä Finazillasta.

Tässä artikkelissa kuvaamme ohjelmistoon tehtyjä muutoksia. Muutoksista valtaosa koskettaa ns. visuaalisia asioita, mutta artikkelin lopussa on muutama muutos, joissa jonkin ominaisuuden käyttötapa muuttuu hieman.

# VISUAALISET MUUTOKSET SEKÄ PARANNUKSET HAKUIHIN

## **Värit ja asettelut**

Tarkkasilmäiset käyttäjät saattavatkin huomata, että Finazillan valikoiden väri on muuttunut hieman aiemmasta. Värit itsessään ovat pääosin samat, mutta niiden sävyä on muutettu hieman. Väritys on muuttunut kaikissa valikoissa ja painikkeissa, sekä mm. kirjautumissivulla.

Värien lisäksi muutoksia on tehty useiden näkymien otsikkokenttiin ja näkymiä on yhtenäistetty. Muutokset ovat hienovaraisia. Muutoksella on pyritty visuaaliseen yhtenäistämiseen ohjelmiston sisällä.

## **Otsikoiden mukaan järjesteleminen**

Aina kun valikossa olevien otsikoiden perässä esiintyy nuolisymbolit ylös- ja alas, tarkoitaa tämä, että kyseistä kenttää voidaan hyödyntää tietojen järjestelyssä. Otsikkoa klikkaamalla näkymä järjestellään klikatun otsikon mukaan aakkosissa joko nousevaan, tai laskevaan järjestykseen.

[![](

## **Haku -toiminnot (search)**

Kaikkiin valikkoihin, missä käyttäjällä esiintyy erilaisia listauksia, on tuotu yläosaan erillinen haku- kenttä. Kenttä mahdollistaa sen, että käyttäjä löytää entistä nopeammin ja helpommin haluamansa asiat Finazillasta. Haku toimii pääosin name -kentän perusteella, muutamia poikkkeuksia lukuun ottamatta (mm. raportointiryhmissä haku hakee ryhmän sisältä myös dimensioita hakusanoilla).

[![](

Haku -kenttä löytyy mm. seuraavista valikoista

* Käyttäjät (customer users sekä company users -näkymät), roolit
* Dimensiot
* Raporttimallit, raporttimalli templaatit, Raportointi (reports)
* Budjetit (budget)
* Vyörytyssäännöt, laskentavakiot
* Tositeporautumisen listaus
## **Haku -toiminnot (search) hierarkisissa näkymissä**

Finazillassa on myös nk. hierarkisia näkymiä, kuten esimerkiksi raportointiryhmät (reporting groups). Tässä näkymässä haku -toiminto on hieman eritavalla näkyvä kuin muualla. Haku toimii tässäkin näkymässä, mutta hakutulos näytetään eri tavalla. Lisäksi search -kentässä ei näy mitään arvoa, ennen kuin kenttään aletaan kirjoittamaan jotakin hakusanaa.

Haku on hieman poikkeava, jotta käyttäjälle voidaan näyttää hakutulos, joka voi olla "piilossa" jossain hierarkisen rakenteen sisällä.

[![](

Mikäli halutuloksia on useita, pääsee hierarkisissa näkymissä helpoiten seuraavaan näkymään klikkaamalla hakukentän perässä olevaa nuolta. Tämän jälkeen käyttäjä ohjataan seuraavaan hakutulokseen. Raksista haku voidaan sulkea ja käyttäjä ohjataan takaisin päänäkymään.

[![](

Haku -kenttä löytyy mm. seuraavista hierarkisista näkymistä

* Tilikartta
* Raportointiryhmät
## **Haku -toiminto (search) tositteissa**

Haku toiminto tositteissa on hieman muista näkymistä poikkeava. Tämä johtuu siitä, että haku on haluttu ulottaa myös dimensioiden hakemiseen. Perinteinen otsikoiden mukaan järjesteleminen ei ole tässä toimiva, sillä tositteilla voi olla useita dimensio -kohdistuksia.

Haku tulee esiin kun jokin tosite klikataan auki vouchers -näkymästä. Haku toimii tämän tyyppisissä näkymissä siten, että erillisessä search -kentässä voidaan hakea dimension arvon (tai arvojen erusteella) tositerivit, joissa haetut dimension arvot esiintyvät.

[![](

## **Haku -toiminto (search) dimensioissa ja dimension arvoissa**

Dimensions -listauksella dimensioita voidaan hakea oikean yläkulman search -valikon kautta. Lisäksi dimensioita voidaan järjestellä otsikkoja klikkaamalla.

[![](

Kun yksittäinen dimensio aukaistaan listasta sen nimeä klikkaamalla, aukeaa listaus kyseiseen dimensioon kuuluvista dimension arvoista. Näitä voidaan hakea haku kentällä tai yläosan vasemman reunan filtterillä.

[![](

Filtterillä löytyy helpoiten arvot, jotka on esimerkiksi piilotettu vaikkapa raportoinnista, kuten alla.

[![](

## **Haku -toiminto tositeporautumisen tositelistauksessa**

Raportin kautta voidaan porautua solun tositteisiin. Myös aukeavaa tositelistaus -näkymää on parannettu. Tositelistauksessa voidaan käyttää hakusanoja, jotka ulottuvat kaikkiin kenttiin (päivä, tositenumero, tilinumero, kuvaus, dimensiot ja summa). Näkymää voi myös järjestellä otsikoiden mukaisesti otsikkoa klikkaamalla.

Tositelistauksessa on myös yläosassa erillinen search -kenttä, jolla voidaan hakea tietyn dimension arvon tositerivejä valitsemalla haettava dimension arvo kenttään.

[![](

## **Cash Flow -näkymä**

Näkymää on selkiytetty siten, että jatkossa numeerinen kassavirta ja graafinen kassavirta ovat alekkain. Näin kumpikin näkymistä saadaan suuremaksi. Samalla kassavirran graafinen kuvaaja on muutettu Finazillan uusien graafisten raporttien muotoon.

## **Company settings -näkymä**

Näkymään on tehty eri toiminnoille omia välilehtiään. Settings -välilehdellä on yrityksen yleiset asetukset, integrations -välilehdelle integraatioihin liittyvät asiat ja saldojen lasketus on välilehdellä recalculate balances. Custom links -näkymä on myös omalla välilehdellään.

[![](

# MUUTOKSET, JOISSA OMINAISUUDEN KÄYTTÖTAPA MUUTTUU JOLLAIN TAVALLA

## **Raportointiryhmien luominen selkeytyy**

Samalla kun raportointiryhmiin tehtiin tyyliuudistus, muutettiin raportointiryhmien luomista hieman. Jatkossa raportointiryhmä luodaan antamalla sille nimi ja kiinnittämällä dimension arvot dimension values -kenttään.

[![](

Muutos on suurin niissä tilanteissa, missä luodaan hierarkisia raportointiryhmiä. Jatkossa luodaan ensin raportointiryhmä ja sen jälkeen luodaan ryhmän alle uusi ryhmä painikkeesta "new child group". Alisteiselle "lapsiryhmälle" annetaan nimi ja kiinnitetään halutut dimension arvot.

[![](

## **Raportointiryhmien näyttäminen muuttuu**

Myös raportointiryhmien näyttämiseen on tehty pieni visuaalinen muutos. Jatkossa raportointiryhmä näyttäytyy siten, että raportointiryhmän nimi on ylimmäisenä. Tämän jälkeen näytetään dimension arvo (kuukausisopimukset) ja sen perässä, mistä dimensiosta kyseinen arvo on.

[![](

## **Laskentavakiot (calculation constants)**

Laskentavakioita on selkiytetty uudistuksen yhteydessä hieman tyylimuutosta laajemmin. Budjettikohtaiset laskentavakiot löytyvät jatkossa kyseiseltä budjetilta omalta välilehdeltään.

[![](

Constants -välilehdellä näkyy kaikki system -tasoiset laskentavakiot (nk. Finazillan luomat valmiit laskentavakiot) , kaikki asiakaskohtaiset laskentavakiot (customer), kaikki yrityskohtaiset laskentavakiot (company), sekä kaikki budjettikohtaiset laskentavakiot (budget).

Näkymässä pystyy luomaan uusia laskentavakioita valitsemalla "new calculation constant". Luotavasta laskentavakiosta tulee budjettikohtainen, mikä tarkoittaa sitä, että kyseinen laskentavakio näkyy, ja on käytettävissä, vain kyseisellä budjetilla.

[![](

Budjetin kautta aukeavasta laskentavakiolistauksesta voidaan muokata kaikkia muita laskentavakioita paitsi system -tasoisia. Näkymän kautta pystyy siis esimerkiksi antamaan company -tasoiselle laskentavakiolle uusia arvoja. Muutokset päivittyvät kaikkialle.



artikkelin osoite on https://intercom.help/finazilla/fi/articles/7924006-finazillan-tyyliuudistukset

