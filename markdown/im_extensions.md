{{schemafile ../schema/inframodel-raw.xsd}}
# Inframodel \<Feature> extensions {#sec:inframodelfeatureextensions}

Inframodel transfer files fully conform to the LandXML v1.2 schema (with one exeption\*), but some extensions have been made using the Feature-mechanism. 
This section lists these Inframodel extensions, providing an index to the Inframodel Feature Dictionary: the **\<FeatureDictionary>** element in Inframodel transfer file with the **name** *'inframodel'* (specifying the **\<Feature>** elements in the file with attribute **source** as *'inframodel'* and the attribute **code** being labeled with ''*IM_*' -prefix).

NB: In addition to these extensions, Inframodel specifies many restrctions on the use of LandXML elements and their attributes. These restrictions are described in this document. Also, further extensions have been specified in separate schema (im.xsd) for 1) Local Coordinate Transformation ({{refsec typecodingsystems}}) 2) Metadata ({{refsec metadata}}) and 3) Deep Foundations ({{refsec deepfoundations}}).

\* LandXML v1.2 \<choice> declaration in \<Roadways> collection has been changed to \<sequence> in Inframodel v4.1.0, whereby both \<Roadway> elements and feature extensions may appear in the same \<Roadways> collection. 

## Local coordinate transformation definition by point pairs {#sec:localcoordinatetransfromationbypointpairsext}

Local coordinate system may be defined as set of control points sourceCRS-targetCRS point pairs under "IM_coordTransformation" \<Feature> extension.

{{xtabulatef IM_coordTransformation--ltFeature--gt}}

Where:

{{xtabulatef sourceCRSname--ltProperty--gt}}

{{xtabulatef sourceEPSGcode--ltProperty--gt}}

{{xtabulatef IM_controlPoint--ltFeature--gt}}

where:

{{xtabulatef useHorizontal--ltProperty--gt}}

{{xtabulatef useVertical--ltProperty--gt}}

{{xtabulatef latitude--ltProperty--gt}}

{{xtabulatef longitude--ltProperty--gt}}

{{xtabulatef altitude--ltProperty--gt}}

{{xtabulatef northing--ltProperty--gt}}

{{xtabulatef easting--ltProperty--gt}}

{{xtabulatef elevation--ltProperty--gt}}


## Type coding systems {#sec:typecodingsystemsext}

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

{{xtabulatef IM_codings--ltFeature--gt}}

where:

{{xtabulatef terrainCoding--ltProperty--gt}}

{{xtabulatef terrainCodingDesc--ltProperty--gt}}

{{xtabulatef terrainCodingSourceRef--ltProperty--gt}}

{{xtabulatef surfaceCoding--ltProperty--gt}}

{{xtabulatef surfaceCodingDesc--ltProperty--gt}}

{{xtabulatef surfaceCodingSourceRef--ltProperty--gt}}

{{xtabulatef infraCoding--ltProperty--gt}}

{{xtabulatef infraCodingDesc--ltProperty--gt}}

{{xtabulatef infraCodingSourceRef--ltProperty--gt}}

Proprietary codelists are defined using "IM_proprietaryCodings" \<Feature>

{{xtabulatef IM_proprietaryCodings--ltFeature--gt}}

where:

{{xtabulatef proprietaryInfraCoding--ltProperty--gt}}

{{xtabulatef proprietaryInfraCodingDesc--ltProperty--gt}}

{{xtabulatef proprietaryInfraCodingSourceRef--ltProperty--gt}} 

More information can be found from {{refsec typecodingsystems}} 


## Type coding {#sec:typecodingext}

Individual type codes are set for the following elements in inframodel file transfers:

- data point groups, in the **\<DataPoints>** element
- breaklines in the **\<BreakLine>** element
- surfaces, in the **\<Surface>** element
- alignments, in the **\<Alignment>** element
- string line layers, in the **"IM_stringlineLayers"** **\<Feature>** element
- other infrastructures in appropriate elements, such as **\<PlanFeature>**, **\<Pipe>** or **\<Struct>**

Individual type codes are set in the individual element, or in the parent element, whose children inherit the values. Type codes are set using the "IM_coding" feature extension, either as *terrain codes* **terrainCoding**, *surface codes* **surfaceCoding** or *object/feature codes* **infraCoding**. Alternative or additional type codes are set using the "IM_proprietaryCoding", where the proprietary code is in **proprietaryInfraCoding** and the name of the coding system in **proprietaryInfraCodingSource** (as declared in **proprietaryInfraCoding** in "IM_proprietaryCodings").

