## Lukituspäivä

[![](

*Versiopäivityksessä 18.3.2022 tuotu parannus lukituspäivään. Tuotu parannus koskettaa vain asiakkuuksia, joissa on useampi kuin yksi yritys.* 

# Lukituspäivä

Perinteinen lukituspäivä löytyy kunkin asiakkuuden yrityksen alta valikosta company ja accounting periods. Nyt tuotu customer -tasoinen lukituspäivä löytyy vastaavasti valikosta customer ja kohdasta settings.

[![](

# Asiakastasoinen lukituspäivä

Käyttämällä asiakkuustasoista lukitusta, mahdollistetaan se, että jokaiselle asiakkuuden yritykselle asetetaan sama lukituspäivä - eikä lukituspäivää täydy päivittää kunkin yrityksen taakse yksitellen.

Mikäli kaikilla asiakkuuden yrityksillä ei haluta käyttää samaa lukituspäivää, voidaan toiminnon avulla määritellä myös, että vaikkapa asiakkuuden viidellä yrityksellä on käytössä asiakkuustasoinen lukituspäivä ja yhdellä yrityksistä käytetään tästä poikkeavaa lukituspäivää käyttämällä company -valikon accounting periods kohdasta löytyvää lukituspäivää.

## Havainnollistavat esimerkit

Havainnollistamme lukituspäivän käyttömahdollisuuksia alla muutamalla esimerkillä.

#### **Esimerkki 1: asiakkuuden kaikissa yrityksissä halutaan käyttää samaa lukituspäivää**

Helpoin tapa käyttää toimintoa kuvatulla tavalla on käydä ensin varmistamassa, että millään asiakkuuden yrityksellä ei ole mitään lukituspäivää valikossa company ja kohdassa accounting periods. Lock date -kentän tulee olla tyhjä.

Tämän jälkeen asiakkuustasolle voidaan asettaa customer lock date, jolloin sama asetettu lukituspäivä näkyy jokaisella asiakkuuden yrityksellä. Jos esimerkiksi lukituspäiväksi asetetaan 28.2.2022, on jokaisella yrityksellä lukituspäivänä 28.2.2022.

Jos asiakkuustasolta käydään poistamassa asetettu lukitus (esimerkiksi yllä mainittu 28.2.2022), poistuu lukituspäivä jokaisesta asiakkuuden yrityksestäkin.

#### **Esimerkki 2: asiakkuuden osassa yrityksistä halutaan käyttää asiakaskohtaista lukituspäivää ja osassa yrityskohtaista lukituspäivää**

Tässä käyttötavassa käydään ensin varmistamassa, että niillä yrityksillä joilla halutaan käyttää asiakaskohtaista lukitusta, ei ole mitään lukituspäivää asetettuna company accounting periods -valikossa. Vastaavasti taas niillä yrityksillä on, joissa halutaan käyttää yrityskohtaista lukitusta.

Tämän jälkeen asiakkuustasolle voidaan asettaa customer lock date, jolloin sama asetettu lukituspäivä näkyy jokaisella asiakkuuden yrityksellä, jolla ei ollut yrityskohtaista lukitusta.

Jos asiakkuustasolta käydään poistamassa asetettu lukitus, poistuu lukituspäivä jokaisesta asiakkuuden yrityksestäkin. Lukitus jää vain niille yrityksille, joilla se on asetettu yrityskohtaisesti.

Toiminto mahdollistaa siis sen, että kun asiakkuudessa on kolme yritystä, joista yhdelle näistä on asetettu lukituspäivä yrityskohtaisesti päivään 31.1.2024 ja muille lukitus asetetaan asiakaskohtaista lukituspäivää käyttämällä hetkeen 28.2.2024. Näin toimien jos yrityskohtaista lukituspäivää muutetaan, heijastuu muutos vain kahteen yritykseen.

#### **Esimerkki 3: asiakkuuden osassa yrityksiä halutaan käyttää asiakaskohtaista lukituspäivää ja osassa ei lainkaan mitään lukituspäivää**

Oheinen skenaario ei ole mahdollinen. Mikäli osassa yrityksissä ei haluta käyttää lainkaan lukituspäivää, pitää lukituspäiviä hallinnoida pelkästään yritystasoisilla lukituspäivillä.

# **Mitä hyötyä lukituspäivästä on?**

Artikkeli ["Lukituspäivän käyttäminen mahdollistaa raportoinnin siihen saakka, mihin kirjanpito on valmistunut"]( kuvaa sitä, mitä hyötyjä lukituspäivällä voidaan saada mm. Finazillan raportoinnin puolella.

Hyötyjä lukituspäivän käytöstä saadaan myös budjetoinnin puolella perinteisessä budget -tyyppisessä budjetissa, sekä forecast -tyyppisessä ennustebudjetissa. Aiheesta löytyy lisätietoja mm. artikkeleistamme ["Budjetin ja osabudjetin lukitseminen](", ["Ennustebudjetti"]( sekä ["Ennustebudjetin ja budjetin eroavaisuudet"](

[![](

*Lukituspäivä voidaan asettaa vain aktiiviselle tilikaudelle.*



artikkelin osoite on https://intercom.help/finazilla/fi/articles/6058321-customer-tasoinen-lukituspaiva

