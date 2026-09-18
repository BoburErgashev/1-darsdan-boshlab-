# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 18:16:45 2026

@author: HP VICTUS
"""

mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"] # mevalar ro'yxati (matnlar)
narhlar = [12000, 18000, 10900, 22000] # narhlar ro'yxati (sonlar)
sonlar = ['bir', 'ikki', 3, 4, 5] # sonlar va matnlar aralash ro'yxat
ismlar = [] # bo'sh ro'yxat
mevalar.append('xurmo')
mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"] # mevalar ro'yxati (matnlar)
print("Birinchi meva: ", mevalar[0])
print("Ikkinchi meva: ", mevalar[1])

mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"] # mevalar ro'yxati (matnlar)
print("Birinchi meva: ", mevalar[0].title())
print("Ikkinchi meva: ", mevalar[1].upper())

narhlar = [12000, 18000, 10900, 22000]
print(narhlar[2] + narhlar[3])

car_models = ['Toyota', 'GM', 'Volvo', 'BMW', 'Hyundai', 'Kia', 'Volkswagen']
print(car_models[-1]) # Listning eng oxirgi elementiga -1 bilan murojat qilamiz cars = [] # bo'sh ro'yxat yaratamiz
cars=[]
cars.append('Lacetti') # ro'yxatga Lacetti mashinasini qo'shamiz
cars.append('Nexia 3') # ro'yxatga Nexia 3 mashinasini qo'shamiz
cars.append('Cobalt')  # ro'yxatga Cobalt  mashinasini qo'shamiz
cars.insert(3, 'captiva')
print('sizga sovringa\n' +cars[2].title()+ '\nmoshinasi chqdi')
ismlar=['sobir', 'jobir', 'qosim']
print('salom', ismlar[0].capitalize(), 'bugun choyxona bormi?')
print(ismlar[1].upper(), 'choyxonaga bormaizmi?')
print('choyxonani pulini bugun', ismlar[2].title() ,'tolaydi')
sonlar=[1,23,4,56,67,88,93]
sonlar.insert(1, 33)
sonlar.append(55)
print(sonlar)
hayvonlar = ['it', 'mushuk', 'sigir', 'qo\'y', 'quyon', 'mushuk']
hayvonlar.remove("mushuk") # Ro'yxatda 2 ta mushuk bor, ulardan birinchisi o'chadi
print(hayvonlar) 
tarixiy_shaxslar=["ibn sino", 'a.temur','mirzo ulug\'bek']
zamonaviy_shaxslar=['shavkat mirziyoyev','rasul kusherbayev','baxodir jalolov']
tarixiy_shaxslar.pop(1)
zamonaviy_shaxslar.pop(2)


cars=['toyota','mazda','hyundai','gm','kia']

for car in cars:
    if car!='gm':
        print(car.upper())
    else:
        print(car.title())