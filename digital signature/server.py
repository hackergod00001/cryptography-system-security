import socket
import random
import math
import pickle
import timeit
import hashlib

s = socket.socket()
print("Socket Created")

s.bind(('localhost', 9999))
s.listen(3)

# define p and q
# n = 143863
# p = 491
# q = 293

n = 391
p = 23
q = 17

phi_n = (p-1)*(q-1)
gcd_lst = []
def generate_e(phi):
    for num in range(2, phi):
        if math.gcd(num, phi) == 1:
            gcd_lst.append(num)
    e = random.choice(gcd_lst)
    return e
  
e = generate_e(phi_n)

def calculateD(e, phi):
    i = 1
    while True:
        d = (phi*i + 1)/e
        if d.is_integer():
            break
        i += 1
    
    return d

d = calculateD(e,phi_n)
print("d: ", d)

list_to_send = pickle.dumps([e, n])

def decryptRSA(ct):
    pt_list = []
    pt = ''

    for character in ct:
        pt_ele = ord(character)**int(d) % n
        pt_list.append(chr(pt_ele))
    
    for ele in pt_list:
        pt += ele

    return pt

def decDs(ds, ec, nc):
    md_str = ''
    for chr_ds in ds:
        md_chr = ord(chr_ds)**int(ec) % nc
        md_str = md_str +chr(md_chr)
    return md_str

# calculate time to generate e
# print( timeit.timeit(generate_e(phi_n), number = 1))

# calculate time to decrypt
sampleCt = "qwasfghjyf"
# print( timeit.timeit(decryptRSA(sampleCt), number = 1))

while True:
    conn, addr = s.accept()
    print("Connected With ", addr)
    conn.send(list_to_send)

    list_from_client = conn.recv(1024).decode('utf-16')
    print(list_from_client)
    # print("CT from client: ", pickle.loads(list_from_client))
    ct_from_client = list_from_client.split(' ')[0]
    enc_ds = list_from_client.split(' ')[1]
    ec= list_from_client.split(' ')[2]
    nc= list_from_client.split(' ')[3]
    print(ct_from_client)
    print(enc_ds)
    dec_ds = decDs(enc_ds, int(ec), int(nc))
    pt = decryptRSA(ct_from_client)
    md2_pt = hashlib.md5(pt.encode()).hexdigest()

    print("dec_ds: ", dec_ds)
    print("md2_pt: ", md2_pt)
    # print("Plain Text: ", pt)

    

    conn.close
    break