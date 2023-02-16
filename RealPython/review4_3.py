# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 16:00:07 2023

@author: ardya
"""

print("Animals".lower())
print("Badger".lower())
print("Honey Bee".lower())
print("Honeybadger".lower())

print("Animals".upper())
print("Badger".upper())
print("Honey Bee".upper())
print("Honeybadger".upper())

string1 = " Filet Mignon"
string2 = "Brisket "
string3 = " Cheeseburger "

print(f"{string1.lstrip()}")
print(f"{string2.rstrip()}")
print(f"{string3.strip()}")

string4 = "Becomes"
string5 = "becomes"
string6 = "BEAR"
string7 = " bEautiful"

print(f"{string4.startswith('be')}")
print(f"{string5.startswith('be')}")
print(f"{string6.startswith('be')}")
print(f"{string7.startswith('be')}")

string8 = "Becomes".lower()
string9 = "becomes".lower()
string10 = "BEAR".lower()
string11 = " bEautiful".lower().lstrip()

print(f"{string8.startswith('be')}")
print(f"{string9.startswith('be')}")
print(f"{string10.startswith('be')}")
print(f"{string11.startswith('be')}")