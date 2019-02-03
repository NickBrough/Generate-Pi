### Find PI to the Nth Digit - Enter a number and have the program generate PI up to that many decimal places.
### Keep a limit to how far the program will go.

import math
from decimal import *
getcontext().prec = 50 # allow for more precise decimals

def Generate_pi(n):
	# using archimedes method of calulating pi (starting with placing a hexagon inside a circle)
	pi = 0 		    #start the pi evaluation at 0
	poly_Sides = 6  #number of sides of the polygon
	sideLength = 1  #length of each side
	diameter = 2

	while poly_Sides < 10000000000000000000000000000:
		
		sideLengthHalfed = Decimal(sideLength)/Decimal(2)
		newRadius_a = (Decimal( Decimal(1) - sideLengthHalfed**2)).sqrt()
		newRadius_b = Decimal(1) - Decimal(newRadius_a)
		newSideLength = (Decimal(sideLengthHalfed**2) + Decimal(newRadius_b**2)).sqrt()

		polyCircum = Decimal(poly_Sides)*Decimal(sideLength)

		#current approximation of pi
		pi = polyCircum/diameter

		#update for next iteration
		sideLength = newSideLength
		poly_Sides = poly_Sides * 2

	return round(pi,n)


def Nth_PI():
	nth = int(input("Enter the amount of decimal places of pi: "))
	print(Generate_pi(nth))


Nth_PI()

