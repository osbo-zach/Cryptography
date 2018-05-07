"""
Created on Wed Jan 24 11:18:38 2018

@author: Zachary Osborne
"""
from Crypto.Cipher import AES
import binascii

plaintext = "This is a top secret."
plaintext += "\x0b" * 11
ciphertext = b'3f814d00c3f1047f1dfa879115970472472a17eabdd9ba4fcd667743e1e03674'
IV = 16 * '\x00'
mode = AES.MODE_CBC

def findKey():
    with open('words.txt', 'r') as infile:
        for word in infile:
            key = word.strip()
            
            if len(key) < 16:
                key += '\x20' * (16 - len(key))
                enc = AES.new(key, mode, IV)
                tmp = binascii.hexlify(enc.encrypt(plaintext))
                if tmp == ciphertext:
                    print("The key is {0}".format(word))