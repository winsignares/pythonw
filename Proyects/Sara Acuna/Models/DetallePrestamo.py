from Config.db import db, app, ma

class DetallePrestamo(db.Model):
    __tablename__ = "tbldetalleprestamo"

    id = db.Column(db.Integer, primary_key = True)
    idPrestamo = db.Column(db.Integer, db.ForeignKey('tblprestamo.id'))

    def __init__(self, idPrestamo):
        self.idPrestamo = idPrestamo

with app.app_context():
    db.create_all()

class DetallePrestamoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'idPrestamo')
        