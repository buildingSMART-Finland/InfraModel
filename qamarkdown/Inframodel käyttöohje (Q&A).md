# Inframodel käyttöohje (Q&A)

## Johdanto

Inframodel (IM) on suomalaisten kehittämä, kansainväliseen LandXML-standardiin (LandXML versio 1.2) perustuva avoin formaatti infratietojen siirtoon. Inframodel-määrittelytyötä on tehty yhdessä alan toimijoiden kanssa buildingSMART Finlandin (bSF) Infran standardointiryhmässä. 

Inframodel tiedonsiirtoa hyödynnetään mm. suunnitteluohjelmissa sekä mittaus-, koneohjaus- ja tarkastussovelluksissa. Yhtenäinen toimintatapa ja avoin tietomallipohjainen formaatti on tehostanut suunnittelua ja rakentamista.

Inframodelin ajantasainen dokumentaatio ja skeema löytyy osoitteesta \<linkki>

Inframodel skeema ja dokumentaatio sisältävät tietoa sovelluskehittäjille ja käyttöohje tukee loppukäyttäjiä.

Inframodel-tiedonsiirtoformaatti tukeutuu Yleisiin inframallivaatimuksiin ja InfraBIM-nimikkeistöjärjstelmään.  

"Pyhä kolminaisuus"

{{figure holytrinity}}

- Yleiset inframallivaatimukset *(ohje ja vaatimus: mitä ja miten mallinnetaan, laadunvarmistus, lopputuotteen määrittely, mallinnusprosessi jne.)*
- InfraBIM nimikkeistö *(miten nimetään ja luokitellaan)*
- Inframodel tiedonsiirto *(miten tieto siirretään)*

Inframodel tiedonsiirron vähimmäisvaatimukset on kuvattu hankevaiheittain Yleisten inframallivaatimusten liitteessä: Luovutusaineiston tiedonsiirron vaatimukset.

**Inframodel 4- tiedonsiirron ominaisuuksia ovat**

*tähän taulukko/lista siirrettävistä asioista ja ominaisuuksista*

- maaperämalli ominaisuustietoineen *(esim. maalajikerrosominaisuudet)*
- pintarakenteet ominaisuustietoineen *(esim materiaaliominaisuudet, aluerajaukset)*
- rakennekerrokset ominaisuustietoineen *(esim. materiaaliominaisuudet)*
- alueet ominaisuustietoineen
- turva- ja varoitusalueet ominaisuustietoineen
- Verkostolajit (jätevesi, hulevesi, vesijohdot, kaukolämpö, kaasu, jäte, kaapelit) ominaisuustietoineen *(esim. materiaali, halkaisija)*
- jalustat ominaisuustietoineen
- liikennemerkit ominaisuustietoineen
- johto- ja kaapelireittien tilavaraukset
- kaiteet ja aidat ominaisuustietoineen
- toteumatiedot ominaisuustietoineen
- pilaristabilointi ominaisuustietoineen
- vapaat ominaisuustiedot *(esim. omistajatieto, lisätieto, tarkennus tms. jollekin objektille, kuten viivalle, pisteelle tai putkiverkolle)*

## Ohjeen sisältö

Tämä ohje täydentää kohdassa 1 mainittua dokumentaatiota ja ohje on kohdennettu loppukäyttäjille. 

Ohjeen jäsentely noudattaa Inframodel dokumentaation sisällysluetteloa. Ohjeen ulkoasu ja sisältö koostuu ohjeista sekä Q&A artikkeleista.

Ohjeistus on jatkuvasti päivittyvä ja täydentyvä kysymyksiin ja vastauksiin perustuva jatkuvasti kehittyvä dokumentti. 

Ohjeistukseen voi itse vaikuttaa antamalla palautetta tai kysymällä buildingSMART Finlandin palautekanavien kautta tai tekemällä suoraan tiketin kehitysympäristöön \<linkki>. Saatu palaute tai tarvittavat lisäykset / tarkennukset täydennetään käyttöohjeeseen ylläpitoprosessin mukaisesti.

## Käyttöohje + Q&A

### Yleistä

Tiedonsiirrossa tulee noudattaa seuraavia yleisiä periaatteita:
- Tiedostojen ja suunnitelman eri osien nimeäminen noudattaa hankkeen yleistä nimeämiskäytäntöä
- Tiedostojen ja suunnitelman osien nimet ovat kuvaavia, mutta lyhyitä ja ytimekkäitä
- Kaikki saman hankkeen tiedot ovat samassa koordinaatti- ja korkeusjärjestelmässä
- Siirrettävistä tiedoista laaditaan hankkeelle aineistoluettelo ja aineistoselostus YIV ohjeiden mukaisesti

