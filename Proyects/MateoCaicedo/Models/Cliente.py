from Config.db import db, app, ma

class Cliente(db.Model):
    __tablename__ = 'clientes'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    apellido = db.Column(db.String(50))
    telefono = db.Column(db.String(15))
    direccion = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __init__(self, nombre, apellido, telefono, direccion, email):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.direccion = direccion
        self.email = email

with app.app_context():
    db.create_all()

class ClienteSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre', 'apellido', 'telefono', 'direccion', 'email')

