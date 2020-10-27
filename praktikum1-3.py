print("{--------Harap masukan nilai dengan benar--------}")

bi = int(input("Masukkan nilai Bhs Indonesia  : "))
mtk =int(input("Masukkan nilai IPA            : "))
ipa =int(input("Masukkan nilai Matematika     : "))

print("{------------------------------------------------}")
if(bi < 0) or (bi > 100) or (mtk < 0) or (mtk > 100) or (ipa < 0) or (ipa > 100):
    print("input anda tidak valid")
    exit()
elif(bi >= 60) and (bi <= 100) and (mtk >= 70) and (mtk <= 100) and (ipa >= 60) and (ipa <= 100):
    print("Status Kelulusan	      : LULUS")
elif(bi >= 0) or (bi < 60) or (mtk >= 0) or (mtk < 70) or (ipa >= 0) or (ipa < 60):
    print("Status Kelulusan	      : TIDAK LULUS")
    print("Sebab			      : ")

if(bi < 60):
    print("- bahasa indo kurang dari 60")

if(mtk < 60):
    print("- ipa kurang dari 70")

if(ipa < 60):
    print("- mtk kurang dari 60")
