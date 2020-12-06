import pytest
from osm.models import PostRequestInput

class TestPostRequestInput:
    @pytest.fixture
    def request_input(self):
        with open(r"tests/samples/sample_data.txt", "r") as file:
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
