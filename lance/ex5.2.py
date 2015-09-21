# repeatedly prompt user for integers until user enters 'done'
#enter values of 4, 5, 7 when prompted to enter a number
#Then print out the largest and smallest numbers
#Insert error handling for non numbers

# largest = None
# for num in [4, 5, 7]:
#     try:
#         num = raw_input("Enter a number: ")
#         if num == "done":
#             break
#         if largest is None or num > largest :
#             largest = num
#     except:
#         print "Invalid input"

# print "Maximum is", largest

# smallest = None
# for num2 in [4, 5, 7]:
#     try:
#         num2 = raw_input("Enter a new number: ")
#         if num2 == "done":
#             break
#         if smallest is None or num2 < smallest:
#             smallest = num2
#     except:
#         print "Invalid input"

# print "Minimum is", smallest

largest = None
while True:
    try:
        num = raw_input("Enter a number: ")
        if num == "done":
            break
        if largest is None or num > largest :
            largest = num
    except:
        print "Invalid input"

print "Maximum is", largest

smallest = None
while True:
    try:
        num2 = raw_input("Enter a new number: ")
        if num2 == "done":
            break
        if smallest is None or num2 < smallest:
            smallest = num2
    except:
        print "Invalid input"

print "Minimum is", smallest