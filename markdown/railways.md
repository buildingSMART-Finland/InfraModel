{{schemafile ../schema/inframodel-raw.xsd}}
# Railway design {#sec:railwaydesign}

The methods used to describe a route in inframodel file transfer are described in detail in the section route planning. It is possible to describe road, street and railway plans and information about water supply and sewerage. A railway plan typically consists of one continuous track for KM-posting and other tracks. The centerlines and the bottoms of the rails of each track are described as geometric alignments. The transition points for cant and design speeds are also described in conjunction with the stationing of the centerlines of the KM-posting track and of other tracks. The current specification does not include description of switches and crossings. The alignments with string line representations can be collected into a string line model of the railway. The model can also include a surface model and structural model, and it is possible to attach additional breakline and random point information.

## Track geometry

One **\<Alignments>** collection containing several **\<Alignment>** elements is used for describing a railway geometry. Only one of those **\<Alignment>** elements can be the centerline of reference track for KM-posting. Description a track centerline is always a geometric **\<Alignment>**.

The geometric alignment description is composed of elements in horizontal and vertical geometry, respectively (see {{refsec alignments}}). The KM-posting reference track and additional track center lines have their own type codes in inframodel rail planning. Other lines than centerlines and the bottoms of the rails are described as line strings. Since the *string line model* of the track only uses line strings, the *line information* contained by the *geometry lines* is also described as an approximate *line string*. These may be presented in any order. The type coding of individual lines determines their purposes; the type code (terrainCoding) for the terrain model is set in a structural extension. The desired lines can be included in a *string line model*, according to the structural extension "IM\_stringlineLayers". In the stringline model the surfaces can be assigned surface codes (**surfaceCoding**). The *surface and structural models of a railway* can also be described as triangular meshes (TIN surfaces). The raiway *plan information* is defined in the optional "IM_plan" structural extension.

## String line model

After a particular **\<Alignment>** out of a group of **\<Alignments>** has been defined, the stringline model may be defined in the structural extension "IM_stringlineLayers". The mode of presentation is akin to cross-sections, the stringline layers of the string line model are refered to by their name **\<Alignment>.name** and the location is described as surfaces. It is not always possible to present all line strings contained by the layer in order from left to right, although this is recommended.

The detailed description of the construction process of line string model can be found in {{refsec stringlinemodel}}. The lines of the string line model employ the same terrain point coding as alignments. Surfaces are defined in the string line model with surface codes (**surfaceCoding**).

![String line representation of railway]({{figure Railstringlinemodel.png}} "String line representation of railway"){{figst stringlinerepresentationofrailway}}


## KM-posting {#sec:kmposting}

The KM-posting method in inframodel uses **\<StaEquation>** in a way that somewhat differs from its typical use in LandXML. The individual km-post station distances from the previous post station are defined by their back stations **staBack** (for the first KM-post on a given alignment, the **staBack** can be set to "NaN", when it is not known or relevant). This use of **\<StaEquation>** does not imply a re-start in the alignment stationing, hence in inframodel the **staAhead** attribute is always set to the same value as **staInternal** attribute. Individual locations according to the KM-posting system on all tracks are presented in relation to the KM-posting reference alignment. The name of the KM-post station is defined by the **desc** attribute.

Although the Finnish KM-posting system is nominally kilometre based, it cannot be used to define distances between points. The actual length of a track is therefore calculated along the centerline **\<Alignment>** of that track, resulting in continuous internal stationing in **staInternal** attribute values.

{{xtabulate StaEquation}}

![KM-posting]({{figure KMpaalutus.png}} "KM-posting"){{figst kmposting}}

{{xtabulate IM_kmPostCoords--ltFeature--gt}}

## Cross-sections and track information {#sec:crosssectionsandtrackinformation}

Cross-section plan contains information that fleshes out the geometry and string line model descriptions of the railway. The information contained by the cross-section element is valid from the given station forward, either to the next transition cross-section element or the end of the line. The cross-section parameters are described under the KM-posting reference track in the **\<Alignment>**.**\<CrossSects>**.**\<CrossSect>** element and its extension "IM_crossSect" (**\<Feature>**).

