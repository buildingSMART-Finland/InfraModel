{{schemafile ../schema/inframodel-raw.xsd}}
# Area structures {#sec:areastructures}

*Area structures* encompass descriptions of surfaces and boundaries that complement routes. Such descriptions are for e.g. landscaping, noise barriers and geostructures. The file in which these structures are described contains the header information presented in {{refsec fileheaders}}. Area structures are described as *defined areas*  **\<Parcel>** with **\<CoordGeom>**, or as  *surfaces* **\<Surface>**. The surface description consist of triangular meshes as explained in {{refsec basedata}}, where it is also possible to attach random points **\<DataPoints>** and breaklines **\<BreakLines>** to the surfaces. 

## Landscaping {#sec:landscaping}

Landscaping encompasses the areas surrounding a design entity. The description consists of a surface description, which is described in further detail in {{refsec terrainmodel}}. The surface description consists of a triangle mesh, which may have random points or breaklines attached to it. Structural surfaces or cross-sections are usually not defined for landscaping.

The landscaping *plan information* is defined in the optional extension "IM_plan". A *surface code* (**SurfaceCoding**) is set for the surfaces . It is also possible to set an alternative type coding (**proprietaryInfraCoding**).

Contents of landscaping:

- surface model
- structural model

Optional surface information
- random points <**DataPoints**>
- breaklines <**BreakLines**>
 
![Surface model]({{figure SurfacesPintamalli.png}} "Surface model"){{figst surfacemodel}}
 
![Ground layer model]({{figure SurfacesMaaperamalli.png}} "Ground layer model"){{figst groundlayermodel}}	


## Noise barriers {#sec:noisebarriers}

Noise barriers are a central part of route planing. The process of describing the components is described in detail in {{refsec terrainmodel}}. The The surface description consists of a triangle mesh, which may have random points or breaklines attached to it. Structural surfaces or cross-sections are usually not defined for noise barriers.

The noise barrier *plan information* is defined in the optional extension "IM_plan". A *surface code* (**SurfaceCoding**) is set for the surfaces . It is also possible to set an alternative type coding (**proprietaryInfraCoding**).

Contents of noise barrier:

- surface model
- structural model

Optional surface information
- random points <**DataPoints**>
- breaklines <**BreakLines**>


## Geostructures {#sec:geostructures}

*Geostructures* refer to area-like structures that can be easily described in terms of surfaces. Examples include stacking of excess mass and subgrade reinforcement, which are possible to describe as surfaces such as described in {{refsec groundlayermodel}}.

The process of describing the components is described in detail in {{refsec terrainmodel}}. The The surface description consists of a triangle mesh, which may have random points or breaklines attached to it. Structural surfaces or cross-sections are usually not defined for geostructures.

The geostructure *plan information* is defined in the optional extension "IM_plan". A *surface code* (**SurfaceCoding**) is set for the surfaces . It is also possible to set an alternative type coding (**proprietaryInfraCoding**).

Contents of geostructures:

- surface model
- structural model
Optional surface information
- random points <DataPoints>
- breaklines <BreakLines>
 
![Surface model]({{figure SurfacesPintamalli.png}} "Surface model"){{figst surfacemodel}}

![Ground layer model]({{figure SurfacesMaaperamalli.png}} "Ground layer model"){{figst groundlayermodel}}	
 
## Surface structures {#sec:surfacetructures}

*Surface structures* potentially span across multiple routes (such as urban street surface plans), or need not be associated with any route plan. These structures are described as *defined areas* under **\<Parcels>** collection, having one or several **\<Parcel>** elements. Optional *plan information* is defined in the extension "IM_plan" for **\<Parcels>** collection, which may also be given a unique **name**. Each **\<Parcel>** shall have a unique **name**, and either its location as **\<Center>** or its boundaries as **\<CoordGeom>**. 
 
The properties of *surface structure* are defined in "IM_surfaceStructure":
 
{{xtabulate IM_surfaceStructure--ltFeature--gt}}
 
*Surface structure* may also have calculated area or volume quantities assinged as "IM_quantity" extension:
 
{{xtabulate IM_quantity--ltFeature--gt}}
 
An area defined as a **\<Parcel>** may have an adjoining area spatial allocation or spatial avoidance (or both). These can be described using "IM_spatialZone" extension:
 
{{xtabulate IM_spatialZone--ltFeature--gt}}
 
![Spatial Zone Area]({{figure SpatialZoneArea.png}} "Spatial Zone Area"){{figst spatialzonearea}}