{{xtabulatef IM_coding--ltFeature--gt}}

{{xtabulatef IM_proprietaryCoding--ltFeature--gt}}

**Details:**

{{refsec typecoding}}

{{refsec routeplanningtypecoding}}

{{refsec structures}}

{{refsec pipes}}

{{refsec planimetricfeaturestypecoding}}


## User defined properties {#sec:userdefinedpropertiesext}

Custom properties may be defined by using "IM_userDefinedProperties" \<Feature>

{{xtabulatef IM_userDefinedProperties--ltFeature--gt}}

where:

{{xtabulatef propertyLabel--ltProperty--gt}}

{{xtabulatef propertyValue--ltProperty--gt}}

{{xtabulatef propertyDescription--ltProperty--gt}}

{{xtabulatef propertySource--ltProperty--gt}}


## Plan information {#sec:planinformationext}

The details of a plan are described for each project part:

- surfaces (data points, breaklines, surfaces), in the **\<Surfaces>** element
- route planning (road, street, railway ja waterway planning), in the **\<Alignments>** element
- water supply and sewerage, in the **\<PipeNetworks>** element.

If the project consists of sub-projects that have different rates of progress, the plan contents of the file are divided into sub-projects according to the same division. The plan information contains the **planName**, **planCode**, the **planState** and the plan description **planDesc**. The plan state is described according to a scheme agreed on by the parties of the project.

{{xtabulatef IM_plan--ltFeature--gt}}

**Details:**  

{{refsec planinformation}}

{{refsec routeplanningplaninformation}}

{{refsec watersupplyandsewerageplaninformation}}

## Quantity information {#sec:qauntityinformationext}

Calculated area of a surface (**\<Surface>**) or the volume below (between two surfaces) can be transferred using "IM_quantity" extension. These quanties may also be assingned to a part of a surface (**\<Surface>**.**\<SourceData>**.**\<Boundaries>**.**\<Boundary>**) or an area defined as a **\<Parcel>**.

{{xtabulatef IM_quantity--ltFeature--gt}}


## Soil properties {#sec:soilpropertiesext}

Soil properties of terrain model or ground layer model are captured in "IM_soil" feature extension.

{{xtabulatef IM_soil--ltFeature--gt}}

**Details:**  

{{refsec terrainmodel}}

{{refsec groundlayermodel}}


## String line model {#sec:stringlinemodelext}

The string line model is composed of *line string alignments* **\<IrregularLine>**. Their order with an **\<Alignment>** is irrelevant. The string line model used in Inframodel is based on the Leica RoadRunner software.

The string line model is defined under an **\<Alignment>** in the **"IM\_stringlineLayers"** extension. The constituent line strings and their locations are set by layer in the **"IM_stringlineLayer"** child element.  The order of description of the line strings does not matter, the alignments are identified by their unique name **\<Alignment>.** name, which are listed in the element, separated by commas. A layer is assigned a **name** and optionally a **centerline**. When describing a layered structure the layers of the string line model are assigned surface codes **SurfaceCoding**. The same line string may belong to several different layers. Layer are listed starting from the top downwards.

{{xtabulatef IM_stringlineLayers--ltFeature--gt}}

{{xtabulatef IM_stringlineLayer--ltFeature--gt}}

**Details:**

{{refsec stringlinemodel}}


## Cross-section parameters {#sec:crosssectionparametersext}

*Cross-section parameters* contain parametric information considered crucial for each route type. They are set for the *stationing reference alignment* in the **\<CrossSects>**.**\<CrossSect>** "IM_crossSect" extension under the **\<Alignment>** element. The chosen cross-section parameters are set in fields (**\<Property>**). It is advisable to describe all parameters for each cross-section. If the some parameters change, the cross-section where the parameter begins to change and the end of the transition are described.

{{xtabulatef IM_CrossSect--ltFeature--gt}}

**Details:**

{{refsec crosssectparameters}}

{{refsec crosssectionsandtrackinformation}}

{{refsec crosssectionparameters}}


## Structural layer properties {#sec:structureallayerpropertiesext}

Material properties of layers in road, street or railway structual model are captured in "IM_structLayer" feature extension.

{{xtabulatef IM_structLayer--ltFeature--gt}}

**Details:**  

{{refsec roadsandstreetsstructurallayers}}

