#Python program to calculate perimeter and area of a rectangle
#stores user input
length = float(input('Enter the length:'))

width = float(input('Enter the width:'))

#outputs user input
print('A rectangle with a length of: %.1f \nAnd a width of: %.1f' %(length,width))
# calculates perimeter and area
per = 2*(length + width)
area = length * width
#outputs calculated results
print('Has a perimeter of: %.1f \nAnd an area of:%.1f' %(per,area))



