#!/usr/bin/env python3
"""
XML Serialization and Deserialization Module
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to an XML file.
    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The XML file to write to.
    """
    # Create the root element
    root = ET.Element("data")

    # Iterate through dictionary items
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)  # create child element
        child.text = str(value)           # store value as string

    # Write the XML tree to file
    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserialize an XML file to a Python dictionary.
    Args:
        filename (str): The XML file to read.
    Returns:
        dict: Dictionary representation of the XML data.
    """
    try:
        tree = ET.parse(filename)       # parse XML file
        root = tree.getroot()           # get root element
        result = {}

        # Iterate over child elements to reconstruct the dictionary
        for child in root:
            result[child.tag] = child.text

        return result

    except (ET.ParseError, FileNotFoundError):
        # Return empty dict or None if file is invalid or missing
        return {}

