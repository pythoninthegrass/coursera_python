# Rate = 45
# Hours = 10.50 (per hour)
# Answer == 498.75

def computepay(hours_number,rate_number):
    return rate_number * 40 + (rate_number * 1.5 * (hours_number - 40))

hours = raw_input("Enter Hours: \n")
hours_number = float(hours)
rate = raw_input("Enter Rate: \n")
rate_number = float(rate)
if hours <= 40 :
    pay = hours_number * rate_number
else :
    pay = computepay(hours_number,rate_number)
print pay