# Pipenetworks {#sec:mvd-watersupplyandsewerage}

## Contents

The drainage plan can be described in the same LandXML file as the rest of the plan content. The units used in drainage planning are the metric units and coordinate systems defined in chapter 1 Headers. If the drainage system utilizes coordinate or unit systems that differ from the rest of the it should be described as a separate LandXML file.

The drainage network in the LandXML standard is a topological one. The drain wells are nodes and the pipes are edges that connect these nodes. The model provides limited tools to design drainage, sewerage and water supply networks. Inframodel file transfers have mandatory, optional and optional description elements. The following network types are implemented in the standard: storm drain, combined sewer, sewer, French drain, culvert, water pipe and "other", allowing the use of "IM_pipeNetworkType" extension for other types of networks, currently district heating, district cooling, gas and waste disposal.

Structures, such as different kind of drain wells are nodes. Pipes are defined as situated between two nodes. The ends of the pipes are modelled as virtual structures, of which there are two types, inlets and outlets. the LandXML standard supports a limited number of different structure and pipe types. Elements of Finnish design standards have been implemented in inframodel file transfers by adding extensions that expand on the LandXML element definitions.

The network topology is presented in the parent element **\<PipeNetworks>** whose child elements are individual **\<PipeNetwork>** elements. A **\<PipeNetwork>** consists of structures and pipes.

- Structures **\<Structs>**
    - types: round and rectangular wells, virtual structures, equipment and pipe joints, extensions and inflexions. (see description hierarchy *1)
    - are given an exact location
    - the pipe inlet is an **\<Invert>**
- Pipes **\<Pipes>**
    - types: Circular pipe, elliptic pipe, egg-shaped pipe, rectangular pipe and through (*see description hierarchy *2*) 
    - are given a relative location - the ending and starting structures are named    
    - the definition length is given as the distance between the centers of the terminal structures in the elevation of the inverts.    
    - the exact length may be described in the extension "IM_pipe" as a length attribute or as the arithmetic distance between the end coordinates of the pipe.    
    - pressurized sewers: described in the inframodel extension "IM_pipe" in an attribute.

{{figure Pipenetworks_general}}

The pipe network is, depending on the situation, usually described in its entirety. LandXML file transfers does not allow you to delimit the network without adhereing to the syntax. E.g. describing the inverts of the delimiting storm drain requires additional pipes and corresponding terminal structures. The process of delimiting the network is described in further detail in {{refsec Structures}} and {{refsec Pipes}}.
   

## Pipe networks {#sec:mvd-pipenetworks}

A file may contain multiple *pipe network groups* **\<PipeNetworks>**. It is mandatory to define the **name** of the pipe network and optional to give a *description* **desc** and **state** of the plan.

The *pipe network groups* are assigned unique names. If the *network group* contains networks with several different states, the **state** is not set.

{{xtabulate5 PipeNetworks}}

### Plan information

The *plan information* of the drainage plan is set in the optional "IM_plan" extension of the **\<PipeNetworks>** element. If the project consists of several sub-entities, which progress at a different rate, the plan content should be divided into several *network group* **\<PipeNetworks>** elements according to those divisions. The plan information contains the **planName** the **planCode**, the **planState**, and the *plan description* **planDesc**. The *plan state* is set according to a scale agreed on by the parties. An example is presented in the tabel below.

{{xtabulate5 IM_plan}}

## Pipe network {#sec:mvd-pipenetwork}

Individual networks are defined by **\<PipeNetwork>** elements organized under their parent element **\<PipeNetworks>**, the *network group*. The number of *networks* in one *network group* is unlimited. The *pipe network* defines a topological model, the **name** and the *network type* **pipeNetType**. The state and *description* **desc** of the network are optional.

The elements in the pipe network are assigned unique names. The **pipeNetType** defines the type of the network as 1) "sanitary" 2) "storm" 3) "water" 4) "other" (not specified, or specified in "IM_pipeNetworkType" extension). If the network contains components in different states, the **state** is not set.

{{xtabulate5 PipeNetwork}}

### Pipe network type extensions <a name="831pipenetworktypeextensions"></a>

When the *pipe network type* is other than one of those covered by the **pipeNetType** attribute of the **\<PipeNetwork>** element, the optional "IM_pipeNetworkType" extension shall be used (with the **pipeNetType** attribute set to "other").

{{xtabulate IM_pipeNetworkType}}

## Units

Drainage and water supply utilizes the units set in the header. If the water supply system utilizes a different coordinate system or units from the rest of the project, it must be stored as a separate LandXML file.

It is possible to split the network description into several files if needed.

