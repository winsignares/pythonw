from Config.db import ma, db, app

class Prestamista(db.Model):
    __tablename__ = 'tblprestamista'

    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(20))
    apellido = db.Column(db.String(20))
    direccion = db.Column(db.String(30))
    correo = db.Column(db.String(50))
    telefono = db.Column(db.Integer)
    
    def __init__(self, nombre,apellido,direccion,correo,telefono):
       self.nombre = nombre
       self.apellido = apellido
       self.direccion = direccion
       self.correo = correo
       self.telefono = telefono

with app.app_context():
    db.create_all()

class PrestamistaSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre','apellido','direccion','correo','telefono')