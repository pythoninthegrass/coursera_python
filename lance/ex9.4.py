fname = raw_input("Enter file: ")
if len(fname) < 1 : name = "mbox-short.txt"
fh = open(fname)

counts = dict()

# sender

for line in fh:
    if line.startswith("From:"):
        line = line.strip()
        words = line.split() # useless with for function below
        email.append(line[6:])

print counts        