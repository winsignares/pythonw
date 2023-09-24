from Config.db import db, app, ma

class Prestamo(db.Model):
    __tablename__ = "tblprestamo"

    id = db.Column(db.Integer, primary_key = True)
    idCliente = db.Column(db.Integer, db.ForeignKey('tblcliente.id'))
    idPrestamista = db.Column(db.Integer, db.ForeignKey('tblprestamista.id'))
    fechaPrestamo = db.Column(db.Date)
    tasa = db.Column(db.Integer)
    valorPrestamo =  db.Column(db.Integer) 
    total = db.Column(db.Integer)

    def __init__(self, idCliente, idPrestamista, fechaPrestamo, tasa, valorPrestamo, total):
        self.idCliente = idCliente
        self.idPrestamista = idPrestamista
        self.fechaPrestamo = fechaPrestamo
        self.tasa = tasa
        self.valorPrestamo = valorPrestamo
        self.total = total

with app.app_context():
    db.create_all()

class PrestamoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'idCliente', 'idPrestamista', 'fechaPrestamo', 'tasa', 'valorPrestamo', 'total')