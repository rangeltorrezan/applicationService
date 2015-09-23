__author__ = 'rangel.torrezan'
from app import db

class Application (db.Model):
    id = db.Column(db.Integer, db.Sequence('id_seq'), primary_key=True, nullable=False)
    application = db.Column('application', db.String (20))
    name = db.Column('name', db.String (20))
    baseUrl = db.Column('baseUrl', db.String(50))
    title = db.Column('title', db.String(50))
    classe = db.Column('classe', db.String(50))
    parent = db.Column('parent', db.String(20))

    def __init__(self, application, name, baseUrl, title, classe, parent):
        self.application = application
        self.name = name
        self.baseUrl = baseUrl
        self.title = title
        self.classe = classe
        self.parent = parent


    def __repr__(self):
        return '<Application %r>' % self.application

    def as_json(self):
        return dict(
            id = self.id,
            application = self.application,
            name = self.name,
            baseUrl = self.baseUrl,
            title = self.title,
            classe = self.classe,
            parent = self.parent)