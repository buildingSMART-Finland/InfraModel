from __future__ import (absolute_import, division, print_function, unicode_literals)
from builtins import *
import sys
import random
from lxml import etree

XMLS = "{http://www.w3.org/2001/XMLSchema}"
CONTENT = "*content*"

class SDict(dict):
    def __getitem__(self, item):
        return dict.__getitem__(self, item) % self
    def get(self, item):
        try:
            return dict.__getitem__(self, item) % self
        except KeyError:
            return item

XSType2DocType = SDict({
    "xs:string":               "string",
    "xs:boolean":              "boolean",
    "xs:decimal":              "double",
    "xs:float":                "float",
    "xs:double":               "double",
    "xs:duration":             "duration",
    "xs:dateTime":             "datetime",
    "xs:time":                 "time",
    "xs:date":                 "date",
    "xs:gYearMonth":           "YearMonth",
    "xs:gYear":                "Year",
    "xs:gMonthDay":            "MonthDay",
    "xs:gDay":                 "Day",
    "xs:gMonth":               "Month",
    "xs:hexBinary":            "hexBinary",
    "xs:base64Binary":         "base64Binary",
    "xs:anyURI":               "URI",
    "xs:QName":                "string",
    "xs:NOTATION":             "string",
    "xs:normalizedString":     "string",
    "xs:token":                "string",
    "xs:language":             "string",
    "xs:NMTOKEN":              "string",
    "xs:NMTOKENS":             "array of string",
    "xs:Name":                 "string",
    "xs:NCName":               "string",
    "xs:ID":                   "id",
    "xs:IDREF":                "idref",
    "xs:IDREFS":               "array of idref",
    "xs:ENTITY":               "entity",
    "xs:ENTITIES":             "array of entity",
    "xs:integer":              "integer",
    "xs:nonPositiveInteger":   "negativeinteger",
    "xs:negativeInteger":      "negativeinteger",
    "xs:long":                 "int64_t",
    "xs:int":                  "int32_t",
    "xs:short":                "int16_t",
    "xs:byte":                 "int8_t",
    "xs:nonNegativeInteger":   "unsigned integer",
    "xs:unsignedLong":         "uint64_t",
    "xs:unsignedInt":          "uint32_t",
    "xs:unsignedShort":        "uint16_t",
    "xs:unsignedByte":         "uint8_t",
    "xs:positiveInteger":      "unsigned integer"
})

class TData():
    def __init__(self,SchemaElemType, ElemName, Type, Use, Desc,Example):
        self.SchemaElemType = SchemaElemType
        self.ElemName = ElemName
        self.Type = Type
        self.Use = Use
        self.Desc = Desc
        self.Example = Example

def safe_typename(typename):
    return typename.replace("-", "_")

def findelement(el, typename):
    typename = safe_typename(typename)
    for x in el.findall(XMLS + "element"):
        if safe_typename(x.get("name"))==typename:
            return x
    return None

def findsimpletype(el, typename):
    typename = safe_typename(typename)
    for x in el.findall(XMLS + "simpleType"):
        if safe_typename(x.get("name"))==typename:
            return x
    return None

def findcomplextype(el, typename):
    typename = safe_typename(typename)
    for x in el.findall(XMLS + "complexType"):
        if safe_typename(x.get("name"))==typename:
            return x
    return None

def get_element_type(elem):
    if elem.get("type"):
        return XSType2DocType.get(elem.get("type"))
    if elem.get("ref"):
        return elem.get("ref")
    if elem.find(XMLS + "complexType") is not None:
        return elem.get("ref") or elem.get("name")
    if elem.find(XMLS + "simpleType") is not None:
        elem=elem.find(XMLS + "simpleType")
    if elem.find(XMLS + "restriction") is not None:
        nelem=elem.find(XMLS + "restriction")
        if(nelem is not None):
            if(nelem.find(XMLS + "enumeration") is not None):
                ret="one of ("
                enums=nelem.findall(XMLS + "enumeration")
                for a in enums:
                    ret=ret+a.get("value")+", "
                ret = ret[:len(ret)-2] + ")"
                return ret
            else:
                return "unknown-simpleType"
        else:
            return "unknown-simpleType"
    if elem.find(XMLS + "choice") is not None:
        return "choice"
    return "unknown"

