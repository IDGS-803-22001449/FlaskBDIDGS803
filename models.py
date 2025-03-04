from flask_sqlalchemy import SQLAlchemy
 
import datetime
# crea una clase de Sqlalchemy para inciar la libreria
db=SQLAlchemy()
class Alumnos(db.Model):
    # crea una tabla llamada alumnos para iniciar la tabla en la bd
    __tablename__='alumnos'
    # crea los campos de la tabla alumnos
    id=db.Column(db.Integer,primary_key=True)
    nombre=db.Column(db.String(50))
    apaterno=db.Column(db.String(50))
    email=db.Column(db.String(50))
    created_date=db.Column(db.DateTime,
                    default=datetime.datetime.now)