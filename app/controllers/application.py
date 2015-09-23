__author__ = 'rangel.torrezan'

from app.models.application import Application
from app import db

class ApplicationCtrl():


    def get(self):
        applications = Application.query.all()
        return applications

    def get_id(self, id):
        application = Application.query.filter_by(id=id).one()
        if(application):
            return application
        else:
            return "Registro nao encontrado"

    def create(self, obj):
        application = Application(
            obj['application'],
            obj['name'],
            obj['baseUrl'],
            obj['title'],
            obj['classe'],
            obj['parent']
        )

        db.session.add(application)
        db.session.commit()
        return application

    def update(self, id, obj):
        application = Application.query.filter_by(id=id).first()

        if(application):
            db.session.query(Application).filter(Application.id == id).update(obj)
            db.session.commit()
            return application
        else:
            return "Registro nao encontrado"

    def delete(self, id):
        application = Application.query.filter_by(id=id).one()

        if(application):
            db.session.query(Application).filter(Application.id == id).delete()
            db.session.commit()
            return "Registro apagado"
        else:
            return "Registro nao encontrado"