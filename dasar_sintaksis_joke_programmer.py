"""
Semua sintaksis dasar bahasa pemrograman terdiri dari:
1. Sekuensial: langkah berurutan
2. Percabangan: langkah melompat jika kondisi terpenuhi
3. Perulangan: mengullang langkah yang sama berkali-kali selama/sampai kondisi terpenuhi
"""

# Sekuensial
print('Ibu berkata, "Pergi ketoko"')
print('Budi Menjawab, "Baik, apa yang harus saya lakukan di toko"')
print('Ibu Menjawab, "Beli 1 botol susu, dan jika ada telur beli 6 telur"')
print('Maka budi berangkat ketoko')
print('Dan mulai berbelanja')

# Percabangan
jumlah_botol_susu = 173
jumlah_telur = 1587
print(f'Jumlah botol susu {jumlah_botol_susu} botol')
print(f'Jumlah telur {jumlah_telur} butir')

if jumlah_botol_susu > 0:
    print('Budi mengecek harga, dan ternyata uangnya cukup')
    if jumlah_telur == 0:
        print('budi membeli 1 botol susu')
    else:
        print('Budi membeli 6 botol susu')
else:
    print('Budi tidak jadi membeli 1 botol susu')

print('Budi pulang ke rumah')
print('Menyampaikan hasil kepada ibu')