It is recommended that all parameters are described along with the cross-section. Details on the Finnish railway design parameters are provided by [Finnish Transport Infrastructure Agency (FTIA)](https://vayla.fi/web/en).

### Cross-sections

The cross-sections for KM-posting reference track are defined by the element **\<Alignment>**.**\<CrossSects>**.**\<CrossSect>**. For individual cross-sections, the cross-section parameters are presented in the extension "IM_crossSect". Transitions are defined in the points where parameters change start and where they have reached their final values after the transition. Triple and higher multiple track railways are composed of double and single track standard cross-sections.

![Cross section]({{figure RailcrossSectcant.png}} "Cross section"){{figst crosssection}}

{{xtabulatef CrossSect}}

The following information must be defined in the extension "IM_crossSect" for an individual cross-section:

- the number of tracks **tracks**
- the distance between track centerlines **trackDist**
- the total thichness of track bed layers **thickness**
- track bed or cut width **bedWidth**

{{xtabulate IM_crossSect--ltFeature--gt__rail}}

### Track information

The transitions in cant and design speed for each track are described under the track centerline **\<Alignment>** in **\<Cant>** sub-elements. The *track information* **\<Cant>** defines the **name**, the track **gauge** and the *cant rotation point* **rotationPoint**.

{{xtabulate Cant}}

The following transitions are described by the track information sub-element:

- **\<CantStation>** is used at cant events, typically: 0-value at the start and end of straight track segments, same value at the start and end of circular curve segments, and different values at start and end of transition curve segments (interpolated according to the horizontal spiral curvature change)
- **\<SpeedStation>** is used when the design speed changes


![Railway cant]({{figure Railcant.png}} "Railway cant"){{figst railwaycant}}

1. When the *cant* changes in the **\<CantStation>**:

{{xtabulate CantStation}}

2. When only the *design speed* changes in the **\<SpeedStation>**

{{xtabulate SpeedStation}}

The **station** attribute of **\<CantStation>** and **\<SpeedStation>** shall have an stationing value where **\<Alignment>.staStart** is taken in account.

### Switch information {#sec:switchinformation}

The information on switches of tracks is given under track centerlines in the **\<Alignment>**.**\<CoordGeom>**.**\<Line>** using "IM_switch" **\<Feature>**

{{xtabulate IM_switch--ltFeature--gt}}

## Terrain model and structural model of the track {#sec:railwaystructurallayers}

The presentation method of the *terrain model* is described in further detail in {{refsec terrainmodel}}. The terrain model of the track only contains the triangular mesh surface of the visible track structures. The structural model contains all surfaces as described in {{refsec  structuralmodel}}. The goal is to assign all surfaces a type code in accordance to the type coding system.

It is also possible to add source data point and breakline information to surfaces. This is described in further detail in the section {{refsec sourcedata}}.

![Railway structural model]({{figure Railstructuremodel.png}} "Railway structural model"){{figst railwaystructuralmodel}}

## Rail plan features {#sec:railwayplanfeatures}

The rail planimetric features such as fences, lightpole or signage footings that are assigned to a particular railway are described under *roadways*. A *roadways collection* **\<Roadways>** may consist of several *roadway* **\<Roadway>** elements. Each *roadway* has a reference to its *centerline* **\<Alignment>**, and it can hold a number of **\<PlanFeature>** elements.

Attributes of the *roadways collection* **\<Roadways>** are not used in inframodel.

{{xtabulate Roadways}}

### Plan features

The individual *plan features* are each described under **\<PlanFeature>**, having a mandatory and unique **name** and optionally **\<Location>** and *geometry* as **\<CoordGeom>**.

{{xtabulate PlanFeature}}

**\<PlanFeature>** *geometry* is described in **\<CoordGeom>** using line strings for linear features, e.g. *cables*, *railings* and *fences*. For point features, such as *footings*, location is given in **\<Location>** element as a two or three dimensional point:

Details of **\<PlanFeature>** are described as **\<Feature>** extension, defined for each type as follows:

1. {{refsec cable}} in "IM_cable" extension
2. {{refsec footing}} in "IM_footing" extension
3. {{refsec railing}} in "IM_railing" extension
4. {{refsec fence}} in "IM_fence" extension
5. {{refsec surfacestructure}} in "IM_surfaceStructure" extension
6. {{refsec genericplanfeature}} in "IM_planfeature" extension


Additionally, all plan features may be type coded in **\<Feature>** using {{refsec typecodingext}} in "IM_coding" extension.

# Railway signs
The individual *railway signs* can be described as **\<RoadSign>** elements.
See {{refsec roadsigns}} for details.