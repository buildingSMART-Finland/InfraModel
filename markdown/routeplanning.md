{{schemafile ../schema/inframodel-raw.xsd}}
# Route planning {#sec:routeplanning}

## Contents

Routes encompass highways, local roads and private roads, waterways and railways. Each route has one continuous stationing reference alignment and a vertical alignment. In inframodel file transfer, a route plan may consist of route geometric alignments, their stringline models and surface or structural models as triangulated meshes.

An *alignment group* \<Alignments> consists of one or several alignments \<Alignment>. Their geometry can be described in two ways:
- Geometric alignment 
- Line string 

Geometric alignments describe parameters of the horizontal and optional vertical elements of an alignment. A line string is a description where consecutive points are connected by line segments (in 2D or 3D). Geometric alignments are typically used to describe the stationing reference line of a road as well as other important geometric descriptions such as road edges. Other route components are usually described as line strings.

![Route geometry]({{figure Road_Geometriakuvaus.png}} "Route geometry"){{figst routegeometry}}


Once the alignments have been described, it is possible to assign them to a string line model, that contains a description of the layers of the route structure, as described in {{refsec stringlinemodel}}. Alternatively, a triangulated surface mesh model can be used to represent the top surface of a route, or its structural model can composed by describing all its layers as triangulated mesh surfaces.

Cross-section parameters, which are described in further detail in the sections covering each route type, complement the route description with design parameter information of the cross-sections (without actual cross section geometry).

### Route description

Route description is driven by stationing reference line (principal alignment). Other geometry lines are given in the same *alignment collection* \<Alignments> each as separate *alignment* \<Alignment>. Geometry lines and string lines are given in separate *alignment collections* \<Alignments>.

Different routes, alignement options and stationing reference line discontinuities are placed in *separate* \<Alignments>.

### Naming and Type coding

*Alignment groups* and each individual *alignment* within a group must be assigned unique name. It is advisble to use different naming convention for *geometric alignments* and line strings in string line models. 

Assigning *type codes* to alignments is optional in Inframodel file transfers. The type coding systems to be used for an **\<Alignment>** shall be defined in the project information. The type code can then be set for each **\<Alignment>** element (whose children inherit the applied coding) in the extension "IM_coding" with the **infraCoding** and its description **infraCodingDesc**. Alternative or additional type coding systems can used (if defined in the project information) and each such type code is set for **\<Alignment>** element using "IM_proprietaryCoding" with **proprietaryInfraCoding**, reference to the coding system (defined in the project information) by **proprietaryInfraCodingSource** and description **proprietaryInfraCodingDesc**.

Layers of a string line model, described in optional "IM_stringLineLayers" extension may also have type codes, as well as the triangulated meshes surfaces in surface or structural models, using "IM_coding" with **surfaceCoding** and its description **surfaceCodingDesc**, or also as "IM_proprietaryCoding".

## Composing alignments

The names *name* of *alignment groups* \<Alignments> are unique. The **state** attribute is optional. The *description* attribute **desc** is also optional and may be used to describe the *alignment group* \<Alignments> in further detail.

{{xtabulate Alignments}}

An **\<Alignment>** is an element that describes 
1. a geometric alignment or 
2. a line string
  
The alignments within a file do not have to be presented in any particular order. It is, however, advisable to first describe geometric alignments and then line strings. The **\<Alignment>** definition describes a **name**, **length**, *the stationing start* **staStart** and the **state** of the **\<Alignment>**. It is recommended that lines are named in an intuitive fashion. If the **state** is set for the entire alignment group **\<Alignments>** the **\<Alignment>** elements will inherit the **state** attribute from the parent element, hence is should not be set. When alternative alignments are being described by different *alignment groups* the differences between elements can be described briefly in the  atrribute **desc**. The optional *object identifying number* **oID** makes object management easier in applications.

{{xtabulate5 alignment}}

A *geometric alignment* contains a horizontal geometry in a **\<CoordGeom>** element and the corresponding *vertical alignment* in a **\<Profile>**.**\<ProfAlign>** element. Line strings are described as a chain of 3D points in the **\<CoordGeom>** element.

### Plan information

The *plan information* of an *alignment group* is described under the **\<Alignments>** element in the optional extension "IM\_plan". If the plan consists of subsets that progress at a different rate or there is some other reason to partition the project into smaller entities, these subsets should be sorted into separate *alignment groups*. The *plan information* contains information about the **planName**, the **planCode**, the **planState** and a description of the plan, **planDesc**. The state is described according to a system agreed on by the parties of the project. See sample in the table below. The *plan information* is also set when describing the surfaces of a route. These are set in the "IM_plan" extension of the **\<Surfaces>** element.

