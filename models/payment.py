
from repository.database import db

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Float)
    paid = db.Column(db.Boolean, default=False)
    bank_paymetn_id = db.Column(db.Integer, nullable=True)
    qr_Code = db.Column(db.String(100), nullable=True)
    expiration_date = db.Column(db.DateTime)

    def __init__(self, id=None, value=None, paid=False, bank_payment_id=None, qr_code=None, expiration_date=None) -> None:
        self.id = id
        self.value = value
        self.paid = paid
        self.bank_paymetn_id = bank_payment_id
        self.qr_Code = qr_code
        self.expiration_date = expiration_date
    def to_dict(self):
        return {
            "id": self.id,
            "value": self.value,
            "paid": self.paid,
            "bank_payment_id": self.bank_paymetn_id,
            "qr_code": self.qr_Code,
            "expiration_date": self.expiration_date
        }

