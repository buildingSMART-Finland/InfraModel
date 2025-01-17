{{schemafile ../schema/inframodel-raw.xsd}}
# File headers {#sec:fileheaders}

## XML file header {#sec:xmlfileheader}

Inframodel XML files shall use UTF-8 character encoding, and encoder attribute shall be set on XML header.

Example:

```xml
<?xml version="1.0" encoding="UTF-8"?>
```


## LandXML container {#sec:landxmlcontainer}

The namespaces in Inframodel file shall be the following:

- The default namespace to be used without prefix for all LandXML elements specialized for Inframodel in schema inframodel.xsd shall be set in the root element as 
  "{{release_directory}}"
- The namespace for elements in Inframodel extension schema im.xsd (if used in the file) to be used with prefix "im" shall be set in the root element as 
  "{{release_directory}}/im"

**Note: The namespace URI is not meant to be used to look up information. Its sole purpose is to give the namespace a unique name.**


The schema locations may be set in an Inframodel transfer file, in which case XML Schema Instance namespace shall be declared in the root element: xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance", and the following schema locations may be set to access online:

- The schema location (xsi:schemaLocation) for the default namespace as 
  "{{release_directory}} {{release_directory}}/inframodel.xsd"
- If elements from im namespace are used in the file, the "im.xsd" schema location (xsi:schemaLocation) as 
  "{{release_directory}}/im {{release_directory}}/im.xsd"


The root element (\<LandXML\>) of the transfer file is used by software to check the validity of the file structure.

{{xtabulate LandXML}}

XML example of \<LandXML\>:

```xml
<LandXML xmlns="{{release_directory}}" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:im="{{release_directory}}/im" xsi:schemaLocation="{{release_directory}} {{release_directory}}/inframodel.xsd {{release_directory}}/im {{release_directory}}/im.xsd" date="2025-01-17" time="09:30:47+02:00" version="1.2"\>
    <Units>
    <CoordinateSystem>
    <Project>
    <Application>
    <Alignments>
    <CgPoints>
    <Parcels>
    <PlanFeatures>
    <PipeNetworks>
    <Roadways>
    <Surfaces>
    <Survey>
    <FeatureDictionary>
    <im:Metadata>
    <im:LocalCoordinateTransformation>
    <im:PileGroups>
</LandXML>
```

## Units {#sec:units}

The units used in the file are defined by the \<Units\> element. Only certain metric SI system units are allowed, and those are defined under the sub-element \<Units>\<Metric>.
Angular (angularUnit) and direction (directionUnit) units are defined counter-clockwise from the base direction. In angular definitions the base direction is east, and in direction definitions it is north.

{{xtabulate Units}}

{{xtabulate Metric}}

## Coordinate and height systems {#sec:coordinateandheightsystems}

The height and coordinate system information is defined in the element \<CoordinateSystem>. 
Exactly one coordinate system shall be defined:

- by defining the \<CoordinateSystem>.epsgCode using the European Petrol Survey Group (EPSG) naming system without a prefix.
- or by defining local system(s) with \<CoordinateSystem>.horizontalCoordinateSystemName (and optionally the \<CoordinateSystem>.verticalCoordinateSystemName).

\<CoordinateSystem>.desc attribute may provide informal information about the system used.

It is also possible to set a rotationAngle for the coordinate system.


{{xtabulate CoordinateSystem}}



### Local coordinate transformation by point pairs {#sec:localcoordinatetransfromationbypointpairs}

Local coordinate system may be defined as set of control points sourceCRS-targetCRS point pairs under "IM_coordTransformation" \<Feature> extension. 
See {{refsec localcoordinatetransfromationbypointpairsext}} for detailed information

### Local coordinate transformation by transformation parameters {#sec:localcoordinatetransfromationbytransformationparameters}

The exact parameters of a local coordinate transformation may be given using \<im:LocalCoordinateTransformation> element in im-extension schema as \<any> element under \<LandXML>. 
The im namespace xml schema (im.xsd) for the extension schema elements is available at Inframodel schema page.

{{xtabulate im:LocalCoordinateTransformation ../schema/im.xsd}}

Coordinate systems use a reference ellipsoid, defined by the semi-major and semi-minor axis, to approximate the shape of the Earth. The datum is then defined by the ellipsoid and its location and orientation, i.e. different datums can use the same ellipsoid but its position varies.

For example, the WGS84 system uses a reference ellipsoid with a semi-major axis of 6 378 137m and a semi-minor axis of 6 356 752m. The ellipsoid center is located at the Earth's center of mass.

#### Source coordinate reference system
{{xtabulate im:SourceCRS ../schema/im.xsd}}

where

{{xtabulate im:Ellipsoid ../schema/im.xsd}}

{{xtabulate im:PrimeMeridian ../schema/im.xsd}}

#### Target coordinate reference system
{{xtabulate im:TargetCRS ../schema/im.xsd}}

#### Datum transformation
{{xtabulate im:DatumTransformation ../schema/im.xsd}}

Helmert3D performs a coordinate transformation from one datum to another.

{{xtabulate im:Helmert3D ../schema/im.xsd}}

#### Projection
{{xtabulate im:Projection ../schema/im.xsd}}

