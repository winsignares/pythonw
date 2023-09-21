from Config.db import db, app, ma

class Detalles_prestamo(db.Model):
    __tablename__ = "tbl_detalles_prestamo"

    id = db.Column(db.Integer, primary_key = True)
    prestamo_id = db.Column(db.Integer, db.ForeignKey('tbl_prestamo.id'))
    prestamo_total = db.Column(db.Numeric)
    deuda = db.Column(db.Numeric)
    fecha_desembolso = db.Column(db.DateTime)
    corte = db.Column(db.DateTime)
    
    def __init__(self, id):
        self.id = id

with app.app_context():
    db.create_all()

class DetallesPrestamoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'prestamo_id', 'deuda', 'prestamo_total', 'fecha_desembolso', 'corte')