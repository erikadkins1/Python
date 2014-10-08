#Python program to read inputs and calculate maximum hull speed of a boat
#stores user input
wl = float(input('Enter the waterline length:'))
#calculates max hull speed
hull = 1.34 * wl **.5
#outputs both input and calculated results
print('A boat with a waterline length:%.1f \nHas a theoretical maximum speed of:%.1f' %(wl,hull))

