try:
    inp1 = raw_input("Enter Score between 0.0 and 1.0:")
    score = float(inp1)
except:
    print "Error, enter numeric value between 0.0 and 1.0"
    quit()
    
if score > 1.0:
	print "Error, enter numeric value between 0.0 and 1.0"
elif score < 0.0:
    print "Error, enter numeric value between 0.0 and 1.0"
elif score >= 0.9: 
	print "A"
elif score >= 0.8: 
	print "B"
elif score >= 0.7: 
	print "C"
elif score >= 0.6: 
	print "D"
elif score < 0.6: 
	print "F"
