{{schemafile ../schema/inframodel-raw.xsd}}
# File headers

## LandXML file container

InfraModel XML files shall use UTF-8 character encoding, and encoder attribute shall be set on XML header.

Example:
```xml
<?xml version="1.0" encoding="UTF-8"?>
```
The namespaces in Inframodel file shall be the following:

- The default namespace to be used without prefix for all LandXML elements specialized for Inframodel in schema inframodel.xsd shall is set in the root element as xmlns="http://buildingsmart.fi/inframodel/404"
- The namespace for elements in Inframodel extension schema im.xsd (if used in the file) to be used with prefix "im" shall is set in the root element as
xmlns:im="http://buildingsmart.fi/im/404"
- The types in Inframodel enumerations schema inframodelEnumerations.xsd are included in the http://buildingsmart.fi/inframodel/404 namespace

**Note: The namespace URI is not meant to be used to look up information. Its sole purpose is to give the namespace a unique name.**


The schema locations may be set in an Inframodel transfer file, in which case XML Schema Instance namespace shall be set in the root element: xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance

The following schema locations can be set to access online:

- The schema location for the default namespace can be set in the root element as xsi:schemaLocation="http://buildingsmart.fi/inframodel/404 https://buildingsmart.fi/infra/schema/4.0.4/inframodel.xsd"
- Additionally, if elements from im namespace are used in the file, the schema location can be set in the root element as xsi:schemaLocation="http://buildingsmart.fi/inframodel/404 https://buildingsmart.fi/infra/schema/4.0.4/inframodel.xsd http://buildingsmart.fi/im/404 https://buildingsmart.fi/infra/schema/4.0.4/im.xsd"
- The Inframodel enumerations schema inframodelEnumerations.xsd location is set automatically by being included in the default schema


The root element (\<LandXML>) of the transfer file is used by software to check the validity of the file structure. Following table defines the required and optional fields.

{{xtabulate4 LandXML}}


## Units

The units used in the file are defined by the \<Units> element. Only certain metric SI system units are allowed, and those are defined under the sub-element \<Units>\<Metric>. The following table lists valid units.
Radians are used as default direction (directionUnit) and angular (angularUnit) units. These are defined counter-clockwise from the base direction. In angular definitions the base direction is east, and in direction definitions it is north.

{{xtabulate4 Metric}}

## Coordinate and height systems

The height and coordinate system information is defined in the element \<CoordinateSystem>. At least one coordinate system shall be defined.

The Open Geospatial Consortium (OGC) naming system shall not be used in Inframodel from version 4.0 onward. 

Exactly one horizontal system shall be defined using the European Petrol Survey Group (EPSG) naming system, or other local system in current use.

The EPSG coordinate system is set in the attribute epsgCode as a valid code without prefix. 

If a local horizontal coordinate system is used instead of a EPSG system, it is set using the attribute horizontalCoordinateSystemName and the optional desc attribute can provide informal information about the system used.

Optionally, one vertical coordinate system can be specified in the attribute verticalCoordinateSystemName.
This can be either using a EPSG namimg system (EPSG prefix and code, to be given here also when it is the same as for horizontal system), or a local vertical coordinate system (and the optional desc attribute can be used to provide informal information about the system used).

It is also possible to set a rotationAngle for the coordinate system.

The name attribute should not be used in Inframodel

{{xtabulate4 CoordinateSystem}}

The optional base point of the coordinate system is given using the element \<CoordinateSystem>.\<Start>. The point is given as a 3D coordinate point, with three space delimited values.

{{xmlsnippet Start}}

For transformation between source geographic coordinate system sourceCRS and target local system targetCRS, a set of control points may be given under "IM_coordTransformation" \<Feature> extension as "IM_controlPoint" \<Feature> extensions, where each point has latitude, longitude and altitude values in source system, and corresponding local system northing, easting and elevation values. 

{{xtabulate IM_coordTransformation--ltFeature--gt}}


See {{refto ImFeatureEXT}} for detailed information about "IM_coordTransformation" \<Feature> extension.


### Local coordinate transformation parameters

The exact parameters of a particular Local Coordinate Transformation are given using \<im:LocalCoordinateTransformation> element in im-extension schema as \<any> element under <LandXML>. The xml schema (im.xsd) for the extension schema elements is available at Inframodel schema page.

{{xtabulate4 im:LocalCoordinateTransformation}}

Coordinate systems use a reference ellipsoid, defined by the semi-major and semi-minor axis, to approximate the shape of the Earth. The datum is then defined by the ellipsoid and its location and orientation, i.e. different datums can use the same ellipsoid but its position varies.

For example, the WGS84 system uses a reference ellipsoid with a semi-major axis of 6 378 137m and a semi-minor axis of 6 356 752m. The ellipsoid center is located at the Earth's center of mass.

