from Config.db import ma, db, app

class Cliente(db.Model):
    __tablename__ = 'tblcliente'

    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50))
    correo = db.Column(db.String(50))
    telefono = db.Column(db.String(10))
    direccion = db.Column(db.String(50))

    def __init__(self, nombre, correo, telefono, direccion):
       self.nombre = nombre
       self.correo = correo
       self.telefono = telefono
       self.direccion = direccion

with app.app_context():
    db.create_all()

class ClienteSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre', 'correo', 'telefono', 'direccion')