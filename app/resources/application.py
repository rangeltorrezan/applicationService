__author__ = 'rangel.torrezan'
import json

from flask import jsonify, abort, request, url_for
from app import app
from app.controllers.application import ApplicationCtrl
from app.resources import error_handler

@app.route('/api/v1/applications', methods=['GET'])
def get_app():
    return json.dumps([ob.as_json() for ob in ApplicationCtrl().get()])

@app.route('/api/v1/applications/<int:app_id>', methods=['GET'])
def get_app_id(app_id):

    application = ApplicationCtrl().get_id(app_id)

    if type (application) is str:
        return application

    else:
        return json.dumps(application.as_json())

@app.route('/api/v1/applications', methods=['POST'])
def create_app():
    if not request.json:
        abort(400)

    return json.dumps(ApplicationCtrl().create(request.json).as_json())

@app.route('/api/v1/applications/<int:app_id>', methods=['PUT'])
def update_app(app_id):
    application = ApplicationCtrl().update(app_id, request.json)

    if type (application) is str:
        return application
    else:
        return json.dumps(application.as_json())

@app.route('/api/v1/applications/<int:app_id>', methods=['DELETE'])
def delete_app(app_id):
    return ApplicationCtrl().delete(app_id)