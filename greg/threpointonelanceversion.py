# Rate = 45
# Hours = 10.50 (per hour)
# Answer == 498.75

hrs = raw_input("Enter Hours: ")
h = float(hrs)
rate = raw_input("Enter Rate: ")
r = float(rate)

# reg = 10.50 * 40.0
#xtratime = h - 40.0
ot = r * 40 + (r * 1.5 * (h - 40))

# if h >= 40.1:
# 	print reg + ot
# elif h <=40.0:
# 	print reg

if h <= 40 :
    pay = h * r
else :
    pay = ot
print pay
