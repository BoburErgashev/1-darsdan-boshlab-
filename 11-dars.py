# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 13:06:54 2026

@author: HP VICTUS
"""

yosh = int(input('Yoshingiz nechida? '))
if yosh<=4:
    print('Sizga kirish bepul.')
elif yosh<=12:
    print('Sizga kirish 5000 so\'m')
else:
    print('Sizga kirish 10000 so\'m')

yosh = int(input('Yoshingiz nechida? '))
if yosh<=4:
    price = 0
elif yosh<=12:
    price = 5000
else:
    price = 10000
    
print(f"Sizga kirish {price} so'm")

yosh = int(input('Yoshingiz nechida? '))
if yosh<=4: # yosh bolalarga bepul
    price = 0
elif yosh<=12: # 4 dan 12 yoshgacha 5000 so'm
    price = 5000
elif yosh<65: # 12 dan katta va 65 dan kichiklarga narh 10000 so'm
    price = 10000
else: # qariyalarga esa 8000 so'm
    price = 8000
print(f"Sizga kirish {price} so'm")

kun = input("Bugun nima kun?>>>")
if kun.lower()=='shanba' or kun.lower()=='yakshanba':
    print('Bugun dam olish kuni.')
else:
    print('Bugun ish kuni.')

kun = input("Bugun nima kun?")
harorat = float(input("Havo harorati qanday?"))
if kun.lower()=='yakshanba' and harorat>=30:
    print("Cho'milgani ketdik!")
elif kun.lower()=='yakshanba' and harorat<30:
    print("Uyda dam olamiz!")

kun = input("Bugun nima kun?")
harorat = float(input("Havo harorati qanday?"))
if (kun.lower()=='shanba' or kun.lower()=='yakshanba') and harorat>=30:
    print("Cho'milgani ketdik!")
elif (kun.lower()=='shanba' or kun.lower()=='yakshanba') and harorat<30:
    print("Uyda dam olamiz!")

narh = 15000 # mijoz 15000 so'mga taom oldi.
choy = True # mijoz choy ham oldi
salat = False # mijoz salat olmadi

if choy and salat: # agar mijoz choy ham salat ham olgan bo'lsa
    narh = narh + 10000 # narhga 10000 so'm qo'shamiz
elif choy or salat: # agar choy yoki salat olgan bo'lsa
    narh = narh + 5000 # narhga 5000 so'm qo'shamiz

print(f"Jami {narh} so'm") # yakuniy narhni chiqaramiz


narh = 15000 # mijoz 15 so'mga ovqat oldi
choy = True
salat = False
non = True
kompot = True
assorti = False
#Quyidagi har bir shart alohida tekshiriladi va bir-biriga bog'liq emas
if choy:   # agar choy olsa
    print("Mijoz choy oldi.")
    narh = narh + 3000
if salat:  # agar salat olsa
    print("Mijoz salat oldi.")
    narh = narh + 5000
if non:    # agar non olsa
    print("Mijoz non oldi.")
    narh = narh + 2000
if kompot: # agar kompot olsa
    print("Mijoz kompot oldi.")
    narh = narh + 5000
if assorti: # agar assorti olsa
    print("Mijoz assorti oldi.")
    narh = narh + 15000
    
print(f"Jami {narh} so'm")


menu = ['osh','qazonkabob','shashlik','norin','somsa']
buyurtmalar = ["osh","somsa","manti", "shashlik"]

for taom in buyurtmalar:
    if taom in menu:
        print(f"Menuda {taom} bor")
    else:
        print(f"Kechirasiz, menuda {taom} yo'q")


menu = ['osh','qazonkabob','shashlik','norin','somsa']
buyurtmalar = ["osh","somsa","manti", "shashlik"]

if buyurtmalar: # ro'yxatda biror element bo'lsa bu ifoda TRUE qaytaradi
    for taom in buyurtmalar:
        if taom in menu:
            print(f"Menuda {taom} bor")
        else:
            print(f"Kechirasiz, menuda {taom} yo'q")
else: # agar ro'yxat bo'sh bo'lsa
    print("Savatchangiz bo'sh!")

                #QUYIDAGI JAVOBLAR
                
son=input("Juft son kirting")
juft_sonlar=list(range(2,1000,1))
if son in juft_sonlar:
    print("raxmat")
else:
    print('juft son kiriting')
  


yosh=int(input("Yoshingizni kiriting>>>"))

if yosh<4 or yosh>60:
    print("kirish bepul")
elif yosh<18:
    print("kirish narxi 10.000 so\'m")
elif yosh<18:
    print("kirish narxi 20.000") 
    
birnichi_son=int(input("Birinchi sonni kiriting>>>"))
ikkinchi_son=int(input("ikkinchi sonni kiriting>>>"))

if birnichi_son>ikkinchi_son:
    print(f"{birnichi_son}>{ikkinchi_son}")
else:
    print(f"{birnichi_sason}<{ikkinchi_son}")


maxsulotlar=['olma','shaftoli','grinki','makaron','gosht','qaymoq ','qiyom']

savat=[]
for n in range(5):
    savat.append(input(f"savatga {n+1} mahsulotni qoshing:::"))

bor_mahsulot=[]            
yoq_mahsulot=[]
for mahsulot in savat:
    if mahsulot in maxsulotlar:
        bor_mahsulot.append(mahsulot)
    else:
        yoq_mahsulot.append(mahsulot)

if yoq_mahsulot:
    print("dokonimizda bu mahsulotlar yoq")
    for mahsulot in yoq_mahsulot:
        print(mahsulot)
else:
    print("siz soragan mahsulotlar dokonimizda bor")

users=['umar','qassob','chol','mol']
login=input("login kiriting>>> ")
if login in users:
    print("login band boshaqa login kiriting!!!!")
else:
    print(f"Xush kelibsiz {login}")

son=int(input('Istalgan butun sonni kiriting'))

for n in range(2,10):
    if not (son%n):
        print(f'{son} son {n} ga qoldiqsiz bolinadi') 


























