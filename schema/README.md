# Editable Inframodel schemas


Inframodel.xsd schema uses specific naming syntax to represent InfraModel \<Feature> extensions and \<Property> elements under most elements specified on schema. 

\<Property> / \<Feature> naming syntax:

**IM_xxxx_yyyy--ltProperty--gt**

Where xxxx is the name of feature extension (ie IM_Codings) and yyyy is the fixed name attribute of the property element(ie surfaceCoding). 

Example:

```xml
<xs:element name="IM_Codings_surfaceCoding--ltProperty--gt">
	<xs:annotation>
		<xs:documentation>--ltProperty--gt element holding surface/category code</xs:documentation>
	</xs:annotation>
	<xs:complexType>
		<xs:attribute name="label" type="xs:string" use="required" fixed="surfaceCoding">
			<xs:annotation>
				<xs:documentation>Fixed value:"surfaceCoding"</xs:documentation>
				<xs:documentation>Example:surfaceCoding</xs:documentation>
			</xs:annotation>
		</xs:attribute>
		<xs:attribute name="value" type="xs:string" use="required">
			<xs:annotation>
				<xs:documentation>Place for surface/category code</xs:documentation>
				<xs:documentation>Example:--code--</xs:documentation>
			</xs:annotation>
		</xs:attribute>
	</xs:complexType>
</xs:element>
```

**IM_xxxx--ltFeature--gt**
Where xxxx is the name of feature extension (ie IM_Codings)

Example:

```xml
<xs:element name="IM_Codings--ltFeature--gt">
	<xs:annotation>
		<xs:documentation>IM_Codings --ltFeature--gt extension.</xs:documentation>
	</xs:annotation>
	<xs:complexType>
		<xs:attribute name="code" type="xs:string" use="required" fixed="IM_Codings">
			<xs:annotation>
				<xs:documentation>Fixed value:IM_Codings</xs:documentation>
				<xs:documentation>Example:IM_Codings</xs:documentation>
			</xs:annotation>
		</xs:attribute>
		<xs:attribute name="name" type="character_string_id" use="optional">
			<xs:annotation>
				<xs:documentation>Unique id of feature</xs:documentation>
				<xs:documentation>Example:--uid--</xs:documentation>
			</xs:annotation>
		</xs:attribute>
	</xs:complexType>
</xs:element>
```



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
