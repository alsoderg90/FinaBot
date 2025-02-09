## Esimerkki

Tässä artikkelissa esittelemme esimerkin avulla, kuinka collapse -ja expand painikkeita voidaan hyödyntää Finazillan raportoinnissa. Kyseiset painikkeet supistavat ja laajentavat raportin raporttipuuta, joten niiden avulla voidaan raporttia esimerkiksi tiivistää helposti ja nopeasti.

# Esimerkki

Luodaan tilikauden mittainen tuloslaskelma, jossa esitysasuna on kuukausittainen näkymä. Raportti aukeaa oheiseen ulkoasuun raporttilistasta avattaessa.

[![](

Alkuperäisessä aukeamisasussa tuloslaskemassa on ensimmäinen sarake (datasource 1), jossa on kunkin rivin yhteenlaskettu summa. Tämän jälkeen kuukaudet järjestyvät tilikauden ensimmäisestä kuukaudesta viimeiseen (koska raportti on muodostettu käyttämällä oletusvalintaa "accounting period" ja "current period").

Rivitasolla tarkasteltuna raportti aukeaa oletusarvoisesti tilitasolle eli esimerkiksi otsikkorivin "liikevaihto" alle aukeaa kaikki tilit, joista yrityksen liikevaihto muodostuu.

Raporttia voi olla kuitenkin miellekästä tarkastella joskus ns. otsikkotasolla, eikä esimerkiksi tilitasoisena. Tällöin on järkevää käyttää raportoinnista löytyvää "collapse" toimintoa.

[![](

# Raportin supistaminen collapse -toiminnolla

Kun raportin "supistaa" käyttämällä collapse -toimintoa, supistuu raportti siten, että kuukaudet poistuvat ja raporttiin jää ainoastaan yhteensä -sarake. Tämän lisäksi raportin raporttipuu supistuu näkymään, jossa yksittäiset tilit poistuvat ja raportti esitetään "otsikkotasoisena".

[![](

Jos raportille halutaan kuitenkin kuukausittainen näkymä, voidaan raporttia muokata klikkaamalla hiirellä datasource 1 sarakkeessa.

[![](

Tämän jälkeen raporttiin nousee kuukaudet mukaan, mutta raportin raporttipuu pysyy ns. supistettuna

[![](

Tämän jälkeen raporttipuuta pystyy avaamaan/supistamaan haluamalleen tasolle vasemman reunan otsikoita klikkaamalla. Kun raportti on muotoiltu haluttuun ulkoasuun, tulee muutokset muistaa tallentaa save -painikkeesta.

[![](

# Raportin laajentaminen expand -painikkeella

Expand -painikkeella vastaavasti raportti taasen aukeaa takaisin alkuperäiseen ulkoasuunsa eli tilitasoiseksi

[![](



artikkelin osoite on https://intercom.help/finazilla/fi/articles/5446890-esimerkki-raportin-muotoilu-collapse-painikkeella

