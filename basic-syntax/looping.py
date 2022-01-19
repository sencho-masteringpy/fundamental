# menggunakan for
jumlah_buku = 10
print('ibu menyuruh membaca semua bukumu')

jumlah_buku_dibaca = 0

for jumlah_buku_dibaca in range(jumlah_buku + 1):
    print(f'membaca buku ke {jumlah_buku_dibaca}')

# menggunakan while
# dengan asumsi ban ke 15 dan 18 bocor, setiap ban bocor dilakukan 3 kali pengecekan ulang
jumlah_ban = 20

jumlah_ban_bocor = 0
jumlah_ban_yang_tidak_bocor = 0
jumlah_pengecekan_ulang = 0


while jumlah_ban_yang_tidak_bocor < jumlah_ban:
    jumlah_ban_yang_tidak_bocor = jumlah_ban_yang_tidak_bocor + 1
    if jumlah_ban_yang_tidak_bocor in (15, 18):
        jumlah_ban_bocor = jumlah_ban_bocor + 1
        print(f'ban ke {jumlah_ban_yang_tidak_bocor} bocor')
        for jumlah_ban_bocor in range(3):
            jumlah_pengecekan_ulang = jumlah_pengecekan_ulang + 1
            print(f'melakukan cek ulang ban ke {jumlah_ban_yang_tidak_bocor} bocor')
    else:
        print(f'ban ke {jumlah_ban_yang_tidak_bocor} aman')

print(f'jumlah ban tidak bocor sebanyak {jumlah_ban_yang_tidak_bocor} ban')
print(f'jumlah ban bocor sebanyak {jumlah_ban_bocor} ban')
print(f'total pengecekan ulang sebanyak {jumlah_pengecekan_ulang} kali')
