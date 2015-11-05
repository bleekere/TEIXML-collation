import xml.etree.ElementTree as ET
tree = ET.parse("xml/liefde.xml")
root = tree.getroot()

# Nodes with name = "p"
x = root.findall(".//p")

# Finds all p that are children of the nodes with the attribute type = "page"

y = root.findall(".//div[@type='page']/p")

# Finds all p-elements that have the attribute style with the value="center"

z = root.findall(".//p[@style='text-indent: 50px;']")

# Finds all p-elements that are the first child of their parent

a = root.findall(".//p[1]")

# Accesses the text content of all p-elements that are first child of their parent (which is div)

for div in root.findall(".//div"):
    for p in div.findall('p/*'):
        b = p.text
        print(b)