def get_element_use(elem):
    if(elem.get("use")=="required"):
        return "Required"
    elif (elem.find(XMLS + "restriction") is not None):
        return "Restriction"
    else:
        return "Optional"

def decode_desc(t):
    t=t.replace("\r","")
    t=t.replace("\n"," ")
    t=t.replace("\\\\","\\")
    t=t.replace("\\lt","\<")
    t=t.replace("\\gt","\>")
    return t

def has_special_naming(ename):
    if(ename.find("--lt")!=-1 and ename.find("--gt")!=-1):
        return True
    return False
    
def has_special_naming2(ename):
    if(ename.find("__lt")!=-1 and ename.find("__gt")!=-1):
        return True
    return False

def has_added_ltgt(ename):
    if(ename.find("\<")>0 and ename.find("\>")>0):
        return True
    return False

def decode_element_name(ename):
    special=(has_special_naming(ename) or has_special_naming2(ename))
    ename=ename.replace("--lt"," \<")
    ename=ename.replace("--gt","\>")
    ename=ename.replace("__lt"," \<")
    ename=ename.replace("__gt","\>")
    if(special):
        return ename
    return "\<"+ename+"\>"

def get_fake_element_name(ename):
    if(has_special_naming(ename)):
        ename=ename[ename.find("--lt")+4:ename.find("--gt")]
        return ename
    if(has_special_naming2(ename)):
        ename=ename[ename.find("__lt")+4:ename.find("__gt")]
        return ename
    if(has_added_ltgt(ename)):
        ename=ename[ename.find("<")+1:ename.find("\>")]
    if(ename.find("\<")==0):
        ename=ename[2:]
    if(ename.find("\>")>0):
        ename=ename[:-2]
    return ename

def encode_element_name(ename):
    if(has_added_ltgt(ename)):
        ename=ename.replace(" \<","--lt")
        ename=ename.replace("\>","--gt")
    if(ename.find("\<")==0):
        ename=ename[2:]
    if(ename.find("\>")>0):
        ename=ename[:-2]
    return ename

def get_element_desc(elem,elemtree):
    if elem.get("type"):
        ann=elem.find(XMLS + "annotation")
        if ann is not None:
            if(ann.find(XMLS+"documentation") is not None):
                text=""
                for doc in ann.findall(XMLS+"documentation"):
                    t=doc.text or ""
                    #remove example data from desc
                    if t.startswith("Example:"):
                        continue
                    text=text+decode_desc(t)
                return text
            else:
                return ""
        else:
            return ""
    else:
        ann=elem.find(XMLS + "annotation")
        if ann is not None:
            if(ann.find(XMLS+"documentation") is not None):
                text=""
                for doc in ann.findall(XMLS+"documentation"):
                    t=doc.text or ""
                    #remove example data from desc
                    if t.startswith("Example:"):
                        continue
                    text=text+decode_desc(t)
                return text
            else:
                return ""
        elif elem.get("ref"):
            refelem=findelement(elemtree,elem.get("ref"))
            return get_element_desc(refelem,elemtree)
        else:
            return ""

