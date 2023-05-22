print('\nPerintah Del')
daftar_buku = ['Principal Accounting', 'Harry Potter', 'How to be rich']
del daftar_buku[0]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah dell dengan list comprehensif')
daftar_buku = ['Principal Accounting', 'Harry Potter', 'How to be rich']
del daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah dell dengan list comprehensif start')
daftar_buku = ['Principal Accounting', 'Harry Potter', 'How to be rich']
del daftar_buku[0:1]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah dell dengan list comprehensif start')
daftar_buku = ['Principal Accounting', 'Harry Potter', 'How to be rich']
del daftar_buku[0::2]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('Membuat list baru dengan')

print('\nMembuat list baru dari list comprehensive')
daftar_buku = ['Principal Accounting', 'Harry Potter', 'How to be rich']
daftar_buku_baru = daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

