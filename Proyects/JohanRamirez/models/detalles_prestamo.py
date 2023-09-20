from config.db import db, app, ma

class DetallesPrestamo(db.Model):
    __tablename__ = "detalles_prestamo"

    id_detalle = db.Column(db.Integer, primary_key = True)
    id_prestamo = db.Column(db.Integer, db.ForeignKey('prestamo.id_prestamo'))
    saldo_pendiente = db.Column(db.Numeric)
    monto_desembolsado = db.Column(db.Numeric)
    fecha_desembolso = db.Column(db.DateTime)
    fecha_pago = db.Column(db.DateTime)
    
    def __init__(self, id_detalle):
        self.id_detalle = id_detalle

with app.app_context():
    db.create_all()

class DetallesPrestamoSchema(ma.Schema):
    class Meta:
        fields = ('id_detalle', 'id_prestamo', 'saldo_pendiente', 'monto_desembolsado', 'fecha_desembolso', 'fecha_pago')
        