{{refsec railwaystructurallayers}}

## Road and street design - Road signs {#sec:roadsignext}

Road signs belonging to a particular route design are described in **\<Roadways>**.**\<Roadway>**.**\<Roadside>**.**\<RoadSign>**, with detailed properties captured in "IM_roadSign" feature extension:

{{xtabulatef IM_roadSign--ltFeature--gt}}

## Railway design - KM post coordinates {#sec:kmpostcoordinatesext}

To assign northing and easting coordinates to railway **\<Alignment>**.**\<StationEquation>**, the parameters are:

{{xtabulatef IM_kmPostCoords--ltFeature--gt}}

**Details:**

{{refsec kmposting}}



## Railway design - switches {#sec:switchesext}

Switch details at railway track **\<Alignment>**.**\<CoordGeom>**.**\<Line>**, the parameters are:

{{xtabulatef IM_switch--ltFeature--gt}}

**Details:**

{{refsec switchinformation}}


## Utility networks - network type {#sec:networktypeext}

When the attribute pipeNetType in \>PipeNetwork> element is set to 'other', the type of utility network may be speficied in "IM_pipeNetworkType" extension:

{{xtabulatef IM_pipeNetworkType--ltFeature--gt}}

## Utility networks - structure details {#sec:structuredetailsext}

It is possible to describe additional details of network structures described in inframodel file transfers. The parameters in "IM_struct" are:

{{xtabulatef IM_struct--ltFeature--gt}}

**Details:**

{{refsec circularstructures}}

{{refsec rectangularstructures}}

{{refsec pipeinletsandoutlets}}

{{refsec pipeconnection}}

{{refsec equipment}}

## Utility networks - pipe details {#sec:pipedetailsext}

It is possible to describe additional details of pipes of a network described in inframodel file transfers. The parameters in "IM_pipe" are:

{{xtabulatef IM_pipe--ltFeature--gt}}

**Details:**

{{refsec circularpipes}}

{{refsec eggpipes}}

{{refsec ellipticpipe}}

{{refsec rectangularpipe}}

{{refsec channels}}

## Utility networks - cable details {#sec:cabledetailsext}

It is possible to describe additional details of cables of a network described in inframodel file transfers. The parameters in "IM_cable" are:

{{xtabulatef IM_cable--ltFeature--gt}}

**Details:**

{{refsec cable}}

## Plan features {#sec:planfeaturesext}

Planimetric features belonging to a particular route design are described in **\<Roadways>**.**\<Roadway>**.**\<PlanFeature>**, or in other cases in **\<PlanFeatures>**.**\<PlanFeature>**. In addition of capability of being classified using "IM_coding" extension (and/or "IM_proprietaryCoding") and having custom properties using "IM_userDefinedProperties", detailed propeties may be assigned by the type of plan feature:

{{xtabulatef IM_footing--ltFeature--gt}}

{{xtabulatef IM_railing--ltFeature--gt}}

{{xtabulatef IM_fence--ltFeature--gt}}

{{xtabulatef IM_surfaceStructure--ltFeature--gt}}

{{xtabulatef IM_planFeature--ltFeature--gt}}

**Details:**

{{refsec roadplanfeatures}}

{{refsec railwayplanfeatures}}

{{refsec waterwayplanfeatures}}

{{refsec planimetricfeatures}}

## As-built survey points {#sec:asbuiltsurveypointsext}

Inframodel enables transfering both planned control points with tolerances (**\<Cgpoints>** as top-level collection), and the measured values (**\<Survey>**.**\<Cgpoints>**), both having detailed properties assign to the collection as "IM_cgpoints":

{{xtabulatef IM_cgpoints--ltFeature--gt}}

Instrument accuracy code may be set with "IM_survey" \<Feature> extension

{{xtabulatef IM_survey--ltFeature--gt}}

**Details:**

{{refsec controlpoints}}

{{refsec asbuiltsurvey}}

## Spatial allocation and spatial avoidance {#sec:spatialallocationandavoidanceext}

An area or a space allocated for some specific use, or a perimeter around an object to be avoided can be defined using "IM_spatialZone" extension, applicable to  **\<PlanFeature>**, **\<Parcel>**, **\<Pipe>** or **\<Struct>**.

{{xtabulatef IM_spatialZone--ltFeature--gt}}

**Details:**

{{refsec planimetricfeatures}}

{{refsec surfacetructures}}

{{refsec structures}}

{{refsec pipes}}
