# Inframodel documentation in markdown format 

In addition to markdown syntax, the document generation toolchain allows use of specific "moustache syntax commands" to extend the functionality of markdown.

Command syntax:

{{command [args]}}

Supported commands:

{{refto ID}} - insert a reference to a annex

{{refsec section-id}} - insert a reference to a (sub)section

{{include FILE}} - recursively include a file (or, if FILE=="annexes", all the annexes in letter order)

{{schemafile FILE}} - set a default schema file

{{xtabulate TYPE SCHEMAFILE}} - produce a table from a xml schema with leading statement.

{{xtabulate2 TYPE SCHEMAFILE}} - same as xtabulate, without leading statement

{{xtabulate3 TYPE SCHEMAFILE}} - same as xtabulate, but more chatty

{{xtabulate4 TYPE SCHEMAFILE}} - same as xtabulate, but with xml code example

{{xtabulate4 TYPE SCHEMAFILE}} - same as xtabulate, but with expanded xml code example (up to 5 levels)

{{xmlsnippet TYPE SCHEMAFILE}} - produce example code from xml schema

{{figure IMAGE}} - path to IMAGE, where IMAGE is a path relative to ./figures

{{figst ID}} - apply default figure styles and set optional id (alphanum-_)+ for figure number referencing

{{figref ID}} - insert a reference to a figure

**main.md file uses {{include}} command to include all main sections as separate markdown files.** 
