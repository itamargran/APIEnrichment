import pytest
from osm.models import Location, House
from osm.tests.osm_data_generator import OsmXmlGenerator


class TestHouse:
    @pytest.fixture
    def xml_generator(self):
        xml_generator = OsmXmlGenerator()
        return xml_generator

    def test_count_entities_around_house(self, xml_generator):
        house = House(Location(0, 0))
        entities = house.count_entities_around_the_house(xml_generator.xml)
        for item in xml_generator.AMENITY_VALUES:
            assert entities[item] == xml_generator.amenities[item]
