from Config.db import db, app, ma

class PrestamoDetalle(db.Model):
    __tablename__ = "tblprestamo_Detalle"

    id = db.Column(db.Integer, primary_key = True)
    idPrestamo = db.Column(db.Integer, db.ForeignKey('tblprestamo.id'))
    cuota = db.Column(db.Integer)
    estado_prestamo = db.Column(db.String(60))

    def __init__(self, idPrestamo,cuota,estado_prestamo):
        self.idPrestamo = idPrestamo
        self.cuota=cuota
        self.estado_prestamo = estado_prestamo

with app.app_context():
    db.create_all()

class PrestamoDetalleSchema(ma.Schema):
    class Meta:
        fields = ('id', 'idPrestamo','cuota','estado_prestamo')
        