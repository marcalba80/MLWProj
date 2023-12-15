1. Run keygen and set a passphrase for the private key (uses RSA key length of 4096) on the attacker's machine.

2. (OPTION 1) Get ransomware to execute on victim's machine, it will encrypt nearly all existent file formats.
    1. First it gets the victim's IP.
    2. Generates a cryptographic key using Fernet for file encryption and decryption.
    3. Writes the generated Fernet key to a file (EMAIL_US.txt).
    4. Encrypts the Fernet key using RSA and writes the encrypted key to a file.
    5. Encrypts or decrypts individual files based on the provided file path.
    6. Uses a thread pool to encrypt or decrypt all files in the specified directory that match the specified file extensions.
    7. Opens web pages related to Bitcoin in a web browser.
    8. Downloads an image from a specified URL and sets it as the desktop background.
    9. Writes a ransom note to a text file.
    10. Repeatedly opens the ransom note in Notepad, ensuring it stays in the foreground.
    11. Continuously checks for a specific file on the desktop (PUT_ME_ON_DESKTOP.txt), and if found, reads the key from it to decrypt the system.

2. (OPTION 2) Execute .exe on victim's machine (it will do the same as the .py file as well as installing all the required libraries)

3. Send the encrypted Fernet key (EMAIL_US.txt) to the attacker's machine.

4. Run dec.py to decrypt encrypted Fernet key (EMAIL_US.txt) with the passphrase previously used.

5. Send PUT_ME_ON_DESKTOP.txt to victim and make them place it on their desktop.
