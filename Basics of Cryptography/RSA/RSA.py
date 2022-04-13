# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 11:34:04 2022

@author: maste
"""
import random
from sympy import *
import math
import sys


print("RSA ENCRYPTOR/DECRYPTOR")
print("*****************************************************")

#Random Prime Numbers
print("RANDOM PRIME No. P & Q SELECTED ARE:")
pp=[i for i in range(1,100) if isprime(i)]
p = random.choice(pp)
qq=[i for i in range(1,100) if isprime(i)]
q = random.choice(qq)
print("P =  ",p)
print("Q =  ",q)
print("*****************************************************")

#RSA Modulus
'''CALCULATION OF RSA MODULUS 'n'.'''
n=p*q
print("RSA Modulus(n) is:",n)
 
#Eulers Toitent
'''CALCULATION OF EULERS TOITENT 'Φ(n)'.'''
phi_n=(p-1)*(q-1)
print("Eulers Toitent(Φ(n)) is:",phi_n)
print("*****************************************************")
 
#GCD
'''CALCULATION OF GCD FOR 'e' CALCULATION.'''
def egcd(e,phi_n):
    while(phi_n!=0):
        e,phi_n=phi_n,e%phi_n
    return e
 
#Euclid's Algorithm
def eugcd(e,phi_n):
    for i in range(1,phi_n):
        while(e!=0):
            a,b=phi_n//e,phi_n%e
            if(b!=0):
                print("%d = %d*(%d) + %d"%(phi_n,a,e,b))
            phi_n=e
            e=b
 
#Extended Euclidean Algorithm
def eea(a,b):
    if(a%b==0):
        return(b,0,1)
    else:
        gcd,s,t = eea(b,a%b)
        s = s-((a//b) * t)
        print("%d = %d*(%d) + (%d)*(%d)"%(gcd,a,t,s,b))
        return(gcd,t,s)
 
#Multiplicative Inverse
def mult_inv(e,phi_n):
    gcd,s,_=eea(e,phi_n)
    if(gcd!=1):
        return None
    else:
        if(s<0):
            print("s=%d. Since %d is less than 0, s = s(modr), i.e., s=%d."%(s,s,s%phi_n))
        elif(s>0):
            print("s=%d."%(s))
        return s%phi_n
 
#e Value Calculation
'''FINDS THE HIGHEST POSSIBLE VALUE OF 'e' BETWEEN 1 and 1000 THAT MAKES (e,phi_n) COPRIME.'''
for i in range(1,phi_n):
    if(egcd(i,phi_n)==1):
        e=i
print("The value of e is:",e)
print("*****************************************************")
 

#d, Private and Public Keys
'''CALCULATION OF 'd', PRIVATE KEY, AND PUBLIC KEY.'''
print("EUCLID'S ALGORITHM:")
eugcd(e,phi_n)
print("END OF THE STEPS USED TO ACHIEVE EUCLID'S ALGORITHM.")
print("*****************************************************")
print("EUCLID'S EXTENDED ALGORITHM:")
d = mult_inv(e,phi_n)
print("END OF THE STEPS USED TO ACHIEVE THE VALUE OF 'd'.")
print("The value of d is:",d)
print("*****************************************************")
public = (e,n)
private = (d,n)
print("Private Key is:",private)
print("Public Key is:",public)
print("*****************************************************")

#Encryption
'''ENCRYPTION ALGORITHM.'''
def encrypt(pub_key,n_text):
    e,n=pub_key
    x=[]
    
    for i in n_text:
        if(i.isupper()):
            m = ord(i)-65
            c=(m**e)%n
            x.append(c)
        elif(i.isspace()):
            spc=400
            x.append(400)
    return x
     
#Decryption
'''DECRYPTION ALGORITHM'''
def decrypt(priv_key,c_text):
    d,n=priv_key
    txt=c_text.split(',')
    x=''
    m=0
    for i in txt:
        if(i=='400'):
            x+=' '
        else:
            m=(int(i)**d)%n
            m+=65
            c=chr(m)
            x+=c
    return x
 
#Message
message = input("What would you like encrypted or decrypted?(Separate numbers with ',' for decryption):")
print("Your message is:",message)


#Choose Encrypt or Decrypt and Print
choose = input("Type '1' for encryption and '2' for decrytion.")
if(choose=='1'):
    enc_msg=encrypt(public,message)
    print("Your encrypted message is:",enc_msg)
elif(choose=='2'):
    dec_msg=decrypt(private,message)
    print("Your decrypted message is:",dec_msg)
else:
    print("You entered the wrong option Please try again with correct option.")
