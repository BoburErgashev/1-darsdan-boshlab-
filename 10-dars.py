# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 17:56:46 2026

@author: HP VICTUS
"""

avtolar = ['audi','bmw','volvo','kia','hyundai']

for avto in avtolar: # avtolar ichidadi har bir avto uchun ...
    if avto == 'bmw':  # ... agar avto bmw ga teng bo'lsa ...
        print(avto.upper()) # avto nomini hamma harflarini katta bilan yoz.
    else: # aks holda ... 
        print(avto.title()) # avto nomini faqat birinchi harfini katta bilann yoz.


avtolar = ['audi','bmw','volvo','kia','hyundai']
for avto in avtolar: # avtolar ichidadi har bir avto uchun ...
    if avto == 'bmw':  # ... agar avto bmw ga teng bo'lsa ...
        print(avto.upper()) # avto nomini hamma harflarini katta bilan yoz.
    else: # aks holda ... 
        print(avto.title()) # avto nomini faqat birinchi harfini katta bilan yoz.


ism = input('Ismingiz nima?\n>>>') # Foydalanuvchi ismini so'raymiz
if ism.lower() != 'ali': # Agar ism Aliga teng bo'lmasa ...
    print(f"Uzr, {ism.title()} biz Alini kutayapmiz.") # quyidagi xabar chiqadi
else:
    print("Salom, Ali")

javob = float(input("12x6 nechiga teng?>>>"))
if javob!=72:
    print("Javob xato!")

yosh = int(input("Yoshingiz nechida?>>>"))
if yosh>=18: # yosh 18 dan katta yoki teng bo'lsa
    print('Xush kelibsiz!')
else: # ask holda
    print('Kirish mumkin emas!')
#=============================================================================

#=============================================================================
login = input("Yangi login tanlang:")
if len(login)<=5: # login uzunligini tekshiramiz
    print("Login 5 harfdan ko'proq bo'lishi shart!")
else:
    print("raxmat")
#=============================================================================

#=============================================================================
yil = int(input("Tug'ilgan yilingizni kiriting:"))
if 2020-yil<18: # foydalanuvchining yoshini hisoblaymiz
    print(f"Yoshingiz {2020-yil}da ekan.")
    print("Kirish mumkin emas!")
else:
    print("Xush kelibsiz!")
#=========================================================
#=============================================================================
yosh = int(input("Yoshingiz nechida?>>>"))
if yosh>65: print("Siz COVID-19 risk guruhida ekansiz")

x, y = 25, 50 # x=25 va y=50
print("x>y") if x>y else print("x<y")
#=============================================================================
cars=['toyota','mazda','hyundai','gm','kia']
for avto in cars:
    if avto!="gm":
        print(avto.upper())
    else:
        print(avto.title())

=============================================================================

ism=input('ismingizni kiriting>>>>')
if ism.lower()=='furqat':
    print("admin xush kelibsiz  sizga foydalanuvchlar ryxati kerakmi?")
else:
    print(f"Xush kelibsiz {ism.upper()}")

y=int(input("1-soni Y kiriting>>>"))
x=int(input("2-soni X kriting>>>"))
if x<y:
    print("y>x",'1-son ikkinchidsn katta')
else:
    print("y<x",'2-son 1-dan kotta')

cars=['toyota','mazda','hyundai','gm','kia']

for car in cars:
    if car!='gm':
        print(car.upper())
    else:
        print(car.title())
son=int(input("istalgan sonni kiriting>>"))

if son>0:
    print(son**2)
else:
    print("Musbat son kiriting!!!")










