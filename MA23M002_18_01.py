# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 10:07:47 2024

@author: Abhinav T K - ma23m002
"""

x = 5.34
y = 2.5
print("x = ",x)
print("y = ",y)
# quotient
q = round(x//y,2)
print("Quotient = ",q)
# remainder
r = round(x%y,2)
print("Remainder = ",r)

# Complex object
a = 3 + 4j
print(a.real)
print(a.imag)
b = a.conjugate()
print(b)

#help(complex)

import math
pi = math.pi
r = 5
area = pi * r**2
print(area)

area1 = math.pi*r**2
print(area1)

# Strings
msg = "Hii, I'm Abhinav"
print(msg)

# Raw string
r1 = r"I\'m learning Python now"
print(r1)

r2 = r'"Ram'
print(r2)

# multi-line
m1 = '''Trying multi 
line'''
m2 = """tryoing 
sjnjnjd """
print(m1)
print(m2)

# Access string elements
str1 = "Abhinav"
print(str1[0])
print(str1[-1])
print(str1[2])
print(id(str1))
# str1[0]= 'C' - TypeError, immutable
str1 = "Kite"
print(id(str1))