1. SourceCRS

{{xtabulate im:SourceCRS}}

where

{{xtabulate im:Ellipsoid}}

{{xtabulate im:PrimeMeridian}}

2. TargetCRS

{{xtabulate im:TargetCRS}}

3. DatumTransformation

Helmert3D \<im:DatumTransformation>.\<im:Helmert3D> performs a coordinate transformation from one datum to another.

{{xtabulate im:Helmert3D}}

4. Projection

Transverse Mercator Map projection \<im:Projection>.\<im:TransverseMercator> transforms geographical coordinates (latitude, longitude, altitude) to a plane (x, ,y, z). The grid origin is taken on the central latitude and longitude, and false easting and northing is then applied to prevent negative coordinates west or south of the origin.

{{xtabulate im:TransverseMercator}}

5. Local transformation

In LocalTransformation \<im:LocalTransformation>, Helmert2D \<im:Helmert2D> transforms the projected (x,y,z) coordinates to the local coordinate system. FittedPlane \<im:FittedPlane> corrects height values using a plane as the geoid model. The corrected height at point (x,y,z) is z_corrected = z + (a*x + b*y +c).

{{xtabulate im:Helmert2D}}

{{xtabulate im:FittedPlane}}

## Project

\<Project> element defines base data of the project, including it's name description and classification system definitios. 

The description can contain ie. the project long name or code. 

The state attribute can be used to describe the state of the project and its content. Sub-elements of the file however may override the state value defined here by setting their own state attribute.

{{xtabulate4 Project}}

where:

{{xtabulate4 stateType}}

{{xtabulate4 IM_codings--ltFeature--gt}}

{{xtabulate4 IM_proprietaryCodings--ltFeature--gt}}

{{xtabulate4 IM_userDefinedProperties--ltFeature--gt}}

{{xmlsnippet Project}}

## Type coding systems

The meaning (semantic) of the points, lines and surfaces is defined in the file. The parties of the project agree on a type coding systems that are used in the data transfer and they are set in the "IM_codings" extension using \<Feature> element under \<Project> defining:

1. The terrain description coding system (source data points and breaklines)(*terrainCoding*)
2. The surface/category description coding system (*surfaceCoding*)
3. The coding system for infrastructure objects (including alignments and breaklines, pipe netweorks, plan features) (*infraCoding*)
4. Additional or alternative type coding systems used in the project (*proprietaryInfraCoding*)

The existing terrain description contains source data points and breaklines. The surface description consists of the individual surfaces of the base data (terrain and ground layers) or the planned route or areal structures as TIN surface model or string line model. In addtion to surfaces, planned objects may be described as alignment geometry, line strings or points. It is possible to set the same type coding system for more than one of these.

The recommended type coding system in Inframodel exchange: 
- For terrain is the Finnish Transport Infrastructure Agency type coding *Infra*]. 
- For surface and infrastructure objects, the recommended type coding system is the general InfraBIM type coding *InfraBIM*.

In addition to the main systems, it is also possible to define additional or alternative type coding systems *(one or more e.g. Ohjelmisto Z, InfraRAK2.3, Vesilaitos X, Kaupunki Y etc.)*, named as proprietaryInfraCoding (the name given here shall be used as prefix in later usage)

## Application

The \<Application> element describes what software was used to create the file. If the file has been created using several different applications, all are described by their own \<Application> element.

{{xtabulate4 Application}}

## Authors

Information of the author of the file is recorded in the sub-element \<Application>.\<Author>. It is possible to define several authors as separate \<Author>-elements.

{{xtabulate4 Author}}

## Feature dictionary

The \<FeatureDictionary> identifies the specification source of extensions used in the file, and the point of access to their documentation.

The contents of \<Feature> elements shall follow the source specification. LandXML-files in general may contain extensions from several different sources. In Inframodel file transfer, proper recognition and interpretation is required only for the extensions documented in this specification ( e.g. for the type coding systems used in an Inframodel file).
  
The dictionary for Inframodel extensions shall be specified using \<FeatureDictionary> element as shown in the table below. 

The name attribute shall be unique, and always 'inframodel' for the dictionary of Inframodel extensions, and exactly the same value shall be set in every Inframodel \<Feature> for attribute source (the \<Feature> attribute code being labeled with IM_ -prefix).

The \<version> should match the version number of the Inframodel schema. 
  
Optional \<DocFileRef> element can be used to provide the URI link to named external documentation where applicable feature code and property type values are described ({{refto IMExtensions}} in the case of Inframodel feature dictionary).

{{xtabulate4 FeatureDictionary}}

## Metadata
  
Metadata is described with the **\<Metadata>** element. Metadata is optional and enables the following features shown below.
  
{{xtabulate IM-Metadata}}
