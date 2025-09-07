import uuid
import qrcode
class Pix:
    def __init__(self) -> None:
        pass

    def create_payment(self):
    #create payment from (fictitious) financial institution
        bank_payment_id = uuid.uuid4()
        #qr_code
        hash_payment = f'hash_payment_{bank_payment_id}'
        img = qrcode.make(hash_payment)
        img.save(f"static/image/qr_code_payment_{bank_payment_id}.png")#type:ignore

        return{"bank_payment_id": bank_payment_id,
               "qr_code_path": f"static/image/qr_code_payment_{bank_payment_id}.png"}
