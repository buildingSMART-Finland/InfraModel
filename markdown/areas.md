# Area structures

## Contents

*Area structures* encompass descriptions of surfaces that complement routes. Such surfaces are e.g. landscaping, noise barriers and geostructures. The file in which these structures are described contains the header information presented in chapter 1. Area structures are described as *surfaces* **\<Surface>** in inframodel compliant file transfers. These surfaces consist of triangular meshes. It is also possible to attach random points **\<DataPoints>** and breaklines **\<BreakLines>** to the surfaces. Area structures are described in the same file as the route they are built in conjunction with, e.g. a noise barrier is in the same file as the railway it is built for.

## Landscaping

Landscaping encompasses the areas surrounding a design entity. The description consists of a surface description, which is described in further detail in section 2.4. The surface description consists of a triangle mesh, which may have random points or breaklines attached to it. Structural surfaces or cross-sections are usually not defined for landscaping.

The landscaping *plan information* is defined in the optional extension "IM_plan". A *surface code* (**SurfaceCoding**) is set for the surfaces . It is also possible to set an alternative type coding (**proprietaryInfraCoding**).

Contents of landscaping:

- surface model
- structural model

Optional surface information
- random points <**DataPoints**>
- breaklines <**BreakLines**>
 
{{figure Surfaces_Pintamalli.png}}

{{xmlsnippet Surface model}}
 
{{figure Surfaces_Maaperamalli.png}}
 
{{xmlsnippet Ground layer model}}	
 
## Noise barriers

Noise barriers are a central part of route planing. The process of describing the components is described in detail in {{refsec Terrain model}}. The The surface description consists of a triangle mesh, which may have random points or breaklines attached to it. Structural surfaces or cross-sections are usually not defined for noise barriers.

The noise barrier *plan information* is defined in the optional extension "IM_plan". A *surface code* (**SurfaceCoding**) is set for the surfaces . It is also possible to set an alternative type coding (**proprietaryInfraCoding**).

Contents of noise barrier:

- surface model
- structural model

Optional surface information
- random points <**DataPoints**>
- breaklines <**BreakLines**>

{{figure Surfaces_Pintamalli.png}}

{{xmlsnippet Surface model}}

{{figure Surfaces_Maaperamalli.png}}

{{xmlsnippet Ground layer model}}

## Geostructures

*Geostructures* in inframodel compliant file transfers refers to area-like structures that can be easily described in terms of surfaces. Examples include stacking of excess mass and subgrade reinforcement, which are possible to describe as surfaces such as described in {{refsec Ground layer model}}.

The process of describing the components is described in detail in {{refsec Terrain model}}. The The surface description consists of a triangle mesh, which may have random points or breaklines attached to it. Structural surfaces or cross-sections are usually not defined for geostructures.

The geostructure *plan information* is defined in the optional extension "IM_plan". A *surface code* (**SurfaceCoding**) is set for the surfaces . It is also possible to set an alternative type coding (**proprietaryInfraCoding**).

Contents of geostructures:

- surface model
- structural model
Optional surface information
- random points <DataPoints>
- breaklines <BreakLines>
 
{{figure Surfaces_Pintamalli.png}}

{{xmlsnippet Surface model}}

{{figure Surfaces_Maaperamalli.png}}

{{xmlsnippet Ground layer model}}
