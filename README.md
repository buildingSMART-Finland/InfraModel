![InfraModel logo](/figures/inframodel-cover.jpg "InfraModel logo")

# InfraModel
This repository contains development versions of the Finnish InfraModel landxml 1.2 subset schema(s),documentation and the example files. 

Official Inframodel publications are available under an open license at www.buildingsmart.fi website.

Document artefacts are built automatically from this repository by github CI actions when content is updated. The artefacts for publification can be found from github repositorys actions tab. 

## Folder structure:

### CI
CI folder contains the build tools and templates for the document generation, used by github actions. The toolchain processes and combines the raw markdown documents to one, and then uses pandoc to convert markdwn to publisheable documents (word,pdf,html). Toolchain also processes the schemas and produces verification schema and enumeration excel document.

### figures
Figures folder contains all figures used by the documentation.

### markdown
Markdown folder contains the editable parts of documentation as markdown(.md) documents. In addition to markdown syntax, the document generation toolchain allows use of specific "moustache syntax commands" to extend the functionality of markdown.

Command syntax

{{*command* [*args*]}}

Supported "moustache commands":
  
  {{refsec section-id}}          - insert a reference to a (sub)section
  
  {{include FILE}}               - recursively include a file (or, if FILE=="annexes", all the annexes in letter order)
  
  {{schemafile FILE}}            - set a default schema file
  
  {{xtabulate TYPE SCHEMAFILE}}  - produce a table from a xml schema with leading statement.
  
  {{xtabulate2 TYPE SCHEMAFILE}} - same as xtabulate, without leading statement
  
  {{xtabulate3 TYPE SCHEMAFILE}} - same as xtabulate, but more chatty
  
  {{xtabulate4 TYPE SCHEMAFILE}} - same as xtabulate, but with xml code example
  
  {{xmlsnippet TYPE SCHEMAFILE}} - produce example code from xml schema
  
  {{figure IMAGE}}               - path to IMAGE, where IMAGE is a path relative to ./figures
 
  {{figst ID}}                   - apply default figure styles and set optional id (alphanum-_)+ for figure number referencing
  
  {{figref ID}}                  - insert a reference to a figure
  
### schema
Schema folder contains the editable InfraModel XML schemas, one containing the elemnts, and another one for the enumerations used by the main schema. 

These schemas use specific naming syntax to represent InfraModel \<Feature> extensions and \<Property> elements under most elements specified on schema. 
Naming syntax:

**IM_xxxx--ltFeature--gt**

**IM_xxxx_yyyy--ltProperty--gt**

Where xxxx is the name of feature extension (ie IM_Codings) and yyyy is the fixed name attribute of the property element 

This special naming is handled by "xtabulateX" moustache commands to produce fully typed tables of landxml elements, and is removed by toolchain when actual verification schema is formed by the github CI actions.

Example xml code snippets are also formed from schema by the toolchain, each xml attribute (and optionally element, if element has contents) shall have example values on schema. Example values are parsed from <xs:documentation> element, each attribute(or element) definition shall have at least two instances of <xs:documentation>, one for human readable description and another with example data.

Example data is regognized by "Example:" keyword, in example:

```xml
<xs:attribute name="date" type="xs:date" use="required">
  <xs:annotation>
		<xs:documentation>UTC date</xs:documentation>
		<xs:documentation>Example:2021-08-20</xs:documentation>
	</xs:annotation>
</xs:attribute>
```

## How to contribute

### Found an error or need some new functionality?
Feel free to submit your issue via the github issues tab.

### Propose a change to documentation, schema or add a new example file set
Create your own fork of this repository, make your changes and/or additions to your fork repository, and send pull request. Be aware that you are publishing under "The Unlicense", so all of the rights of your content are given to public domain. 

### Wan't to get involved more?
Join us at buildingsmart.fi


