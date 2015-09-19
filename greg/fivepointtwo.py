# repeatedly prompt user for integers until user enters 'done'
#enter values of 4, 5, 7 when prompted to enter a number
#Then print out the largest and smallest numbers
#Insert error handling for non numbers
largest = None
while True:
    try:
        nums = raw_input("Enter a number: ")
        if nums == "done":
            break
        num = int(nums)
        if num > None:
            largest = num
    except:
        print "Invalid input"

print "Maximum is", largest

smallest = None
while True:
    try:
        nums2 = raw_input("Enter a new number: ")
        if nums2 == "done":
            break
        num2 = int(nums2)
        if smallest == None:
            smallest = num2
        elif num2 < smallest:
            smallest = num2
    except:
        print "Invalid input"

print "Minimum is", smallest