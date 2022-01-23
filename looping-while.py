print('calculate how many tires to check')

# calculating
# the 15th and 18th tires are leaking, and every leaking tire is checked three times
number_of_tires = 20
leaking_tires = (15, 18)

# empety variable
number_of_leaking_tires = 0
number_of_not_leaking_tires = 0
number_of_rechecked = 0

while number_of_not_leaking_tires < number_of_tires:
    number_of_not_leaking_tires = number_of_not_leaking_tires + 1
    if number_of_not_leaking_tires in leaking_tires:
        jumlah_ban_bocor = number_of_leaking_tires + 1
        print(f'ban ke {number_of_not_leaking_tires} bocor')
        for jumlah_ban_bocor in range(3):
            number_of_rechecked = number_of_rechecked + 1
            print(f'melakukan cek ulang ban ke {number_of_not_leaking_tires} bocor')
    else:
        print(f'ban ke {number_of_not_leaking_tires} aman')

if number_of_tires == number_of_not_leaking_tires:
    print('semua ban aman')
else:
    print(f'terdapat ban yang bocor yaitu sebanya {number_of_leaking_tires} ban')

print('berikut adalah ringkasan pemeriksaan ban:')
print(f'jumlah ban tidak bocor sebanyak {number_of_not_leaking_tires} ban')
print(f'jumlah ban bocor sebanyak {number_of_leaking_tires} ban yatu di ban ke {leaking_tires}')
print(f'total pengecekan ulang sebanyak {number_of_rechecked} kali')
