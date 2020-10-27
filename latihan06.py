print("“Hai.. nama saya Mr. Lappie, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silakan tebak ya!!!”")
hitung = 0
while True:
    hitung += 1
    bil = int(input("Tebakan Anda :"))
    if(bil < 0) or (bil > 100):
        print("error")
        exit()
    elif(bil < 10):
        print("Hehehe… Bilangan tebakan anda terlalu kecil")
    elif(bil > 10):
        print("Hehehe… Bilangan tebakan anda terlalu besar")
    elif(bil == 10):
        break
print("Yeeee… Bilangan tebakan anda BENAR :-)")

print("SCORE ANDA : ", 100 - hitung*2 + 2)