print('\ntipe data skalar => tipe data sederhana')
anak1 = 'Muhammad'
anak2 = 'Ilham'
anak3 = 'Saifullah'
anak4 = 'Juli'

print(anak1)
print(anak2)
print(anak3)
print(anak4)

print('\ntipe data list/daftar/array')
anak = ['Muhammad', 'Ilham', 'Saifullah', 'Juli']
print(anak)
anak.append('Bambang')
print(anak)

print('\nsapa anak ke 2')
print(f'hai {anak[1]}!')

print('\nSapa semua anak')
for a in anak:
    print(f'hai {a}!')

print('\nSapa semua anak: cara ribet')
for a in range (0, len(anak)):
    print(f'{a+1}. Hai {anak[a]}')