# percabangan
# variabel adalah tempat untuk menyimpan data (bisa berupa text, angka, atau suatu kondisi benar atau salah)

panjang_kemacetan = 50
lama_kemacetan = 2

print(f"panjang kemacetan yaitu {panjang_kemacetan} M")
print(f"lama kemacetan yaitu {lama_kemacetan} Menit")

if lama_kemacetan < 5:
    if panjang_kemacetan > 100:
        print('lewat jalur alternatif')
    else:
        print('mohon tunggu')
else:
    print('lewat jalur alternatif')
