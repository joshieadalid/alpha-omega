from flask import Blueprint, render_template
from utils.auth import jwt_required

modes_bp = Blueprint('modes', __name__)


@modes_bp.route('/meeting')
def mode_meeting():
    return render_template('modes/mode_meeting.html')
