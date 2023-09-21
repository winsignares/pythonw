from Config.db import db, app, ma

class Prestamo(db.Model):
    __tablename__ = 'prestamos'

    id = db.Column(db.Integer, primary_key=True)
    id_cliente = db.Column(db.Integer)
    id_prestamista = db.Column(db.Integer)
    fecha_solicitud = db.Column(db.Date)
    monto_solicitado = db.Column(db.Float)
    fecha_aprobacion = db.Column(db.Date)
    monto_aprobado = db.Column(db.Float)
    termino_meses = db.Column(db.Integer)
    tasa_interes_aplicada = db.Column(db.Float)
    cuota_mensual = db.Column(db.Float)
    estado_prestamo = db.Column(db.String(20))

    def __init__(self, id_cliente, id_prestamista, fecha_solicitud, monto_solicitado, fecha_aprobacion, monto_aprobado, termino_meses, tasa_interes_aplicada, cuota_mensual, estado_prestamo):
        self.id_cliente = id_cliente
        self.id_prestamista = id_prestamista
        self.fecha_solicitud = fecha_solicitud
        self.monto_solicitado = monto_solicitado
        self.fecha_aprobacion = fecha_aprobacion
        self.monto_aprobado = monto_aprobado
        self.termino_meses = termino_meses
        self.tasa_interes_aplicada = tasa_interes_aplicada
        self.cuota_mensual = cuota_mensual
        self.estado_prestamo = estado_prestamo

with app.app_context():
    db.create_all()

class PrestamoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'id_cliente', 'id_prestamista', 'fecha_solicitud', 'monto_solicitado', 'fecha_aprobacion', 'monto_aprobado', 'termino_meses', 'tasa_interes_aplicada', 'cuota_mensual', 'estado_prestamo')