def get_element_example(elem,elemtree):
    if elem.get("type"):
        ann=elem.find(XMLS + "annotation")
        if ann is not None:
            if(ann.find(XMLS+"documentation") is not None):
                text=""
                for doc in ann.findall(XMLS+"documentation"):
                    t=doc.text or ""
                    #return example data
                    if t.startswith("Example:"):
                        text=t[8:]
                        if(text=="--uid--"):
                            return "%X" % random.randrange(100000,20000000)
                        elif(text=="--code--"):
                            return "%d" % random.randrange(1000,20000)
                        else:
                            return text
            else:
                return ""
        else:
            return ""
    else:
        ann=elem.find(XMLS + "annotation")
        if ann is not None:
            if(ann.find(XMLS+"documentation") is not None):
                text=""
                for doc in ann.findall(XMLS+"documentation"):
                    t=doc.text or ""
                    #return example data
                    if t.startswith("Example:"):
                        text=t[8:]
                        if(text=="--uid--"):
                            return "%X" % random.randrange(100000,20000000)
                        elif(text=="--code--"):
                            return "%d" % random.randrange(1000,20000)
                        else:
                            return text
            else:
                return ""
        elif elem.get("ref"):
            refelem=findelement(elemtree,elem.get("ref"))
            return get_element_example(refelem,elemtree)
        else:
            return ""
    return ""

def handle_simpletype(elem,fieldlist,elemtree,exttype=""):
    desc=get_element_desc(elem,elemtree)
    example=get_element_example(elem,elemtree)
    for z in elem.getchildren():
        if(z.tag == XMLS + "annotation"):
            continue
        if exttype=="":
            field=elem.get("name")
        else:
            field=exttype
        if z.tag == XMLS + "restriction":
            t=XSType2DocType.get(z.get("base"))
            if z.find(XMLS+"enumeration") is not None:
                u="One of ("
                for x in z.findall(XMLS+"enumeration"):
                    u=u+x.get("value")+", "
                u = u[:len(u)-2] + ")"

            elif z.find(XMLS+"length") is not None:
                x=z.find(XMLS+"length")
                numitems=int(x.get("value"))
                if(numitems==1):
                    u="One of type %s" % t
                else:
                    u="%d of type %s" % (numitems,t)
            elif ((z.find(XMLS+"minLength") is not None) or (z.find(XMLS+"maxLength")) is not None):
                x=z.find(XMLS+"minLength")
                if x is not None:
                    minitems=x.get("value")
                else:
                    minitems="0"
                x=z.find(XMLS+"maxLength")
                if x is not None:
                    maxitems=x.get("value")
                else:
                    maxitems="-1"
                ma=int(maxitems)
                mi=int(minitems)
                u="%d to %d of type %s" % (mi,ma,t)
            else:
                u="unknown"
            fieldlist.append(TData("ATTR",field,t,u,desc,example))
        elif z.tag == XMLS + "list":
            t=XSType2DocType.get(z.get("itemType"))
            t="Whitespace delimited list of %ss" % t
            u="Required"
            fieldlist.append(TData("CONTENT",field,t,u,desc,example))

def handle_extension(elem,fieldlist,elemtree):
    basetype = elem.get('base')
    if basetype is not None:
        base = findsimpletype(elemtree,basetype)
        if base is None:
            base = findcomplextype(elemtree,basetype)
            handle_complextype(base,fieldlist,elemtree)
        else:
            handle_simpletype(base,fieldlist,elemtree,CONTENT)
    else:
        return
    for z in elem.getchildren():
        if z.tag == XMLS + "attribute":
            fieldlist.append(TData("ATTR",z.get("name"),get_element_type(z),get_element_use(z),get_element_desc(z,elemtree),get_element_example(z,elemtree)))

def handle_simplecontent(elem,fieldlist,elemtree):
    #print("simplecontent")
    for z in elem.getchildren():
        if(z.tag == XMLS + "extension"):
            handle_extension(z,fieldlist,elemtree)

