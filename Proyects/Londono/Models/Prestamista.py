from Config.db import db, app, ma

class Prestamista(db.Model):
    __tablename__ = "tblprestamista"

    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50))
    correo = db.Column(db.String(50))
    telefono = db.Column(db.String(10))

    def __init__(self, nombre, correo, telefono):
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono

with app.app_context():
    db.create_all()

class PrestamistaSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre', 'correo', 'telefono')