{{xtabulate5 Pipenetworkunits}}

## Structures <a name="85structures"></a>

The topological network consists of different kind of structures whose exact location is defined in the file. The different structures in the **\<PipeNetwork>** compose the *structure group* **\<Structs>**, that has no attributes.

{{xtabulate Struct}}

LandXML standard structure types:

- Circular structures
- Rectangular structures
- Pipe inlets
- Pipe outlet
- Pipe joints, extensions or points of intersection
- Equipment (description utilizes inframodel extensions)

Dividing the network is a special case that is described in further detail in the sections covering the element that describes pipe joints, extensions or points of intersection.

{{xtabulate5 IM_struct}}

#### General data

The **name**, *rim elevation* **elevRim**, *sump elevation* **elevSump** and the **state** of the structure are mandatory attributes. 

All structural elements in the file are assigned individual names.

{{xtabulate5 Struct}}

#### Center

***Circular and rectangular structures:*** The center of the cross-section at the bottom of the well or the sump is set by 3D coordinates, separated by spaces in the **\<Center>** element.

***Pipe inlets and outlets:*** The pipe end is defined by space-separated 32-coordinates in the **\<Center>** element.

***Pipe connections:*** The **\<Center>** of a connection, joint or point of intersection at the mounting level is set using space-separated 32 coordinates.

***Equipments:*** The **\<Center>** of a piece of equipment at the mounting level is set using space-separated 2D coordinates.

{{xtabulate5 Center}}

#### Inverts

The adjoining inlet and outlet inverts are described using the element **\<Invert>**. The required attributes of invert are: the elevation **\<elev>** as the crown level for pressure pipes and the invert level for others, the flow direction **\<flowDir>** and the pipe reference **\<refPipe>**.

{{xtabulate5 Invert}}

#### Details

It is optional to present additional information of the inframodel file transfer. the structure may be labeled by a **structLabel**.

The dates of different actions may also be defined, suct as the **constructionDate** and the **renewalDate**. The dates of the actions are typically give in years. It is also possible to describe the renewal in further detail, e.g. the method used, using the **renowalDesc** attribute.

The additional information for the rim encompasses the **rimType** and the rim load bearing class **rimLoad**.

***Circular structures:***
When describing a conical well the **diameter** describes the diameter of the bottom of the cone. The **rimDiameter** describes the *inner diameter* of the rim and the **rimCenter** defines the *3 coordinates of the rim center*. The description of the sump contains a description of the *depth of the sump* **heightDeposit** and the *volume of the sump*, **volumeDeposit**. 

***Rectangular structure:***
 The description of the sump contains a description of the *depth of the sump* **heightDeposit** and the *volume of the sump*, **volumeDeposit**. 

***Equipment:***
It is possible to define more detailed type information of a piece of equipment between two pipes, e.g. a Valve using the attributes **equipmentType**, **equipmentCode** and an equipment description **equipmentDesc**. The rim is defined by the *rim type* **rimType** and *rim load bearing class* **rimLoad**. 

{{xtabulate5 IM_struct}}

### Circular structures {#sec:mvd-circularstructure}

Inspection wells of French drains are an example of a circular structure. Circular structures are defined using the structure element **\<Struct>** and its child elements.

1. Structure element **\<Struct>**
2. Structure center **\<Center>**
3. Circular structures **\<CircStruct>**
4. Inverts **\<Invert>**
5. Structure details **\<Feature>** "IM_struct" extension

The figure below illustrates the representation of a drain well, including a sump. The sump is defined in the extension "IM_struct" by defining the sump height and volume.

The *body* **diameter** at the bottom of the well, the *description* **desc**, the **material** and the **thickness** of the shell material. The well cone and sump are described in further detail in the extension "IM_struct"

{{figure Pipenetwork_CircStruct}}

{{xtabulate5 CircStruct}}

### Rectangular structures {#sec:mvd-rectangularstructures}

The illustration below describes the description method of a rectangular structure. The structure is defined using the **\<Struct>** element and its child elements:
1. General data **\<Struct>**
2. Center **\<Center>**
3. Rectangular structure **\<RectStruct>**
4. Pipe invert **\<Invert>**
5. Structure details **\<Feature>** "IM_struct" extension

The illustration demonstrates the method of description of a rectangular well, including a sump as an example. The sump is defined by its depth and/or volume.

The mandatory attributes of a rectangular structure are the **length** the direction of the long edge **lenghtDir**, the **width** of the short edge width, the **material** of the structure and the **thickness** of the surface structure.

{{figure Pipenetwork_RectStruct}}

{{xtabulate5 RectStruct}}

