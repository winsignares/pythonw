from Config.db import db, app, ma


class Loan(db.Model):
    __tablename__ = "tbl_loan"

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('tbl_customer.id'))
    lender_id = db.Column(db.Integer, db.ForeignKey('tbl_lender.id'))

    def __init__(self, customer_id, lender_id):
        self.customer_id = customer_id
        self.lender_id = lender_id


with app.app_context():
    db.create_all()


class LoanSchema(ma.Schema):
    class Meta:
        fields = ('id', 'customer_id', 'lender_id')
