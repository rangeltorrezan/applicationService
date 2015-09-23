__author__ = 'rangel.torrezan'
from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Application Service"