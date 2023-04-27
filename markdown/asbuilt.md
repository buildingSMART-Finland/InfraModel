{{schemafile ../schema/inframodel-raw.xsd}}
# AsBuilt data {#sec:asbuilt}

An Inframodel file of any plan contains the header information described in the section 1.
This section describes as-built data that can include both planned control points with tolerances, and the measured values with metadata (survey and its accuracy). Also the diffence vectors between planned (designed) and measured can be captured.

## Control points {#sec:controlpoints}

Collections of *coordinate geometry points* grouping control points on a planned surface, on a breakline or on a plan feature, with same tolerance values, are set in **\<CgPoints>** elements. Each collection has a unique **name** and a **code**, and these collections can be nested; code is set to "control" in root level control points collection, and to any approriate value in each subcollection. Optionally, a **description** can be given and a **state** can be set (usually "proposed" for planned points) for any collection of control points. Additionally, the collection may include an IM\_coding **\<Feature>** element classifying the surface, breakline or planimetric feature where the control points are assigned to. The tolerance values are set in IM_cgpoints **\<Feature>** element.

{{xtabulate CgPoints}}

### Control point {#sec:controlpoint}

Each individual control point is set under **\<CgPoint>** element, and shall have **name** that is a Universal Unique Identifier (UUID as defined in ISO/IEC 9834-8:2005), and shall be generated in compressed form as explained for IFC Globally Unique Identifier (GUID). When the **name** is a GUID, a human-readable name shall be given in **description**. Additionally, **surveyOrder** (sequence number) shall be set.

{{xtabulate CgPoint}}

### Tolerances {#sec:tolerances}

Tolerance values for all the control points under **\<CgPoints>** collection element are set in IM_cgpoints **\<Feature>** element.

Horizontal tolerance is given either

1. as allowable deviation *toleranceXY* without specified direction from a given point \<CgPoint>*northing easting*\</CgPoint>
2. or as allowable deviations from a given point <CgPoint>northing easting\</CgPoint> in specified direction dirA (e.g. along a referenced alignment) as *toleranceAmin* and *toleranceAmax*, and in perpendicular (offset) direction *toleranceBmin* and *toleranceBmax*. Both directions, dirA and perpendicular, or only one of these may be specified. Also, in both directions it is possible to specify either min or max toleance, or both. If any of these are specified, also dirA shall be.

In both cases, horizontal tolerances can be coupled with vertical tolerance values *toleranceZmin* and *toleranceZmax*. The required combination of tolerance values to be set in IM_cgpoints **\<Feature>** must be agreed for each use case separately (in Common InfraBIM Requirements or other such guidelines).

{{xtabulate IM_cgpoints}}


![As-built plan]({{figure AsBuilt_plan.png}} "As-built plan"){{figst asbuiltplan}}

## As-built survey {#sec:asbuiltsurvey}

Measured as-built data is grouped in survey collection for each surface under **\<Survey>** element. No attributes of **\<Survey>** are required to be used in Inframodel, but optionally a **description** may be given.

The mandatory element **\<SurveyHeader>** under **\<Survey>** has a mandatory **name** (to give name to the survey data set) and optional **purpose** (to be set "asbuilt").

{{xtabulate SurveyHeader}}

### Survey equipment {#sec:surveyequipment}

Under each **\<Survey>** element, an **\<Equipment>** element (no attributes) shall specify the details of the survey instrument used as **\<InstrumentDetails>**, with attributes **id** (mandatory identification) and optional **manufacturer**, **model** and **serialNumber**. These details are extended further under **\<Corrections>** element (no attributes used in Inframodel) in "IM_survey" extension **\<Feature>**.

{{xtabulate InstrumentDetails}}

{{xtabulate InstrumentDetailsandCorrectionsinIM_surveyFeature}}

The **Finnish RAK survey code list** is recommended to be used for accuracyType and corresponding accuracyDescription in Inframodel transfer.

### Survey points {#sec:surveypoints}

The survey points belonging to the survey are grouped under <Survey>.<CgPoints> element with attributes described above in 10.2: the name is used to identify the correspoding collection of control points, and code can be set to "survey" at the root of nested collections.
Within the survey points collection, another <CgPoints> element is used as a wrapper, to pair <CgPoint> elements with an "IM_cgpoints" <Feature>, and optionally also an "IM_coding" <Feature>. Each survey point <CgPoint> shall have a unique name, and pntRef shall be used to identify the corresponding control point (set as explained in 10.2.1), as well as timeStamp when surveyed (always as UTC) and surveyOrder (sequence number).

{{xtabulate CgPoint}}

3D location as surveyd is set in 
{{xmlsnippet CgPoint}}

{{xtabulate IM_cgpoints}}


![As-built survey]({{figure AsBuilt_survey.png}} "As-built survey"){{figst asbuiltsurvey}}
