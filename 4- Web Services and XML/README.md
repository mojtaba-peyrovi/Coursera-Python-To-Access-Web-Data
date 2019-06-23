### Web Services and XML 

---

In order to have data flow on the web between applications, we need to standardized the process. There are two ways that data can flow between apps: XML and JSON.

(data-on-the-web.jpg)

__Wire Protocol:__ The technology that sends data across the web. (wire-protocol.jpg)

__XML: (Extensible Markup Language):__ It is so similar to HTML and the tags and their hierarchy works the same way as HTML code.

(xml-example.jpg)

As seen in the photo, the most inner level of elements, are called __Simple Elements__, and the elements(tags) with childs, are called __Complex Elements.__ 

The difference between html and xml, is you can make up any tag you want based on your data. Here is the basic xml concepts: (xml-basic-concepts.jpg)

__XML as a Tree:__ We can see the whole XML document as a tree with different nodes, and each node can have either other nodes under it, or text values and attributes. Both attributes and text values belong to a node as fruits and leaves.
(xml-as-a-tree.jpg)

__XML as Path:__ We can also write each text value or attribute of the XML as a path. (xml-as-path.jpg)

### XML Schema:

It is another XML document that defines the name and type of each tag. 

xs:complex means the type of the tag is complex.
xs:sequence means there is a sequence of tags.
xs:element means the type of the tag is element. (text, or attribute)

(xml-schema.jpg)

__Schema constraints:__ We can also define constraints in a xml schema document. for example: minOccurs can be defined to check how many times a specific tag has occurs. or also maxOccurs works the same way.

(xml-occurance.jpg)

We can also define datatypes in xml (xml-datatypes.jpg)

__PYTHON and XML:__ In order to parse xml data in py, we have xml library that makes a tree out of xml and we can call any elements inside it.

(python-basic-xml-parse.jpg)

And there are more complicated cases where the nodes have sub nodes and we may have to loop through nodes that we can see an example in python-basic-xml-parse-nested-case.jpg


