try:
    hrs = raw_input("Enter Hours:")
    h = float(hrs)
    rate = raw_input("Enter Rate:")
    r = float(rate)
except:
    print "Error, need numeric input"
    quit()
    
def computepay (h,r):
	if h <= 40:
		return h*r
	elif h > 40:
		return (40*r)+((h-40)*(1.5*r))

print computepay(h,r)