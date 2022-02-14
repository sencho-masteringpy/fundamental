# list == array

car = ['ferrari', 'lamborghini', 'porsche', 'bmw', 'mercedes']

# show all list
print(car)

# show per element value in list
print(car[1])

# show all list using loop
for i in car:
    print(i)

# dynamical type languague
car = [320, 'civic', 'corrola', 86, 'gtr']
print(car)


phone = ['samsung', 'iphone', 'asus', 'xiaomi']
# add variable to list from behind
phone.append('nokia')
# add variable to list from front
phone.prepend('HTC')
print(phone)

# delete the list in the variable
phone = ['samsung', 'iphone', 'asus', 'xiaomi']
phone.clear()
print(phone)

# replace element on list
phone = ['samsung', 'iphone', 'asus', 'xiaomi']
phone[0] = 'vivo'
print(phone)

# takes one of the elements in the list and show
# if pop is not given a value / index it will remove the last value
# if pop is given a negative value it will do the calculation backwards (useful for stack data types)
phone = ['samsung', 'iphone', 'asus', 'xiaomi']
non_android = phone.pop(1)
print(phone)
print(non_android)

# delete list with cells (using list comprehension method) formula = [start(index):end(total):step(skip)]
phone = ['samsung', 'iphone', 'asus', 'xiaomi', 'vivo', 'nokia']
del phone[::2]
print(phone)

# create a new list from the old list
phone = ['samsung', 'iphone', 'asus', 'xiaomi']
new_phone = phone[:]

del phone[:]
print(new_phone)

# combine 2 list
car = ['porsche', 'bmw', 'mercedes']
motorcycle = ['kawasaki', 'honda', 'yamaha']

vehicle = car + motorcycle

