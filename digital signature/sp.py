# import random
# import math

# gcd_lst = []
# def generate_e(phi):
#     for num in range(2, phi):
#         if math.gcd(num, phi) == 1:
#             gcd_lst.append(num)
#     e = random.choice(gcd_lst)
#     return e

# print(generate_e(184))

# print(chr(4))

# print((10/2).is_integer())

# def calculateD(e, phi):
#     i = 1
#     while True:
#         d = (phi*i + 1)/e
#         print(d)
#         if d.is_integer():
#             break
#         i += 1
    
#     return d

# d = calculateD(25, 336)
# print("d: ", d)

# print(chr(10))

# print(63**23 % 77)

print(11.0 % 12)
print(11 % 12)