# Annex 1. Inframodel käyttöohje (Q&A)

## Johdanto

Inframodel (IM) on suomalaisten kehittämä, kansainväliseen LandXML-standardiin (LandXML versio 1.2) perustuva avoin formaatti infratietojen siirtoon. Inframodel-määrittelytyötä on tehty yhdessä alan toimijoiden kanssa buildingSMART Finlandin (bSF) Infran standardointiryhmässä. 

Inframodel tiedonsiirtoa hyödynnetään mm. suunnitteluohjelmissa sekä mittaus-, koneohjaus- ja tarkastussovelluksissa. Yhtenäinen toimintatapa ja avoin tietomallipohjainen formaatti on tehostanut suunnittelua ja rakentamista.

Inframodel skeema ja dokumentaatio sisältävät tietoa sovelluskehittäjille ja käyttöohje tukee loppukäyttäjiä.

Inframodel-tiedonsiirtoformaatti tukeutuu Yleisiin inframallivaatimuksiin ja InfraBIM-nimikkeistöjärjestelmään.  

![Kolminaisuus]({{figure Kolminaisuus.png}} "Kolminaisuus"){{figst Kolminaisuus}}

- Yleiset inframallivaatimukset *(ohje ja vaatimus: mitä ja miten mallinnetaan, laadunvarmistus, lopputuotteen määrittely, mallinnusprosessi jne.)*
- InfraBIM nimikkeistö *(miten nimetään ja luokitellaan)*
- Inframodel tiedonsiirto *(miten tieto siirretään)*

Inframodel tiedonsiirron vähimmäisvaatimukset on kuvattu hankevaiheittain Yleisten inframallivaatimusten liitteessä: Luovutusaineiston tiedonsiirron vaatimukset.

![Aiempien Inframodel versioiden tiedonsiirtomahdollisuudet, joita versio {{github_release}} täydentää]({{figure previousinframodel.png}} "Aiempien Inframodel versioiden tiedonsiirtomahdollisuudet, joita versio {{github_release}} täydentää"){{figst previous_inframodel}}

**Inframodel {{github_release}} tiedonsiirron uusia ominaisuuksia ovat**

- Vapaamuotoiset ominaisuustiedot – Mahdollistavat entistä laajemman kohdekohtaisen ominaisuustiedon siirtämisen standardin avulla
- Metadatan laajempi hyödyntäminen – esim. Tiedostokohtaisesti voidaan osoittaa kuka on tiedon omistaja
- Määrätiedot - Pintojen ja aluerajojen mukana voidaan kuljettaa tietoa pinta-alasta ja tilavuustiedosta
- Kaapelitiedon välittäminen selkeämpää – Kaapelitiedot siirtyvät skeemassa pipenetwork elementin alle 
- Putkille ja kaivoille lisätty ominaisuustietoja – Kaivon pohjanpaksuus - Putken lujuusluokka
- Liikennemerkkitietojen siirtäminen – Mahdollista siirtää liikennemerkkien, pylväiden ja jalustan tietoja
- Kaiteet ja aidat – Pylväsväli lisätty ominaisuustietoihin
- Name attribuutit uniikeiksi – Määritellään name-attribuutit tiedostokohtaisesti uniikeiksi
- Turvarajat ja varoalueet - Muutos mahdollistaa tilavaraus- ja turvaetäisyystiedon siirtämisen
- Aluemaiselle tiedolle ominaisuudeksi pinta-ala – Mahdollistaa pinta-ala tiedon myös aluerajauksille

Silta- ja muiden taitorakenteiden tietomallipohjaiseen tiedonsiirtoon käytetään IFC-standardia, jota kehittää buildingSMART organisaatio. 

Pohjatutkimusten siirtoon käytetään SGY:n (Suomen Geoteknillinen Yhdistys) Infra-pohjatutkimusformaattia.

Inframodel on eräänlainen tietokantamuoto, joka sisältää geometriaa, objektikuvauksia sekä metatietoja. Metatiedoille saattaa olla rajoitettuja arvojoukkoja, jotka ovat sallittuja ko. objekteille. 

Inframodel- formaatti on kehittyvä ja sen tietosisältöä laajennetaan tulevissa versioissa. Inframodel on suomalainen lokalisaatio, miten infran tietoa siirretään koneluettavassa muodossa. Tulevaisuuden tavoite on, että Inframodel aineistoa voidaan kirjoittaa ja lukea LandXML sekä IFC muodossa.

## Ohjeen sisältö

Tämä ohje täydentää kohdassa 1 mainittua dokumentaatiota ja ohje on kohdennettu loppukäyttäjille. 

