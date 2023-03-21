{{schemafile ../schema/inframodel-raw.xsd}}
# Inframodel \<Feature> extensions

Inframodel transfer files fully conform to the LandXML v1.2 schema (with one exeption\*), but some extensions have been made using the Feature-mechanism. 
This section lists these Inframodel extensions, providing an index to the Inframodel Feature Dictionary: the **\<FeatureDictionary>** element in Inframodel transfer file with the **name** *'inframodel'* (specifying the **\<Feature>** elements in the file with attribute **source** as *'inframodel'* and the attribute **code** being labeled with ''*IM_*' -prefix).

NB: In addition to these extensions, Inframodel specifies many restrctions on the use of LandXML elements and their attributes. These restrictions are described in chapters 1 to 11 of this document. Also, further extensions have been specified in separate schema (im.xsd) for 1) Local Coordinate Transformation (section 1.6) 2) Metadata (section 1.10) and 3) Deep Foundations (section 11).

\* LandXML v1.2 \<choice> declaration in \<Roadways> collection has been changed to \<sequence> in Inframodel v4.1.0, whereby both \<Roadway> elements and feature extensions may appear in the same \<Roadways> collection. 

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
1. The type coding systems are declared in the project information **\<Project>** using "IM_codings" and/or "IM_proprietaryCodings" feature extension and 
2. individual type codes and their descriptions are set under each element using "IM_coding" and/or "IM_proprietaryCoding" feature extension.

The main systems set in the project information using "IM_codings" are:
1. The terrain coding system (**terrainCoding**) usually existing breaklines and points of interest on visible surfaces
2. The surface coding system (**surfaceCoding**) usually individual existing or planned surfaces
3. Infra object type coding system (**infraCoding**) usually individual planned objects and features, not modelled as surfaces.

It is possible to set the same system for several categories. It is also possible to set alternative or additional type coding systems (e.g. InfraRYL) for use within an organization or in a software used.

4. Optional, alternative or additional type coding systems (individually named **proprietaryInfraCoding**) set by defining one or more "IM_proprietaryCodings" \<Feature>.

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


## Type coding

Individual type codes are set for the following elements in inframodel file transfers:

- data point groups, in the **\<DataPoints>** element
- breaklines in the **\<BreakLine>** element
- surfaces, in the **\<Surface>** element
- alignments, in the **\<Alignment>** element
- string line layers, in the **"IM_stringlineLayers"** **\<Feature>** element
- other infrastructures in appropriate elements, such as **\<PlanFeature>**, **\<Pipe>** or **\<Struct>**

Individual type codes are set in the individual element, or in the parent element, whose children inherit the values. Type codes are set using the "IM_coding" feature extension, either as *terrain codes* **terrainCoding**, *surface codes* **surfaceCoding** or *object/feature codes* **infraCoding**. Alternative or additional type codes are set using the "IM_proprietaryCoding", where the proprietary code is in **proprietaryInfraCoding** and the name of the coding system in **proprietaryInfraCodingSource** (as declared in **proprietaryInfraCoding** in "IM_proprietaryCodings").

**Details:**

{{refsec BasedataTypecoding}}

{{refsec RouteplanningTypecoding}}

{{refsec Structures}}

{{refsec Pipes}}

{{refsec PlanimetricfeaturesTypecoding}}


## User defined properties

Custom properties may be defined by using "IM_userDefinedProperties" \<Feature>

{{xtabulate IM_userDefinedProperties--ltFeature--gt}}

where:

{{xtabulate propertyLabel--ltProperty--gt}}

{{xtabulate propertyValue--ltProperty--gt}}

{{xtabulate propertyDescription--ltProperty--gt}}

{{xtabulate propertySource--ltProperty--gt}}


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

## Quantity information

Calculated area of a surface (**\<Surface>**) or the volume below (between two surfaces) can be transferred using "IM_quantity" extension. These quanties may also be assingned to a part of a surface (**\<Surface>**.**\<SourceData>**.**\<Boundaries>**.**\<Boundary>**) or an area defined as a **\<Parcel>**.

