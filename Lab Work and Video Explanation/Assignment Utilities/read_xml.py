import xml.etree.ElementTree as ET

# Parse XML file
tree = ET.parse("testdata.xml")
root = tree.getroot()

# Read student data
for student in root.findall("student"):
    name = student.find("name").text
    email = student.find("email").text

    print("Name:", name)
    print("Email:", email)
    print()
    