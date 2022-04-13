# -*- coding: utf-8 -*-
"""
Created on Fri Feb 04 06:28:10 2022

@author: maste
"""

import random
import hashlib
import sys

g=int(input("Enter your comman value for g: "))
p=int(input("Enter your comman value for p: "))

a=random.randint(5, 10) #in you want you can enter the value of a nd b as well

b=random.randint(10,20)

A = (g**a) % p
B = (g**b) % p

print('g: ',g,' (a shared value), p: ',p, ' (a prime number)')

print('\nAlice calculates:')
print('a (Alice random): ',a)
print('Alice value (A): ',A,' (g^a) mod p')

print('\nBob calculates:')
print('b (Bob random): ',b)
print('Bob value (B): ',B,' (g^b) mod p')

print('\nAlice calculates:')
keyA=(B**a) % p
print('KeyA: ',keyA,' (B^a) mod p')
print('KeyA: ',hashlib.sha256(str(keyA).encode()).hexdigest())

print('\nBob calculates:')
keyB=(A**b) % p
print('KeyB: ',keyB,' (A^b) mod p')
print('KeyB: ',hashlib.sha256(str(keyB).encode()).hexdigest())
print('\n')
print('---------------------Final Key Value i.e K-----------------------------')
if (keyA==keyB):
    print('keyK:',hashlib.sha256(str(keyA).encode()).hexdigest())
    print('keyK:',hashlib.sha256(str(keyB).encode()).hexdigest())
else:
    print("There is some error please check back")



# =============================================================================
# OUTPUT:
#     runfile('C:/Users/maste/Desktop/CSS/Exp 2/diffie-hellman.py', wdir='C:/Users/maste/Desktop/CSS/Exp 2')
# 
#     Enter your comman value for g: 5
# 
#     Enter your comman value for p: 7
#     g:  5  (a shared value), p:  7  (a prime number)
# 
#     Alice calculates:
#     a (Alice random):  6
#     Alice value (A):  1  (g^a) mod p
# 
#     Bob calculates:
#     b (Bob random):  10
#     Bob value (B):  2  (g^b) mod p
# 
#     Alice calculates:
#     KeyA:  1  (B^a) mod p
#     KeyA:  6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b
# 
#     Bob calculates:
#     KeyB:  1  (A^b) mod p
#     KeyB:  6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b
# 
# 
#     ---------------------Final Key Value i.e K-----------------------------
#     keyK: 6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b
#     keyK: 6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b
# =============================================================================
