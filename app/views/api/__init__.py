from flask import Blueprint, abort, request, jsonify
from dboard import convert_error_to_json_response
from werkzeug.exceptions import HTTPException
from ...queries.pagila import RentalsList, PaymentsList


api_bp = Blueprint('api_bp', __name__)


@api_bp.errorhandler(HTTPException)
def handle_exception(e):
    return convert_error_to_json_response(e)

@api_bp.route("/rentals")
def rentals():
    return RentalsList().render_response()

@api_bp.route("/payments")
def payments():
    return PaymentsList().render_response()

@api_bp.route("/dummy")
def dummy():
    page = int(request.args.get("page", 1))
    return jsonify({
        "status": "success",
        "data": [{
            "day": "2020-03-02",
            "count": 10 * page
        }, {
            "day": "2020-03-03",
            "count": 15 * page
        }, {
            "day": "2020-03-04",
            "count": 19 * page
        }, {
            "day": "2020-03-05",
            "count": 15 * page
        }],
        "page": page,
        "per_page": 4,
        "total_pages": 8,
        "total_items": 30,
        "columns": ["day", "count"]
    })