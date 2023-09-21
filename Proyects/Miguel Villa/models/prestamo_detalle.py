from config.db import ma, db, app

class Prestamos_detalle(db.Model):
    __tablename__ = "tblprestamos_detalle"

    id = db.Column(db.Integer, primary_key = True)
    idPrestamo = db.Column(db.Integer, db.ForeignKey('tblprestamos.id'))
    monto = db.Column(db.Integer)
    fecha_pago= db.Column(db.Integer)
    estado = db.Column(db.String(20))

    def __init__(self, idPrestamo):
        self.idPrestamo = idPrestamo

with app.app_context():
    db.create_all()

class Prestamos_detalleSchema(ma.Schema):
    class Meta:
        fields = ('id', 'idPrestamo','monto','fecha_pago','estados')
        