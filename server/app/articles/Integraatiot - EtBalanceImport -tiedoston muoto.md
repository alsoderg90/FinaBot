## EtBalanceImport -tiedoston muoto

Olemme käsitelleet aihetta aikaisemmassa artikkelissamme "[Tietojen siirtyminen Finazillaan tiedostopohjaisella tuonnilla jos rajapintaa ei ole käytettävissä](" sekä "[Tietojen päivittäminen Finazillaan kesken päivän](". Aikaisemmat artikkelimme kuvaavat toimintoa yleisellä tasolla.

Tässä artikkelissa näytämme, minkälainen siirtotiedostosta tulee rakentaa. Ohje pätee asiakkaisiin, joiden lähdejärjestelmänä on ET Balance Import.

# EtBalanceImport -tiedoston muoto

Kun asiakkaalla on käytössä ns. ET Balance Import integraationa niin tämä tarkoittaa käytännössä sitä, että saldoaineisto muodostetaan lähdejärjestelmästä esimerkkitiedoston muotoon (csv). Tämän jälkeen integraatio siirtää tilisaldot Finazillaan Finazillan Dropbox-tiedonsiirtotyökalulla.

Alla on kuvattuna esimerkki siitä, minkälainen aineiston tulee olla, mikäli käytössä on dimensiot.

[![](

Mikäli aineistossa ei ole lainkaan dimensioita, muodostetaan aineisto muutoin samanlaiseksi kuin yllä olevassa esimerkissä, mutta sarakkeet E-J voi jättää kokonaan pois.

# Lisätietoja

[Finazillaan siirtyy tietoa joko valmiin rajapinnan kautta tai tiedostopohjaisella viennillä](

[Tietojen siirtyminen Finazillaan tiedostopohjaisella tuonnilla jos rajapintaa ei ole käytettävissä](



artikkelin osoite on https://intercom.help/finazilla/fi/articles/4601768-esimerkki-tiedostopohjainen-tositteiden-tuonti-etbalanceimport

