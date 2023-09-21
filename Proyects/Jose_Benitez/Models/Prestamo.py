from Config.db import db, app, ma

class Prestamo(db.Model):
    __tablename__ = "tblprestamo"

    id = db.Column(db.Integer, primary_key = True)
    monto = db.Column(db.Integer)
    idCliente = db.Column(db.Integer, db.ForeignKey('tblcliente.id'))
    idPrestamista = db.Column(db.Integer, db.ForeignKey('tblprestamista.id'))

    def __init__(self,monto, idCliente,idPrestamista):
        self.monto = monto
        self.idCliente = idCliente
        self.idPrestamista = idPrestamista

with app.app_context():
    db.create_all()

class PrestamoSchema(ma.Schema):
    class Meta:
        fields = ('id','monto', 'idCliente','idPrestamista')