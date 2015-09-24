# Use words.txt as the file name
fname = raw_input("Enter file name: ")

try:
    fobj = open(fname)
    
    # for line in fobj:
    #     line = line.rstrip()

    print(fobj.read())
    fobj.close()
    
    # up_fobj = fobj.upper
    # print(fobj.read())
    # fobj.close()
    
except:
    print "File can't be opened:", fname
    exit()