#### Aineiston jakaminen osiin

Hankkeissa tulee noudattaa selkeää jaottelua loogisiin osakokonaisuuksiin tai sopiviin tietomääriin. Hankkeissa on suositeltua noudattaa esim. seuraavanlaista jakoa:

- Maastomalli
- Maaperämallin pinnat
- Väyläkohtainen: geometriat, rakennekerrokset
- Vesihuolto / kuivatus kokonaisuutena tai verkostolajeittain
- Varusteet ja laitteet kokonaisuutena tai tekniikkalajeittain

Näiden lisäksi voi tulla tarpeeseen jakaa aineistoa myös paaluväleittäin selkeyttämään suunnittelurajoja tai mallinnusositusta. Vaikka tietomalli säsältää tiedon aineiston käyttötarkoituksesta, nimeämisessä olisi hyvä muistaa käyttää loogisia jaotteluita. Aineiston jakamisesta sopiviin osiin on hyvä sopia ennen hankkeen alkua, koska hankevaihe tai -muoto vaikuttaa myös aineiston jakamisen tarpeisiin. Esim. varhaisen suunnitteluvaiheen aineistoa voi olla helpompi jakaa isompina kokonaisuuksina, jopa yhtenä projektitietona.

{{figure kuva tiedostojaottelusta}}

*Kuva. Esimerkki aineistojaottelusta*

Käytännössä tiedonsiirron tarpeet ovat monenlaisia ja kokonaisuudet on sovittava hankkeen alussa selkeästi. Esimerkiksi kun suunnittelija toimittaa malleja koneohjaukseen, voidaan toimia väylärakenteiden toteutusmalliohjeen mukaisesti (Väylärakenteen toteutusmallin vaatimukset ja -ohjeet) Tai kun maastomallin eri mittausaineistot (likimalli, tarkka maastomalli, täydennysmittaukset) halutaan selkeästi erottaa omina tiedostoina toisistaan.

Aineiston luomisessa, dokumentoinnissa, laadunvarmistuksessa, objekti- ja tiedostonimeämisessä sekä kansioinnissa noudatetaan yleisiä inframallivaatimuksia \<linkki>

#### Q&A

### Headers
Linkki dokumentaatioon {{refsec Headers}}


#### Codings
Linkki dokumentaatioon {{refsec Codings}}

##### Lajiluokitukset ja nimikkeistöt
Inframodel tiedonsiirrossa aineiston laatimisessa käytetty luokittelu ja nimikkeistö esitetään Codings elementillä.

Yleisesesti koodaukseen on sovittu seuraavat arvot ja käyttötarkoitus:

Lähtötietoaineisto: maastomallin ja maaperämallin kohteet
- **\<terrainCoding>** = Infra*
Lähtötietoaineisto: maastomallin ja maaperämallin pinnat
- **\<surfaceCoding>** = Infra*
Suunniteltujen kohteiden (pinnat, alueet, pisteet, verkostot jne.) luokitus
- **\<infraCoding>** = InfraBIM**

\* *Tie ja ratahankkeiden maastotiedot, mittausohje (liikennevirasto 18/2017), koodiluettelo*

\** *InfraBIM-nimikkeistö*

Lisäksi on mahdollista sisällyttää yksi tai useampi muu tarkentava koodaus. Esimerkiksi ohjelmiston oma lajiluokitus, organisaation oma luokitus, vesilaitoksen luokitus jne.

- \<proprietaryCoding> = käyttäjän asettama arvo***
    - Lähdejärjestelmän lajiluokitus (vapaaehtoinen)
        - esim. \<Proprietary label = "proprietaryInfraCoding" value="Tekla"\>

\*** *Suositellaan käytettäväksi tarvittaessa lisäinformaationa esimerkiksi silloin, kun em. luokitukset eivät ole riittäviä kyseisessä kohteessa. Tämän soveltamisesta pitää sopia erikseen hankekohtaisesti.*

#### Q&A

### Base data
Linkki dokumentaatioon {{refsec Base data}}

#### Lähtötietoaineisto ja maaperämallit

Maastomalli/kartoitusaineistot jaetaan eri ryhmiin tai tiedostoihin (Surface) sekä alkuperän mukaisesti, esim. ilmakuvilta mitattu, laserkeilattu, maastossa mitattu. Lähtötietoaineiston tarkkuusvaatimuksia voivat olla esim. pintamallin yhtenäinen kolmiointi ja pisteiden tai viivojen noudattaminen maastomittausohjetta.

