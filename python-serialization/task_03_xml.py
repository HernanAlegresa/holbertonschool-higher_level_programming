#!/usr/bin/env python3
"""
3. Serializing and Deserializing with XML
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    root = ET.Element('data')
    for key, value in dictionary.items():
        child = ET.Element(root, key)




def deserialize_from_xml(filename): 
    