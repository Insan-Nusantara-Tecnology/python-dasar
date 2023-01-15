"""
Program perulangan membaca buku dengan while
"""

jumlah_buku = 10
jumlah_buku_terbaca = 0

print('Ibu berkata, "Baca semua bukumu"')
print(f'Jumlah buku yang sudah dibaca {jumlah_buku_terbaca}')

while jumlah_buku_terbaca < jumlah_buku:
    jumlah_buku_terbaca = jumlah_buku_terbaca + 1
    print(f'Buku ke {jumlah_buku_terbaca} sudah dibaca')

print(f'Jumlah buku yang sudah dibaca{jumlah_buku_terbaca}')