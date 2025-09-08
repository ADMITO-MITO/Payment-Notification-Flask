import uuid
import qrcode
import os

class Pix:
    def __init__(self) -> None:
        pass

    def create_payment(self, base_path=''):
        bank_payment_id = str(uuid.uuid4())

        hash_payment = f'hash_payment_{bank_payment_id}'
        img = qrcode.make(hash_payment)

        filename = f"qr_code_payment_{bank_payment_id}.png"
        filepath = os.path.join(base_path, 'static', 'image', filename)

        os.makedirs(os.path.dirname(filepath), exist_ok=True)


        img.save(filepath) #type:ignore
        print(f"QR code salvo em: {filepath}")  #debug

        return {
            "bank_payment_id": bank_payment_id,
            "qr_code_path": f"static/image/{filename}"
        }