def handle_complextype(elem,fieldlist,elemtree):
    #print("complex")
    for z in elem.getchildren():
        if(z.tag == XMLS + "annotation"):
            continue
        if z.tag == XMLS + "sequence":
            handle_sequence(z,fieldlist,elemtree)
        elif z.tag == XMLS + "choice":
            handle_choice(z,fieldlist,elemtree)
        elif z.tag == XMLS + "complexType":
            handle_complextype(z,fieldlist,elemtree)
        elif z.tag == XMLS + "simpleContent":
            handle_simplecontent(z,fieldlist,elemtree)
        elif z.tag == XMLS + "attribute":
            fieldlist.append(TData("ATTR",z.get("name"),get_element_type(z),get_element_use(z),get_element_desc(z,elemtree),get_element_example(z,elemtree)))

def handle_sequence(elem,fieldlist,elemtree):
    #print("sequence")
    for z in elem.getchildren():
        if(z.tag == XMLS + "annotation"):
            continue
        if z.tag == XMLS + "sequence":
            handle_sequence(z,fieldlist,elemtree)
        elif z.tag == XMLS + "choice":
            handle_choice(z,fieldlist,elemtree)
        elif z.tag == XMLS + "complexType":
            handle_complextype(z,fieldlist,elemtree)
        else:
            mintmp=z.get("minOccurs") or "1"
            maxtmp=z.get("maxOccurs") or "1"
            if(maxtmp=="unbounded"):
                maxtmp="-1"
            minOcc=int(mintmp)
            maxOcc=int(maxtmp)
            elemtype = decode_element_name(get_element_type(z))
            if(minOcc>0):
                use ="Required"
                if (maxOcc==-1):
                    if(minOcc==1):
                        field="At least one *%s* element" %elemtype
                    else:
                        field="At least %d *%s* elements" %(minOcc,elemtype)
                elif maxOcc>1:
                    if maxOcc==minOcc:
                        field="%d *%s* elements" %(minOcc,elemtype)
                    else:
                        field="%d to %d *%s* elements" %(minOcc,maxOcc,elemtype)
                else:
                    field="One *%s* element" % elemtype
            else:
                use="Optional"
                if (maxOcc>1):
                    field="At most %d *%s* elements" %(maxOcc,elemtype)
                elif (maxOcc==1):
                    field="Zero or one *%s* element" % elemtype
                else:
                    field="Zero or more *%s* elements" % elemtype
            fieldlist.append(TData("ELEM",field,elemtype,use,get_element_desc(z,elemtree),get_element_example(z,elemtree)))

def handle_element_non_recursive(elem,fieldlist,elemtree):
    mintmp=elem.get("minOccurs") or "1"
    maxtmp=elem.get("maxOccurs") or "1"
    if(maxtmp=="unbounded"):
        maxtmp="-1"
    minOcc=int(mintmp)
    maxOcc=int(maxtmp)
    elemtype = decode_element_name(get_element_type(elem))
    if(minOcc>0):
        use ="Required"
        if (maxOcc==-1):
            if(minOcc==1):
                field="At least one *%s* element" %elemtype
            else:
                field="At least %d *%s* elements" %(minOcc,elemtype)
        elif maxOcc>1:
            if maxOcc==minOcc:
                field="%d *%s* elements" %(minOcc,elemtype)
            else:
                field="%d to %d *%s* elements" %(minOcc,maxOcc,elemtype)
        else:
            field="One *%s* element" % elemtype
    else:
        use="Optional"
        if (maxOcc>1):
            field="At most %d *%s* elements" %(maxOcc,elemtype)
        elif (maxOcc==1):
            field="Zero or one *%s* element" % elemtype
        elif (maxOcc==0) and (minOcc==0):
            return
        else:
            field="Zero or more *%s* elements" % elemtype
    fieldlist.append(TData("ELEM",field,elemtype,use,get_element_desc(elem,elemtree),get_element_example(elem,elemtree)))

def handle_choice(elem,fieldlist,elemtree):
    #print("choice")
    for z in elem.getchildren():
        if z.tag == XMLS + "attribute":
            fieldlist.append(TData("ATTR",elem.get("name"),get_element_type(elem),get_element_use(elem),get_element_desc(elem,elemtree),get_element_example(elem,elemtree)))
        elif z.tag == XMLS + "choice":
            handle_choice(z,fieldlist,elemtree)
        elif z.tag == XMLS + "element":
            handle_element_non_recursive(z,fieldlist,elemtree)
