{{schemafile ../schema/inframodel-raw.xsd}}
# Deep foundations {#sec:deepfoundations}

An Inframodel file of any plan contains the header information described in {{refsec fileheaders}}.

This section describes deep foundations (such as pile groups) transferred using **\<any>** element under **\<LandXML>**. The xml schema (im.xsd) for these extensions is available at Inframodel schema page.

## Pile groups {#sec:pilegroups}

Collection of **pile groups** in a soil stabilization plan.

{{xtabulate im_PileGroups--ltFeature--gt}}

## Pile group {#sec:pilegroup}

Each individual pile group in a pile groups collection representing a stabilization plan is described under **\<im:PileGroup>** element. Each pile group shall have an inividual identifier **oID**, and may have a **name** and **description**. A number of other attributes may used to describe the material properties of the pilings; spacing between piles (center to center) in the grid can be spcified in **pileSpacing** attribute. The size of an individual pile can be specified in subelement **\<im:CircPile>** or **\<im:SquarePile>**, respectively (choice by the type of pile cross section).


![Pile group]({{figure pilegroup.png}} "Pile group"){{figst pilegroup}}

Attributes of \<im:PileGroup>:

{{xtabulate im_PileGroup--ltFeature--gt}}

The size of an individual pile in a pile group is set in \<im:CircPile>\ or \<im:SquarePile>\, respectively. All piles in a group are expetected to share the same shape and size.

{{xtabulate im_CircPile--ltFeature--gt}}

{{xtabulate im_SquarePile--ltFeature--gt}}

The top and bottom boundaries of a pile group are given in **\<im:TopBoundary>** and **\<im:BottomBoundary>** elements as irregular lines, defined by point lists (min. 3 points with 2D northing easting coordinates separated by spaces); the delimiting surfaces at the top and at the bottom may set by reference in **surfaceRef** attribute to the **\<Surface>** element with geometry definition, or the coding of the initial and target surfaces may be given in "IM_coding" **\<im:Feature>**.

## Pile {#sec:pile}

Individual piles in a pile group are described under **\<im:Pile>** element. Each pile shall have an individual identifier **oID** and **status**, as well as optional **topPoint**, **bottomPoint**, **horizontalDirection** and **slope**.

Attributes of \<im:Pile>:

{{xtabulate im_Pile--ltFeature--gt}}

Attributes of \<im:GroutLayer>:

{{xtabulate im_GroutLayer--ltFeature--gt}}
