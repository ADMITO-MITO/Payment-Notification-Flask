from flask import Flask, jsonify, request
from repository.database import db
from models.payment import Payment
from datetime import datetime, timedelta

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECREAT_KEY'] = 'SECREAT_KEY_WEBSOCKET'
with app.app_context():
    db.init_app(app)
    db.create_all()
    db.session.commit()
@app.route('/payments/pix', methods=["POST"])
def create_paymetn_pix():
    data = request.get_json()

    if 'value' not in data:
        return jsonify({"message": "Invalid value"}), 400
    expiration_date = datetime.now() + timedelta(minutes=30)
    new_payment = Payment(value=data['value'], expiration_date=expiration_date)
    db.session.commit()
    return jsonify({"message": "The payment has been created", "payment": new_payment.to_dict()})

@app.route('/payments/pix/confirmation', methods=["POST"])
def pix_confirmation():
    return jsonify({"message": "The payment has been confrimed"})


@app.route('/payments/pix/<int:paymetn_id>', methods=["GET"])
def payment_pix_page(paymetn_id):
    return 'Pagamento pix'

if __name__ == "__main__":
    app.run(debug=True)
