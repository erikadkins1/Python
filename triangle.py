#Python program to read inputs for a triangle to determine if the vaules
#meet the requirements to be a triangle and if so to output the triangle properties
#otherwise output an error message
import math

# takes user input of the sides
A = float(input('Enter the length of side A:'))
B = float(input('Enter the length of side B:'))
C = float(input('Enter the length of side C:'))

#compares input to valid triangle 
if (A+B<C) or (B+C<A) or (A+C<B):
#fails triangle perameters outputs error
        print 'Error invalid input (not a valid triangle)'

else:

        print('A triangle with sides the length of\n: %.1f \n: %.1f \n: %.1f' %(A,B,C))
# defines perimeter        
        per = A+B+C
# uses herons therom for area
        p = per/2
        area = ((p*(p-A)*(p-B)*(p-C))**.5)
#valid output
        print('Has a perimeter of: %.2f \nAnd an area of:%.2f' %(per,area))



