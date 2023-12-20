import xml.etree.ElementTree as ET
"""
This file is helping tool for creating python classes for complex types in RFEM API
It is not necessary to use it, but it is very helpful for creating new complex types
Usage:
    1) Create file 'complexType.xml' in the same folder as this file
    2) Copy complex type from wsdl file to 'complexType.xml' (the whole complexType starting with <complexType name="..."> and ending with </complexType>)
    3) Run this file and copy the output to the complexTypes.py file
    4) You can directly append new type to the complexTypes.py file by running this file with '>> complexTypes.py' at the end of the command, but I noticed some errors in PowerShell

"""

def snake_to_camel(word):
    return ''.join(x.capitalize() for x in word.split('_'))

class Element:
    def __init__(self, name, type):
        self.name = name
        self.type = type

def createClass(root):
    """
    Parses xml element and prints the code for python class
    """
    name = snake_to_camel(root.attrib['name'])

    elements = []
    # root[0] -> <sequence>
    for child in root[0]:
        elements.append(Element(child.attrib['name'], child.attrib['type']))

    print(f"\n\nclass {name}(BaseComplexType):")
    print(f"    def __init__(self,")
    for element in elements[:-1]:
        print(f"        {element.name} = None, # {element.type}")
    print(f"        {elements[-1].name} = None # {elements[-1].type}")
    print(f"    ):")
    for element in elements:
        print(f"        self.{element.name} = {element.name}")

if  __name__ == "__main__":
    tree = ET.parse('./complexType.xml')
    root = tree.getroot()

    # It is possible to adjust code here and goo through multiple elemets or even whole wsdl file
    createClass(root)