from config.db import ma, db, app

class Cliente(db.Model):
    __tablename__ = "tblcliente"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255))
    apellido = db.Column(db.String(255))
    direccion = db.Column(db.String(255))
    telefono = db.Column(db.String(20))
    correo_electronico = db.Column(db.String(255))

    def __init__(self, id, nombre, apellido, direccion, telefono, correo_electronico):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.telefono = telefono
        self.correo_electronico = correo_electronico

with app.app_context():
    db.create_all()

class ClienteSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre', 'apellido', 'direccion', 'telefono', 'correo_electronico')
