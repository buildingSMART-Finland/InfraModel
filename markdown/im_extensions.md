{{schemafile ../schema/inframodel-raw.xsd}}
# Inframodel \<Feature> extensions

Inframodel transfer files fully conform to the LandXML v1.2 schema, but some extensions have been made using the Feature-mechanism. 
This section lists these Inframodel extensions, providing an index to the Inframodel Feature Dictionary: the **\<FeatureDictionary>** element in Inframodel transfer file with the **name** *'inframodel'* (specifying the **\<Feature>** elements in the file with attribute **source** as *'inframodel'* and the attribute **code** being labeled with ''*IM_*' -prefix).

NB: In addition to these extensions, Inframodel specifies many restrctions on the use of LandXML elements and their attributes. These restrictions are described in chapters 1 to 11 of this document.

## Local coordinate transformation definition by point pairs

Local coordinate system may be defined as set of control points sourceCRS-targetCRS point pairs under "IM_coordTransformation" \<Feature> extension.

{{xtabulate IM_coordTransformation--ltFeature--gt}}

Where:

{{xtabulate sourceCRSname--ltProperty--gt}}

{{xtabulate sourceEPSGcode--ltProperty--gt}}

{{xtabulate IM_controlPoint--ltFeature--gt}}

where:

{{xtabulate useHorizontal--ltProperty--gt}}

{{xtabulate useVertical--ltProperty--gt}}

{{xtabulate latitude--ltProperty--gt}}

{{xtabulate longitude--ltProperty--gt}}

{{xtabulate altitude--ltProperty--gt}}

{{xtabulate northing--ltProperty--gt}}

{{xtabulate easting--ltProperty--gt}}

{{xtabulate elevation--ltProperty--gt}}


## Type coding systems

Type coding systems define the purpose of geometric elemnents (points, lines and surfaces) as well as other types of elements (such as plan features, pipes and structures in pipe networks, etc).) in Inframodel file transfers. 

The information is set in two phases: 
1. The type coding systems are declared in the project information **\<Project>** using **"IM\_codings"** feature extension and 
2. individual type codes and their descriptions are set under each element using ("IM_coding" feature extension).

The main systems set in the project information are:
1. The terrain coding system (**terrainCoding**) usually existing breaklines and points of interest on visible surfaces
2. The surface coding system (**surfaceCoding**) usually individual existing or planned surfaces
3. Infra object type coding system (**infraCoding**) usually individual planned objects and features, not modelled as surfaces.

It is possible to set the same system for several categories. It is also possible to set alternative or additional type coding systems (e.g. InfraRYL) for use within an organization or in a software used.

4. Software or organization specific type coding systems (**proprietaryInfraCoding**) by defining one or more "IM_proprietaryCodings" \<Feature>

{{xtabulate IM_codings--ltFeature--gt}}

where:

{{xtabulate terrainCoding--ltProperty--gt}}

{{xtabulate terrainCodingDesc--ltProperty--gt}}

{{xtabulate terrainCodingSourceRef--ltProperty--gt}}

{{xtabulate surfaceCoding--ltProperty--gt}}

{{xtabulate surfaceCodingDesc--ltProperty--gt}}

{{xtabulate surfaceCodingSourceRef--ltProperty--gt}}

{{xtabulate infraCoding--ltProperty--gt}}

{{xtabulate infraCodingDesc--ltProperty--gt}}

{{xtabulate infraCodingSourceRef--ltProperty--gt}}

Proprietary codelists are defined using "IM_proprietaryCodings" \<Feature>

{{xtabulate IM_proprietaryCodings--ltFeature--gt}}

where:

{{xtabulate proprietaryInfraCoding--ltProperty--gt}}

{{xtabulate proprietaryInfraCodingDesc--ltProperty--gt}}

{{xtabulate proprietaryInfraCodingSourceRef--ltProperty--gt}} 

TODO-MISSING FEATURE ITEM
{{xtabulate IM_coding--ltFeature--gt}}


More information can be found from {{refsec Typecodingsystems}} 

## User defined properties

Custom properties may be defined by using "IM_userDefinedProperties" \<Feature>

{{xtabulate IM_userDefinedProperties--ltFeature--gt}}

where:

{{xtabulate propertyLabel--ltProperty--gt}}

{{xtabulate propertyValue--ltProperty--gt}}

{{xtabulate propertyDescription--ltProperty--gt}}

{{xtabulate propertySource--ltProperty--gt}}


 

## Type coding

Individual type codes are set for the following elements in inframodel file transfers:

- data point groups, in the **\<DataPoints>** element
- breaklines in the **\<BreakLine>** element
- surfaces, in the **\<Surface>** element
- alignments, in the **\<Alignment>** element
- string line layers, in the **"IM_stringlineLayers"** **\<Feature>** element
- other infrastructures in appropriate elements, such as **\<PlanFeature>**, **\<Pipe>** or **\<Struct>**

Individual type codes are set in the individual element, or in the parent element, whose children inherit the values. Type codes are set using the **"IM_Coding"** feature extension, either as *terrain codes* **terrainCoding**, *surface codes* **surfaceCoding** or *object/feature codes* **infraCoding**. Alternative or additional type coding systems are set with assigned name as *proprietary codes* **proprietaryInfraCoding**.

