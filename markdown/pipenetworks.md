# Pipenetworks {#sec:pipenetworks}

The **\<PipeNetworks>** in Inframodel covers diffrent drainage and utility network types: storm drain, combined sewer, sewer, French drain, culvert, water pipe, district heating, district cooling, gas, waste disposal and cable networks.

A network model can be transferred in a separate file or (e.g. in case of route drainage plan) in the same file as other (route) plan content. The metric units used in network plan and the coordinate system are defined in {{refsec fileheaders}}.

The definition of a utility network in LandXML is a topological one. The structures (manholes, drain wells etc.) are nodes and the pipes (or cables) are links that connect these nodes. As the pipes are always defined between two nodes, the free ends of pipes are modelled as virtual structures, of which there are two types, inlets and outlets.

The networks are presented in the parent element **\<PipeNetworks>** whose child elements are individual **\<PipeNetwork>** elements. A **\<PipeNetwork>** consists of structures and pipes.

- Structures **\<Structs>**
    - types: circular and rectangular wells, virtual (inlet/outlet) structures, equipment and pipe joints, extensions and inflexions (virtual joints).
    - are given an explicit location (northing, easting, elevation)
    - pipe inlet/outlet in a structure is an **\<Invert>**
- Pipes **\<Pipes>**
    - types: circular pipe, elliptic pipe, egg-shaped pipe, rectangular pipe and open channel.
    - have a relative location by the named ending and starting structure  
    - the length is given as the distance between the centers of the terminal structures at the elevation of the inverts.    
    - the exact length may be calculated as the distance between the coordinates of the pipe start and end given in the extension "IM_pipe".    
    - pressurized pipes can be described in Inframodel extension "IM_pipe" using the property "pressureClass".

![Pipe networks]({{figure Pipenetworks_general.png}} "Pipe networks"){{figst pipenetworks}}

The pipe network is, depending on the situation, usually described in its entirety. LandXML schema exposes some limitations on how a network can be delimited. E.g. describing the inverts of a delimiting storm drain requires additional pipes and corresponding terminal structures to be in the model. The process of delimiting the network is described in further detail in {{refsec structures}} and {{refsec pipes}}.
   

## Pipe networks 

A file may contain multiple *utility network groups* **\<PipeNetworks>**. It is mandatory to give a **name** and optional to give a *description* **desc** and **state**.

The names of *utility network groups* are unique within the file. If a *network group* contains networks with different states, the **state** shall not be set for the group.

{{xtabulate PipeNetworks}}

### Plan information {#sec:watersupplyandsewerageplaninformation}

The *plan information* of a *network group* is set in the optional "IM_plan" extension under **\<PipeNetworks>** element. If the project consists of several sub-divisions, which progress at different rate, the plan content can be divided into several *network group* **\<PipeNetworks>** elements according to those divisions, or alternatively *plan information* may be set for each *network* in separate "IM_plan" under **\<PipeNetwork>** elements. The plan information contains the **planName** the **planCode**, the **planState**, and the *plan description* **planDesc**. The *plan state* is set according to a scale agreed on by the parties. An example is presented in the tabel below.

{{xtabulate IM_plan--ltFeature--gt}}

## Pipe network {#sec:pipenetwork}

Individual networks are described in **\<PipeNetwork>** elements, organized under their parent element **\<PipeNetworks>**, the *network group*. The number of *networks* in one *network group* is unlimited. The *pipe network* defines a topological model, with mandatory **name** and **pipeNetType**. The **state** and *description* **desc** are optional.

{{xtabulate pipeNetType}}

{{xtabulate PipeNetwork}}

### Pipe network type extensions

When the *network type* is not one of those covered by the **pipeNetType** (attribute set to "other"), the "IM_pipeNetworkType" extension can be used to specify the type.

{{xtabulate IM_pipeNetworkType--ltFeature--gt}}

## Units

In Inframodel, the same metric units (as specified in {{refsec fileheaders}}) shall always be used. The LandXML capability to assing separate units for structures and pipes in networks shall not be used in Inframodel.

## Structures {#sec:structures}

The topological network consists of different kinds of structures whose exact location is defined in the file. The different structures in the **\<PipeNetwork>** compose the *structure group* **\<Structs>**, that has no attributes.

{{xtabulate Struct}}

LandXML standard structure types:

- Circular structure
- Rectangular structure
- Inlet structure (free intake end of pipe)
- Outlet structure (free exhaust end of pipe)
- Connections 
- Pipe joints, extensions and inflexions
- Equipment (as specified in Inframodel extension)

Delimiting the network is a special case of using connection, described in further detail in the section covering the **\<Connection>** element.

{{xtabulate IM_struct--ltFeature--gt}}

