{{schemafile ../schema/inframodel-raw.xsd}}
# Planimetric features

## Contents

In an Inframodel file, any plan contains the header information described in {{refsec Headers}}. The design content in the file is defined in metric units, using an adequate number of decimals for accuracy. For example, when the length unit in use is meter, the values must be defined to at least six decimal places.

Planimetric features, such as *cables*, lightpole or signage *footings*, *railings* and *fences*, or any other objects not otherwise defined by LandXML schema are described using **\<PlanFeature>** element. These features often interface with route (road, street, rail or waterway), in which case they are described under **\<Roadways>** collection in the same file, as defined in chapters 4, 5 and 6. This chapter covers those planimetric features not directly assigned to any particular route, and surface structures potentially spanning across multiple routes (such as urban street surface plans).

## Plan features

The planimetric features not directly assigned to any particular route (road, street, rail or waterway) are grouped in *planimetric features collections* under \<PlanFeatures> consisting of several \<PlanFeature> elements. How the planimetric features are arranged into collections (e.g. by types) is subject to project guidelines or other usage agreements. Each collection shall have a unique **name**.

{{xtabulate5 PlanFeatures}}

*Planimetric features collections* may be also be type coded in **\<Feature>** using 7. Type coding in "IM_coding" extension. In particular, this should be used when the collections contains surface structrure definition associated with the topmost surface of a plan: [InfraCoding] set to value [201000]

### Plan feature

The individual plan features are each described under <PlanFeature>, having a mandatory and unique name and optionally <Location> and geometry as <CoordGeom>.

{{xtabulate5 PlanFeature}}

**\<PlanFeature>** *geometry* is described in **\<CoordGeom>** using **line string**s for linear features, e.g. *cables*, *railings* and *fences*; in case of sruface structure boudaries, also **circular** or **spiral** curve arcs may be used. For point features, such as *footings*, location is given in **\<Location>** element as a two or three dimensional point:

{{xmlsnippet Location}}

Details of **\<PlanFeature>** are described as **\<Feature>** extension, defined for each type as follows:


1. Cable information in "IM_cable" extension
2. Footing information in "IM_footing" extension
3. Railing information in "IM_railing" extension
4. Fence information in "IM_fence" extension
5. Surface structure properties in "IM_surfaceStructure" extension
6. Generic plan feature in "IM_planfeature" extension

Additionally, all plan features may be type coded in **\<Feature>** using 7. Type coding in "IM_coding" extension.

#### Cable

Details of **\<PlanFeature>** in "IM_cable" **\<Feature>**

{{xtabulate5 IM_cable}}

todo kuva PlanFeature_cable

#### Footing

Details of **\<PlanFeature>** in "IM_footing" **\<Feature>**

{{xtabulate5 IM_footing}}

todo kuva PlanFeature_footing


#### Railing

In Inframodel, this type of planfeature covers guardrails and guide bars, as well as touch, bump and collision protection structures.

{{xtabulate5 IM_railing}}

todo kuva PlanFeature_railing

#### Fence

In Inframodel, this type of planfeature covers fences, booms and barriers, as well as gates and openings such as fence manholes.

{{xtabulate5 IM_fence}}

todo kuva PlanFeature_fence

#### Surface structure

In Inframodel, this type of planfeature covers surface structure properties (material, thickness).

{{xtabulate5 IM_surfaceStructure}}

#### Generic feature

When no specific **\<Feature>** extension defined above can be applied, these generic definitions can be used.

{{xtabulate IM_planfeature}}

#### Type coding

{{xtabulate IM_coding}}
