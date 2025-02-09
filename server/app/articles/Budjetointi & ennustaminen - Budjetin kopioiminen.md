## Budjetin kopioiminen

Olemme kertoneet artikkelissamme ["budjetin kopioiminen"]( kuinka budjettia voidaan kopioida ja miten valitaan, mitä dataa kopioitavaan versioon sisällytetään. Tässä artikkelissa kuvaamme nimenomaan tilannetta, missä budjetti halutaan kopioida siten, että kopiossa on eri määrä dimensioita käytössä, kuin alkuperäisessä budjetissa on.'

# Budjetin kopioiminen

Vanhan olemassa olevan budjetin kopioiminen tapahtuu "Budgets" näkymässä. Kopio kannattaa tehdä sellaisesta budjetista, missä budjetin *rakenne* osabudjetteineen on mahdollisimman samanlainen kuin uuden haluttavan budjetin rakenne.

Kopio otetaan budjetin nimen perässä olevan "copy" painikkeen kautta, jolloin käyttäjälle aukeaa syöttöikkuna. Syöttöikkunassa budjetille annetaan nimi sekä valitaan, mitä kaikkea halutaan kopioida.

[![](

# Dimensioiden valitseminen budjettikopioon

Yllä olevassa esimerkissä budjetilla on ollut käytössä kolme dimensiota; asiakasryhmä, maa/alue ja tapahtumat. Käyttäjä voi vapaasti valita mitä dimensioita kopioon halutaan sisällyttää. Kopion ei siis ole pakko sisältää kaikkia samoja dimensioita.

Kopiota ottaessa voidaan valita, että kopioon halutaan vain dimensiot asiakasryhmä ja maa/alue. Ruksimalla dimensio "tapahtuma" pois valinnoista, ei kopioon tule lainkaan dimensiota "tapahtuma".

## Budjettikopio, jossa on enemmän dimensioita kuin alkuperäisessä budjetissa

mikäli kopiossa on enemmän dimensioita kuin kopioidussa, ei tämä aiheuta mitään huomioitavaa. Budjetille tuodaan yksi ylimääräinen dimensio näkyviin ja käyttäjä voi budjetoida sinne haluamansa luvut.

## Budjettikopio, jossa on vähemmän dimensioita kuin alkuperäisessä budjetissa

Mikäli kopiossa on vähemmän dimensioita, tulee huomioida, että mikäli yritetään poistaa dimensiota, joka on käytössä joko lisäkohdistuksessa tai vyörytyssäännössä, ei dimensiota voi ottaa pois käytöstä. Tällaisen dimension poisjättäminen ei ole siis mahdollista.

Mikäli budjetilta otetaan pois sellainen dimensio, jota on käytetty matriisikohdistuksessa, niin budjetilla tehdään uudelleenkohdistus jäljelle jääneelle dimensiolle. Esimerkiksi jos alkuperäisessä budjetissa olisi kohdistettu lukuja dimensiolle tapahtuma+ asiakasryhmä, ja kopioon ei sisällytettäisi enää tapahtumaa, kohdistettaisiin tällaiset luvut dimensiolle asiakasryhmä.

Dimensiokiinnitetyissä budjeteissa dimensiokiinnitys poistetaan, mikäli kyseinen dimensio ei ole enää käytössä uudessa kopioidussa budjetissa.



artikkelin osoite on https://intercom.help/finazilla/fi/articles/9239827-budjetin-kopioiminen-siten-etta-kopiossa-on-eri-maara-dimensioita-kaytossa

