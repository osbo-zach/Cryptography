"""
Created on Tue Jan 23 17:24:50 2018

@author: Zachary Osborne
"""

from Crypto.Cipher import AES

def encrypt_txt_CBC(key, IV, in_filename, out_filename=None):
    if not out_filename:
        out_filename = 'encrypted.txt'
    encryptor = AES.new(key, AES.MODE_CBC, IV=IV)
    with open(in_filename, 'rb') as infile:
        text = infile.read()
        # open output file
        with open(out_filename, 'wb') as outfile:
            outfile.write(encryptor.encrypt(text))
            
def encrypt_txt_ECB(key, in_filename, out_filename=None):
    if not out_filename:
        out_filename = 'encrypted.txt'
    encryptor = AES.new(key, AES.MODE_ECB)
    with open(in_filename, 'rb') as infile:
        text = infile.read()
        # open output file
        with open(out_filename, 'wb') as outfile:
            outfile.write(encryptor.encrypt(text))

def decrypt_txt_CBC(key, IV, in_file):
    decryptor = AES.new(key, AES.MODE_CBC, IV=IV)
    out_file = 'decrypted.txt'
    with open(in_file, 'rb') as infile:
        text = infile.read()
        with open(out_file, 'wb') as outfile:
            outfile.write(decryptor.decrypt(text))
            
def decrypt_txt_ECB(key, in_file):
    decryptor = AES.new(key, AES.MODE_ECB)
    out_file = 'decrypted.txt'
    with open(in_file, 'rb') as infile:
        text = infile.read()
        with open(out_file, 'wb') as outfile:
            outfile.write(decryptor.decrypt(text))
            
key = b'Sixteen byte key'
IV = 16 * '\x00'       
in_filename = 'input.txt'   