Ohjeen jäsentely noudattaa Inframodel dokumentaation sisällysluetteloa. Ohjeen ulkoasu ja sisältö koostuu ohjeista sekä Q&A artikkeleista.

Ohjeistus on jatkuvasti päivittyvä ja täydentyvä kysymyksiin ja vastauksiin perustuva jatkuvasti kehittyvä dokumentti. 

Ohjeistukseen voi itse vaikuttaa antamalla palautetta tai kysymällä buildingSMART Finlandin palautekanavien kautta tai tekemällä suoraan tiketin kehitysympäristöön. Saatu palaute tai tarvittavat lisäykset / tarkennukset täydennetään käyttöohjeeseen ylläpitoprosessin mukaisesti.

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

![Tiedostolista]({{figure tiedostolista.png}} "Tiedostolista"){{figst Tiedostolista}}

Käytännössä tiedonsiirron tarpeet ovat monenlaisia ja kokonaisuudet on sovittava hankkeen alussa selkeästi. Esimerkiksi kun suunnittelija toimittaa malleja koneohjaukseen, voidaan toimia väylärakenteiden toteutusmalliohjeen mukaisesti (Väylärakenteen toteutusmallin vaatimukset ja -ohjeet) Tai kun maastomallin eri mittausaineistot (likimalli, tarkka maastomalli, täydennysmittaukset) halutaan selkeästi erottaa omina tiedostoina toisistaan.

Aineiston luomisessa, dokumentoinnissa, laadunvarmistuksessa, objekti- ja tiedostonimeämisessä sekä kansioinnissa noudatetaan yleisiä inframallivaatimuksia.

#### Q&A

### Headers
Linkki dokumentaatioon {{refsec fileheaders}}

#### Yleistiedot

Inframodel tukee LandXML-versiota 1.2 Inframodel- ja LandXML-versio näkyy aina tiedoston alussa. **Aineiston toimittaja vastaa siitä, että tiedosto on näiden suhteen validi, eli täyttää sisällön ja ominaisuustietojen (attribuuttien) rajausten ja eheyden osalta ko. versioiden vaatimukset.**

**Mittayksikkösuositukset:**

{{refsec units}}

- sijainnin ja etäisyyden mittayksikkönä käytetään metriä (m)
- pinta-alalle neliömetri (m2)
- tilavuuden yksikkö kuutiometri (m3)

**Yleistietona on annettava seuraavat:**

- Projektin
    - lyhyt nimi tai tunnus
    - pitkä koko nimi
- Koordinaatti- ja korkeusjärjestelmän nimi yksiselitteisesti
    - Suosituksena globaali EPSG- koodi
- Käytetyt lajiluokitusjärjestelmät
    - lähtötietoaineisto, eli maaastomallin ja maaperämallin kohteet ja pinnat
    - suunniteltujen kohteiden luokitus
    - lisäksi muut mahdolliset hankkeessa sovitut luokitukset
- Lähdeohjelmistosta ohjelman nimi ja versio
- Toimittajatiedoista
    - yritys
    - toimittajan nimi
    - sähköpostiosoite
    - tulostuksen aikaleima

Tiedoston ja objektin nimi ei saa sisältää erikois- tai skandinaavisia merkkejä.

#### Codings

Linkki dokumentaatioon {{refsec typecodingsystems}} ja {{refsec typecodingsystemsext}}

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

Linkki dokumentaatioon {{refsec basedata}}

#### Lähtötietoaineisto ja maaperämallit

Maastomalli/kartoitusaineistot jaetaan eri ryhmiin tai tiedostoihin (Surface) sekä alkuperän mukaisesti, esim. ilmakuvilta mitattu, laserkeilattu, maastossa mitattu. Lähtötietoaineiston tarkkuusvaatimuksia voivat olla esim. pintamallin yhtenäinen kolmiointi ja pisteiden tai viivojen noudattaminen maastomittausohjetta.

Kalliopinta-aineisto jaetaan avokalliopisteisiin ja tulkittuihin pisteisiin. Erottelu tehdään tulkintapisteiden luokittelulla. Lisäksi tulkintapisteet voidaan projektikohtaisesti sopia jaoteltavan tarkemmin: varmistettu porakoneella tai koekuopasta, tulkinta kairauksen kohdalla, tulkinta maatutkaluotauksesta, muu tulkinta.

Maakerrosrajapinnat tms. maaperämallin pinnat tulostetaan joko kaikki samaan tiedostoon omina pintoina tai erikseen kukin pinta omaan tiedostoon.

![Maalajipinnat esimerkki 1]({{figure maalajipinnat.png}} "Maalajipinnat esimerkki 1"){{figst maalajipinnat}}

