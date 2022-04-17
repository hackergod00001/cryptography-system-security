import socket
import pickle 
import timeit
import hashlib
import math
import random

s = socket.socket()

s.connect(('localhost', 9999))

server_public_key =  pickle.loads(s.recv(1024))
print("Public Key From server: ", server_public_key)

es = server_public_key[0]
ns = server_public_key[1]

ptStr = input("Enter Plain Text: ").replace(" ", "")
pt_list = list(ptStr)
# print(pt_list)

ct_list = []

nc = 377 #client
p = 29
q = 13

phi_n = (p-1)*(q-1) #client
gcd_lst = []
def generate_e(phi):
    for num in range(2, phi):
        if math.gcd(num, phi) == 1:
            gcd_lst.append(num)
    e = random.choice(gcd_lst)
    return e
  
ec = generate_e(phi_n)

def calculateD(e, phi):
    i = 1
    while True:
        d = (phi*i + 1)/ec
        if d.is_integer():
            break
        i += 1
    return d

private_key_d = calculateD(ec, phi_n)

def encrypt(ptStr):
    ctStr = ''
    for letter in ptStr:
        ct_letter = chr(ord(letter)**es % ns)
        ctStr= ctStr+ct_letter
    return ctStr

encrypted_ds_list = []
# calculate digital signature
def calDS(orig_mess):
    encrypted_ds = ''
    mess_digest = hashlib.md5(orig_mess.encode()).hexdigest()
    for letter in mess_digest:
        ct_letter = chr(ord(letter)**int(private_key_d) % nc)
        encrypted_ds = encrypted_ds + ct_letter
    return encrypted_ds


enc_ds = calDS(ptStr)
ctStr = encrypt(ptStr) #ciphertext

print("enc_ds: " ,enc_ds)
print("CT: ", ctStr)

# list 
str = ctStr+' '+enc_ds+' '+str(ec)+' '+str(nc)
s.send(str.encode('utf-16'))

# print time to encrypt
# print( timeit.timeit(encrypt, number = 1))


