from flask.testing import FlaskClient
import pytest
from typing import Dict

from app import app
from tests.data_generator import PostRequestContentGenerator


class TestApp:
    @pytest.fixture
    def test_client(self) -> FlaskClient:
        return app.test_client()

    def test_add_number_of_schools(self, test_client):
        url = "/api/enrich"

        empty_response = test_client.post(url, data={})
        assert empty_response.status_code == 400

        valid_response = test_client.post(
            url,
            data=(
                PostRequestContentGenerator.generate_post_request_content()
            ),
        )
        assert valid_response.status_code == 200
