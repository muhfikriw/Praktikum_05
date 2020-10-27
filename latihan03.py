h = 0
sum = 0
for x in range (0,100):
    if x % 2 == 1:
        h = h + 1
        sum = sum + x
        print(x)
print("jumlah bilangan ganjil  :" + str(h))
print("jumlah seluruh bilangan :" + str(sum))