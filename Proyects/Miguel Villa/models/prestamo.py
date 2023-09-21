from config.db import ma, db, app

class Prestamos(db.Model):
    __tablename__ = "tblprestamos"

    id = db.Column(db.Integer, primary_key = True)
    idPrestamista = db.Column(db.Integer, db.ForeignKey('tblprestamistas.id'))
    idCliente = db.Column(db.Integer, db.ForeignKey('tblclientes.id'))
    monto = db.Column(db.Integer)
    interes = db.Column(db.Integer)
    fecha = db.Column(db.String(20))
    estado = db.Column(db.String(20))

    def __init__(self, idCliente, idPrestamista):
        self.idCliente = idCliente
        self.idPrestamista = idPrestamista

with app.app_context():
    db.create_all()

class PrestamosSchema(ma.Schema):
    class Meta:
        fields = ('id', 'idCliente','idPrestamista', 'monto','interes','fecha','estado')
        