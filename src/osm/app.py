import json

from flask import Flask, jsonify, request

from errors import fail
from models import House, PostRequestInput


app = Flask(__name__)


@app.route("/api/enrich", methods=["POST"])
def add_number_of_schools():
    try:
        request_content = PostRequestInput(request.data)
        house = House(request_content.get_house_location())
        request_content.add_to_house_details(
            key="Schools",
            value=house.get_amenity_frequency("school")
        )
    except json.decoder.JSONDecodeError:
        return fail(400, "Could not read the request body")
    except TypeError:
        return fail(400, "Something is wrong with the input's data stractures")
    except KeyError:
        return fail(400, "Input should have lat and lon")
    return jsonify(request_content.build_response())


if __name__ == "__main__":
    app.run(debug=True, port=5000)
