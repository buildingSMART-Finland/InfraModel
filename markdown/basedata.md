{{schemafile ../schema/inframodel-raw.xsd}}
# Base data {#sec:basedata}

The base data contains the data points and breaklines of the source data, as well as the triangulated representation of mesh surfaces.
The surface description contains the points used to form the surface (as vertices of the triangles in TIN)).
Breaklines are not used to form surfaces, but if transferred under \<Surface> as source data they shall coincide with the triangulation defining the surface, i.e. each pair of consecutive breakline points given in 3D coordinates, must match the coordinates of two vertices of a triangle (exactly, within the numeric precision of the exchange file).

Surface meshes are used for terrain or ground layer models (top surface of each layer) as described in this section. 
They are also used for terrain (visible surface) or structural models of roads, streets, railways, waterways and area structures, as described in following sections.

Surfaces and source data is described as surface groups \<Surfaces>, which are made of individual \<Surface>-elements. 

{{xtabulate Surfaces}}

{{xtabulate Surface}}

## Plan information {#sec:planinformation}

For the surface description the project is divided into surface groups \<Surfaces> with optional "IM_plan" \<Feature> extension.
If the project consists of sub-projects that have different rates of progress, the plan contents of the file are divided into sub-projects according to the same division.
Note:The plan state is described according to a scheme agreed on by the parties of the project.

{{xtabulate IM_plan--ltFeature--gt}}

### Current and planned surfaces {#sec:currentandplannedsurfaces}

An existing surface is defined by setting the state of the \<Surfaces> or \<Surface> element to "existing". 

If all the surfaces within a surface group have the same state, it is possible to set the state on a higher level in the surface group \<Surfaces>. 
However, \<Surface> element (or its sourcedata element(s)) may override the parent state by defining its own state. 

### Type coding {#sec:typecoding}

The type coding systems used in Inframodel file transfers are set in the header information. Type codes can be set for individual plan elements:

- In the element <DataPoints> for source data points
- In the element <BreakLine> for breaklines
- In the element <Boundary> for part of surface
- In the element <Surface> for surface
- In the element <Surfaces> for surface group

Type coding is set by "IM_Coding" \<Feature> extension under a parent element.

{{xtabulate IM_coding--ltFeature--gt}}

Individual type codes are set primarily in parent elements, from which the child elements will inherit the values. 
Terrain points and breaklines are type coded using the **terrainCoding** and a coding description **terrainCodingDesc**.
It is optional to set a **surfaceCoding** and a surface coding description **surfaceCodingDesc** for terrain points and breaklines.
Surfaces are given a **surfaceCoding** and a surface coding description **surfaceCodingDesc**, and optionally **terrainCoding** and a coding description **terrainCodingDesc**.
These both may be given an **infraCoding** and its description **infraCodingDesc**. 
 
Alternative type codings can be given using "IM_proprietaryCoding" with **proprietaryInfraCoding** and their descriptions **proprietaryInfraCodingDesc**, and with **proprietaryInfraCodingSource** where they both have prefix per proprietary coding systems named under \<Project> element.
Type coding set by the parent element is also inherited by the child elements, ie. \<Surfaces> element may also set the type coding of its child elements.

### Quantity information {#sec:quantityinformation}

Calculated area or volume quantities may be assinged to entire \<Surface>, or part of it in source data \<Boundary>, using "IM_quantity" extension:
 
{{xtabulate IM_quantity--ltFeature--gt}} 
 
## Source data {#sec:sourcedata}

The source data is described by the element \<SourceData>. This element has no attributes.
Source data consists of:

 - Source data points \<DataPoints> and
 - Breaklines \<BreakLines>

![Source data]({{figure SurfacesPinnat-perus.png}} "Source data"){{figst sourcedata}}

### Data points {#sec:datapoints}

Source *data points* are described by the element \<DataPoints>, sorting every point group into individual elements. 

{{xtabulate DataPoints}}

