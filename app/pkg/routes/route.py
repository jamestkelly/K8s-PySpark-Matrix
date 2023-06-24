from flask import Blueprint, jsonify
from app.pkg.utils.utils import *


bp = Blueprint('routes', __name__)


@bp.route('/')
def hello():
    """Root hello message call.

    Returns:
        dict: A JSON response containing the status of the API.
    """
    return jsonify({
        'status': 'ok',
        'message': 'Hello from K8s PySpark Matrix!'
    })


@bp.route('/health')
def health_check():
    """Health check endpoint to verify the status of the API.

    Returns:
        dict: A JSON response containing the status of the API.
    """
    return jsonify({
        'status': 'ok',
        'message': 'Service is live',
        'timestamp': get_local_time_string(),
        'machine': get_machine_details(),
        'performance': get_performance_metrics()
    })