Kalliopinta-aineisto jaetaan avokalliopisteisiin ja tulkittuihin pisteisiin. Erottelu tehdään tulkintapisteiden luokittelulla. Lisäksi tulkintapisteet voidaan projektikohtaisesti sopia jaoteltavan tarkemmin: varmistettu porakoneella tai koekuopasta, tulkinta kairauksen kohdalla, tulkinta maatutkaluotauksesta, muu tulkinta.

Maakerrosrajapinnat tms. maaperämallin pinnat tulostetaan joko kaikki samaan tiedostoon omina pintoina tai erikseen kukin pinta omaan tiedostoon.

{{figure maalajipinnat}}

Lähtitietoaineistot sisältävät ko. pintojen ns. lähtiedot eli pisteet ja viivat. Näistä muodostettuja kolmiopintoja voidaan siirtää omina tiedostoinaan, jos tiedoston koko muuten kasvaa liian isoksi.

Maaperämallin pintojen lajikoodausta on tarkennettu InfraBIM-nimikkeistössä. Suosituksen mukaisesti maaperämallin tulkinta pitää luokitella tulkintatarkkuuden mukaan ja luokituksesta on tehty valmiit arvojoukot eli luettelo sallituista tietoarvoista.

#### Q&A

### Route planning
Linkki dokumentaatioon {{refsec Route planning}}

#### Väylätiedot
Inframodel-tiedonsiirrossa väylällä on yksi jatkuva mittalinja ja tasaus. Tien mittalinjan InfraBIM-koodi tulee olla nimikkeistön mukaisesti (tie= 101 tai rata=111). Ratamallissa kilometripaalutus liitetään mittaraiteeseen. Muut geometrialinjat ja taiteviivat sekä pinnat nimetään InfraBIM-luokituksen mukaisesti. Taiteviivamallin viivoilla tulee olla väyläkohtainen yksilöllinen nimi (@name).

Aineistojen nimeämisessä noudatetaan Yleisten inframallivaatimusten sekä InfraBIM-nimikkeistön mukaisia numerointi- ja nimeämiskäytäntöjä. Aineistossa siirretään mallin objekteja sekä niihin liitettyä tietoa. Objektit voivat olla esim. pisteitä, viivoja, geometrioita sekä kolmiointeja. Kolmioinnin vaatimuksena on käyttää kolmioverkkoa, jonka *sourcedata* osiosta löytyy myös BreakLine-tieto (kolmioinnin laskentaa ohjaavat taiteviivat).

{{figure esimerkkikuva}}

*Kuva. Inframodel osamalleja voi yhdistää samaan näkymään eri työkaluilla.*

Aineistossa siirretään mallin objekteja sekä niihin liitettyä tietoa. Objektit voivat olla esim. pisteitä, viivoja, alueita, geometrioita sekä kolmiointeja. 

#### Q&A

### Roads and street
Linkki dokumentaatioon {{refsec Roads and street}}

#### Q&A

### Railways
Linkki dokumentaatioon {{refsec Railways}}

#### Q&A

### Waterways
Linkki dokumentaatioon {{refsec Waterways}}

#### Q&A

### Areas
Linkki dokumentaatioon {{refsec Areas}}

#### Q&A

### Water supply and sewerage
Linkki dokumentaatioon {{refsec Water supply and sewerage}}

#### Kuivatus

Vesihuoltoverkostot siirretään koko hankkeen kattavana tiedostona. Suurissa hankkeissa tiedostot voidaan jakaa esim. suunnitteluosuuksiin tai verkostolajeittain.

Kaivoilla ja laitteilla tulee olla koko aineiston kattava yksilöllinen nimi (@name). Vaatimuksena on myös sisällyttää putken korkeustaso uloskirjoitukseen.

#### Verkostolajit: Kaukolämpö, kaukokylmä, kaasu, jäte yms.

Inframodel sisältää omat määritteet verkostolajeina jäte, hule, vesi, kaukolämpö, kaukojäähdytys, kaasu, jätteen putkikeräys sekä kaapelit varten. Verkkolajit sisällytetään metatietolajiin "IM_pipeNetworkType".

{{figure esimerkkikuvaxxxxxx}}

#### Q&A

### Planimetric features
Linkki dokumentaatioon {{refsec Planimetric features}}

#### Pintarakenteet ja niiden materiaaliominaisuudet

Pintarakenteiden materiaali esitetään aluerajauksina. Rajaus annetaan geometrialinjoina tai 3D- tai 3D-taiteviivaketjuina. Materiaalin päänimike tulee InfraBIM-luokituksen mukaisesti. Lisäksi voidaan antaa kerrospaksuus ja tarkempi kuvaus materiaalista tekstinä kuvauskentässä.

{{figure esimerkkikuvaxxx}}

