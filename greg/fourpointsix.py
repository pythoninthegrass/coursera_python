#promt user for hours and rate per hour using raw_input
#all hours over 40 get 1.5 times pay
#logic for time and half goes into function called computepay()
#use computepay() to do computation
#hours = 45
#Rate of pay = 10.50
#pay = 498.75
#convert str to float for raw_input value.
#Don't do error checking unless desired
hrs = raw_input("Enter Hours:")
h = float(hrs)

xtrahours = h - 40
hours = 40.0
r = 10.50
ot = (10.50 * 1.5) * xtrahours

def computepay(x,y):
    return x + y

r = raw_input("Enter pay rate:")
nr = float(r)

pay = hours * nr

if h >= 40.1:
	print computepay(ot,pay)
