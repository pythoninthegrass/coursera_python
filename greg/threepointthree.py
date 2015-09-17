#Write a program to prompt for a score between 0.0 and 1.0. If the score #is out of range, print an error. If the score is between 0.0 and 1.0, #print a grade using the following table:
#Score Grade
#>= 0.9 A
#>= 0.8 B
#>= 0.7 C
#>= 0.6 D
#< 0.6 F
#If the user enters a value out of range, print a suitable error message #and exit. For the test, enter a score of 0.85.

print "You will be working with a score range"
print "The range is 0.0 - 1.0"

grades = ["A", "B", "C", "D", "F"]
score = raw_input("What score does it deserve?")
yourscore = float(score)

if yourscore == 0.9:
	print grades[0]

elif yourscore == 0.8:
	print grades[1]

elif yourscore == 0.7:
	print grades[2]

elif yourscore == 0.6:
	print grades[3]

elif yourscore == 0.5:
	print grades[4]
	
quit()