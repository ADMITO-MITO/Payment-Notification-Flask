from doctest import debug
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/payments/pix', methods=["POST"])
def create_paymetn_pix():
    return jsonify({"message": "The payment has been created"})

@app.route('/payments/pix/confirmation', methods=["POST"])
def pix_confirmation():
    return jsonify({"message": "The payment has been confrimed"})


@app.route('/payments/pix/<int:paymetn_id>', methods=["GET"])
def payment_pix_page(paymetn_id):
    return 'Pagamento pix'

if __name__ == "__main__":
    app.run(debug=True)
