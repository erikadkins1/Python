# Python program to calculate different properties of a sphere
import math

# input from user
radius = float(input('Enter the radius: '))

#calculates volume
volume = ((float(4)/3)* math.pi *(radius**3))


#calculates surface area

sarea = (4* math.pi *(radius**2))
#outputs inputs and calculated results
print('A sphere of a radius: %.2f \nHas a volume of:%.2f' %(radius,volume))
print('Has a surface area of: %.2f ' %(sarea))