### Breaklines {#sec:breaklines}

Source *breakline group* is described by the element \<BreakLines>, where each \<BreakLine> presents single continous line. 

{{xtabulate Breaklines}}

{{xtabulate Breakline}}

### Boundaries {#sec:boundaries}

Additionally, it is also possible to define boundaries of the source data in the boundary group \<Boundaries>, where each \<Boundary> is presented in its own element. Each boundary may have properties of the area as "IM_surfaceStructure", "IM_structLayer" or "IM_soil", as well as calculated area or volume quantities as "IM_quantity". 

{{xtabulate Boundaries}}

{{xtabulate Boundary}}
 
{{xtabulate IM_surfaceStructure--ltFeature--gt}}
 
{{xtabulate IM_structLayer--ltFeature--gt}}
 
{{xtabulate IM_soil--ltFeature--gt}}
 
{{xtabulate IM_quantity--ltFeature--gt}}

## Triangular mesh surface {#sec:triangulatedmeshsurface}

Surface geometry is described as triangulated meshes. 
Each surface is defined under the \<Definition> in terms of boundaries, exterior features and holes. 
A triangular mesh is defined in two steps:

- First by defining the vertices of the triangular faces as surface points, 
- Then each individual face by three vertices. 

The surface points used as vertices are assigned unique identifiers id within the same surface definition \<Surface>.\<Definition> element. 
The face definitions are done by referring to the id numbers id of the vertice points.

![Triangular mesh]({{figure Surfaceskolmioverkko.png}} "Triangular mesh"){{figst triangularmesh}}

{{xtabulate Definition}}

The surface type surfType is fixed to "TIN" when describing a triangular mesh. 
The presicion of the mesh model depends on the available software and data.

### Vertices {#sec:vertices}

The *vertex point group* \<Pnts> contains a listing of individual vertices \<P>, which are each assigned an individual id number id.

{{xtabulate Pnts}}

{{xtabulate P}}

### Faces {#sec:faces}

The *triangulation* is defined by the \<Faces> collection. It consists of consecutive list of faces \<F>. 
The order of the faces implicitly defines the index number of each triangle (1,2,..). 
Each face is defined by referencing three vertex id numbers.

{{xtabulate Faces}}

{{xtabulate F}}

![Triangle face definition]({{figure Surfaceskolmiokuvaus.png}} "Triangle face definition"){{figst trianglefaces}}

## Terrain model {#sec:terrainmodel}

The *terrain model* contains the description of the topmost terrain surface (also Relief or Digital Elevation Model) as one or more \<Surface> under \<Surfaces> *surface group*. 
It consists of the vertices of the component faces <Pnts> and the faces <Faces> as explained above. 
In inframodel file transfers it is also possible to assign source data points and breaklines to the surface.
An "IM_coding" \<Feature> extension enables surface classifications, and "IM_soil" \<Feature> extension allows to add the technical properties. 
Terrain model may be part of a optional plan described in "IM_plan" \<Feature>. 

![Terrain model]({{figure Surfacesterrain.png}} "Terrain model"){{figst terrainmodel}}
 
### Soil properties {#sec:soilproperties}

When no information of individual ground layers is available, surface model may define the soil propertites below the topmost surface by using "IM_soil" \<Feature> extension.

{{xtabulate IM_soil--ltFeature--gt}}

## Ground layer model {#sec:groundlayermodel}

The *ground layer model* contains a description of all the surfaces between different ground layers (and the topmost surface) in the plan. 
It is recommended that surfaces are described top-down. Individual layer surfaces are constructed as explained above.
A surface may be part of a plan described in "IM_plan" \<Feature>. 
A "IM_coding" \<Feature> extension provides surface classifications. 
The technical properties of each soil layer between two surfaces may be given in "IM_soil" <Feature> extension described above. 

![Ground layer model]({{figure SurfacesMaaperamalli.png}} "Ground layer model"){{figst groundlayermodel}}	




