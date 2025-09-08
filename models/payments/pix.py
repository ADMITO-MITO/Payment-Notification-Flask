import uuid
import qrcode
import os
class Pix:
    def __init__(self) -> None:
        pass

    def create_payment(self, base_path=''):
        # Create payment from financial institution
        bank_payment_id = str(uuid.uuid4())

        # QR code
        hash_payment = f'hash_payment_{bank_payment_id}'
        img = qrcode.make(hash_payment)

        # Caminho para salvar a imagem
        filename = f"qr_code_payment_{bank_payment_id}.png"
        filepath = os.path.join(base_path, 'static', 'image', filename)

        # Criar diretório se não existir
        os.makedirs(os.path.dirname(filepath), exist_ok=True)

        # Salvar imagem
        img.save(filepath)#type:ignore

        return {
            "bank_payment_id": bank_payment_id,
            "qr_code_path": f"static/image/{filename}"
        }