{{xtabulate5 IM_quantity}}


## Soil properties

Soil properties of terrain model or ground layer model are captured in "IM_soil" feature extension.

**Details:**  

{{refsec BasedataTerrainmodel}}

{{refsec BasedataGroundlayernmodel}}

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

## Strcutural layer properties

Material properties of layers in road, street or railway structual model are captured in "IM_structLayer" feature extension.

**Details:**  

{{refsec RoadandstreetdesignStructurallayers}}

{{refsec RailwaydesignStructurallayers}}

## Road and street design - Road signs

Road signs belonging to a particular route design are described in **\<Roadways>**.**\<Roadway>**.**\<Roadside>**.**\<RoadSign>**, with detailed properties captured in "IM_roadSign" feature extension:

{{xtabulate5 IM_roadSign}}

## Railway design - KM post coordinates

To assign northing and easting coordinates to railway **\<Alignment>**.**\<StationEquation>**, the parameters are:

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

## Utility networks - network type

When the attribute pipeNetType in \>PipeNetwork> element is set to 'other', the type of utility network may be speficied in "IM_pipeNetworkType" extension:

- districtheating
- districtcooling
- gas
- waste transport piping
- cable

## Utility networks - structure details

It is possible to describe additional details of network structures described in inframodel file transfers. The parameters in "IM_struct" are:

{{xtabulate5 IM_struct}}

**Details:**

{{refsec Circularstructures}}

{{refsec Rectangularstructures}}

{{refsec Pipeinletsandoutlets}}

{{refsec Pipeconnections}}

{{refsec Equipment}}

## Utility networks - pipe details

It is possible to describe additional details of pipes of a network described in inframodel file transfers. The parameters in "IM_pipe" are:

{{xtabulate5 IM_pipe}}

**Details:**

{{refsec Circularpipes}}

{{refsec Eggpipes}}

{{refsec Ellipticpipes}}

{{refsec Rectangularpipes}}

{{refsec Channels}}

## Utility networks - cable details

It is possible to describe additional details of cables of a network described in inframodel file transfers. The parameters in "IM_cable" are:

{{xtabulate5 IM_cable}}

**Details:**

{{refsec Cables}}

## Plan features

Planimetric features belonging to a particular route design are described in **\<Roadways>**.**\<Roadway>**.**\<PlanFeature>**, or in other cases in **\<PlanFeatures>**.**\<PlanFeature>**. In addition of capability of being classified using "IM_coding" extension (and/or "IM_proprietaryCoding") and having custom properties using "IM_userDefinedProperties", detailed propeties may be assigned by the type of plan feature:

- cable properties in **"IM_cable"**
- footing properties in **"IM_footing"**
- railing properties in **"IM_railing"**
- fence properties in **"IM_fence"**
- surface structure properties in **"IM_surfaceStruct"**
- generic (none of the above) properties in **"IM_planFeature"**

**Details:**

{{refsec Roadplanfeatures}}

{{refsec Railplanfeatures}}

{{refsec Waterwayplanfeatures}}

{{refsec Planimetricfeatures}}

## As-built survey points

Inframodel enables transfering both planned control points with tolerances (**\<Cgpoints>** as top-level collection), and the measured values (**\<Survey>**.**\<Cgpoints>**), both having detailed properties assign to the collection as "IM_cgpoints":

{{xtabulate IM_cgpoints}}

**Details:**

{{refsec Controlpoints}}
{{refsec As-builtsurvey}}

## Spatial allocation and spatial avoidance

An area or a space allocated for some specific use, or a perimeter around an object to be avoided can be defined using "IM_spatialZone" extension, applicable to  **\<PlanFeature>**, **\<Parcel>**, **\<Pipe>** or **\<Struct>**.

{{xtabulate IM_spatialZone}}

**Details:**

{{refsec Planimetricfeatures}}
{{refsec Parcels}}
{{refsec Structures}}
{{refsec Pipes}}
