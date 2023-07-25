{{schemafile ../schema/inframodel-raw.xsd}}
# Road and street design {#sec:roadandstreedesign}

The file describing a road or street plan contains the header information described in the previous section. In inframodel-compliant file transfers a road or street alignment is defined in according to the process defined in {{refsec routeplanning}}. A LandXML file may contain plans describing several topics, i.e. the same file may contain e.g. road, street, and railway plans.

The content of the design file is defined in metric units, using an adequate number of decimals for accuracy. For example, when the length unit in use is a meter, the values must be defined to at least six decimal places. Street designs often interface with  water supply and sewerage systems , which are described in the same file. The constituent surfaces of the water supply and sewerage design are defined as triangular meshes and the design information in the \<PipeNetworks> element.

A road or street design in inframodel may contain:

- individual alignments and their purpose, defined by type coding (geometric alignments and line strings)
- line string model (line string alignments)
- a terrain model (the visible surface)
- a structural model (the visible surface and the structural layers of the road or street)
- cross-section parameters
- road signs and planimetric features

The plan information may optionally contain the following:

- source data (random points and breaklines)
- drainage plan
- railway plan
- waterway plan

The superelevation of the road can be described alongside the cross-section parameters. Cross-section parameters are described at the transition points, when the transition of the value of a parameter begins or ends. Superelevation encompasses the cross slope of the roadway and in case of a street also the sidewalk.

## Geometry of roads and streets

An *alignment group* of road or street **\<Alignments>** contains a *geometric description* of a continuous stationing reference **\<Alignment>**. The *geometric description* is composed of horizontal and vertical geometric elements. The central *alignments* such as the centerline and left and right edges of a road or the centerline and edges of a sidewalk for a street are described as *geometric alignments* while the rest are described in terms of *line strings*. The alignments described as *geometric descriptions* are also described as *line strings* for use in the *line string model*.

The *alignments* **\<Alignment>** of an *alignment group* **\<Alignments>** are described before the *line string model* or the *plan information* contained by the extensions "IM_stringlinelayers" and "IM_plan". The particular order of the alignments **\<Alignment>** within the alignment group **\<Alignments>** does not matter. The alignment description process is described in further detain in {{refsec alignments}} .

The **infraCode** is set in the extension "IM_coding" - this *type coding* for an individual **\<Alignment>** describes the purpose of the alignment.

Selected alignments are included in the *line string model* defined by the extension "IM_stringlineLayers". It is defined in the file after the **\<Alignment>** elements and arranges line strings into surfaces using **surfaceCoding**.

## String line model of roads and streets

Once the *alignments* **\<Alignment>** of an *alignment group* **\<Alignments>** are defined, the string line model of the *alignment group* is defined in the extension "IM_stringlineLayers". The presentation method resembles a cross-section, a *layer* of the string line model are referred to by their name **\<Alignment>.name** and their location is presented as surfaces. It is not always possible to present all line strings contained by the layer in order from left to right, although this is recommended.

The detailed description of the construction process of line string model can be found in {{refsec stringlinemodel}}. The string line model employs the same **infraCoding** system for *line strings* as the **\<Alignment>**. The surface codes are set using the **surfaceCoding**.

![Stringline representaion of road]({{figure Road_stringline_model.png}} "Stringline representaion of road"){{figst stringlinerepresentaionofroad}}

![Stringline representaion of street]({{figure Street_stringlinemodel.png}} "Stringline representaion of street"){{figst stringlinerepresentaionofstreet}}

## Cross-section parameters of roads and streets

The cross *section parameters* of an *alignment group* **\<Alignments>** expand on the geometric description and line string model by defining the cross sections by station intervals in a parametric form. The cross-section parameters are set in inframodel file transfers in the "IM_crossSect" extension along with the cross-section elements. The implementation of the extension is similar to that for waterways.

The cross-section parameters describe the situation at a given station, including the *cross-slopes* of the roadways, streets and sidewalks. The following elaborates on the process of description: the cross-section parameters are presented at a station where a value begins or stops changing. Cross-slopes are set for each lane starting from the left to the right. A positive superelevation indicates a superelevation where the edge located further from the centerline of two is above the inner one. Accordingly, a negative one indicates that the outer edge is below the inner one.

![Road cross section]({{figure Road_crossSect_slope.png}} "Road cross section"){{figst roadcrosssection}}

### Cross-section parameters {#sec:crosssectparameters}

