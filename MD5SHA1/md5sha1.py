# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 14:18:19 2022

@author: maste
"""

import hashlib
import timeit



class hassfun:
    def md5(self,test_strings):
        self.test_strings = test_strings
        self.result=hashlib.md5(self.test_strings.encode("utf-8")).hexdigest()
        start_time=timeit.default_timer()
        print("md5 output ",i+1)
        print(self.result)
        end_time=timeit.default_timer()
        print("time taken for md5: ",end_time-start_time)
    def sha1(self,test_strings):
        self.test_strings = test_strings
        self.result=hashlib.sha1(self.test_strings.encode("utf-8")).hexdigest()
        start1_time=timeit.default_timer()
        print("sha1 output ",i+1)
        print(self.result)
        end1_time=timeit.default_timer()
        print("time taken for sha1: ",end1_time-start1_time)
    def filemd5(self,filename):
        self.filename = filename
        start1_time=timeit.default_timer()
        print("md5 output for file ",i+1)
        md5_hash = hashlib.md5()
        with open(self.filename,"rb") as f:
            # Read and update hash in chunks of 4K
            for byte_block in iter(lambda: f.read(4096),b""):
                md5_hash.update(byte_block)
            print(md5_hash.hexdigest())
        end1_time=timeit.default_timer()
        print("time taken for md5: ",end1_time-start1_time)
    def filesha1(self,filename):
        self.filename = filename
        start1_time=timeit.default_timer()
        print("sha1 output for file ",i+1)
        sha1_hash = hashlib.sha1()
        with open(self.filename,"rb") as f:
            # Read and update hash in chunks of 4K
            for byte_block in iter(lambda: f.read(4096),b""):
                sha1_hash.update(byte_block)
            print(sha1_hash.hexdigest())
        end1_time=timeit.default_timer()
        print("time taken for sha1: ",end1_time-start1_time)
                
if __name__ == '__main__':
    c = hassfun()
    n=int(input("Total No. of input please:"))
    print(" ")
    print("====================================")
    print("Enter your Choise:")
    print("1. input String")
    print("2. input files (Note: File size of 1kb, 5kb & 10kb only)")
    print("====================================")
    option = int(input())
    if option == 1:
        print(" ")
        print("====================================")
        print("Enter your Choise:")
        print("1. MD5")
        print("2. SHA1")
        print("====================================")
        option = int(input())
        if option == 1:
            for i in range(0,n):
                test_strings = input()
                c.md5(test_strings)
        elif option == 2:
            for i in range(0,n):
                test_strings = input()
                c.sha1(test_strings)
        else:
            print("Please enter the correct input no. again")
    elif option == 2:
        print(" ")
        print("====================================")
        print("Enter your Choise:")
        print("1. MD5")
        print("2. SHA1")
        print("====================================")
        option = int(input())
        if option == 1:
            for i in range(0,n):
                filename = input("Enter the file name: ")
                c.filemd5(filename)
        elif option == 2:
            for i in range(0,n):
                filename = input("Enter the file name: ")
                c.filesha1(filename)
        else:
            print("Please enter the correct input no. again")
    else:
        print("Please enter the correct input no. again")
                
    



# =============================================================================
# Input:
# 1234567890
# abcdefghijklmnopqrstuvwxyz
# message digest
# =============================================================================


######MD5###################################
# =============================================================================
# runfile('C:/Users/maste/Desktop/CSS/Exp 6/md5sha1.py', wdir='C:/Users/maste/Desktop/CSS/Exp 6')
# 
# Total No. of input please:3
#  
# ====================================
# Enter your Choise:
# 1. input String
# 2. input files (Note: File size of 1kb, 5kb & 10kb only)
# ====================================
# 
# 1
#  
# ====================================
# Enter your Choise:
# 1. MD5
# 2. SHA1
# ====================================
# 
# 1
# 
# 1234567890
# md5 output  1
# e807f1fcf82d132f9bb018ca6738a19f
# time taken for md5:  0.0018540000019129366
# 
# abcdefghijklmnopqrstuvwxyz
# md5 output  2
# c3fcd3d76192e4007dfb496cca67e13b
# time taken for md5:  0.0016455000004498288
# 
# message digest
# md5 output  3
# f96b697d7cb7938d525a2f31aaf161d0
# time taken for md5:  0.0018965999988722615
# =============================================================================


######SHA1###################################
# =============================================================================
# runfile('C:/Users/maste/Desktop/CSS/Exp 6/md5sha1.py', wdir='C:/Users/maste/Desktop/CSS/Exp 6')
# 
# Total No. of input please:3
#  
# ====================================
# Enter your Choise:
# 1. input String
# 2. input files (Note: File size of 1kb, 5kb & 10kb only)
# ====================================
# 
# 1
#  
# ====================================
# Enter your Choise:
# 1. MD5
# 2. SHA1
# ====================================
# 
# 2
# 
# 1234567890
# sha1 output  1
# 01b307acba4f54f55aafc33bb06bbbf6ca803e9a
# time taken for sha1:  0.0016561000011279248
# 
# abcdefghijklmnopqrstuvwxyz
# sha1 output  2
# 32d10c7b8cf96570ca04ce37f2a19d84240d3a89
# time taken for sha1:  0.0019860999964294024
# 
# message digest
# sha1 output  3
# c12252ceda8be8994d5fa0290a47231c1d16aae3
# time taken for sha1:  0.0015562999979010783
# =============================================================================
