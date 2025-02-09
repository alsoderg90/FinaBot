## Raporttimalli

Olemme käsitelleet operatiivisen datan artikkeleissamme sitä, kuinka myyntiä pystytään raportoimaan. Ohje myyntien raportointiin löytyy [tästä.]( 

Tässä artikkelissa otamme myyntien raportoimiseen lisäkulman siitä näkökulmasta, että myyntejä halutaan raportoida 10 suurimman asiakkaan osalta. Myynnistä halutaan siis raportoida Top 10 asiakkaat.

Tämän artikkelin ymmärtämistä helpottaa, jos käyttäjä tietää mitä operatiivinen data on ja osaa raportoida sitä.

# Raporttimalli

Operatiivisen datan raportoiminen edellyttää aina raporttimallia, joka on tehty operatiivisen datan raportoimiseen. Operatiivisia raporttimalleja olemme kuvanneet tarkemmin artikkelissamme ["Operatiivisen raporttimallin luominen silloin kun raportoitava data on 100% operatiivista dataa".]( 

Yksinkertaisimmillaan operatiivista myyntiä voidaan raportoida vaikkapa oheisella raporttimallilla. Kyseinen esimerkki on tehty yritykselle, jolla on Procountor. Operative data group on siis esimerkiksi Netvisor ja Lemonsoft -asiakkailla eri kuin alla olevassa esimerkissä.

[![](

# Raportin luominen

Raportoinnin puolella oleellista on valittu operatiivisen datan raportointiin tarkoitettu raporttimalli. Tämän lisäksi tietolähteellä tulee valita vaihtoehto dimensio/column, jonka jälkeen pääsee valitsemaan nk. dimension presentation type -valintaa. Alasvetovalikosta löytyy useita vaihtoehtoja, kuten tämän esimerkin Top 10 -valinta.

Operative dimensions -kenttään kannattaa tämän lisäksi valita operatiivinen dimensio "customer" eli asiakas.

[![](

# Raportin pivotointi

Raportti aukeaa siten, että kullakin kuukaudella näkyy myyntien yhteissumma. Asiakas -dimensio ei tule automaattisesti näkyviin, vaan se tulee pivotoida raporttiin Fields -painikkeen takaa. Se, mihin customer dimension raportilla asettaa, on käyttäjän mieltymyksistä ja tarpeista kiinni. Asiakas dimension voi asettaa vaikkapa raportin riveille.

Asiakkaat tulevat raportille aakkosjärjestyksessä. Mikäli asiakkaat halutaan raporttiin suurimmasta pienimpään, voidaan ne filtteröidä arvon mukaan.

[![](

[![](

*Raporttiin tulee myös asiakas "others", jossa on mukana kaikki muut asiakkaat, paitsi yksittäisinä dimensionarvoina näkyvät asiakkaat.* 

[![](

*Tämän artikkelin ohjetta voi soveltaa myös esimerkiksi Top 10 ostojen raportointiin. Tällöin raporttimallille tulee valita ostojen tietovirta ja operatiivinen dimensio raportin tietolähteellä on supplier, eli toimittaja*



artikkelin osoite on https://intercom.help/finazilla/fi/articles/8582339-esimerkki-top-10-raportointi

