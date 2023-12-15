from Crypto.PublicKey import RSA
import getpass

def generate_keys():
    key = RSA.generate(4096)
    passphrase = getpass.getpass("Enter passphrase for private key: ")
    private_key = key.export_key(passphrase=passphrase, pkcs=8)
    public_key = key.publickey().export_key()

    with open('private.pem', 'wb') as priv_file:
        priv_file.write(private_key)

    with open('public.pem', 'wb') as pub_file:
        pub_file.write(public_key)

if __name__ == "__main__":
    generate_keys()