## Raporttimallin luominen

Finazillan raportointi mahdollistaa operatiivisen datan tuomisen Finazillaan ja sen rikastamisen kirjanpidon datalla tai Finazillan laskennalla. Hyvä ja yksinkertainen esimerkki tästä voisi olla vaikkapa yrityksen työtuntien suhteuttaminen myyntilaskutukseen.

Tämä artikkeli on edistyneemmille käyttäjille, joten oletusarvona on, että käyttäjä osaa jo luoda perinteisen kirjanpidon raporttimallin. Lisätietoa raporttimallien laatimiseen löytyy artikkelistamme [täältä.]( Käyttäjän tulee tämän lisäksi hallita siirtotiedoston laatiminen operatiivisen datan tuomiseen. Ohjeet oikeanlaisen siirtotiedoston luomiseen löydät artikkelistamme [tästä.]( 

# Raporttimallin luominen

Kun yllämainitut toiminnot ovat tuttuja, voi käyttäjä luoda raporttimalleja, joissa yhdistellään operatiivista dataa ja kirjanpidon dataa.

Operatiivisen datan toimintalogiikka vastaa sitä, miten balance rivit haetaan raporttimallille; näin ollen raporttimallia tehdessä ei tarvitse/kuulu tietää yhtään yrityksen dimensio rakenteesta, vaan siinä valitaan mitä kokonaisuuksia raportille halutaan. Esimerkiksi raportille halutaan"myyntitilit" tai "tehdyt työtunnit".

Raporttimallin row type -valintana on "Operative data (new)" ja "Name" kenttään täytettään otsikko, minkä halutaan näkyvän raportilla. Operative data group -valikosta aukeaa kaikki kyseisen yrityksen operatiiviset datat mitä on tuotu Finazillaan sisään ja näistä valitaan haluttu. Operative Item Data Type -kentässä määritellään raportoidaanko Amount vai Quantity määrettä.

Huomaa, että jos siirtotiedostossa esimerkiksi työtunnit ovat olleet Quantityn alla, tulee myös tässä valita Quantity; muutoin tunnit eivät nouse raportille.

[![](

.

Raporttimallia voi käyttää luomaan sekä "Myyntiä per työtunti ravintolassa", että "Myyntiä per työtunti työntekijällä" tai jopa "Myyntiä per työtunti" konsernin yrityksissä, joista kumpikin tekee täysin eri tuotteita.

Raporttimallin näkökulmasta operatiivinen data group käyttäytyy siis aivan kuten kirjanpidon tili. Näin ollen käyttäjä osaa luoda operatiivisen raportin, jos hän osaa luoda kirjanpidon raportin.

# Esimerkki

Raporttimallin raporttipuu silloin kun halutaan raportoida myyntiä per tehdyt työtunnit

[![](

Porautuminen kirjanpidon datan, eli myyntirivin, näkymään

[![](

Operatiivinen tietolähde eli tunnit aukaistuna:

[![](

Kaavarivi aukaistuna:   
​

[![](

# Raportointi luodulla raporttimallilla

Luodulla raporttimallilla voidaan tämän jälkeen raportoida "Reports" valikon kautta aivan samoin kuin millä tahansa muullakin raporttimallilla.

[![](

*Kun halutaan raportoida esimerkiksi siten, että poimitaan kirjanpidon datasta vain jokin tietty dimensio, tehdään se laittamalla kyseinen dimensio kenttään "Dimensions" raportin määrityksissä Reports -valikossa. Tällöin raporttiin nousee kirjanpidon datasta vain ko. dimension data ja operatiivisesta datasta kaikki.* 

*Jos halutaan rajata myös operatiivista dataa, niin laitetaan dimensio kenttään "Operative dimensions" haluttu dimensio raportin määrityksissä Reports -valikossa. Tällöin raporttiin nousee operatiivinen data ko. rajauksin (+mahdollinen aikaisemmin laitettu kirjanpidon datan osuus).*

*Edellä mainituista voidaan tehdä haluttuja yhdistelmiä vapaasti.*   
​



artikkelin osoite on https://intercom.help/finazilla/fi/articles/4279975-operatiivista-dataa-ja-kirjanpidon-dataa-yhdistavan-raporttimallin-luominen-finazillaan