{{xtabulate5 IM_plan}}


## Geometric alignments

The geometric alignment contains the horizontal and vertical alignment information. The *horizontal alignment* information is described in the **\<CoordGeom>** and the corresponding (0 or 1) *vertical geometry* in the element **\<Profile>**.**\<ProfAlign>**. For the connection between horizontal and vertical geometry it is crucial that the geometric description is continuous from the beginning of the first element to the end of the last element. The *horizontal geometry* is described using a 2D coordinate representation, and the final elevation values along the element can only be produced once the vertical geometry is finished. The illustration below shows the horizontal and vertical geometry definition and their connection principal, the optional **staStart** attribute in **\<Line>**, **\<Curve>**, **\<Spiral>** and **\<Profile>** **SHALL NOT** be used for calculating horizontal or vertical geometry.

![Alignment]({{figure Alignments_Hor_Ver.png}} "Alignment"){{figst alignment}}

### Horizontal geometry

The dimensioning components of horizontal alignments:

- **\<Line>**
- **\<Curve>**
- **\<Spiral>**

The horizontal alignment is a listing of consecutive dimensioning components, starting at the **staStart** of the parent **\<Alignment>**. The precise location of the elements is defined in terms of 2D coordinates.

![Horizontal geometry]({{figure Road_Line-curve-spiral.png}} "Horizontal geometry"){{figst horizontalgeometry}}

inframodel does not use attributes for the  **\<CoordGeom>** element.

{{xtabulate CoordGeom}}

#### Line

A **\<Line>** is defined by **\<Start>** and **\<End**> 2D coordinates (3D definition of is possible, but should not be used in horisontal alignment definitions). In addition, attributes *direction* **dir** and **length** are mandatory, but shall be used as additional information only.

1. {{xtabulate5 Line}}
2. The format for the **\<Start>** and **\<End>** coordinates of a **\<Line>**, the 2D coordinates are separated by spaces.

{{xmlsnippet Start}}

{{xmlsnippet End}}

#### Curve

A circular arc **\<Curve>** is defined by **\<Start>** **\<Center>** and **\<End>** 2D coordinates (3D definition of is possible, but should not be used in horisontal alignment definitions). In addition, attributes *direction of rotation* **rot**, **chord**, *end direction* **dirEnd**, *start direction* **dirStart**, **length** and **radius** are mandatory, but shall be used as additional information only.

1. {{xtabulate5 Curve}}
2. The **\<Start>**, **\<Center>** and **\<End>** of a **\<Curve>**, the 2D coordinates are separated by spaces.

{{xmlsnippet Start}}
  
{{xmlsnippet Center}}
  
{{xmlsnippet End}}

#### Transition curve

A **\<Spiral>** is defined by **\<Start>**, *point of intersection of the end tangents* **\<PI>** and **\<End>** 2D coordinates (3D definition of is possible, but should not be used in horisontal alignment definitions), together with mandatory attribute *transition curve type* **spiType**. In addition, attributes **length**, *end radius* **radiusEnd**, *start radius* **radiusStart**, *direction of rotation* **rot**, the *transition curve parameter* **constant**, *end direction* **dirEnd** and *start direction* **dirStart** are mandatory. In Finnish route design the default *transition curve type* is an Euler spiral "clothoid"; bi-quadratic parabola "biquadraticParabola", or third-degree spiral "cubic" may be used under special circumstances e.g. in railway design.

NOTE: since attribute **spiType** is mandatory, but has no meaning for "biquadraticParabola" or "cubic", it shall have value set to "NaN" in these cases.

{{xtabulate5 Curve}}

The **\<Start>**, point on intersection of start and end tangents **\<PI>** and **\<End>** are defined as 2D coordinates separated by spaces.

### Vertical geometry

The vertical geometry is described in the **\<Profile>**.**\<ProfAlign>** element in concert with the horizontal geometry. In Inframodel, each horizontal geometry can have only one (or 0) vertical geometry. The dimensioning components of the vertical geometry are:

- Point of Vertical Intersection **\<PVI>**
- Vertical circular arc **\<CircCurve>**

![Vertical geometry]({{figure Road_PVI_CircCurve.png}} "Vertical geometry"){{figst verticalgeometry}}

