from Config2.db import app, db, ma

class Prestamo(db.Model):
    __tablename__ = "tblprestamo"

    id = db.Column(db.Integer, primary_key = True)
    idCliente = db.Column(db.Integer, db.ForeignKey('tblcliente.id'))
    monto = db.Column(db.String(50))
    tasainteres = db.Column(db.Float)
    fechainicio = db.Column(db.String(50))
    fechafin = db.Column(db.String(50))

    def __init__(self, idCliente):
        self.idCliente = idCliente

with app.app_context():
    db.create_all()

class PrestamoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'idCliente','monto','tasainteres','fechainicio','fechafin')
        