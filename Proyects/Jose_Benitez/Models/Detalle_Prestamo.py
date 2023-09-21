from Config.db import db, app, ma

class Detalle_Prestamo(db.Model):
    __tablename__ = "tbldetalle_prestamo"

    id = db.Column(db.Integer, primary_key = True)
    fecha = db.Column(db.String(60))
    idPrestamo = db.Column(db.Integer, db.ForeignKey('tblprestamo.id'))

    def __init__(self,fecha, idPrestamo):
        self.fecha = fecha
        self.idPrestamo = idPrestamo

with app.app_context():
    db.create_all()

class Detalle_PrestamoSchema(ma.Schema):
    class Meta:
        fields = ('id','fecha', 'idPrestamo')