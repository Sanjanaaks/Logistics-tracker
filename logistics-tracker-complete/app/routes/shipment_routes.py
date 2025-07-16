from flask import Blueprint, request, jsonify, current_app
from bson.objectid import ObjectId

shipment_bp = Blueprint('shipment_bp', __name__)

@shipment_bp.route('/shipments', methods=['POST'])
def create_shipment():
    data = request.json
    data['status'] = 'Created'
    result = current_app.db.shipments.insert_one(data)
    return jsonify({"shipment_id": str(result.inserted_id), "details": data})

@shipment_bp.route('/shipments/<shipment_id>', methods=['GET'])
def get_shipment(shipment_id):
    shipment = current_app.db.shipments.find_one({"_id": ObjectId(shipment_id)})
    if shipment:
        shipment['_id'] = str(shipment['_id'])
        return jsonify(shipment)
    return jsonify({"error": "Shipment not found"}), 404

@shipment_bp.route('/shipments/<shipment_id>/status', methods=['PUT'])
def update_status(shipment_id):
    new_status = request.json.get('status')
    result = current_app.db.shipments.update_one(
        {"_id": ObjectId(shipment_id)},
        {"$set": {"status": new_status}}
    )
    if result.matched_count:
        shipment = current_app.db.shipments.find_one({"_id": ObjectId(shipment_id)})
        shipment['_id'] = str(shipment['_id'])
        return jsonify({"message": "Status updated", "shipment": shipment})
    return jsonify({"error": "Shipment not found"}), 404
