{{schemafile ../schema/inframodel-raw.xsd}}
# Planimetric features {#sec:planimetricfeatures}

In an Inframodel file, any plan contains the header information described in {{refsec fileheaders}}. The design content in the file is defined in metric units, using an adequate number of decimals for accuracy. For example, when the length unit in use is meter, the values must be defined to at least six decimal places.

Planimetric features, such as *cables*, lightpole or signage *footings*, *railings* and *fences*, or any other objects not otherwise defined by LandXML schema are described using **\<PlanFeature>** element. These features often interface with route (road, street, railway or waterway), in which case they are described under **\<Roadways>** collection in the same file, as defined in chapters 4, 5 and 6. This chapter covers those planimetric features not directly assigned to any particular route, and surface structures potentially spanning across multiple routes (such as urban street surface plans).

## Plan features {#sec:planfeatures}

The planimetric features not directly assigned to any particular route (road, street, railway or waterway) are grouped in *planimetric features collections* under **\<PlanFeatures>** consisting of one or several **\<PlanFeature>** elements. How the planimetric features are arranged into collections (e.g. by types) is subject to project guidelines or other usage agreements. Each collection shall be given a unique **name**.

{{xtabulate PlanFeatures}}

*Planimetric features collections* may be type coded in **\<Feature>** using "IM_coding" extension, as well as given alternative or additional type codes in "IM_proprietaryCoding" extension. In particular, this may be practical when the collection contains surface structrure definitions associated with the topmost surface of a plan, all having the same type code.
*Planimetric features collections* may also be assigned custom properties in **\<Feature>** using "IM_userDefinedProperties" extension.

### Plan feature

The individual planimetric features are each described under **\<PlanFeature>**, having a mandatory and unique **name** and either **\<Location>** or line geometry as **\<CoordGeom>**.

{{xtabulate PlanFeature}}

**\<PlanFeature>** *geometry* is described in **\<CoordGeom>**. For linear features, e.g. *cables*, *railings* and *fences* it shall be either single **line* geometry (also **circular** or **spiral** curve arcs may be used) or **polyline** geometry. In case of *surface structure* boudaries **closed polyline** geometry shall be given (same value in both  **\<Start>** and **\<End>** of **\<IrregularLine>**). For point features, such as *footings*, location is given in **\<Location>** element as a two or three dimensional point:
  
Related to their *geometry* planimetric features may have an area or a volume for spatial allocation or avoidance defined as "IM_spatialZone" extension. Both **spatialAllocation** and **spatialAvoidance** are given as single metric value (in file length units), interpreted according to the type of the plan feature geometry definition:

Point geometry as \<Location>: 

![Spatial Zone Point]({{figure SpatialZonePoint.png}} "Spatial Zone Point"){{figst spatialzonepoint}}
   
Line or Polyline as \<CoorGeom>:

![Spatial Zone Line]({{figure SpatialZoneLine.png}} "Spatial Zone Line"){{figst spatialzoneline}}

Closed polyline area as \<CoorGeom>: 

![Spatial Zone Area]({{figure SpatialZoneArea.png}} "Spatial Zone Area"){{figst spatialzonearea}}

Details of **\<PlanFeature>** are described as **\<Feature>** extension, defined for each type as follows:


1. Cable information in {{refsec cable}} "IM_cable" extension
2. Footing information in {{refsec footing}} "IM_footing" extension
3. Railing information in {{refsec railing}} "IM_railing" extension
4. Fence information in {{refsec fence}} "IM_fence" extension
5. Surface structure properties in {{refsec surfacestructure}} "IM_surfaceStructure" extension
6. Generic plan feature in {{refsec genericplanfeature}} "IM_planfeature" extension

All plan features may be type coded in **\<Feature>** using "IM_coding" extension, as well as given alternative or additional type codes in "IM_proprietaryCoding" extension. All plan features may also be assigned custom properties in **\<Feature>** using "IM_userDefinedProperties" extension.

#### Cable {#sec:cable}

Details of **\<PlanFeature>** in "IM_cable" **\<Feature>**

{{xtabulate IM_cable--ltFeature--gt}}

![Plan Feature cable]({{figure PlanFeaturecable.png}} "Plan Feature cable"){{figst planFeaturecable}}

#### Footing {#sec:footing}

Details of **\<PlanFeature>** in "IM_footing" **\<Feature>**

{{xtabulate IM_footing--ltFeature--gt}}

![Plan Feature footing]({{figure PlanFeaturefooting.png}} "Plan Feature footing"){{figst plafFeaturefooting}}


#### Railing {#sec:railing}

In Inframodel, this type of planfeature covers guardrails and guide bars, as well as touch, bump and collision protection structures.

{{xtabulate IM_railing--ltFeature--gt}}

![Plan Feature railing]({{figure PlanFeaturerailing.png}} "Plan Feature railing"){{figst planFeaturerailing}}

#### Fence {#sec:fence}

In Inframodel, this type of planfeature covers fences, booms and barriers, as well as gates and openings such as fence manholes.

{{xtabulate IM_fence--ltFeature--gt}}

![Plan Feature fence]({{figure PlanFeaturefence.png}} "Plan Feature fence"){{figst planFeaturefence}}

#### Surface structure {#sec:surfacestructure}

In Inframodel, this type of planfeature covers surface structure properties (material, thickness).

{{xtabulate IM_surfaceStructure--ltFeature--gt}}

#### Generic feature {#sec:genericplanfeature}

When no specific **\<Feature>** extension defined above can be applied, these generic definitions can be used.

{{xtabulate IM_planfeature--ltFeature--gt}}

#### Type coding {#sec:planimetricfeaturestypecoding}

Type coding is defined in {{refsec typecodingsystemsext}}

{{xtabulate IM_coding--ltFeature--gt}}
