print('calculate how many tires to check')

# calculating
# the 15th and 18th tires are leaking, and every leaking tire is checked three times
number_of_tires = 20
leaking_tires = (15, 18)

# empety variable
number_of_leaking_tires = 0
number_of_checked_tires = 0

# make a program
while number_of_checked_tires < number_of_tires:
    number_of_checked_tires = number_of_checked_tires + 1
    if number_of_checked_tires in leaking_tires:
        number_of_leaking_tires = number_of_leaking_tires + 1
        print(f'tires number {number_of_checked_tires} leaking')
        for number_of_leaking_tires in range(3):
            print('recheked tire number', number_of_checked_tires)
    else:
        print(f'tires number {number_of_checked_tires} not leaking')


# code for counting how much tire not leaking & summary
number_of_not_leaking_tire = number_of_tires - number_of_leaking_tires

print('this is a summary of tire inspection:')
print(f'number of tires that dont leak {number_of_not_leaking_tire} tyre')

if number_of_tires == number_of_not_leaking_tire:
    print('all tires is safe')
else:
    print(f'there is a leaking vehicle tire as much as {number_of_leaking_tires} tires in {leaking_tires}')
