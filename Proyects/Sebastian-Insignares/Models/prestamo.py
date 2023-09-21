from Config.db import db, app, ma

class Prestamo(db.Model):
    __tablename__ = "tblprestamo"

    id = db.Column(db.Integer, primary_key = True)
    id_cliente = db.Column(db.Integer, db.ForeignKey('tblcliente.id'))
    id_prestamista = db.Column(db.Integer, db.ForeignKey('tblprestamista.id'))
    fecha_solicitud = db.Column(db.DateTime)
    tasa_interes = db.Column(db.Numeric)
    plazo_meses = db.Column(db.Integer)
    estado = db.Column(db.String(50))

    def __init__(self, id_cliente):
        self.id_cliente = id_cliente

with app.app_context():
    db.create_all()

class PrestamoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'id_cliente', 'id_prestamista', 'fecha_solicitud', 'tasa_interes', 'plazo_meses', 'estado')
        