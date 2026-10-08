from flask import Flask, jsonify, request
from backend.database import emergency_collection
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return jsonify({
        "message": "Smart Emergency Route Navigator API is running!"
    })


@app.route("/test-db")
def test_db():
    emergency_collection.insert_one({
        "test": "MongoDB connection successful"
    })

    return jsonify({
        "message": "Data inserted into MongoDB successfully!"
    })


@app.route("/emergency", methods=["POST"])
def emergency_request():
    data = request.get_json()

    emergency = {
        "patient_name": data.get("patient_name"),
        "pickup_location": data.get("pickup_location"),
        "destination": data.get("destination"),
        "emergency_type": data.get("emergency_type")
    }

    result = emergency_collection.insert_one(emergency)

    return jsonify({
        "message": "Emergency request created successfully!",
        "request_id": str(result.inserted_id)
    }), 201



@app.route("/emergencies", methods=["GET"])
def get_emergencies():

    emergencies = list(emergency_collection.find())

    results = []

    for emergency in emergencies:

        emergency_id = str(emergency["_id"])
        emergency.pop("_id", None)

        emergency["id"] = emergency_id

        results.append(emergency)

    return jsonify({
        "emergencies": results
    })
@app.route("/activate-signal", methods=["POST"])
def activate_signal():

    data = request.get_json()

    if data.get("ambulance") == True:
        return jsonify({
            "message": "Ambulance priority activated successfully!"
        }), 200

    return jsonify({
        "message": "Ambulance priority activation failed."
    }), 400
if __name__ == "__main__":
    app.run(debug=True)


# Do not run the app here; use the project's root launcher (app.py)