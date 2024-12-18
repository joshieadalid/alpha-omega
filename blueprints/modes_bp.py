from flask import Blueprint, render_template

modes_bp = Blueprint('modes', __name__)

@modes_bp.route('/recording')
def mode_recording():
    return render_template('modes/mode_recording.html')

@modes_bp.route('/meeting')
def mode_meeting():
    return render_template('modes/mode_meeting.html')
