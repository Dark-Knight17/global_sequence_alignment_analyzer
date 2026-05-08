from flask import Blueprint, render_template, request, jsonify
from app.services.alignment_service import AlignmentService

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/align', methods=['POST'])
def align():
    data = request.get_json()
    if not data:
        return jsonify({"success": False, "error": "No data provided"}), 400
        
    result = AlignmentService.run_alignment(data)
    return jsonify(result)
