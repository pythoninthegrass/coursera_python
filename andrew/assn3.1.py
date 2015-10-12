try:
    hrs = raw_input("Enter Hours:")
    h = float(hrs)
    rate = raw_input("Enter Rate:")
    r = float(rate)
except:
    print "Error, need numeric input"
    quit()
    
if h <= 40:
	print h*r
elif h > 40:
	print (40*r)+((h-40)*(1.5*r))
