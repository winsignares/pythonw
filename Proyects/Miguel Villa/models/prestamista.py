from config.db import ma, db, app

class Prestamistas(db.Model):
    __tablename__ = 'tblprestamistas'

    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50))
    direccion = db.Column(db.String(50))
    numero_celular = db.Column(db.Integer)
    correo_electronico = db.Column(db.String(50))

    def __init__(self, nombre):
       self.nombre = nombre

with app.app_context():
    db.create_all()

class PrestamistasSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre', 'direccion', 'numero_celular', 'correo_electronico')