#### General data

All structural elements in the file are assigned individual names.

{{xtabulate Struct}}

#### Center

***Circular and rectangular structures:*** The center of the cross-section at the inside bottom level of the structure is set by space-separated 3D-coordinates in the **\<Center>** element.

***Pipe inlets and outlets:*** The pipe end is defined by space-separated 3D-coordinates in the **\<Center>** element.

***Pipe connections:*** The **\<Center>** of a connection, joint or point of intersection at the mounting level is set using space-separated 3D coordinates.

***Equipments:*** The **\<Center>** of a piece of equipment at the mounting level is set using space-separated 3D coordinates.


#### Inverts

The inlets and outlets in a structure for adjoining pipes are described using the element **\<Invert>**. The required attributes of invert are: the elevation **\<elev>**, the flow direction **\<flowDir>** and the reference to the adjoining pipe **\<refPipe>**. The elevation is given according to "elevType" set for the adjoining pipe in "IM_pipe" extension (crown level for pressure pipes and the invert level for others).

{{xtabulate Invert}}

#### Details

It is possible to set additional properties for structures in "IM_struct" extension. 

Common properties applicable to all types of structures are **structLabel** and the dates of different actions, such as the **constructionDate** and the **renewalDate**. The dates of the actions are typically give in years. It is also possible to describe the renewal in further detail, e.g. the method used, using the **renowalDesc** attribute.- 

Additionally, common to the three structure types below are **rimType** and the rim load bearing class **rimLoad**, as well as **bottomThickness**.

***Circular structures:***
When describing a conical well the **diameter** attribute describes the inner diameter at the bottom level. The **rimDiameter** describes the inner diameter of the rim and the **rimCenter** defines the 3D coordinates of the rim center. The parameters of the sump are its depth **heightDeposit** and its volume **volumeDeposit**. 

***Rectangular structure:***
 The parameters of the sump are its depth **heightDeposit** and its volume **volumeDeposit**. 

***Equipment:***
It is possible to define more detailed type information of a piece of equipment between two pipes, e.g. a Valve using the attributes **equipmentType**, **equipmentCode** and an equipment description **equipmentDesc**. 

#### Spatial allocation and avoidance

Related to structure geometry an area or a volume for spatial allocation or avoidance may be defined as "IM_spatialZone" extension. Both spatialAllocation and spatialAvoidance are given as single metric value (in file length units). The allocation and avoidance geometry is interpreted according to the structure geometry definition as a radius around the vertical line defined by structure \<Center> 3D coordinates at the bottom level and @elevRim.

![Spatial Zone Pipe]({{figure SpatialZonePipe.png}} "Spatial Zone Pipe"){{figst SpatialZonePipe}}

### Circular structures {#sec:circularstructures}

Inspection wells of French drains are an example of a circular structure. Circular structures are defined using the structure element **\<Struct>** and its child elements.

1. Structure element **\<Struct>**
2. Structure center **\<Center>**
3. Circular structures **\<CircStruct>**
4. Inverts **\<Invert>**
5. Structure details **\<Feature>** "IM_struct" extension

The figure below illustrates the representation of a drain well, including a sump. The sump is defined in the extension "IM_struct" by defining the sump height and volume.

The *body* **diameter** at the bottom of the well, the *description* **desc**, the **material** and the **thickness** of the shell material. The well cone and sump are described in further detail in the extension "IM_struct"

![Circular structures]({{figure Pipenetwork_CircStruct.png}} "Circular structures"){{figst circularstructures}}

{{xtabulate CircStruct}}

### Rectangular structures {#sec:rectangularstructures}

The illustration below describes the description method of a rectangular structure. The structure is defined using the **\<Struct>** element and its child elements:
1. General data **\<Struct>**
2. Center **\<Center>**
3. Rectangular structure **\<RectStruct>**
4. Pipe invert **\<Invert>**
5. Structure details **\<Feature>** "IM_struct" extension

The illustration demonstrates the method of description of a rectangular well, including a sump as an example. The sump is defined by its depth and/or volume.

The mandatory attributes of a rectangular structure are the **length** the direction of the long edge **lenghtDir**, the **width** of the short edge width, the **material** of the structure and the **thickness** of the surface structure.

![Rectangular structures]({{figure Pipenetwork_RectStruct.png}} "Rectangular structures"){{figst rectangularstructures}}

{{xtabulate RectStruct}}

### Pipe inlets and outlets {#sec:pipeinletsandoutlets}

Pipe inlets and outlets are end of the pipe network pipes. The following illustration demonstrates the method of description. The virtual structures of the pipe ends are defined using the structure attribute **\<Struct>** and its child elements:

