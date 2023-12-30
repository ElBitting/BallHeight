g = 9.81
v0 = float(input("What is the initial velocity "))
t = float(input("What time do you want to check "))

while t< 0:
    print('Error, the time must be greater than zero.')
    t = float(input("What is the time you want to check "))

y = v0 * t - g * t ** 2 / 2

if t > 2*v0/g or y == 0:
    print("That ball is on the ground")
else:
    print('The ball is '+str(y)+' meters above the ground')

