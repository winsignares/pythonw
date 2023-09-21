from config.db import db, app, ma

class Prestamo(db.Model):
    __tablename__ = "tblprestamo"

    id = db.Column(db.Integer, primary_key=True)
    id_cliente = db.Column(db.Integer, db.ForeignKey('tblcliente.id'))
    prestamista_id = db.Column(db.Integer, db.ForeignKey('tblprestamista.id'))
    monto_prestamo = db.Column(db.Float)
    fecha_inicio = db.Column(db.Date)
    fecha_finalizacion = db.Column(db.Date)
    tasa_interes = db.Column(db.Float)
    estado_prestamo = db.Column(db.String(50))
    cuotas_pendientes = db.Column(db.Integer)

    def __init__(self, id_cliente, prestamista_id, monto_prestamo, fecha_inicio, fecha_finalizacion, tasa_interes, estado_prestamo, cuotas_pendientes):
        self.id_cliente = id_cliente
        self.prestamista_id = prestamista_id
        self.monto_prestamo = monto_prestamo
        self.fecha_inicio = fecha_inicio
        self.fecha_finalizacion = fecha_finalizacion
        self.tasa_interes = tasa_interes
        self.estado_prestamo = estado_prestamo
        self.cuotas_pendientes = cuotas_pendientes

with app.app_context():
    db.create_all()

class PrestamoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'id_cliente', 'prestamista_id', 'monto_prestamo', 'fecha_inicio', 'fecha_finalizacion', 'tasa_interes', 'estado_prestamo', 'cuotas_pendientes')