Lähtitietoaineistot sisältävät ko. pintojen ns. lähtiedot eli pisteet ja viivat. Näistä muodostettuja kolmiopintoja voidaan siirtää omina tiedostoinaan, jos tiedoston koko muuten kasvaa liian isoksi.

Maaperämallin pintojen lajikoodausta on tarkennettu InfraBIM-nimikkeistössä. Suosituksen mukaisesti maaperämallin tulkinta pitää luokitella tulkintatarkkuuden mukaan ja luokituksesta on tehty valmiit arvojoukot eli luettelo sallituista tietoarvoista.

![Maalajipinnat esimerkki 2]({{figure maalajipinnat2.png}} "Maalajipinnat esimerkki 2"){{figst maalajipinnat2}}

#### Q&A

### Route planning

Linkki dokumentaatioon {{refsec routeplanning}}

#### Väylätiedot
Inframodel-tiedonsiirrossa väylällä on yksi jatkuva mittalinja ja tasaus. Tien mittalinjan InfraBIM-koodi tulee olla nimikkeistön mukaisesti (tie= 101 tai rata=111). Ratamallissa kilometripaalutus liitetään mittaraiteeseen. Muut geometrialinjat ja taiteviivat sekä pinnat nimetään InfraBIM-luokituksen mukaisesti. Taiteviivamallin viivoilla tulee olla tiedostokohtainen yksilöllinen nimi (@name).

Aineistojen nimeämisessä noudatetaan Yleisten inframallivaatimusten sekä InfraBIM-nimikkeistön mukaisia numerointi- ja nimeämiskäytäntöjä. Aineistossa siirretään mallin objekteja sekä niihin liitettyä tietoa. Objektit voivat olla esim. pisteitä, viivoja, geometrioita sekä kolmiointeja. Kolmioinnin vaatimuksena on käyttää kolmioverkkoa, jonka *sourcedata* osiosta löytyy myös BreakLine-tieto (kolmioinnin laskentaa ohjaavat taiteviivat).

![Esimerkki yhdistelmämalli]({{figure yhdistelmämalli.png}} "Esimerkki yhdistelmämalli"){{figst yhdistelmämalli}}

Aineistossa siirretään mallin objekteja sekä niihin liitettyä tietoa. Objektit voivat olla esim. pisteitä, viivoja, alueita, geometrioita sekä kolmiointeja. 

#### Q&A

### Roads and street

Linkki dokumentaatioon {{refsec roadandstreedesign}}

#### Q&A

### Railways

Linkki dokumentaatioon {{refsec railwaydesign}}

#### Q&A

### Waterways

Linkki dokumentaatioon {{refsec waterwaydesign}}

#### Q&A

### Areas

Linkki dokumentaatioon {{refsec areastructures}}

#### Q&A

### Water supply and sewerage

Linkki dokumentaatioon {{refsec pipenetworks}}

#### Kuivatus

Vesihuoltoverkostot siirretään koko hankkeen kattavana tiedostona. Suurissa hankkeissa tiedostot voidaan jakaa esim. suunnitteluosuuksiin tai verkostolajeittain.

Kaivoilla ja laitteilla tulee olla koko aineiston kattava yksilöllinen nimi (@name). Vaatimuksena on myös sisällyttää putken korkeustaso uloskirjoitukseen.

#### Verkostolajit: Kaukolämpö, kaukokylmä, kaasu, jäte yms.

Inframodel sisältää omat määritteet verkostolajeina mm. vesijohdolle, kaukolämmölle, kaasulle sekä sähkö ja tietoliikennekaapelisuojaputkille. Verkkolajit sisällytetään metatietolajiin "IM_pipeNetworkType".

![Esimerkki verkostoista]({{figure verkostoesimerkki.png}} "Esimerkki verkostoista"){{figst verkostoesimerkki}}


#### Q&A

### Planimetric features

Linkki dokumentaatioon {{refsec planimetricfeatures}}

#### Pintarakenteet ja niiden materiaaliominaisuudet

Linkki dokumentaatioon {{refsec roadsandstreetsterrainmodel}}

Pintarakenteiden materiaali esitetään aluerajauksina. Rajaus annetaan geometrialinjoina tai 2D- tai 3D-taiteviivaketjuina. Materiaalin päänimike tulee InfraBIM-luokituksen mukaisesti. Lisäksi voidaan antaa kerrospaksuus ja tarkempi kuvaus materiaalista tekstinä kuvauskentässä.


#### Rakennekerrosten materiaaliominaisuudet

Linkki dokumentaatioon {{refsec surfacestructure}}