#### Rakennekerrosten materiaaliominaisuudet

Päällyste- ja pintarakennekerroksille luokitellaan materiaaliominaisuudet. Perusperiaatteena, että ominaisuus liitetään kerroksen yläpintaan. Tiedolla kuvataan kerroksen materiaali ja/tai materiaalin ominaisuuksia. Inframodel sisältää materiaaliominaisuuksista valmiit arvojoukkoluettelot.

{{figure esimerkkikuvaxxxx}}

#### Jalustojen ominaisuudet

Jalusta on pistemäinen PlanFeatures- kohde, jolla on InfraBIM-luokitus. Lisäksi jalustalle voicdaan antaa lisätietoja kuten korkeus, materiaali, perustustapa, numero ja tilavaraus. Korkeus esitetään tietomallin *Units* asetusten mukaisesti. Jalustan tilavaraus määritetään joko säteenä tai suorakulmion nurkkapisteinä suhteessa jalustan keskipisteeseen.

{{figure esimerkkikuvayy}

#### Johto- ja kaapelireitit

Kaapelirakenteet on kvuattu Inframodelissa PlanFeature objekteina. Kaapeli on murtoviivaa, jolla on InfraBIM-luokitus. Kaapelin muita ominaisuuksia ovat omistaja, kaapelin tyyppi, tunnus ja tilavaraus. Tilavaraus kuvataan metatietona säteenä tai suorakulmion nurkkapisteinä suhteessa kaapelin keskipisteeseen.

{{figure kaapeliesimerkki}}

#### Kaiteiden ja aitojen ominaisuudet

Kaide ja aitarakenteet on kuvattu Inframodelissa PlanFeature-objekteina. Kohteet ovat murtoviivaa, jolla on InfraBIM-luokitus. Objektin asennuskohdan XYZ ilmaistaan ylimmän yhdistelmäpinnan (yyp) koordinaatteina. Lisäinformaatio voi sisältää esim. kaidetyyppi, käyttötarkoitus, törmäyskestävyys, joustovara, aurauskestävyys, toimintaleveys, korkeus, kaiteen aloitus ja lopetus

{{figure esimerkkikaide}}

#### Q&A

### As-built
Linkki dokumentaatioon {{refsec As-built}}

#### Toteumatiedot

Toteutuneen tilanteen tallentamista kutsutaan toteumatiedoksi. Tietoihin sisällytetään selkeästi yksilöitävät pistetiedot, toleranssit, erovektorit sekä mittausmenetelmän tarkkuusluokka.

Toteumamallin käyttötarkoitus on rakenteen geometrisen laadun ja vaatimusten mukaisen toteutuksen todenaminen tilaajalle ja omaisuudenhallinnan lähtötietona toimiminen tilaajan ylläpitoprosessissa. Suosituksena on vähentää laadunvarmistukseen liittyvän mittaustiedon paperidokumentaation laatimiseen käytettävää työmäärää ja dokumentteja.

{{figure esimerkkimalli}}

Väylärakenteen toteutusmalli koostuu seuraavista INFRA 2015 rakennusosa- ja hankenimikkeistön mukaisista rakennusosista:

**tähän lista rakennusosista**
- 1100 Olevat rakenteet ja rakennusosat
- 1200 Pilaantuneet maat
- 1300 Perustusrakenteet
- 1400 Pohjarakenteet
- 1600 Maaleikkaukset ja -kaivannot
- 1700 Kallioleikkaukset ja -kaivannot
- 1800 Penkereet, maapadot ja täytöt
- 2000 Päällys- ja pintarakenteet
- 2100 Päällysrakenteen osat ja radan alusrakennekerrokset
- 2200 Reunatuet, kourut, askelmat ja eroosiosuojaukset
- 2300 Kasvillisuusrakenteet
- 2400 Ratojen päällysrakenteet
- muut mahdolliset ohjeiston mukaiset lisäykset

#### Q&A

### Deep foundations
Linkki dokumentaatioon {{refsec Deep foundations}}

#### Pilari- ja massastabilointi

Pilari- ja massastabilointi on pääelementti Inframodelissa. Pilariryhmä voidaan kuvata pintojen välisenä tilavarauksena (ulkoreuna ylä- ja alapinnassa) tai yksittäisen pilarin tarkkuudella. Molemmissa tavoissa ryhmään voi liittää useita ominaisuuksia, kuten esim. halkaisija, sideainetyyppi, sideainemäärä.

{{figure stabilointiesimerkki}}

{{figure erillinen skeemakuvaus}}

#### Q&A

### Extensions
Linkki dokumentaatioon {{refsec Extensions}}

#### Q&A

