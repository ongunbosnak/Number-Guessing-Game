import random

r = random.random()

tahmin = int(100*r) + 1

alt_limit = 1
üst_limit = 100

print("benim tahminim bu", tahmin)

a = input()

while a != "doğru":
    if a == "büyüktür":
         alt_limit = int(tahmin)
         tahmin = int((üst_limit + alt_limit)/2)
         
         print(tahmin)
          
         a = input()
    elif a == "küçüktür":
         üst_limit = int(tahmin)
         tahmin = int((üst_limit + alt_limit)/2)
         print(tahmin)
        
         a = input()
         
print("doğru")    


     