{{xtabulate5 Profile}}

{{xtabulate5 ProfAlign}}

#### Point of vertical intersection

The first and last element of the *vertical profile* is always *a Point of Vertical Intersection* **\<PVI>**.

*A Point of Vertical Intersection* **\<PVI>** marks the ends of the line segments of a vertical geometry. *A Point of Vertical Intersection* is described by a **station** and an **elevation**. These are separated by a space.

{{xtabulate5 PVI}}

#### Vertical curve

Vertical circular arcs may be combined into S-curves or compound curves. The first and last element of a vertical *profile* is never a vertical circular arc **\<CircCurve>**.

The location of the **\<CircCurve>** is defined by the *station* and *elevation*, separated by spaces.

{{xtabulate5 CircCurve}}

## Line strings

*Line strings* are defined in concert with the *horizontal geometry* **\<CoordGeom>**. *Line strings* are defined as a series of 2D points (when 2D representation is sufficient) or 3D points, hence it does not need a vertical **\<Profile>** element for 3D representation. The dimensioning element of a line string is:

- **\<IrregularLine>**

![Irregular line]({{figure Road_IrLine.png}} "Irregular line"){{figst irregularline}}

### Line string

A *line string* has optional attributes and sub-elements to define its **\<Start>**, **\<End>** and the *intermediate points* either as **\<PntList2D>** or **\<PntList3D>**.

{{xtabulate5 IrregularLine}}

## String line model

An *alignment group* **\<Alignments>** is a collection of geometric alignments and line strings. The string line model of a route is composed of their descriptions in the file, ordered into layers. The order of *alignment* descriptions within the *alignment group* does not matter. The string line model used in Inframodel is based on the Leica RoadRunner software.

![String line model]({{figure Road_stringline_model.png}} "String line model]"){{figst stringlinemodel]}}

The string line model of a **\<Alignment>** is defined by the "IM\_stringlineLayers" extension. The string line model consists of individual line strings, whose locations are described layer by layer in the "IM_stringlineLayer" child element. The order of the **\<Alignment>** elements is irrelevant, because their unique names are used as alignment identifiers **\<Alignment>.name.** Each layer of the string line model is assigned a **unique name** and the **alignments** it contains. It is optional to define a **centerline** and set the *surface codes* **surfaceCoding**.

The procedure for constructing a new layer in the string line model in the *"IM_stringlineLayers"* extension goes as follows:

1. The layer is assigned a unique **name**.
2. The constituent line string alignments are selected by addressing the line strings by their name **\<Alignment>.name** going from the left to the right. The line names are separated by commas.
3. The **centreline** may optionally be set.
4. The **surfaceCoding** and **surfaceCodingDesc** may optionally be set.

A line string may belong to several different layers. It is recommended to describe the layers in order beginning from the topmost layer. The string line model sample below utilizes the general surface coding. The sample describes a road surface and the underside of the lowest structural layer.

{{xtabulate5 IM_stringLineLayers}}

## Terrain model

The *route terrain model* (**\<Surfaces>**) contains a description of the topmost surface (one or more **\<Surface>**) of the route (Digital Elevation Model). It consists of the vertices of the component faces **\<Pnts>** and the faces **\<Faces>** as explained in {{refsec sourcedata}} Also, random points and breaklines of the surface can be described as explained in {{refsec sourcedata}}. The route terrain model shall have the same name as the route alignments group, i.e. **\<Surfaces>.name** shall match the corresponding **\<Alignments>.name**

The route terrain model consists of:

- Triangle vertices and
- Faces,
- Random points and
- Breaklines,
- Inframodel type coding.

![Terrain model]({{figure Surfaces_terrain.png}} "Terrain model]"){{figst terrainmodel]}}

{{xtabulate Surfaces}}

## Structural model

The structural model of a route contains the surface meshes of all structural layers. When several layers are transferred in the same file, they shall be described in order from top to down, as explained in {{refsec groundlayermodel}} .

![Structural model]({{figure Surfaces_Rakennemalli.png}} "Structural model]"){{figst structuralmodel]}}

![Triangulated model]({{figure Surfaces_kolmiomalli.png}} "Triangulated model]"){{figst triangulatedmodel]}}

{{xtabulate Surfaces}}

## Cross-section parameters

Cross-section parameters refer to parametric information complementing the model represented as surface or stringline models. These include design parameters such as the widths and superelevations of roads.

The relevant cross-section parameters for each route type are described in further detail in the corresponding section of each route type.