**Details:**

{{refsec BasedataTypecoding}}

{{refsec RouteplanningTypecoding}}

{{refsec Structures}}

{{refsec Pipes}}

{{refsec PlanimetricfeaturesTypecoding}}

## Plan information

The details of a plan are described for each project part:

- surfaces (data points, breaklines, surfaces), in the **\<Surfaces>** element
- route planning (road, street, railway ja waterway planning), in the **\<Alignments>** element
- water supply and sewerage, in the **\<PipeNetworks>** element.

If the project consists of sub-projects that have different rates of progress, the plan contents of the file are divided into sub-projects according to the same division. The plan information contains the **planName**, **planCode**, the **planState** and the plan description **planDesc**. The plan state is described according to a scheme agreed on by the parties of the project.

**Details:**  

{{refsec BasedataPlaninformation}}

{{refsec RouteplanningPlaninformation}}

{{refsec WatersupplyandseweragePlaninformation}}

## String line model

The string line model is composed of *line string alignments* **\<IrregularLine>**. Their order with an **\<Alignment>** is irrelevant. The string line model used in Inframodel is based on the Leica RoadRunner software.

The string line model is defined under an **\<Alignment>** in the **"IM\_stringlineLayers"** extension. The constituent line strings and their locations are set by layer in the **"IM_stringlineLayer"** child element.  The order of description of the line strings does not matter, the alignments are identified by their unique name **\<Aligenment>.name**, which are listed in the element, separated by commas. A layer is assigned a **name** and optionally a **centerline**. When describing a layered structure the layers of the string line model are assigned surface codes **SurfaceCoding**. The same line string may belong to several different layers. Layer are listed starting from the top downwards.

**Details:**

{{refsec Stringlinemodel}}

## Cross-section parameters

*Cross-section parameters* contain parametric information considered crucial for each route type. They are set for the *stationing reference alignment* in the **\<CrossSects>**.**\<CrossSect>** "IM_crossSect" extension under the **\<Alignment>** element. The chosen cross-section parameters are set in fields (**\<Property>**). It is advisable to describe all parameters for each cross-section. If the some parameters change, the cross-section where the parameter begins to change and the end of the transition are described.

The described parameters vary by route type:

**parameters in road and street planning**
- **pavementClass**
- **pavementThickness**
- **subgradeLoadCapacityClass**
- (perpendicular) **slope**

**railway planning parameters**
- number of **tracks**
- track distance **trackDist**
- **thickness** of permanent way
- track bed width **bedWidth**

**waterway planning parameters**
- minumum **depth**
- waterway **width**
- dimensioning water level height **waterLevel**

**Details:**

{{refsec Crosssectparameters}}

{{refsec Crosssectionsandtrackinformation}}

{{refsec Crosssectionparameters}}

## Water supply and sewerage - structure details

It is possible to describe additional details for the water supply and sewerage network structures described in inframodel file transfers. The parameters are:

- structure code **structCode**
- **rimType**
- **rimMaterial**
- **rimLoad class**
- inner diameter of the drain rim **rimDiameter**
- 2D coordinate of the rim center **rimCenter**
- height of the sump **heightDeposit**
- volume of the sump **volumeDeposit**
- construction date **constructionDate**
- renewal date **renowalDate**
- renewal description **renowalDesc**
- equipment type **equipmentType**
- equipment code **equipmentCode**
- equipment description **equipmentDesc**

**Details:**

{{refsec Circularstructures}}

{{refsec Rectangularstructures}}

{{refsec Pipeinletsandoutlets}}

{{refsec Pipeconnections}}

{{refsec Equipment}}

## Water supply and sewerage - pipe details

Describing pipe details is optional in inframodel file transfers. It is possible to set the following attributes:


- pipe code **pipeCode**
- pipe start and end point coordinates (3D)
    - elevation type **elevType**
    - start coordinates **pipeStart**
    - end  coordinates **pipeEnd**
- joint type **jointType**
- pressure class **pressureClass**
- construction date **constructionDate**
- renewal date **renowalDate**
- renewal description **renowalDesc**

**Details:**

{{refsec Circularpipes}}

{{refsec Eggpipes}}

{{refsec Ellipticpipes}}

{{refsec Rectangularpipes}}

{{refsec Channels}}


## Railway design - KM post coordinates

To assing northing and easting coordinates to railway **\<Alignment>**.**\<StationEquation>**, the parameters are:

- northing coordinate **northing**
- easting coordinate **easting**

**Details:**

{{refsec KM-posting}}

## Railway design - switches

Switch details at railway track **\<Alignment>**.**\<CoordGeom>**.**\<Line>**, the parameters are:

- switch type **switchType**
- switch hand **switchHand**
- switch joint **switchJoint**

**Details:**

{{refsec Switchinformation}}

## Plan features

Planimetric features belonging to a particular route design are described in **\<Roadways>**.**\<Roadway>**.**\<PlanFeature>**, or in other cases in **\<PlanFeatures>**.**\<PlanFeature>**, by following data:

- type **type**
- optional material **material**
- type code **Infracoding** in embedded Type coding



**Details:**

{{refsec Roadplanfeatures}}

{{refsec Railplanfeatures}}

{{refsec Waterwayplanfeatures}}

{{refsec Planimetricfeatures}}
