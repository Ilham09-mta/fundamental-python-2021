# KONSTRUKSI DASAR PYTHON
# SEQUENTIAL : Eksekusi berurutan
print('Hello World!')
print('by Saifullah')
print('Tanggal 09 Februari 2021')
print('-' * 30)

# PERCABANGAN : Eksekusi terpilih
ingin_cepat = False
if ingin_cepat:
    print('jalan lurus aja ya!')
else:
    print('lewat jalan lain')

# PERULANGAN
jumlah_anak = 4

for index_anak in range(1, jumlah_anak+1): # jumlah perulangan = 5 - 1 = 4
    print(f'Hallo anak #{index_anak}')
