from tarfile import data_filter
from flask import Flask, jsonify, request
from repository.database import db
from datetime import datetime, timedelta
import uuid
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECREAT_KEY'] = 'SECREAT_KEY_WEBSOCKET'
with app.app_context():
    db.init_app(app)
    db.create_all()
    db.session.commit()

static_image_path = os.path.join(BASE_DIR, 'static', 'image')
os.makedirs(static_image_path, exist_ok=True)
print(f"Diretório criado em: {static_image_path}")


from models.payment import Payment
from models.payments.pix import Pix

@app.route('/payments/pix', methods=["POST"])
def create_paymetn_pix():
    data = request.get_json()

    if 'value' not in data:
        return jsonify({"message": "Invalid value"}), 400
    expiration_date = datetime.now() + timedelta(minutes=30)

    pix_obj = Pix()
    data_payment_pix = pix_obj.create_payment(BASE_DIR)
    new_payment = Payment(value=data['value'], expiration_date=expiration_date, bank_payment_id=data_payment_pix['bank_payment_id'], qr_code=data_payment_pix['qr_code_path'])
    db.session.add(new_payment)
    db.session.commit()
    return jsonify({
        "message": "The payment has been created",
        "payment": new_payment.to_dict(),
        "qr_code_url": f"/static/image/qr_code_payment_{data_payment_pix['bank_payment_id']}.png"
    })

@app.route('/payments/pix/confirmation', methods=["POST"])
def pix_confirmation():
    return jsonify({"message": "The payment has been confrimed"})


@app.route('/payments/pix/<int:paymetn_id>', methods=["GET"])
def payment_pix_page(paymetn_id):
    return 'Pagamento pix'

if __name__ == "__main__":
    app.run(debug=True)
