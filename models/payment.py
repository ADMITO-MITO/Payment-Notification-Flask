
from repository.database import db

class Payment(db.Model):
    id = db.Column(db.Interger, primary_key=True)
    value = db.Column(db.Float)
    paid = db.Column(db.Boolean, default=False)
    bank_paymetn_id = db.Column(db.Interger, nullable=True)
    qr_Code = db.Column(db.String(100), nullable=True)
    expiration_date = db.Column(db.DateTime)

    def __init__(self, id, value, paid, bank_payment_id, qr_code, expiration_date) -> None:
        self.id = id
        self.value = value
        self.paid = paid
        self.bank_paymetn_id = bank_payment_id
        self.qr_Code = qr_code
        self.expiration_date = expiration_date