def handle_element(elem,fieldlist,elemtree):
    #print("element")
    for z in elem.getchildren():
        if(z.tag == XMLS + "annotation"):
            continue
        if z.tag == XMLS + "sequence":
            handle_sequence(z,fieldlist,elemtree)
        elif z.tag == XMLS + "choice":
            handle_choice(z,fieldlist,elemtree)
        elif z.tag == XMLS + "complexType":
            handle_complextype(z,fieldlist,elemtree)
        elif z.tag == XMLS + "attribute":
            fieldlist.append(TData("ATTR",elem.get("name"),get_element_type(elem),get_element_use(elem),get_element_desc(elem,elemtree),get_element_example(elem,elemtree)))

def splitattribs(source):
    new=""
    tabs=""
    for c in source:
        if ((c=='\t') or (c==' ')):
            tabs=tabs+c
        else:
            break
    tabs=tabs+"  "

    if((source.find("<",0,10)<10) and (source.find("<",10)>10) and (source.find("<",10)!=source.find("</",10))):
        # pretty print glitch... if parent element has "contents", first chilkd will be written to same line
        new=source[:source.find("<",10)]+"\n"+tabs+source[source.find("<",10):]
    else:
        # too many attributes on single line.... split to two rows
        a = source.find("\" ",80)
        if(a>=80):
            new=source[:a+1]+"\n"+tabs+source[a+2:]
            a = new.find("\" ",a+80)
            if(a>=160):
                new=new[:a+1]+"\n"+tabs+new[a+2:]
        else:
            new=source
    return new



def get_fieldlist_for_type(xsd,typename,fl):
    elem = findelement(xsd, typename)
    if (elem is not None):
        handle_element(elem,fl,xsd)
    else:
        #check if we are looking for simpleType declaration
        elem=findsimpletype(xsd,typename)
        if(elem is not None):
            raise ValueError("Type %s is simple, can't create compatible fieldlist!" % (typename))
        else:
            #check if we are looking for complexType declaration
            elem=findcomplextype(xsd,typename)
            if(elem is not None):
                handle_complextype(elem,fl,xsd)
            else:
                raise ValueError("Type %s not found!" % (typename))
    return

def fieldlist_to_nodes(xsd,rootnode,fl,recursedepth=1):
    if(recursedepth<0):
        return
    for f in fl:
        if f.SchemaElemType=="ELEM" or f.SchemaElemType=="LIST":
            child = etree.SubElement(rootnode, get_fake_element_name(f.Type))
            child.text = f.Example
            newfl=[]
            get_fieldlist_for_type(xsd,encode_element_name(f.Type),newfl)
            if(len(newfl)>0):
                fieldlist_to_nodes(xsd,child,newfl,recursedepth-1)
        elif f.SchemaElemType=="CONTENT":
             rootnode.text=f.Example
        elif f.SchemaElemType=="ATTR":
            if(f.ElemName==CONTENT):
                rootnode.text=f.Example
            else:
                rootnode.set(f.ElemName,f.Example)

