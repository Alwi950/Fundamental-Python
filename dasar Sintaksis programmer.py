#Sekuensial
print('Ibu berkata,"Beli 1 susu, jika ada telur beli 6"')
print("Budi berangkat ke toko")
print("Budi mulai berbelanja")

#Percabangan
jumlah_botol_susu = 124
jumlah_butir_Telur = 210
print(f"jumlah botol susu {jumlah_botol_susu} Botol")
print(f"jumlah butir telur {jumlah_butir_Telur} Butir")

if jumlah_botol_susu > 0:
    print("Budi mengecek harga dan uangnya cukup")
    print("Budi membeli 1 botol susu ")
    if jumlah_butir_Telur == 0 :
        print("Budi membeli 1 botol susu")
    else:
        print("Budi membeli 6 butir telur ")
else:
    print("Budi tidak membeli 1 botol susu"  )

print("Budi pulang ke rumah")
print("Budi menyerahkan belanjaan ke Ibu")
