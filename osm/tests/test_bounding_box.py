import pytest
from osm.models import BoundingBox, Location


class TestBoundingBox:
    def test_location_to_bounding_box(self):
        location = Location(0, 0)
        bounding_box = BoundingBox(location, padding=1)
        assert bounding_box.borders == [-1, -1, 1, 1]
