# A = >= 0.9
# B = >= 0.8
# C = >= 0.7
# D = >= 0.6
# F = < 0.6

input = raw_input("What did you get on that Python test? ")
score = float(input)

if score >= 0.9 :
    print "A"
elif score >= 0.8 :
    print "B"
elif score >= 0.7 :
    print "C"
elif score >= 0.6 :
    print "D"
elif score < 0.6 :
    try:
        print "F"
    except:
        score = -1

# print "At least you tried! "