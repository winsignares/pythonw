from Config.db import db, app, ma

class Prestamo(db.Model):
    __tablename__ = "tblprestamo"

    id = db.Column(db.Integer, primary_key = True)
    idPrestamista = db.Column(db.Integer, db.ForeignKey('tblprestamista.id'))
    idCliente = db.Column(db.Integer, db.ForeignKey('tblcliente.id'))
    monto = db.Column(db.Integer)
    interes = db.Column(db.Integer)
    fecha_solicitud = db.Column(db.Integer)
    status = db.Column(db.String(20))

    def __init__(self, idCliente, idPrestamista):
        self.idCliente = idCliente
        self.idPrestamista = idPrestamista

with app.app_context():
    db.create_all()

class PrestamoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'idCliente','idPrestamista', 'monto','interes','fecha_solicitud','status')
        