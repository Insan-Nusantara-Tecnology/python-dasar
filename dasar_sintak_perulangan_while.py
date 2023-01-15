"""
Program perulangan membaca buku dengan while
"""

jumlah_buku = 10
jumlah_buku_terbaca_dan_dipahami = 0
total_jumlah_baca = 0

print('Ibu berkata, "Baca semua bukumu"')
print(f'Jumlah buku yang sudah dibaca dan dipahami {jumlah_buku_terbaca_dan_dipahami}')

while total_jumlah_baca < jumlah_buku:
    print(total_jumlah_baca)
    total_jumlah_baca +=1


'''
while total_jumlah_baca < jumlah_buku * 2:
    total_jumlah_baca = total_jumlah_baca + 1

    if jumlah_buku_terbaca_dan_dipahami == 9:
        print(f"Buku ke {jumlah_buku_terbaca_dan_dipahami + 1} belum paham")
    else:
        jumlah_buku_terbaca = jumlah_buku_terbaca_dan_dipahami + 1
        print(f'Buku ke {jumlah_buku_terbaca} sudah dibaca dan dipahami')

print(f'Jumlah buku yang sudah dibaca{jumlah_buku_terbaca_dan_dipahami}')
if jumlah_buku_terbaca_dan_dipahami == jumlah_buku:
    print('Bu, semua buku sudah dibaca dan dipahami')
else:
    print(f'Bu, tidak semua buku bisa dipahami.'
          f' budi hanya bisa memahami {jumlah_buku} buku')
'''