Transverse Mercator Map projection \<im:Projection>.\<im:TransverseMercator> transforms geographical coordinates (latitude, longitude, altitude) to a plane (x, ,y, z). The grid origin is taken on the central latitude and longitude, and false easting and northing is then applied to prevent negative coordinates west or south of the origin.

{{xtabulate im:TransverseMercator ../schema/im.xsd}}

#### Local transformation

In LocalTransformation \<im:LocalTransformation>, Helmert2D \<im:Helmert2D> transforms the projected (x,y,z) coordinates to the local coordinate system. FittedPlane \<im:FittedPlane> corrects height values using a plane as the geoid model. The corrected height at point (northing,easting,elevation) is elevation\_corrected = elevation + (a\*northing + b\*easting + c).

{{xtabulate im:Helmert2D ../schema/im.xsd}}

{{xtabulate im:FittedPlane ../schema/im.xsd}}

## Project {#sec:project}

\<Project> element defines base data of the project, including it's name description and classification system definitions. 

The description may contain ie. the project long name or code. 

The state attribute may be used to describe the state of the project and its content. Sub-elements of the file however may override the state value defined here by setting their own state attribute.

{{xtabulate5 Project}}

where:

{{xtabulate stateType}}


## Type coding systems {#sec:typecodingsystems}

The meaning (semantic) of the points, lines and surfaces is defined in the file. The parties of a project agree on type coding systems that are used in the data transfer.

The main coding systems are set in the "IM_codings" extension *(exactly one in each file)* using \<Feature> element under \<Project>, defining:

1. The terrain description coding system (source data points and breaklines)(*terrainCoding*)
2. The surface/category description coding system (*surfaceCoding*)
3. The coding system for infrastructure objects (including alignments and breaklines, pipe netweorks, plan features) (*infraCoding*)

The existing terrain description contains source data points and breaklines. The surface description consists of the individual surfaces of the base data (terrain and ground layers) or the planned route or areal structures as TIN surface model or string line model. In addtion to surfaces, planned objects may be described as alignment geometry, line strings or points. It is possible to set the same type coding system for more than one of these.

In addition to the main coding systems, it is also possible to define additional or alternative type coding systems *(none, one or more e.g. Company X etc.)*, using "IM_proprietaryCodings" extension (one instance per coding system) under \<Project>. When a code from a proprietary system is used for an element, each "IM_proprietaryCoding" \<Feature> instance placed under the element being coded shall identify the coding system by its property proprietaryInfraCodingSource, having the same value as the system name set in "IM_proprietaryCodings" property proprietaryInfraCoding.

Detailed information about "IM_codings", "IM_proprietaryCodings" and "IM_userDefinedProperties" \<Feature> extensions can be found from {{refsec inframodelfeatureextensions}}


## Application {#sec:application}

The \<Application> element describes what software was used to create the file. If the file has been created using several different applications, all are described by their own \<Application> element.

{{xtabulate Application}}

## Authors {#sec:authors}

Information of the author of the file is recorded in the sub-element \<Application>.\<Author>. It is possible to define several authors as separate \<Author>-elements.

{{xtabulate Author}}

## Feature dictionary {#sec:featuredictionary}

The \<FeatureDictionary> identifies the specification source of extensions used in the file, and the point of access to their documentation.

The contents of \<Feature> elements shall follow the source specification. LandXML-files in general may contain extensions from several different sources. In Inframodel file transfer, proper recognition and interpretation is required only for the extensions documented in this specification ( e.g. for the type coding systems used in an Inframodel file).
  
The dictionary for Inframodel extensions shall be specified using \<FeatureDictionary> element as shown in the table below. 

The name attribute shall be unique, and always 'inframodel' for the dictionary of Inframodel extensions, and exactly the same value shall be set in every Inframodel \<Feature> for attribute source (the \<Feature> attribute code being labeled with IM_ -prefix).

The \<version> should match the version number of the Inframodel schema. 
  
\<DocFileRef> element can be used to provide the URI link to named external documentation where applicable feature code and property type values are described ( {{refsec inframodelfeatureextensions}} in the case of Inframodel feature dictionary).

{{xtabulate FeatureDictionary}}

Proprietary extensions can be included in addition to Inframodel extensions, as "IM_userDefinedProperties" (generic extension specified in Inframodel feature dictionary)
For more information about "IM_userDefinedProperties" see {{refsec userdefinedpropertiesext}}

## Metadata {#sec:metadata}
  
Metadata is described with the **\<im:Metadata>** element (specified im-extension schema) as **\<any>** element under **\<LandXML>**. The im namespace xml schema (im.xsd) for the extension schema elements is available at Inframodel schema page.

Metadata is optional and enables the following features shown below.
  
{{xtabulate im:Metadata ../schema/im.xsd}}

Where:

{{xtabulate im:CreatedBy ../schema/im.xsd}}

{{xtabulate im:ContactInformation ../schema/im.xsd}}

{{xtabulate im:DataOwner ../schema/im.xsd}}

{{xtabulate im:History ../schema/im.xsd}}

{{xtabulate im:ModifiedTimestamp ../schema/im.xsd}}

{{xtabulate im:DataQuality ../schema/im.xsd}}

{{xtabulate im:Source ../schema/im.xsd}}

{{xtabulate im:ModelStatus ../schema/im.xsd}}