Päällyste- ja pintarakennekerroksille luokitellaan materiaaliominaisuudet. Perusperiaatteena, että ominaisuus liitetään kerroksen yläpintaan. Tiedolla kuvataan kerroksen materiaali ja/tai materiaalin ominaisuuksia. Inframodel sisältää materiaaliominaisuuksista valmiit arvojoukkoluettelot.


#### Jalustojen ominaisuudet

Linkki dokumentaatioon {{refsec footing}}

Jalusta on pistemäinen PlanFeatures- kohde, jolla on InfraBIM-luokitus. Lisäksi jalustalle voicdaan antaa lisätietoja kuten korkeus, materiaali, perustustapa, numero ja tilavaraus. Korkeus esitetään tietomallin *Units* asetusten mukaisesti. Jalustan tilavaraus määritetään joko säteenä tai suorakulmion nurkkapisteinä suhteessa jalustan keskipisteeseen.

![Esimerkkikuva jalustat]({{figure PlanFeaturefooting.png}} "Esimerkkikuva jalustat"){{figst jalustat}}

#### Johto- ja kaapelireitit

Linkki dokumentaatioon {{refsec cable}}

Kaapelirakenteet on kuvattu Inframodelissa PlanFeature objekteina. Kaapeli on murtoviivaa, jolla on InfraBIM-luokitus. Kaapelin muita ominaisuuksia ovat omistaja, kaapelin tyyppi, tunnus ja tilavaraus. Tilavaraus kuvataan metatietona säteenä tai suorakulmion nurkkapisteinä suhteessa kaapelin keskipisteeseen.

Inframodel {{github_release}} versiossa johdot ja kaapelit voidaan kuvata myös putkiverkkona. {{refsec pipes}}

#### Kaiteiden ja aitojen ominaisuudet

Linkki dokumentaatioon {{refsec railing}} ja {{refsec fence}}

Kaide ja aitarakenteet on kuvattu Inframodelissa PlanFeature-objekteina. Kohteet ovat murtoviivaa, jolla on InfraBIM-luokitus. Objektin asennuskohdan XYZ ilmaistaan ylimmän yhdistelmäpinnan (yyp) koordinaatteina. Lisäinformaatio voi sisältää esim. kaidetyyppi, käyttötarkoitus, törmäyskestävyys, joustovara, aurauskestävyys, toimintaleveys, korkeus, kaiteen aloitus ja lopetus

![Esimerkkikuva kaiteet]({{figure PlanFeaturerailing.png}} "Esimerkkikuva kaiteet"){{figst kaiteet}}

![Esimerkkikuva aidat]({{figure PlanFeaturefence.png}} "Esimerkkikuva aidat"){{figst aidat}}

#### Q&A

### As-built

Linkki dokumentaatioon {{refsec asbuilt}}

#### Toteumatiedot

Toteutuneen tilanteen tallentamista kutsutaan toteumatiedoksi. Tietoihin sisällytetään selkeästi yksilöitävät pistetiedot, toleranssit, erovektorit sekä mittausmenetelmän tarkkuusluokka.

Toteumamallin käyttötarkoitus on rakenteen geometrisen laadun ja vaatimusten mukaisen toteutuksen todenaminen tilaajalle ja omaisuudenhallinnan lähtötietona toimiminen tilaajan ylläpitoprosessissa. Suosituksena on vähentää laadunvarmistukseen liittyvän mittaustiedon paperidokumentaation laatimiseen käytettävää työmäärää ja dokumentteja.

Väylärakenteen toteumamalli koostuu seuraavista INFRA 2015 rakennusosa- ja hankenimikkeistön mukaisista rakennusosista:


#### Q&A

### Deep foundations

Linkki dokumentaatioon {{refsec deepfoundations}}

#### Pilari- ja massastabilointi

Pilari- ja massastabilointi on pääelementti Inframodelissa. Pilariryhmä voidaan kuvata pintojen välisenä tilavarauksena (ulkoreuna ylä- ja alapinnassa) tai yksittäisen pilarin tarkkuudella. Molemmissa tavoissa ryhmään voi liittää useita ominaisuuksia, kuten esim. halkaisija, sideainetyyppi, sideainemäärä.

![Esimerkki pilaristabilointi]({{figure pilaristabilointi.png}} "Esimerkki pilaristabilointi"){{figst pilaristabilointi}}

![Esimerkki skeemakuvaus]({{figure erillinenskeemakuvaus.png}} "Esimerkki skeemakuvaus"){{figst skeemakuvaus}}

#### Q&A

### Extensions

Linkki dokumentaatioon {{refsec inframodelfeatureextensions}}

#### Q&A

