from Config.db import db, app, ma

class DetallePrestamo(db.Model):
    __tablename__ = 'detalle_prestamos'

    id = db.Column(db.Integer, primary_key=True)
    id_prestamo = db.Column(db.Integer)
    fecha_desembolso = db.Column(db.Date)
    monto_desembolsado = db.Column(db.Float)
    fecha_vencimiento = db.Column(db.Date)
    monto_pendiente = db.Column(db.Float)
    intereses_acumulados = db.Column(db.Float)
    capital_pagado = db.Column(db.Float)
    cuota_mensual = db.Column(db.Float)

    def __init__(self, id_prestamo, fecha_desembolso, monto_desembolsado, fecha_vencimiento, monto_pendiente, intereses_acumulados, capital_pagado, cuota_mensual):
        self.id_prestamo = id_prestamo
        self.fecha_desembolso = fecha_desembolso
        self.monto_desembolsado = monto_desembolsado
        self.fecha_vencimiento = fecha_vencimiento
        self.monto_pendiente = monto_pendiente
        self.intereses_acumulados = intereses_acumulados
        self.capital_pagado = capital_pagado
        self.cuota_mensual = cuota_mensual


with app.app_context():
    db.create_all()

class DetallePrestamoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'id_prestamo', 'fecha_desembolso', 'monto_desembolsado', 'fecha_vencimiento', 'monto_pendiente', 'intereses_acumulados', 'capital_pagado', 'cuota_mensual')

