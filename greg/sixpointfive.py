# Write code using find() and string slicing
#extract number at end of the line below
#convert extracted value to a float and print it

text = "X-DSPAM-Confidence:    0.8475";
num = text.find('0')
#print num: #num = 23
combobreaker = text[num:]
print float(combobreaker)