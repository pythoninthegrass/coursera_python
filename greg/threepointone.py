hrs = raw_input("Enter Hours:")
h = float(hrs)
reg = 10.50 * 40.0
xtratime = h - 40.0
ot = (10.50 * 1.5) * xtratime

if h >= 40.1:
	print reg + ot
elif h <=40.0:
	print reg