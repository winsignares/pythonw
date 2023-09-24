from Config.db import db, app, ma

class Prestamo(db.Model):
    __tablename__ = "tblprestamo"

    id = db.Column(db.Integer, primary_key = True)
    idCliente = db.Column(db.Integer, db.ForeignKey('tblcliente.id'))
    idPrestamista = db.Column(db.Integer, db.ForeignKey('tblprestamista.id'))
    fecha = db.Column(db.Date)
    tasa = db.Column(db.Integer)
    montoPrestado =  db.Column(db.Integer) 
    total = db.Column(db.Integer)

    def __init__(self, idCliente, idPrestamista, fecha, tasa, montoPrestado, total):
        self.idCliente = idCliente
        self.idPrestamista = idPrestamista
        self.fecha = fecha
        self.tasa = tasa
        self.montoPrestado = montoPrestado
        self.total = total

with app.app_context():
    db.create_all()

class PrestamoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'idCliente', 'idPrestamista', 'fecha', 'tasa', 'montoPrestado', 'total')
        