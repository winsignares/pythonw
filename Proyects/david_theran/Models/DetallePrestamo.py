from Config.db import db, app, ma

class LoanDetail(db.Model):
    __tablename__ = "tbl_loan_detail"

    id = db.Column(db.Integer, primary_key=True)
    loan_id = db.Column(db.Integer, db.ForeignKey('tbl_loan.id'))

    def __init__(self, loan_id):
        self.loan_id = loan_id

with app.app_context():
    db.create_all()

class LoanDetailSchema(ma.Schema):
    class Meta:
        fields = ('id', 'loan_id')