seen_tables = {}
def xsd_tabulate(schema_file,typename, chatty=False, leadingStatement=False, codeSnippet=False, tabulate=True, snippetrecurse=0):
    typename = safe_typename(typename)
    xsd = etree.parse(schema_file)
    fl=[]
    is_simple=False
    elem = findelement(xsd, typename)
    if (elem is not None):
        handle_element(elem,fl,xsd)
    else:
        #check if we are looking for simpleType declaration
        elem=findsimpletype(xsd,typename)
        if(elem is not None):
            is_simple=True
            handle_simpletype(elem,fl,xsd)
        else:
            #check if we are looking for complexType declaration
            elem=findcomplextype(xsd,typename)
            if(elem is not None):
                handle_complextype(elem,fl,xsd)
            else:
                # raise ValueError("Type %s not found from %s!" % (typename,schema_file))
                print("ERROR: Type %s not found from %s!" % (typename,schema_file));
                return
    field_len = 5
    types_len = 3
    use_len = 10
    for f in fl:
        if len(f.ElemName) > field_len: field_len=len(f.ElemName)
        if len(f.Type) > types_len : types_len=len(f.Type)
        if len(f.Use) >use_len : use_len=len(f.Use)
    # pad because of glyphing... this is... hacky!
    field_len += 4
    types_len += 6
    use_len += 2
    # the description can get what is left over
    desc_len = 80 - (field_len + types_len + use_len)
    # prevent any colum from being too wide...
    if field_len > 40: field_len = 40
    if types_len > 40: types_len = 40
    if use_len > 40: use_len = 40
    # and too narrow!
    if desc_len < 30: desc_len = 30
    tbl_ref = "xtbl_%s" % (typename)
    if seen_tables.get(tbl_ref):
        print("\nType {} is defined per Table {} above.\n".format(("*%s*" % (decode_element_name(typename))) if (is_simple) else ("*\<%s>*" % typename), "{@tbl:%s}" % (tbl_ref)))
        return
    seen_tables[tbl_ref] = True
    if tabulate:
        FMT = """|%-{}s|%-{}s|%-{}s|%-{}s|""".format(field_len, types_len, use_len, desc_len)
        if leadingStatement:
            print("""A{} {}{} {}\n""".format(
                "n" if typename[0] in ["a","e","i","o", "u","A","E","I","O", "U"] else "",
                ("*%s*" % (typename)) if (is_simple) else ("*%s*" % decode_element_name(typename)),
                "" if ((not chatty)or(get_element_desc(elem,xsd)is None)) else (" \"%s\"" % get_element_desc(elem,xsd)),
                ("is defined per Table %s:" if (is_simple) else "shall have the fields defined in Table %s:") % ("{@tbl:%s}" % (tbl_ref))))
        if chatty and (not leadingStatement) and get_element_desc(elem,xsd):
            print("""\<{}>:{}\n""".format(typename,get_element_desc(elem,xsd)))

        print("\n\nTable: %s %s. {#tbl:%s}\n\n" % (decode_element_name(typename),
            "definition" if is_simple else "fields",
            tbl_ref))
        if(is_simple):
            print(FMT % ("**Type**", "**Basetype**", "**Restriction**", "**Description**"))
        else:
            print(FMT % ("**Field**", "**Type**", "**Use**", "**Description**"))
        print(FMT % (":"+"-"*(field_len-1), ":"+"-"*(types_len-1), ":"+"-"*(use_len-1), ":"+"-"*(desc_len-1)))
        for f in fl:
            print(FMT % (f.ElemName,"*"+f.Type+"*",f.Use,f.Desc))
            #print(f.SchemaElemType)
    if codeSnippet and not is_simple:

        root=etree.Element(get_fake_element_name(typename))
        root.text=get_element_example(elem,xsd)
        fieldlist_to_nodes(xsd,root,fl,snippetrecurse)
        print("\n")
        print("XML example of *%s*:" % decode_element_name(typename))
        print("```xml")
        etree.indent(root)
        xx = etree.tostring(root,encoding='unicode',method='xml',pretty_print=True)

        new=""
        lines = xx.splitlines()
        for line in lines:
            if len(line)>40:
                new=new+splitattribs(line)
                if not new.endswith("\n"):
                    new=new+"\n"
            else:
                new=new+line+"\n"
        while new.endswith("\n"):
            new=new[:-1]
        print(new)
        print("```")

if __name__ == "__main__":
    xsd_tabulate(sys.argv[1],sys.argv[2],True,True,True)
