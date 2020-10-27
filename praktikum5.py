kode = int(input("Masukkan kode karyawan	                : "))
nama = str(input("Masukkan nama karyawan	                : "))
gol  = str(input("Masukkan golongan(A/B/C/D)              : "))
nkh = input("Masukkan status(1=menikah/ 2=blmmenikah): ")
anak = int(input("Masukkan jumlah anak(jika nga ada 0)    : "))


#potongan gaji golongan
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
    print("anda salah input golongan")
    exit()


1 == "menikah"
2 == "blmmenikah"

tunistri = 0
tunanak = 0
#tunjangan
if(nkh == "menikah"):
    tunistri = gaji/10
tunanak = anak*gaji/20

#perhitungan gaji
kotor = gaji + tunistri + tunanak
kali = gaji*potongan/100
bersih = kotor - kali


print("")
print("==================================")
print("STRUK RINCIAN GAJI KARYAWAN")
print("==================================")
print("")
print("Nama Karyawan		: ", nama)
print("Golongan	        : ", gol)
print("Status Menikah	        : ", nkh)
if(nkh == "menikah"):
    print("Jumlah Anak	        : ", anak ,"anak")
print("")
print("[][][][][][][][][][][][][][][][][]")
print("")
print("Gaji Pokok		: Rp ", int(gaji))
print("Tunjangan Istri/Suami	: Rp ", int(tunistri))
print("Tunjangan anak		: Rp ", int(tunanak))
print("---------------------------------")
print("Gaji kotor	        : Rp ", int(kotor))
print("Potongan (XXXX %)	:", potongan, "%")
print("---------------------------------")
print("Gaji Bersih		: Rp ", int(bersih))