*The cross-section parameters* are set under **\<Alignment>**.**\<CrossSects>**.**\<CrossSect>** in the extension "IM_crossSect". 

It is recommended that all parameters are described along with the cross-section. When transitions from one parameter value to another occur, the start and end of the transition are defined. Details on the Finnish road design parameters are provided by Finnish Transport Infrastructure Agency (FTIA).

{{xtabulate CrossSect}}

{{xtabulate IM_crossSect--ltFeature--gt}}

### Transitions in superelevation

The superelevation is defined at the transition points, when a transition in the superelevation either begins or end. The cross-slopes are defined along with the cross-section parameters. The following picture illustarates the process in a road design environment.

![Superelevation]({{figure Road_slope.png}} "Superelevation"){{figst superelevation}}

## Terrain model and structural model of road or street {#sec:roadsandstreetsterrainmodel}

The process of constructing a terrain model or structural model is described in detail in {{refsec terrainmodel}} and {{refsec structuralmodel}} of a route. The terrain model only contains a triangle mesh of the visible surfaces. The structural model contains all the structure boundaries. All layers in the terrain model and the structural model may be assigned a *type code* (**surfaceCoding**).

It is also possible to attach source data point or breakline information to the meshes, with assigned a *type code* (**terrainCoding**). The process is described in further detail in the {{refsec sourcedata}}.

The example illustrations below demonstrate the composition of structural models in road and street design.

![Structural model of a road]({{figure Road_structuremodel.png}} "Structural model of a road"){{figst structuralmodelofaroad}}

![Structural model of a street]({{figure Street_structuremodel.png}} "Structural model of a street"){{figst structuralmodelofastreet}}

### Structural layers {#sec:roadsandstreetsstructurallayers}

The material properties of a structural layer between two surfaces are assigned to its top surface, i.e. in a *structural model* of road or street an "IM_structLayer" **\<Feature>** extension describes the soil properties below the **\<Surface>**.

Details of **\<Surface>** in "IM_structLayer" **\<Feature>**

{{xtabulate IM_structLayer--ltFeature--gt}}

## Road signs and plan features {#sec:roadplanfeatures}

The road signs and planimetric features such as fences, guard rails, lightpole or signage footings that are assigned to a particular road or street are described under *roadways*. A *roadways collection* **\<Roadways>** may consist of several *roadway* **\<Roadway>** elements. Each *roadway* has a reference to its *stationing reference line* **\<Alignment>**, and it can hold a number of **\<PlanFeature>** elements, as well as **\<Roadside>** elements with **\<RoadSign>** elements.

Attributes of the *roadways collection* **\<Roadways>** are not used in inframodel.

{{xtabulate Roadway}}

### Plan features

The individual *plan features* are each described under **\<PlanFeature>**, having a mandatory and unique **name** and optionally **\<Location>** and *geometry* as **\<CoordGeom>**.

Attributes of **\<PlanFeature>**:

{{xtabulate PlanFeature}}

**\<PlanFeature>** *geometry* is described in **\<CoordGeom>** using **line strings** for linear features, e.g. *cables*, *railings* and *fences*. For point features, such as *footings*, location is given in **\<Location>** element as a two or three dimensional point:

Details of **\<PlanFeature>** are described as **\<Feature>** extension, defined for each type as follows:

1. {{refsec cable}} in "IM_cable" extension
2. {{refsec footing}} in "IM_footing" extension
3. {{refsec railing}} in "IM_railing" extension
4. {{refsec fence}} in "IM_fence" extension
5. {{refsec surfacestructure}} in "IM_surfaceStructure" extension
6. {{refsec genericplanfeature}} in "IM_planfeature" extension

Additionally, all plan features may be type coded in **\<Feature>** using {{refsec typecodingext}} in "IM_coding" extension.

### Road signs  {#sec:roadsigns}

The individual *road signs* are each described under **\<RoadSign>** (placed under **\<RoadSide>**, having no attributes). Mandatory attributes of **\<RoadSign>** in Inframodel are **width** and **height**, defining the bounding rectangle around the *road sign*, the actual shape and other properties can be specified "IM_roadSign" extension.

Attributes of **\<RoadSign>**:

{{xtabulate RoadSign}}

{{xtabulate IM_roadSign--ltFeature--gt}}

![Road sign]({{figure RoadSign.png}} "Road sign"){{figst roadsign}}
