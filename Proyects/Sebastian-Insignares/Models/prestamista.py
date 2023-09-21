from Config.db import ma, db, app

class Prestamista(db.Model):
    __tablename__ = 'tblprestamista'

    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50))
    telefono = db.Column(db.String(50))
    
    def __init__(self, nombre):
       self.nombre = nombre

with app.app_context():
    db.create_all()

class PrestamistaSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre', 'telefono')