1. General description **\<Struct>**
2. Center **\<Center>**
3. Pipe inlet <InletStruct> or pipe outlet **\<OutletStruct>**
4. Inverts **\<Invert>**
5. Structure details **\<Feature>** "IM_struct" extension

The illustration below demonstrates how pipe inlets and outlets are described. The example demonstrates an outlet.

*Inlets* **\<InletStruct>** and *outlets* **\<OutletStruct>** have no attributes.

![Inlets and outlets]({{figure Pipenetwork_InletOutletStruct.png}} "Inlets and outlets"){{figst inletsandoutlets}}

### Pipe connections {#sec:pipeconnection}

Pipe connections, joints and points of intersection are defined by the **\<Connection>** elements. The illustration below demonstrates the mode of description, which contains the attributes of the structure **\<Struct>** and its child elements:

1. General data **\<Struct>**
2. Center **\<Center>**
3. Pipe connections, joints or points of intersection **\<Connection>**
4. Inverts **\<Invert>**
5. Details **\<Feature>** "IM_struct" structural extension

The illustration demonstrates the description method of a point of intersection.
When using the element to delimit a pipe network, the terminal drainage well is connected to a pipe that terminates in a **\<Connection>** element. It is thus possible to also describe the connections of the outermost wells in the plan network. It is advisable to name the elements in a fashion that is clearly different from the rest of the plan.

When the element describes a delimiting element, all attributes are not used. The elevation of the rim elevRim, the elevation of the sump elevSump and the state of the structure are left undefined (given value "NaN").
    
When a **\<Connection>** is used for modeling a bend (inflexion) of a flexible pipe of cable (being actually continuous), its name and description desc should indicate that it is not a physical conncection.  
Connections, joints or points of intersection are defined using the **\<Connection>** element, that has no attributes.

![Pipe connections]({{figure Pipenetwork_Connection1.png}} "Pipe connections"){{figst pipeconnections}}

{{xtabulate Connection}}

### Equipment {#sec:equipment}

Equipment is defined using the **\<Connection>** element. The illustration bellow describes the mode of description of a *structure* **\<Struct>** and its child elements:

1. General data **\<Struct>**
2. Center **\<Center>**
3. Equipment **\<Connection>**
4. Inverts **\<Invert>**
5. Details **\<Feature>** "IM_struct" structural extension

The illustration demonstrates the mode of description of a valve:

![Equipment]({{figure Pipenetwork_Connection2.png}} "Equipment"){{figst equipment}}

A *piece of equipment* is defined using the element **\<Connection>**, that has no attributes. Details of the equipment is defined in the extension "IM_struct".

{{xtabulate Connection}}


## Pipes {#sec:pipes}

The topological network consists of different kinds of structures, whose exact location is given. The pipes that compose the **\<PipeNetwork>** are described as a *structure collection* **\<Pipes>** that has no attributes. A **\<Pipe>** is defined between two structure nodes **\<Struct>** by refering to them in the start- and end-attributions.

NOTE: In the special case of "network" where there is only one single pipe (such as a culvert with no specified connection at either end), the referenced start and end structure shall be **\<InletStruct>** and **\<OutletStruct>**, respectively.

Available pipe types in the LandXML standard:

- Circular pipe
- Egg-shaped pipe
- Elliptic pipe
- Rectangular pipe
- Channel

{{xtabulate Pipe}}

### Pipe

The **name**, end reference **refEnd**, start reference **refStart**, **slope** and **state** are mandatory attributes.
Setting the exact length of a pipe is optional. All pipe elements are assigned unique names.

When using a pipe to delimit a network, its refEnd or refStart shall be to a \<Connection> with a name that clearly distinguishes it from other content in the file. 
    
When a pipe has several segments, with \<Connection> elements (physical or virtual) between them, each segment must be a \<Pipe> element with unique **name**. If the whole pipe (e.g. from one well to another) needs a name, it should be given in **desc** attribute of every segment. In particular, this should be provided for continuous flexible pipes or cables having inflexions modeled as virtual connections.

{{xtabulate Pipe}}

## Center

The pipe curvature is defined by space-separated 3D-coordinates in the \<Center> element.

{{xtabulate Center}}

More details can be found from {{refsec pipedetails}}

## Details {#sec:pipedetails}

It is optional to define details in inframodel file transfers using "IM_pipe" extension. The label of pipe can be given using a pipeLabel. The start and end coordinates of a pipe are defined by three parameters: 

1. elevation type elevType 
2. start coordinate pipeStart and the 
3. end coordinate pipeEnd. 

The jointType sets the type of joints and connections used for the pipe. When the defined pipe is a pressurized sewer the pressureClass of the pipe is defined. Procedure details are defined with the constructionDate and renewalDate. It is also possible to define detailed information of the renewal using the renewal description renewalDesc, e.g. the method used to renew the pipe.

