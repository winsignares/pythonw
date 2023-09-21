from config.db import db, app, ma

class Pago(db.Model):
    __tablename__ = "tblpago"

    id = db.Column(db.Integer, primary_key=True)
    id_prestamo = db.Column(db.Integer, db.ForeignKey('tblprestamo.id'))
    fecha_pago = db.Column(db.Date)
    monto_pago = db.Column(db.Float)
    numero_cuota = db.Column(db.Integer)


    def __init__(self, id_prestamo, fecha_pago, monto_pago, numero_cuota):
        self.id_prestamo = id_prestamo
        self.fecha_pago = fecha_pago
        self.monto_pago = monto_pago
        self.numero_cuota = numero_cuota

with app.app_context():
    db.create_all()

class PagoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'id_prestamo', 'fecha_pago', 'monto_pago', 'numero_cuota')