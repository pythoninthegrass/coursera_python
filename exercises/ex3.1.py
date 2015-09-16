# Rate = 45
# Hours = 10.50 (per hour)
# Answer == 498.75

hours = raw_input("Enter Hours: \n")
hours_number = float(hours)
rate = raw_input("Enter Rate: \n")
rate_number = float(rate)

# original faulty code
# gross_pay = float(hours) * float(rate)
#     if float(hours) > 40
#         (float(hours) * float(rate)) * 1.5
#     else
#         print gross_pay
# print gross_pay

# modified answer via worked ex3.2
if hours <= 40 :
    pay = hours_number * rate_number
else :
    pay = rate_number * 40 + (rate_number * 1.5 * (hours_number - 40))
print pay