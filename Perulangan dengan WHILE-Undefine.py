"""
Program Pengulangan membaca buku dengan while sampai paham
"""

Jumlah_Buku = 10
print('Ibu berkata,"Baca semua bukumu sampai paham"')

Jumlah_Buku_yang_sudah_dibaca_dan_dipahami = 0
print(f"Jumlah buku yang sudah dibaca dan dipahami {Jumlah_Buku_yang_sudah_dibaca_dan_dipahami}")

total_jumlah_baca = 0

while total_jumlah_baca < Jumlah_Buku * 2:
    total_jumlah_baca = total_jumlah_baca + 1
    if Jumlah_Buku_yang_sudah_dibaca_dan_dipahami == 9:
        print(f"Buku ke {Jumlah_Buku_yang_sudah_dibaca_dan_dipahami + 1} belum paham")
    else:
        Jumlah_Buku_yang_sudah_dibaca_dan_dipahami = Jumlah_Buku_yang_sudah_dibaca_dan_dipahami + 1
        print(f"Buku ke {Jumlah_Buku_yang_sudah_dibaca_dan_dipahami} sudah dibaca dan dipahami")

print(f"Jumlah buku yang sudah dibaca dan dipahami {Jumlah_Buku_yang_sudah_dibaca_dan_dipahami}")