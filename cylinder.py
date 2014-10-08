#Python program to calculate cylinder properties
# calls math feature
import math
# stores user input
radius = float(input('Enter the radius:'))

height = float(input('Enter the height:'))

#outputs user input
print('A cylinder with a radius of: %.2f \nAnd a height of: %.2f' %(radius,height))
#calculates volume and area of cylinder
vol = math.pi*(radius**2)* height

area = (2* math.pi* radius* height) + (2* math.pi*(radius**2))
#outputs calculated results
print('Has a volume of: %.2f \nAnd a surface area of:%.2f' %(vol,area))



