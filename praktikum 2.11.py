from random import randint
h = 0
while True:
    bil = randint(0,10)
    print(bil)
    h += 1
    if bil == 5:
        break

print("jumlah perulangan  :" + str(h))