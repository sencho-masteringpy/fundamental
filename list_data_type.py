car = ['ferrari', 'lamborghini', 'porsche', 'bmw', 'mercedes']

# tampilkan semua list
print(car)

# tampilkan per elemen nilai didalam list
print(car[1])

# tampilkan semua list menggunakan looping
for i in car:
    print(i)

# dynamical type languague
car = [320, 'civic', 'corrola', 86, 'gtr']
print(car)

# menambahkan variabel kedalam list
phone = ['samsung', 'iphone', 'asus', 'xiaomi']
phone.append('nokia')
print(phone)

# menghapus list yang ada didalam variabel
phone = ['samsung', 'iphone', 'asus', 'xiaomi']
phone.clear()
print(phone)

# ganti elemen pada list
phone = ['samsung', 'iphone', 'asus', 'xiaomi']
phone[0] = 'vivo'
print(phone)

# mengambil salah satu elemen pada list dan menampilkan
# jika pop tidak diberikan nilai / index maka akan menghilangkan nilai paling terakhir
# jika pop diberikan nilai negatif maka akan melakuan perhitungan dari belakang (berguna untuk tipe data stack)
phone = ['samsung', 'iphone', 'asus', 'xiaomi']
non_android = phone.pop(1)
print(phone)
print(non_android)

# menghapus list dengan del (menggunakan cara list comperhension) rumus = [start(index):end(jumlah):step(lewat)]
phone = ['samsung', 'iphone', 'asus', 'xiaomi', 'vivo', 'nokia']
del phone[::2]
print(phone)

# membuat list baru dari list lama
phone = ['samsung', 'iphone', 'asus', 'xiaomi']
new_phone = phone[:]

del phone[:]
print(new_phone)