### Pipe inlets and outlets {#sec:mvd-pipeinletsandoutlets}

Pipe inlets and outlets are end of the pipe network pipes. The following illustration demonstrates the method of description. The virtual structures of the pipe ends are defined using the structure attribute **\<Struct>** and its child elements:

1. General description **\<Struct>**
2. Center **\<Center>**
3. Pipe inlet <InletStruct> or pipe outlet **\<OutletStruct>**
4. Inverts **\<Invert>**
5. Structure details **\<Feature>** "IM_struct" extension

The illustration below demonstrates how pipe inlets and outlets are described. The example demonstrates an outlet.

*Inlets* **\<InletStruct>** and *outlets* **\<OutletStruct>** have no attributes.

{{figure Pipenetwork_InletOutletStruct}}

{{xtabulate5 InletStruct}}

### Pipe connections {#sec:mvd-pipeconnection}

Pipe connections, joints and points of intersection are defined by the **\<Connection>** elements. The illustration bellow demonstrates the mode of description, which contains the attributes of the structure **\<Struct>** and its child elements:

1. General data **\<Struct>**
2. Center **\<Center>**
3. Pipe connections, joints or points of intersection **\<Connection>**
4. Inverts **\<Invert>**
5. Details **\<Feature>** "IM_struct" structural extension

The illustration demonstrates the description method of a point of intersection.
When using the element to delimit a pipe network, the terminal drainage well is connected to a pipe that terminates in a **\<Connection>** element. It is thus possible to also describe the connections of the outermost wells in the plan network. It is advisable to name the elements in a fashion that is clearly different from the rest of the plan, e.g. "Terminal1", "Terminal2".

When the element describes a delimiting element, all attributes are not used. The name of the structure and the description desc are set to differ from the plan informatuion as much as possible e.g. by naming them "Terminal1", "Terminal2". The elevation of the rim elevRim, the elevation of the sump elevSump and the state of the structure are left undefined.

Connections, joints or points of intersection are defined using the **\<Connection>** element, that has no attributes.

{{figure Pipenetwork_Connection1}}

{{xtabulate5 Connection}}

### Equipment {#sec:mvd-equipment}

Equipment is defined using the **\<Connection>** element. The illustration bellow describes the mode of description of a *structure* **\<Struct>** and its child elements:

1. General data **\<Struct>**
2. Center **\<Center>**
3. Equipment **\<Connection>**
4. Inverts **\<Invert>**
5. Details **\<Feature>** "IM_struct" structural extension

The illustration demonstrates the mode of description of a valve:

{{figure Pipenetwork_Connection2}}

A *piece of equipment* is defined using the element **\<Connection>**, that has no attributes. Details of the equipment is defined in the extension "IM_struct".

{{xtabulate5 Connection}}

#### Inverts {#sec:mvd-inverts}
The adjoining inlet and outlet inverts are described using the element \<Invert>. The required attributes of invert are: the elevation \<elev> as the crown level for pressure pipes and the invert level for others, the flow direction \<flowDir> and the pipe reference \<refPipe>.

{{xtabulate Invert}}


## Pipes {#sec:mvd-pipes}

The topological network consists of different kinds of structures, whose exact location is given. The pipes that compose the **\<PipeNetwork>** are described as a *structure collection* **\<Pipes>** that has no attributes. A **\<Pipe>** is defined between two structure nodes **\<Struct>** by refering to them in the start- and end-attributions.

NOTE: In the special case of "network" where there is only one single pipe (such as a culvert with no specified connection at either end), the referenced start and end structure shall be **\<InletStruct>** and **\<OutletStruct>**, respectively.

Available pipe types in the LandXML standard:

- Circular pipe
- Egg-shaped pipe
- Elliptic pipe
- Rectangular pipe
- Channel

Using a pipe to delimit a pipe network is a special case that is described separately for each pipe type.

{{xtabulate Pipe}}

### Pipe

The **name**, end reference **refEnd**, start reference **refStart**, **slope** and **state** are mandatory attributes.
Setting the exact length of a pipe is optional. All pipe elements are assigned unique names.

When using a pipe to delimit a pipe network the pipe is given a name that clearly distinguishes it from other content in the file, e.g. "Terminal1". The **name**, end reference **refEnd** and start reference **refStart** are the only mandatory attributes. The other attributes are not set.

{{xtabulate5 Pipe}}

## Center

The pipe curvature is defined by space-separated 3D-coordinates in the \<Center> element.

{{xmlsnippet Center}}

{{xtabulate5 Center}}

More details can be found from {{refsec mvd-pipedetails}}

