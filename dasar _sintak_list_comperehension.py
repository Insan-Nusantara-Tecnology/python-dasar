print("Perintah del")
daftar_buku = ["Seven Habits", "How to Influence People", "First Things First", "4DX"]
del daftar_buku[0]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nPerintah list dengan list comperehension")
daftar_buku = ["Seven Habits", "How to Influence People", "First Things First", "4DX"]
del daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nPerintah del dengan list comprehension start")
daftar_buku = ["Seven Habits", "How to Influence People", "First Things First", "4DX"]
del daftar_buku[0:-1]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nPerintah del dengan list comprehension harak 2")
daftar_buku = ["Seven Habits", "How to Influence People", "First Things First", "4DX"]
del daftar_buku[0::2]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nMembuat list baru")
daftar_buku = ["Seven Habits", "How to Influence People", "First Things First", "4DX"]
daftar_buku_baru = daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])


print("\nMembuat list baru")
del daftar_buku[:]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print("\nMembuat list baru dengan comperehension: ganjil")
daftar_buku = ["1 Seven Habits", "2 How to Influence People", "3 First Things First", "4 4DX"]
daftar_buku_baru = daftar_buku[0::2]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print("\nMembuat list baru dengan comperehension: genap")
daftar_buku = ["1 Seven Habits", "2 How to Influence People", "3 First Things First", "4 4DX"]
daftar_buku_baru = daftar_buku[1::2]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print("\nMembuat list baru dengan comperehension: buang ujing")
daftar_buku = ["1 Seven Habits", "2 How to Influence People", "3 First Things First", "4 4DX"]
daftar_buku_baru = daftar_buku[1:-1:2]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print("\nMembuat list baru dengan comperehension: ganjil")
daftar_buku = ["1 Seven Habits", "2 How to Influence People", "3 First Things First", "4 4DX"]
print(daftar_buku[0::2])
