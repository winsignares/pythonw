from config.db import ma, db, app

class Cliente(db.Model):
    __tablename__ = 'cliente'

    id_cliente = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50))
    apellido = db.Column(db.String(50))
    telefono = db.Column(db.String(50))
    direccion = db.Column(db.String(50))
    

    def __init__(self, nombre):
       self.nombre = nombre

with app.app_context():
    db.create_all()

class ClienteSchema(ma.Schema):
    class Meta:
        fields = ('id_cliente', 'nombre', 'apellido', 'telefono', 'direccion')