from Config.db import ma, db, app

class Cliente(db.Model):
    __tablename__ = 'tblcliente'

    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50))

    def __init__(self, nombre):
       self.nombre = nombre

with app.app_context():
    db.create_all()

class ClienteSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre')