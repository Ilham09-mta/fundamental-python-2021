"""
Tipe data dictionary sekedar menghubungkan antara KEY dan VALUE
KVP = Key Value Pair
dictionary = kamus
"""

kamus_ind_eng = {'anak': 'son', 'istri': 'wive', 'ayah': 'father', 'ibu': 'mother'}

print(kamus_ind_eng)
print(kamus_ind_eng['ayah'])
print(kamus_ind_eng['ibu'])
print(kamus_ind_eng['anak'])
print(kamus_ind_eng['istri'])

print('\nData Ini Dikirimkan Oleh Server Gojek, Untuk Memberikan Info Driver Di Sekitar Pemakai Aplikasi')
Data_Dari_Server_Gojek = {
    'tanggal ': '2021-02-09',
    'driver_list': [
        {'nama': 'Muhammad', 'jarak': 10},
        {'nama': 'Ilham', 'jarak': 30},
        {'nama': 'Saifullah', 'jarak': 20},
        {'nama': 'Juli', 'jarak': 40},
        {'nama': 'Bambang', 'jarak': 60}
    ]
}
print(Data_Dari_Server_Gojek)
print(f"\nDriver disekitar sini {Data_Dari_Server_Gojek['driver_list']}")
print(f"Driver #1 {Data_Dari_Server_Gojek['driver_list'][0]}")
print(f"Driver #1 {Data_Dari_Server_Gojek['driver_list'][3]}")
print(f"Driver terdekat berjarak {Data_Dari_Server_Gojek['driver_list'][3]['jarak']} meter")