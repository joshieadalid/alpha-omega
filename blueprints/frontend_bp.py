from flask import Blueprint, send_from_directory, redirect
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_BUILD_DIR = os.path.join(BASE_DIR, '..', 'jira_project_frontend', 'build')

frontend_bp = Blueprint('frontend', __name__, static_folder=FRONTEND_BUILD_DIR)

@frontend_bp.route('/index.html')
def redirect_index():
    return redirect('/')

@frontend_bp.route('/', defaults={'path': ''})
@frontend_bp.route('/<path:path>')
def serve_react(path):
    full_path = os.path.join(frontend_bp.static_folder, path)
    if path != "" and os.path.exists(full_path):
        return send_from_directory(frontend_bp.static_folder, path)
    return send_from_directory(frontend_bp.static_folder, 'index.html')
