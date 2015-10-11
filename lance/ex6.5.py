text = "X-DSPAM-Confidence:    0.8475"
#print text

index = text.find(':') # locates colon l
#print index

# print text[index:] # shows ":" onwards
# print text[index+1:] # removes ":" leaving white space

conf_num = float (text[index+1:])
print conf_num