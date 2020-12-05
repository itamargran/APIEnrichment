import json

from flask import Flask, jsonify, request
from typing import Dict
from errors import fail
import models


app = Flask(__name__)

@app.route("/api/enrich", methods=["POST"])
def add_number_of_schools():
    try:
        request_content = models.PostRequestInput(request.data)
        house = models.House(request_content.get_house_location())
        request_content.add_to_house_details("Schools", house.get_entity_frequency("school"))
    except json.decoder.JSONDecodeError:
        return fail(400, "Could not read the request body")
    except TypeError:
        return fail(400, "Something is wrong with the input's data stractures")
    except KeyError:
        return fail(400, "Input should have lat and lon")
    return jsonify(request_content.build_response())

if __name__ == "__main__":
    app.run(debug=True)
