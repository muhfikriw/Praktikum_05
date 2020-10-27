kode = int(input("Masukkan kode karyawan	  : "))
nama = str(input("Masukkan nama karyawan	  : "))
gol  = str(input("Masukkan golongan(A/B/C/D): "))


if( gol == "A"):
    gaji = 10000000
    potongan = 2.5
elif( gol == "B"):
    gaji = 8500000
    potongan = 2.0
elif( gol == "C"):
    gaji = 7000000
    potongan = 1.5
elif( gol == "D"):
    gaji = 5500000
    potongan = 1.0
else:
    print("anda salah input")
    exit()
   
#perhitungan gaji
hasil = gaji*(100-potongan)/100

print("")
print("=================================")
print("STRUK RINCIAN GAJI KARYAWAN")
print("---------------------------------")
print("Nama Karyawan		: ", nama)
print("Golongan	        : ", gol)
print("---------------------------------")
print("Gaji Pokok	        : Rp ", gaji)
print("Potongan (XXXX %)	: ", potongan)
print("---------------------------------  -")
print("Gaji Bersih		: Rp ", hasil)