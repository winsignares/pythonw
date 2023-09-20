from Config.db import db, app, ma

class Detalles_prestamo(db.Model):
    __tablename__ = "tbldetalles_prestamo"

    id = db.Column(db.Integer, primary_key = True)
    id_prestamo = db.Column(db.Integer, db.ForeignKey('tblprestamo.id'))
    saldo_pendiente = db.Column(db.Numeric)
    monto_desembolsado = db.Column(db.Numeric)
    fecha_desembolso = db.Column(db.DateTime)
    fecha_pago = db.Column(db.DateTime)
    
    def __init__(self, id):
        self.id = id

with app.app_context():
    db.create_all()

class DetallesPrestamoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'id_prestamo', 'saldo_pendiente', 'monto_desembolsado', 'fecha_desembolso', 'fecha_pago')
        