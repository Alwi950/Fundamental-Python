#Data List

daftar_buku = ['Principal Accounting', 'Harry Potter', 'How to be rich']
print('Tampilkan variabel daftar buku')
print(daftar_buku)

print('\nProses semua dengan for in')
for buku in daftar_buku :
    print(buku)

print('\nTampilkan isi daftar_buku pada indeks tertentu')
print(daftar_buku[0])
print(daftar_buku[2])

print('\nDengan range in')
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nKembalikan nilai awal daftar buku')
daftar_buku = ['Principal Accounting', 'Harry Potter', 'How to be rich']
print(daftar_buku)

print('\nTambahkan Buku Baru')
daftar_buku.append('PSAK')
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nClear list')
daftar_buku.clear()
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nGanti Elemen Pertama')
daftar_buku = ['Principal Accounting', 'Harry Potter', 'How to be rich']
daftar_buku[0] = 'Perpajakan 1'
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nAmbil Buku ke 2')
buku = daftar_buku.pop(1)
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nBuku yang diambil tadi')
print(buku)

