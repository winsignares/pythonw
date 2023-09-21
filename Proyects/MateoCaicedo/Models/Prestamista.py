from Config.db import db, app, ma

class Prestamista(db.Model):
    __tablename__ = 'prestamistas'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    telefono = db.Column(db.String(15))
    direccion = db.Column(db.String(100))
    email = db.Column(db.String(100))
    tasa_interes = db.Column(db.Float)

    def __init__(self, nombre, telefono, direccion, email, tasa_interes):
        self.nombre_prestamista = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.email = email
        self.tasa_interes = tasa_interes

with app.app_context():
    db.create_all()

class PrestamistaSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre', 'telefono', 'direccion', 'email', 'tasa_interes')
