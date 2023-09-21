from Config.db import db, app, ma

class Prestamo_detalle(db.Model):
    __tablename__ = "tbleprestamo_detalle"

    id = db.Column(db.Integer, primary_key = True)
    idPrestamo = db.Column(db.Integer, db.ForeignKey('tblprestamo.id'))
    monto = db.Column(db.Integer)
    fecha_pago= db.Column(db.Integer)
    status = db.Column(db.String(20))

    def __init__(self, idPrestamo):
        self.idPrestamo = idPrestamo

with app.app_context():
    db.create_all()

class Prestamo_detalleSchema(ma.Schema):
    class Meta:
        fields = ('id', 'idPrestamo','monto','fecha_pago','status')
        