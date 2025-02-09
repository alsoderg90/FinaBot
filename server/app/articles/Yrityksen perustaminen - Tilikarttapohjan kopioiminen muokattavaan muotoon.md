## Tilikarttapohjan kopioiminen muokattavaan muotoon

Lähtökohtaisesti uusien asiakkaiden avaukset hoitaa Finazilla, jolloin asiakkaille ei tule vastaan tarvetta luoda uusia tilikarttoja tai tehdä tilikartan muokkauksia. **Tämä ohje on tarkoitettu siis vain niille asiakkaille, joilla on tarve muokata tilikarttaa.** 

Olemme kuvanneet artikkelissamme ["yrityksen tilikartan määrittäminen"]( kuinka luotavalle yritykselle kiinnitetään jokin Finazillan valmiista tilikartoista. Tyypillisin valmis tilikartta on liikekirjurin tilikartta. Tässä artikkelissa kerromme, miten tulee toimia, mikäli tilikartta ei noudattele mitään valmista mallia, vaan sitä tulee muokata.

# **Tilikarttapohjan kopioiminen muokattavaan muotoon**

Tilikartan rakentamisessa ja muokkaamisessa kannattaa lähteä liikkeelle siitä, että katsoo, mikä valmis tilikarttapohja olisi lähimpänä omaa tilikarttaa. Tilikarttapohjasta voi ottaa kopion, ja muokata kopiota sen jälkeen haluttuun suuntaan. Näin rakentamista ei tarvitse lähteä tekemään tyhjästä.

[![](

## Tilikartan rakentaminen

Tilikarttapohjan rakentamisen logiikka vastaa raporttimallien logiikkaa monelta osin. Merkittävin ero tilikarttapohjassa on raporttimalliin nähden se, että sama tili tai tiliväli ei voi esiintyä useassa paikassa. Jos tilivälejä täytyy muuttaa, vaatii se usein sen, että ensin käydään korjaamassa tilikarttapohjassa olevan vanha väärä tiliväli oikeaksi, ennen kuin voidaan lisätä uusi tiliväli toisaalle.

Tilikarttapohjaan voi tehdä kaikenlaisia muutoksia; olemassa olevien otsikoiden nimiä voidaan vaihtaa edit-painikkeen kautta, uusia otsikoita voidaan lisätä haluttuihin väleihin new group -painikkeen kautta ja uusia alisteisia lapsirivejä voidaan luoda new child row -painikkeella.

Myös olemassa olevia tilivälejä voidaan korjata editoimalla ja uusia tilivälejä voidaan luoda new -painikkein. Aina kun tilivälejä lisätään, tulee muistaa, että tileille pitää tehdä oikea debit/credit määrittely kohdassa "row factor" (esimerkiksi myyntitilit ovat tyypiltään credit). Finazilla ottaa rivin row factorin oletusarvoisesti luotavan rivin parent -riviltä.

[![](

Sen jälkeen kun tilikarttapohja on muokattu halutunlaiseksi, kiinnitetään se yrityksen tilikartaksi.

# **Tilikartan määrittely**

Tilikartan määrittäminen tehdään Company -valikon Account Schemes toiminnoissa valitsemalla oikeasta yläkulmasta "New Account Scheme". Tilikartta nimetään esimerkiksi yrityksen nimellä.

Create Account Scheme -toiminnolla luotu tilikartta ilmestyy tilikartta -toiminnon alle.

## **Täsmäytystilien määritteleminen**

Seuraavaksi tilikartalle pitää määritellä ns. täsmäytystilit klikkaamalla tilikartan nimeä.

Tämän jälkeen klikataan oikeasta yläkulmasta Settings –painiketta, jolloin täsmäytystilit tulevat näkyviin. Tämän jälkeen valitaan alasvetovalikoista oikeat tilit; myös hakutoimintoa voi käyttää.

```
Määriteltävät täsmäytystilit ovat:
```
```
• Tilikauden voitto, eli ”Profit” –tili (tase)
```
```
• Pankkitili eli ”Reconciliation” (jos käytössä on useita, valitaan yksi)
```
```
• Edellisten tilikausien voitot, eli ”Retained Earnings”–tili
```
```
• Osingonjakotili, eli ”Profit Distribution” (mikäli tiliä ei ole   
tilikartassa, tulee tili perustaa Company -valikon Accounts –toiminnoissa).
```
[![](

# **Tilin lisääminen manuaalisesti**

Mikäli joku yllämainituista tileistä puuttuu yhtiön tilikartasta on se lisättävä manuaalisesti. Tällöin mennään takaisin Company -valikon Accounts –toimintoon ja valitaan vaihtoehto ”New Account” ja lisätään tili. Tämän jälkeen palataan Account Scheme –toimintoon ja nyt luodun tilin pitäisi näkyä listalla.

# **Tilikauden tuloksen käsitteleminen**

Tilikauden tuloksen kirjaamisen logiikka vaihtelee myös eri järjestelmien välillä ja sen vuoksi on tarpeen toisinaan luoda myös tilikauden voitolle uusi tili (esim. Netvisorissa tilikauden voitot ja tappiot on ohjattu taseessa eri tileille. Tällöin lisätään tili ”2370 Tilikauden tulos Finazilla” ja valitaan Setting –osiossa Profit -tiliksi tämä tili. Tämän jälkeen Finazilla laskee tuloskelman kirjaukset yhteen ja lisää sen mukaisen voiton/tappion taseeseen tälle tilille.

[![](

*Lopuksi on hyvä tarkistaa, että sivun alalaidassa ”Other” –kohdan alla ei ole listattuna yhtään tiliä. Mikäli tilejä näkyy Other –kohdassa, niin kysymys on siitä, että jokin tili ei numeronsa perusteella osu tilikarttaan määriteltyihin tulos- ja tase-eriin. Tällöin tilikartan tiliohjaukset tulee tarkistaa.*

[![](

*Tilien row factor määrittelyä voi aina "luntata" valmiilta system tasoiselta tilikarttapohjalta (account scheme template), mikäli on epävarma tilin tyypistä.* 



artikkelin osoite on https://intercom.help/finazilla/fi/articles/5471770-yrityksen-tilikartan-muokkaaminen

