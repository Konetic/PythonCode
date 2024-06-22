""" Importing xml docs"""
import xml.etree.ElementTree as ET

#parse XML into Element Tree

tree = ET.parse("xml_file.xml")
root = tree.getroot()
#orrrr
#root = ET.fromstring(xml_file.xml)

#Root
print(root.tag)