## Details

It is optional to define details in inframodel file transfers. The label of pipe can be given using a pipeLabel. The start and end coordinates of a pipe are defined by three parameters: 

1. elevation type elevType 
2. start coordinate pipeStart and the 
3. end coordinate pipeEnd. 

The jointType sets the type of joints and connections used for the pipe. When the defined pipe is a pressurized sewer the pressureClass of the pipe is defined. Procedure details are defined with the constructionDate and renewalDate. It is also possible to define detailed information of the renewal using the renewal description renewalDesc, e.g. the method used to renew the pipe.

***Rectangular and elliptic pipe:*** *When start and end coordinates are defined, elevation type shall be given as one of the elevTypes illustrated for circular pipes.*

***Egg pipe:*** *When start and end coordinates are defined, elevation type shall be given as one of the elevTypes illustrated for circular pipes, center being at the level where the cross section is the widest.*

When the start and end coordinates are given with elevation values, elevation type shall be given as one of the enumerated elevTypes shown below.

{{figure Pipenetwork_elevType}}

***A="crown level", B="center level", C="invert level", D="bottom level"***

{{xtabulate5 IM_pipe}}

#### Circular pipes {#sec:mvd-circularpipes}

The following illustation descibes the definition of a round pipe  The definition employs the element **\<Pipe>** and its child elements.

1. Pipe **\<Pipe>**
2. Circular pipe **\<CircPipe>**
3. Center **\<Center>**
4. Pipe details **\<Feature>** "IM_pipe" extension

{{figure Pipenetwork_CircPipe}}

The **diameter**, *type description* **desc**, **material** and wall **thickness** of the pipe are mandatory attributes.

When defining a network-limiting pipe the **diameter** is the only defined attribute. Other attributes are not defined.

{{xtabulate5 CircPipe}}


### Egg pipes {#sec:mvd-eggpipes}

The following illustation descibes the definition of an egg-shaped pipe  The definition employs the element \<Pipe> and its child elements.

1. Pipe **\<Pipe>**
2. Egg pipe **\<EggPipe>**
3. Center **\<Center>**
4. Pipe details **\<Feature>** "IM_pipe" extension

Illustration of egg-shaped pipe represenation.

Mandatory attributes are *height* **height**, *width* **span**, *type description* **desc**, *material* **material** and pipe *thickness* **thickness**.

When defining a network-limiting pipe the *height* **height** and *width* **span** are set. Other attributes are not set.

{{xtabulate5 EggPipe}}

### Elliptic pipes {#sec:mvd-ellipticpipe}

The following illustation descibes the definition of an elliptical pipe. The definition employs the element \<Pipe> and its child elements.

1. Pipe **\<Pipe>**
2. elliptic pipe **\<ElliPipe>**
3. Center **\<Center>**
4. Pipe details **\<Feature>** "IM_pipe" extension

{{figure Pipenetwork_ElliPipe}}

Mandatory attributes are pipe section *height* **height**, *width* **span**, pipe type *description* **desc**, *material* **material** and pipe *thickness* **thickness**.

When defining a network mandatory attributes are *height* **height** ja *width* **span**. Other attributes are not set.

{{xtabulate5 ElliPipe}}

### Rectangular pipes {#sec:mvd-rectangularpipe}

The following illustation descibes the definition of a rectangular pipe.  The definition employs the element \<Pipe> and its child elements.

1. Pipe **\<Pipe>**
2. Rectangular pipe **\<RectPipe>**
3. Center **\<Center>**
4. Pipe details **\<Feature>** "IM_pipe" extension

{{figure Pipenetwork_RectPipe}}

The pipe *height* **height**, *width* **width**, *description* **desc**, **material** and pipe **thickness**.

When defining a network-limiting pipe the **height** and **width** are mandatory attributes. Other attributes are not set.

{{xtabulate5 RectPipe}}

### Channels {#sec:mvd-channels}

The following illustation descibes the definition of a channel pipe. The definition employs the element \<Pipe> and its child elements.

1. Pipe **\<Pipe>**
2. channel **\<Channel>**
3. Center **\<Center>**
4. Pipe details **\<Feature>** "IM_pipe" extension

Illustration of channel description:

{{figure Pipenetwork_Channel}}

Mandatory attributes are channel section *height* **height**, *top width* **widthTop**, *bottom width* **widthBottom**, pipe type *description* **desc**, *material* **material** and *thickness* **thickness**.

When defining a network mandatory attributes are *height* **height**, *top width* **widthTop** and *bottom width* **widthBottom**. Other attributes are not set.

{{xtabulate5 Channel}}
