# branch
# a variable is a place to store data (can be text, numbers, or a true or false condition)

print('ask people how long estimated time and how traffic crowded')

# this variable for the program
estimated_time = 2
is_traffic_crowded = True

print('get answers from a people')
print(f"estimated time is  {estimated_time} Minute")
print(f"is traffic {is_traffic_crowded} crowded")

# make a program
if estimated_time < 5:
    print('go with car')
    if is_traffic_crowded:
        print('use your driver')
    else:
        print('driving without driver')
else:
    print('go with motorcycle')

print('arrive at the office')
