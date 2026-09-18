# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 15:27:15 2026

@author: HP VICTUS
"""

ismlar=['Bobur','Fathullo','Mirabror','Umid','Jampolat']
for ism in ismlar:
    print(f"{ism} ,ishlar qalay bugun kochaga chiqamizmi?")
print(list(ismlar))


sonlar=range(11,101,2)
print(sonlar)
for son in sonlar:
    print(son**3)


kinolar=[]
print("5 ta eng yoqtrgan kinolarini kiriting")
for kino in kinolar:
    kinolar.append(input(f"{kino+1}-kinoni nomi>>>"))
print(kinolar)

mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
for mehmon in mehmonlar:
    print(f"Hurmatli {mehmon}, sizni 20 Dekabr kuni nahorga oshga taklif qilamiz")
    print("Hurmat bilan, Palonchiyevlar oilasi")

mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
for mehmon in mehmonlar:
    print(f"Hurmatli {mehmon}, sizni 20 Dekabr kuni nahorga oshga taklif qilamiz")
print("Hurmat bilan, Palonchiyevlar oilasi\n")


sonlar = list(range(1,11))
for son in sonlar:
    print(f"{son} ning kvadrati {son**2} ga teng")

dostlar = [] # bo'sh ro'yxat
print("5 ta eng yaqin do'stingiz kim?")
for n in range(5): # n bu yerda 0 dan 4 gacha qiymatlar oladi
    dostlar.append(input(f"{n+1}-do'stingizning ismini kiriting: "))
print(dostlar)



























