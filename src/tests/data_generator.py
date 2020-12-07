import json
import random

import xml.etree.ElementTree as ET


class OsmXmlGenerator:
    CHILDREN = ["node", "way", "relation"]
    AMENITY_VALUES = ["school", "bench", "coffee", "river"]
    XML_LENGTH = 200

    def __init__(self):
        self.amenities = {key: 0 for key in OsmXmlGenerator.AMENITY_VALUES}
        self.xml = self._generate_xml()

    def _generate_xml(self):
        xml_doc = ET.Element("osm")
        for _ in range(OsmXmlGenerator.XML_LENGTH):
            child = self.generate_child(xml_doc)
            if random.randint(0, 1):  # Since not all elements have tags
                amenity = self.generate_tag(child)
                self.update_amenities(amenity)
        return xml_doc

    def generate_child(self, xml_doc) -> ET.SubElement:
        return ET.SubElement(xml_doc, self.random_child_name())

    def generate_tag(self, child) -> str:
        amenity = self.random_tag_name()
        ET.SubElement(child, "tag", k="amenity", v=amenity)
        return amenity

    def random_child_name(self) -> str:
        number_of_children_options = len(OsmXmlGenerator.CHILDREN)
        return OsmXmlGenerator.CHILDREN[random.randint(0, number_of_children_options - 1)]

    def random_tag_name(self):
        number_of_amenities = len(OsmXmlGenerator.AMENITY_VALUES)
        return OsmXmlGenerator.AMENITY_VALUES[random.randint(0, number_of_amenities - 1)]

    def update_amenities(self, amenity_kind: str):
        self.amenities[amenity_kind] += 1

    # https://stackoverflow.com/questions/749796/pretty-printing-xml-in-python/38573964#38573964
    def prettify(self, element, indent='  '):
        queue = [(0, element)]  # (level, element)
        while queue:
            level, element = queue.pop(0)
            children = [(level + 1, child) for child in list(element)]
            if children:
                element.text = '\n' + indent * (level+1)  # for child open
            if queue:
                element.tail = '\n' + indent * queue[0][0]  # for sibling open
            else:
                element.tail = '\n' + indent * (level-1)  # for parent close
            queue[0:0] = children  # prepend so children come before siblings

    def save_xml(self):
        self.prettify(self.xml)
        tree = ET.ElementTree(self.xml)
        tree.write("dummy_xml.xml", encoding="UTF-8", xml_declaration=True)


class PostRequestContentGenerator:
    @staticmethod
    def generate_post_request_content() -> json:
        content = {
            "Latitude": random.uniform(-90, 90),
            "Longitude": random.uniform(-180, 180),
        }
        response = {"data": [content]}
        return json.dumps(response)
