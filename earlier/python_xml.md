# Python and XML

## Standard Library

### [xml.etree](https://docs.python.org/2/library/xml.etree.elementtree.html)

ElementTree && Element

+   ElemenTree: represent the whole XML document as a tre
+   Element: represent a single node in the tree

Parsing XML

    import xml.etree.ElementTree as ET
    root = ET.parse('file.xml')
    root = ET.fromstring('<root><tag attrib='value'>text</tag></root>')

    print root[0].text
    print root.tag, root.attrib
    for child in root:
        print child.tag, child.root

Fiding interesting elements

+   Element.iter:
        
        for neighbor in root.iter('neightbor'):
            print neighbor.attrib

+   Element.findall && Element.find:

        for country in root.findall('country'):
            rank = country.find('rank').text
            name = country.get('name')
            print rank, name

Modifying an XML File

+   Elemenet.write, Element.text = value, Element.set('atrrib', value), Elemend.[remove|append]

Building XML documents

    a = ET.Element('a')
    b = ET.Element(a, 'b')
    c = ET.Element(a, 'c')
    d = ET.Element(c, 'd')

Parsing XML with Namespaces

+   prefix:tag -> {uri}tag

        root.find('{http://people.example,com}actor');

+   dict as namespace

        ns = {'real_person': 'http://people.example.com'}
        root.find('real_person:actor', ns);

XMLParser Objects

[Additional Resource](http://effbot.org/zone/element-index.htm)

### [lxml](http://lxml.de)


## External Libray

1.  [generatorDS](https://pypi.python.org/pypi/generateDS)

