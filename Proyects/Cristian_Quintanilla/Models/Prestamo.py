from Config.db import db, app, ma

class Prestamo(db.Model):
    __tablename__ = "tblprestamo"

    id = db.Column(db.Integer, primary_key = True)
    idCliente = db.Column(db.Integer, db.ForeignKey('tblcliente.id'))
    idPrestamista = db.Column(db.Integer, db.ForeignKey('tblprestamista.id'))
    totalPrestado = db.Column(db.Integer)
    fecha_aprobacion = db.Column(db.String(60))
    fecha_vencimiento = db.Column(db.String(60))

    def __init__(self, idCliente,idPrestamista,totalPrestado,fecha_aprobacion,fecha_vencimiento):
        self.idCliente = idCliente
        self.idPrestamista=idPrestamista
        self.totalPrestado = totalPrestado
        self.fechaAprobacion = fecha_aprobacion
        self.fecha_vencimiento = fecha_vencimiento
        

with app.app_context():
    db.create_all()

class PrestamoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'idCliente','idPrestamista','totalPrestado','fecha_aprobacion','fecha_vencimiento')
        