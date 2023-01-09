# InfraModel
This repository contains a development version of the Finnish InfraModel landxml-subset schema(s) and documentation. Official publications are available under an open license on www.buildingsmart.fi website.

##Folder structure:

###CI
CI folder contains the build tools and templates for the document generation, used by github actions. The toolchain processes and combines the raw markdown documents to one, and then uses pandoc to convert markdwn to publisheable documents (word,pdf,html). Toolchain also processes the schemas and produces verification schema and enumeration excel document.

###figures
Figures folder contains all figures used by the documentation.

###markdown
Markdown folder contains the editable parts of documentation as markdown(.md) documents. In addition to markdown syntax, the document generation toolchain allows use of specific "moustache syntax commands" to extend the functionality:
Supported "moustache commands":
  {{ command [args]}}
  Currently:
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



Final documents are built automatically from this repository by github CI actions when content is updated. The final artefacts for publification can be found from github repository actions tab. 
