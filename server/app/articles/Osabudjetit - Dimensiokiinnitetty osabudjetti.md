## Dimensiokiinnitetty osabudjetti

Tässä artikkelissa kuvaamme tilannetta, missä käyttäjällä on luotuna osabudjetti, jossa on lukuja. Osabudjetin luvut on kohdistettu tietylle dimension arvolle (tai arvoille) tekemällä osabudjetista ns. dimensiokiinnitetty. Tämän jälkeen osabudjettia halutaan kopioida jollekin toiselle dimensionarvolle lukuineen.

# Dimensiokiinnitetty osabudjetti

Dimensiokiinnitetty osabudjetti tarkoittaa sitä, että kun osabudjetti on luotu, on sen kerrottu kuuluvan jollekin tietylle dimensionarvolle. Tämä tehdään kentässä "Target to dimension value".

Tällaisen osabudjetin luvut kohdistuvat aina automaattisesti kyseiselle dimensionarvolle.

[![](

## Dimensiokiinnitetyn osabudjetin kopioiminen

Kyseinen myyntibudjetti voidaan kopioida budjetin takana kohdassa sub budgets - aivan kuten muutkin osabudjetit kopioidaan.

Kopiointi tehdään siten, että lähdetään luomaan uuutta osabudjettia "new sub budget" painikkeen takaa. Tämän jälkeen valitaankin oikean reunan alasvetovalikosta, että mikä osabudjetti halutaan kopioida. Osabudjetille annetaan haluttu nimi kentässä name ja target to dimension value -kentässä voidaan kertoa, mille dimensionarvolle se kopioidaan. Copy selections -kohdassa valitaan, että mitä osabudjetista halutaan kopioida.

Move for months -valinnalla lukuja voidaan siirtää eteenpäin; eli jos esimerkiksi alkuperäinen osabudjetti on vuodella 2022, ja luvut halutaan siirtää vuodelle 2023, valitaan kenttään 12. Toimintoa on kuvattu yleisellä tasolla enemmän [täällä.](

[![](

# Havainnollistavat esimerkit

**Esimerkki 1:**

Osabudjetti on kohdistettu dimensionarvolle "hallinto". Osabudjetti kopioidaan ja kopio kohdistetaan dimensionarvolle "markkinointi". Kopioidun osabudjetin luvut siirtyvät dimensionarvolle "markkinointi" ja alkuperäisen osabudjetin luvut ovat edelleen dimensionarvolla "hallinto". Käyttäjällä on nyt kaksi erillistä osabudjettia.

**Esimerkki 2:**

Osabudjetissa on lukuja kahdella eri dimensionarvolla (hallinto + Jyväskylä). Osabudjetti kopioidaan ja kopio kohdistetaan yhdelle dimensionarvolle (Kuopio). Kopioidun osabudjetin kaikki luvut (hallinto + Jyväskylä yhteenlasketut) siirtyvät dimensionarvolle Kuopio ja alkuperäisen osabudjetin luvut ovat edelleen dimensionarvoilla hallinto + Jyväskylä.

**Esimerkki 3:**

Osabudjetissa on lukuja kahdella eri dimensionarvolla (hallinto + Jyväskylä). Osabudjetti kopioidaan ja kopiota ei kohdisteta mihinkään dimensionarvoon. Kopioidun osabudjetin kaikki luvut (hallinto + Jyväskylä yhteenlasketut) siirtyvät niille dimensionarvoille missä ne olivat, eli hallinto + Jyväskylä. Nämä kaksi osabudjettia ovat siten siis identtisiä.

**Esimerkki 4:** 

Osabudjetissa on lukuja kahdella eri dimensionarvolla (hallinto + Jyväskylä). Osabudjetti kopioidaan ja kopiota ei kohdisteta mihinkään dimensionarvoon. Lisäksi kopioitaessa käytetään valintaa "move for months" ja valitaan kenttään luku 12. Kopioidun osabudjetin kaikki luvut (hallinto + Jyväskylä yhteenlasketut) siirtyvät niille dimensionarvoille missä ne olivat, eli hallinto + Jyväskylä. Tämän lisäksi osabudjetin luvut siirtyvät 12 kuukautta eteenpäin (jos luvut olivat siis 1-12/2022, niin nyt ne ovat 1-12/2023).



artikkelin osoite on https://intercom.help/finazilla/fi/articles/6824401-dimensioille-budjetoidun-osabudjetin-kopiointi-datoineen

