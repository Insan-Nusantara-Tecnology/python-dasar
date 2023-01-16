"""
Program perulangan membaca buku dengan while
"""

jumlah_buku = 10
terbaca_dan_dipahami = 0
jumlah_baca = 0

print('Ibu berkata, "Baca semua bukumu"')
print(f'Jumlah buku yang sudah dibaca dan dipahami {terbaca_dan_dipahami}')

'''
while total_jumlah_baca < jumlah_buku:
    print(total_jumlah_baca)
    total_jumlah_baca +=1
'''

while jumlah_baca < jumlah_buku * 2:
    jumlah_baca = jumlah_baca + 1

    if terbaca_dan_dipahami == 9:
        print(f"Buku ke {terbaca_dan_dipahami + 1} belum paham")
    else:
        terbaca_dan_dipahami = terbaca_dan_dipahami + 1
        print(f'Buku ke {terbaca_dan_dipahami} sudah dibaca dan dipahami')

print(f'Jumlah buku yang sudah dibaca dan dipahami {terbaca_dan_dipahami}')
if terbaca_dan_dipahami == jumlah_buku:
    print('Bu, semua buku sudah dibaca dan dipahami')
else:
    print(f'Bu, tidak semua buku bisa dipahami.'
          f' budi hanya bisa memahami {terbaca_dan_dipahami} buku')
