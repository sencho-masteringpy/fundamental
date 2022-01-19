# branch
# a variable is a place to store data (can be text, numbers, or a true or false condition)

jam_length = 50
jam_time = 2

print(f"panjang kemacetan yaitu {jam_length} Meter")
print(f"lama kemacetan yaitu {jam_time} Minute")

if jam_time < 5:
    if jam_length > 100:
        print('lewat jalur alternatif')
    else:
        print('mohon tunggu')
else:
    print('lewat jalur alternatif')
