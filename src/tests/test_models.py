import os

import pytest

from osm.models import BoundingBox, House, Location, PostRequestInput
from tests.data_generator import OsmXmlGenerator


class TestBoundingBox:
    def test_location_to_bounding_box(self):
        location = Location(0, 0)
        bounding_box = BoundingBox(location, padding=1)
        assert bounding_box.borders == [-1, -1, 1, 1]


class HouseForTesting(House):
    def count_amenities_around_the_house(self, tree):
        amenities = {}
        for child in tree:
            for description in child.findall("tag"):
                if description.attrib["k"] == "amenity":
                    amenities[description.attrib["v"]] = amenities.get(description.attrib["v"], 0) + 1
        return amenities


class TestHouse:
    @pytest.fixture
    def xml_generator(self):
        xml_generator = OsmXmlGenerator()
        return xml_generator

    def test_count_entities_around_house(self, xml_generator):
        house = HouseForTesting(Location(0, 0))
        entities = house.count_amenities_around_the_house(xml_generator.xml)
        for item in xml_generator.AMENITY_VALUES:
            assert entities[item] == xml_generator.amenities[item]


class TestPostRequestInput:
    @pytest.fixture
    def request_input(self):
        path = os.path.join("tests", "samples", "sample_data.txt")
        with open(path, "r") as file:
            sample_data = file.read()
        return PostRequestInput(sample_data)

    def test_get_house_location(self, request_input):
        location = request_input.get_house_location()
        assert (
            location.latitude == request_input.house_details["Latitude"]
            and location.longitude ==  request_input.house_details["Longitude"]
        )

    def test_add_to_house_details(self, request_input):
        request_input.add_to_house_details("test_key", "test_value")
        assert request_input.house_details["test_key"] == "test_value"