***Rectangular and elliptic pipe:*** *When start and end coordinates are defined, elevation type shall be given as one of the elevTypes illustrated for circular pipes.*

***Egg pipe:*** *When start and end coordinates are defined, elevation type shall be given as one of the elevTypes illustrated for circular pipes, center being at the level where the cross section is the widest.*

When the start and end coordinates are given with elevation values, elevation type shall be given as one of the enumerated elevTypes shown below.


![Elevation type]({{figure Pipenetwork_elevType.png}} "Elevation type"){{figst elevationtype}}

{{xtabulate IM_pipe--ltFeature--gt}}
    
***Cable:*** *When the \<Pipe> represents a cable, and its start and end coordinates are defined, elevation type shall be given as one of the elevTypes illustrated for circular pipes.* Also, cable-specific properties in separate "IM_cable" extension:
    
{{xtabulate IM_cable--ltFeature--gt}}

#### Spatial allocation and avoidance

Related to pipe geometry an area or a volume for spatial allocation or avoidance may be defined as "IM_spatialZone" extension. Both spatialAllocation and spatialAvoidance are given as single metric value (in file length units). The allocation and avoidance geometry is interpreted according to the pipe geometry definition as a radius around the pipe path defined by start and end structure \<Center> coordinates and their **\<Invert>** elevation values .    

![Spatial zone - around Pipe]({{figure SpatialZonePipe.png}} "Spatial zone - around Pipe"){{figst spatialzonearoundpipe}}    
    
#### Circular pipes {#sec:circularpipes}

The following illustation descibes the definition of a round pipe  The definition employs the element **\<Pipe>** and its child elements.

1. Pipe **\<Pipe>**
2. Circular pipe **\<CircPipe>**
3. Center **\<Center>**
4. Pipe details **\<Feature>** "IM_pipe" extension


![Circular pipe]({{figure Pipenetwork_CircPipe.png}} "Circular pipe"){{figst circularpipe}}

When defining a network-limiting pipe the **diameter** is the only defined attribute. Other attributes are not defined.

{{xtabulate CircPipe}}


### Egg pipes {#sec:eggpipes}

The following illustation descibes the definition of an egg-shaped pipe  The definition employs the element \<Pipe> and its child elements.

1. Pipe **\<Pipe>**
2. Egg pipe **\<EggPipe>**
3. Center **\<Center>**
4. Pipe details **\<Feature>** "IM_pipe" extension

Illustration of egg-shaped pipe represenation.

When defining a network-limiting pipe the *height* **height** and *width* **span** are set. Other attributes are not set.

{{xtabulate EggPipe}}

### Elliptic pipes {#sec:ellipticpipe}

The following illustation descibes the definition of an elliptical pipe. The definition employs the element \<Pipe> and its child elements.

1. Pipe **\<Pipe>**
2. elliptic pipe **\<ElliPipe>**
3. Center **\<Center>**
4. Pipe details **\<Feature>** "IM_pipe" extension

![Circular pipe]({{figure Pipenetwork_CircPipe.png}} "Circular pipe"){{figst circularpipe}}

When defining a network mandatory attributes are *height* **height** ja *width* **span**. Other attributes are not set.

![Elliptic pipe]({{figure Pipenetwork_ElliPipe.png}} "Elliptic pipe"){{figst ellipticpipe}}

{{xtabulate ElliPipe}}

### Rectangular pipes {#sec:rectangularpipe}

The following illustation descibes the definition of a rectangular pipe.  The definition employs the element \<Pipe> and its child elements.

1. Pipe **\<Pipe>**
2. Rectangular pipe **\<RectPipe>**
3. Center **\<Center>**
4. Pipe details **\<Feature>** "IM_pipe" extension

When defining a network-limiting pipe the **height** and **width** are mandatory attributes. Other attributes are not set.

![Rectangular pipe]({{figure Pipenetwork_RectPipe.png}} "Rectangular pipe"){{figst rectpipe}}

{{xtabulate RectPipe}}

### Channels {#sec:channels}

The following illustation descibes the definition of a channel pipe. The definition employs the element \<Pipe> and its child elements.

1. Pipe **\<Pipe>**
2. channel **\<Channel>**
3. Center **\<Center>**
4. Pipe details **\<Feature>** "IM_pipe" extension

Illustration of channel description:

![Channel]({{figure Pipenetwork_Channel.png}} "Channel"){{figst channel}}

When defining a network mandatory attributes are *height* **height**, *top width* **widthTop** and *bottom width* **widthBottom**. Other attributes are not set.

{{xtabulate Channel}}
