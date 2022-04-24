"""This program counts the distribution of the hour of the day
for each of the messages. You can pull the hour from the “From” line
by finding the time string and then splitting that string into parts using
the colon character. Once you have accumulated the counts for each
hour, print out the counts, one per line, sorted by hour as shown below """
with open("mbox-short.txt") as file:
    newlines = ""
    for line in file:
        line = line.rstrip()
        if line.startswith("From ") and line.endswith("2008"):
            newlines = newlines + "\n" + line
        continue
    print(newlines)

    newlines = newlines.split()
    dict = {}
    time = []
    for words in newlines:
        if ":" in words:
            time.append(words)
        continue
    print(time)
   
    for word in time:
        newtime = word.split(":")
        dict[newtime[0]] = dict.get(newtime[0], 0) + 1
    for k, v in sorted(dict.items()):
        print(k, v)
        


            
    
