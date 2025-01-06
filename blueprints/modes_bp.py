from flask import Blueprint, render_template

modes_bp = Blueprint('modes', __name__)


@modes_bp.route('/meeting')
def mode_meeting():
    return render_template('modes/mode_meeting.html')

@modes_bp.route('/minutes')
def mode_minute():
    return render_template('modes/minutes.html')
