from Config.db import db, app, ma

class DetPrestamo(db.Model):
    __tablename__ = "tbldetPrestamo"

    id = db.Column(db.Integer, primary_key = True)
    idPrestamo = db.Column(db.Integer, db.ForeignKey('tblprestamo.id'))
    fechaAbono = db.Column(db.Date)
    cuota = db.Column(db.Integer)


    def __init__(self, idPrestamo, fechaAbono, cuota):
        self.idPrestamo = idPrestamo
        self.fechaAbono = fechaAbono
        self.cuota = cuota


with app.app_context():
    db.create_all()

class DetPrestamoSchema(ma.Schema):
    class Meta:
        fields = ('id','idPrestamo', 'fechaAbono', 'cuota')