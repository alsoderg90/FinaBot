## Uusien roolien luominen

Artikkelimme ["Mikä merkitys eri rooleilla on Finazillassa?"]( kuvaa sitä, mihin roolien luomisella voidaan vaikuttaa ja mikä niiden käyttötapa Finazillassa on. Artikkelimme

["Roolien oikeuslistauksen järjestelminen haluttuun järjestykseen"]( taas antaa ohjeita listan organisoimiseen. Tässä artikkelissa opastamme, miten eri rooleja luodaan.

# Uusien roolien luominen

Roolien luominen aloitetaan valikossa "company" kohdassa "roles". Näkymään listautuu kaikki yritykselle luodut roolit. Listassa on valmiina roolit "CompanySuperUser" sekä "CompanyUser", sekä kaikki yrityksen itse luomat roolit.

# Finazillassa valmiiksi olevat Company -tasoiset roolit

## CompanyUser -rooli

Automaattisesti jokaiselle uudelle käyttäjätunnukselle syntyvä rooli. Tällä roolilla ei ole oikeutta tehdä tai nähdä mitään Finazillassa (paitsi käyttäjälle erikseen jaettuja Dashboardeja ja raportteja). Kyseisen roolin annetaan olla käyttäjälle kiinnitettynä eli sitä ei poisteta, vaan kyseiselle käyttäjälle kiinnitetään lisäksi rooli, mikä määrittelee käyttäjän oikeudet.   
​

## CompanySuperUser -rooli

Yritystasoinen pääkäyttäjätunnus, jolla pystyy näkemaan kaiken datan kyseisen yrityksen alla sekä muokkaamaan kaikkea. Tällaiselle käyttäjälle ei näy customer -valikko, eikä sen alla olevat valinnat.

# Uuden personoidun roolin luominen

Uusi rooli luodaan oikean yläkulman painikkeesta "create role". Tämän jälkeen roolille annetaan kuvaava nimi. Tässä esimerkissä luomme roolin, jolla voidaan budjetoida. Roolin luomisen jälkeen Rooli ilmestyy listaukseen.

## Roolille annettavat oikeudet

Roolille annetaan oikeuksia klikkaamalla roolin nimeä ja valitsemalla "Select Permissions". Uudet roolit saavat aina automaattisesti tietyt oletusoikeudet taustalle. Nämä oikeudet ovat ns. pakollisia oikeuksia.

[![](

Select permissions valikossa aukeaa hakuikkuna, jonka alasvetovalikosta näkyy toiminnot, joihin käyttäjälle voi antaa oikeuksia. Oikeudet (onko kyseessä pelkkä lukuoikeus vai myös esim. muokkausoikeus ja poisto-oikeus), määritellään seuraavassa vaiheessa.

[![](

Halutut oikeudet valitaan listasta klikkaamalla yksitellen haluttuja oikeuksia, kunnes kaikki halutut oikeudet on valittu. Apply -painikkeesta päästään määrittelemään oikeuksia tarkemmin.

[![](

## Oikeuksien rajaaminen

Tämän jälkeen oikeuksia voi vielä rajata lisää vaihtoehdoin "read", "edit", "delete" ja "create" (sekä budjetti -kohdassa edellä mainittujen lisäksi "input"). Jos esimerkiksi jossain osa-alueessa roolille halutaan vain lukuoikeus, voidaan sen kohdalta poistaa muut oikeudet ja jättää pelkkä read -oikeus.

[![](

Yllä olevassa esimerkissä käyttäjän oikeuksia budjetoinnissa on rajoitettu siten, että käyttäjä voi budjetoida ainoastaan budjettia 2023, sekä siellä olevaa osabudjettia "myyntibudjetti". Käyttäjälle ei näy lainkaan muut budjetit/osabudjetit.

Budjettien puolella oleva erillinen input -oikeus tarkoittaa sitä, että jos käyttäjällä on pelkästään input -oikeus (ei lainkaan siis edit -oikeutta), saa käyttäjä ainoastaan budjetoida. Tällainen käyttäjä ei saa koskea budjetin ja/tai osabudjetin rakenteisiin. Molemmat oikeudet omaava käyttäjä saa sekä budjetoida, että muokata rakenteita.

Edellä esimerkissä näkyvyyttä myös dimensioihin oli rajoitettu. Jos näkyvyyttä dimensioihin ei olisi rajoitettu, eli kaikki oikeudet olisi annettu (vihreinä), käyttäjä näkisi pääbudjetille syötetyt luvut dimensioittain eriteltynä monitorinäkymästä ja myös pääbudjetointinäkymästä kulloinkin valittuna olevan dimension osalta. Käytännössä tällöin käyttäjä näkisi koko budjetin, mutta pystyisi syöttämään lukuja kuitenkin vain siinä osabudjetissa, johon hänelle on annettu muokkausoikeudet.

Mikäli näkyvyyttä pitää rajata, tämä tapahtuu siis rajoittamalla dimensioita. Dimensioista pystyy rajamaan pois myös yksittäisiä arvoja, kuten kuvassa alla.

[![](

Lisäksi tässä yhteydessä on hyvä tiedostaa, että mikäli esimerkin budjetoijan pitää pystyä raportoimaan, tulee hänelle antaa oikeudet raporttimalleihin (report scheme).

Jos esimerkin budjetoijalla on tarve raportoida laatimansa budjetit, voidaan roolille/käyttäjälle tehdä oma raportimalli. Raporttimalleihin liittyvät artikkelit löytyvät esimerkiksi hakusanalla"raporttimalli".

[![](

# Käyttäjätunnuksen kiinnittäminen luotuun rooliin

Kun tarvittavat roolit on luotu ja rajattu halutulla tavalla, niin niihin voidaan kiinnittää company –tasoisia tunnuksia. Company -tasoiset tunnukset pitää aina liittää rooliin, ennen kuin mitään toimintoja pystyy näkemään tai käyttämään Finazillassa.

Rooli kiinnitetään käyttäjätunnukseen company -valikossa kohdassa users. Listasta valitaan käyttäjätunnus nimeä klikkaamalla ja näkymän ylöosassa voidaan hakea käyttäjätunnukselle tarvittavat roolit "add user to role" painikkeen kautta.

Käyttäjälle voi myös antaa saman roolin (esim. CompanySuperUser) useaan eri asiakkuuden yritykseen. Tämä on ohjeistettu artikkelissamme [täällä.](

[![](

*Uuteen käyttäjätunnuksen liitettävää roolia voi testata etukäteen oheisesti. Liitä rooli käyttäjätunnukseen ja ennen käyttäjätunnuksen luovuttamista, testaa rooli kirjautumalla tunnuksella sisään Finazillaan ja tarkistamalla, mitä rooli näkee.*

*Muista myös informoida käyttäjätunnuksen haltijaa hänen rajoitetuista oikeuksistaan Finazillassa.* 

*Roolit on myös hyvä nimetä mahdollisimman kuvaavasti tai jokaiselle käyttäjälle tai osalle käyttäjistä on oma personoitu rooli.*

[![](

*Saman käyttäjätunnuksen voi kiinnittää roolien kautta useampaan yritykseen. Tämä tehdään valikossa Company - Users. Klikataan käyttäjän nimeä, jolloin kyseinen tunnus voidaan kiinnittää rooliin. Valitaan "Company" kenttään yritys, mihin oikeus annetaan.*

# Useiden roolien luominen kun annettavat oikeudet ovat lähellä toisiaan

Mikäli personoidut roolit ovat lähellä toisiaan, ja ne eroavat esimerkiksi vaikkapa vain dimensioiden suhteen, voi olla järkevää kopioida rooli ja muokata sen jälkeen tehtyä kopiota.

Roles -listauksessa on roolien nimen perässä copy -painike, jolla kyseisen roolin voi kopioida.

[![](

Kopiota luotaessa roolille syntyy nimeksi alkuperäisen roolin nimi siten, että perässä lukee (copy). Roolille voidaan jo tässä kohdin antaa muu haluttu nimi. Roolien nimiä voi myös muuttaa jälkikäteen roolin nimen perässä olevan edit -painikkeen kautta



artikkelin osoite on https://intercom.help/finazilla/fi/articles/4318702-roolien-kautta-maaritellaan-yritystasoisen-kayttajan-kayttooikeudet-finazillassa

