## Raportin jakaminen suoraan raporttilistalta

Raportteja voidaan jakaa Finazillassa usealla eri tavalla. Tässä artikkelissa kuvaamme kaikki erilaiset vaihtoehdot jakaa raportti toiselle Finazilla käyttäjälle. Tarkemmat työohjeet kuhunkin jakotapaan löytyvät varsinaisista työohjeista, joihin löytyy linkit artikkelin lopusta.

# Raportin jakaminen suoraan raporttilistalta

Yksittäisen raportin voi jakaa Reports -valikosta kyseisen raportin perässä olevalla "share" -toiminnolla. Jotta raportin voi jakaa, tulee jaettavan raportin olla jakajan itsensä laatima ja omistama.

Raportin voi jakaa kerralla useammallekin käyttäjälle. Jos raportti jaetaan rajatulle käyttäjäroolille, tulee huomioida onko käyttäjällä oikeus kaikkeen raportin sisältämään dataan.

# Raportin jakaminen kansioimalla raportti

Raportteja voidaan jakaa luomalla kansioita ja raahaamalla raportteja kansioihin. Kansiot luodaan varsinaisessa raporttilistauksessa kohdassa "new folder". Mikäli raportille kiinnitetään Customer -tasoinen tagi, näkyy raportti kaikille Customer -tasoisille käyttäjille. Kansio näkyy, vaikka yritystä ei olisi valittu.

Company -tasoisen kansion käyttäminen raportin jakamisessa on hieman moniulotteisempi. Company -tasoinen kansio jakaa raportin kaikille Customer ja CompanySuperUser -tasoisille käyttäjille. kansio näkyy, vaikka yritystä ei olisi valittu.

CompanyUser -käyttäjälle (eli käyttäjälle, jolle on kiinnitetty jokin rajoitettu rooli) raportti pitää jakaa antamalla käyttäjäroolille oikeus kyseiseen kansioon. Tämä tehdään "roles" toiminnoissa. Luonnollisesti myös muut raportin jakamistavat ovat mahdollisia. Roolin oikeudet raportin sisältöön tulee kuitenkin huomioida aina, kun raportteja jaetaan rajatulle roolille.

User -tasoinen kansio ei jaa raporttia kenellekään; sen merkitys on enemmänkin omien henkilökohtaisten raporttien organisointi haluttuun järjestykseen eri kansioiden alle.

## Company -tasoinen käyttäjä haluaa jakaa raportin Customer -tasoiselle käyttäjälle

Normaali share -painikkeen kautta tehtävä jako ei ole mahdollinen, mikäli kyseessä on tilanne, missä company -tasoinen käyttäjä haluaisi jakaa raportteja pääkäyttäjälle. Share -painikkeen kautta näkyviin tulee vain muut company -tasoiset käyttäjät.

Company -tasoinen käyttäjä voi jakaa raportin pääkäyttäjälle luomalla company -tasoisen tagin. Customer -tasoinen pääkäyttäjä näkee companytagit ja pääsee sitä kautta näkemään raportit.

# Raportin jakaminen Dashboardin kautta

Raportteja voidaan jakaa myös Dashboard -näkymän kautta. Tällöin tulee huomioida, että käyttäjälle tulee jakaa kyseinen raportti "reports" valikon kautta sekä jakaa Dashboard, jolla raportti on. Jos Dashboardilla on useita raportteja ja ne kaikki halutaan jakaa, tulee jako kaikille raporteille tehdä yksitellen.

# Lisätietoja

[Raportin jakaminen toiselle Finazilla käyttäjälle](

[Raporttien kansioiminen tagien avulla kansioi raportin sekä mahdollistaa raportin jakamisen](

[Dashboardin jakaminen toiselle käyttäjälle](



artikkelin osoite on https://intercom.help/finazilla/fi/articles/4942313-eri-tavat-jakaa-raportteja-toiselle-kayttajalle

