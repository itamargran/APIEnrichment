import json
import requests

import xml.etree.ElementTree as ET
from typing import Dict, List, Tuple, Union


class Location:
    def __init__(self, latitude: float, longitude: float):
        self.latitude = latitude
        self.longitude = longitude


class BoundingBox:
    def __init__(self, location: Location, padding: float):
        self.borders: List = self.locations_to_bounding_box(location, padding)

    def locations_to_bounding_box(self, location, padding) -> List:
        bounding_box = [None, None, None, None]
        bounding_box[0] = min(bounding_box[0] or location.longitude, location.longitude) - padding
        bounding_box[1] = min(bounding_box[1] or location.latitude, location.latitude) - padding
        bounding_box[2] = max(bounding_box[2] or location.longitude, location.longitude) + padding
        bounding_box[3] = max(bounding_box[3] or location.latitude, location.latitude) + padding
        return bounding_box
    

class House:
    def __init__(self, location: Location, padding: float = 0.01):
        self.location = location
        self.bounding_box = BoundingBox(location, padding).borders

    def _get_nodes(self) -> ET.Element:
        url = 'http://www.overpass-api.de/api/xapi?*[amenity=*][bbox=%s]' % ",".join([str(x) for x in self.bounding_box])
        response = requests.get(url)
        if response.status_code != 200:
            print(f'Got status code: {response.status_code} from osm request')
            return []
        return ET.fromstring(response.content)

    def count_amenities_around_the_house(self) -> Dict:
        tree = self._get_nodes()
        amenities = {}
        for child in tree:
            for description in child.findall("tag"):
                if description.attrib["k"] == "amenity":
                    amenities[description.attrib["v"]] = amenities.get(description.attrib["v"], 0) + 1
        return amenities

    def get_amenity_frequency(self, amenity: str) -> int:
        counted_amenities = self.count_amenities_around_the_house()
        return counted_amenities.get(amenity, 0)


class PostRequestInput:
    def __init__(self, data) -> None:
        data = json.loads(data)
        self.title = self._get_main_key(data)
        self.house_details = self._get_body(data)

    def _get_main_key(self, data) -> str:
        return list(data.keys())[0]

    def _get_body(self, data) -> Dict:
        return data[self._get_main_key(data)][0]

    def get_house_location(self) -> Location:
        return Location(self.house_details["Latitude"], self.house_details["Longitude"])

    def add_to_house_details(self, key, value) -> None:
        self.house_details[key] = value

    def build_response(self) -> Dict:
        return {self.title: [self.house_details]}
