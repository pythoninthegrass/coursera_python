# A = >= 0.9
# B = >= 0.8
# C = >= 0.7
# D = >= 0.6
# F = < 0.6

grades = ["A", "B", "C", "D", "F"]
# print "The range is 0.0 - 1.0" # trips up Coursera interpreter
input = raw_input("What did you get on that Python test? ")
score = float(input) #fails to convert integers (e.g., 90, 80, etc.)

if score >= 0.9 :
    print grades[0]
elif score >= 0.8 :
    print grades[1]
elif score >= 0.7 :
    print grades[2]
elif score >= 0.6 :
    print grades[3]
# else on line 21 doesn't work for some invalid syntax error
elif score <= 0.6 :
    print grades[4]