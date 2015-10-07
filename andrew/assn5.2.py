largest = None
while True:
#for value in inp:
    num = raw_input('Enter a number: ')
    
    #handle the edge cases
    if num == 'done' : break
    if len(num) < 1 : break #check for empty line
    try:
        num = int(num)
    except:
        print 'Invalid input'
        continue
        
    #Performing actual function work
    if largest is None:
        largest = num
    elif num > largest:
        largest = num
        continue
print "Maximum is",largest

smallest = None
while True:
#for value in inp:
    num = raw_input('Enter a number: ')
    
    #handle the edge cases
    if num == 'done' : break
    if len(num) < 1 : break #check for empty line
    try:
        num = int(num)
    except:
        print 'Invalid Input'
        continue
        
    #Performing actual function work
    if smallest is None:
        smallest = num
    elif num < smallest:
        smallest = num
        continue
        
print "Minimum is",smallest