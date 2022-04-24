"""
This program Reads and parse the “From” lines and pull out the addresses from the line. Count the number of messages from each person using a dictionary.
After all the data has been read, print the person with the most commits
by creating a list of (count, email) tuples from the dictionary. Then
sort the list in reverse o
"""
with open("mbox-short.txt") as file:
    newlines = ""
    for line in file:
        line = line.rstrip()
        if line.startswith("From "):
            newlines = newlines + "\n" + line
        continue
    #print(newlines)

    newlines = newlines.split()
    dict = {}
    emails = []
    for words in newlines:
        if "@" in words:
            emails.append(words)
        continue
    #print(emails)
    for email in emails:
        dict[email] = dict.get(email, 0) + 1
    freqCount = max(dict.values())
    freqEmail = None
    for keys, values in sorted(dict.items(), reverse=True):
        sorted_tuple = (keys, values)
        print(sorted_tuple)
        if values == freqCount:
            freqEmail = keys
    print("The most frequent email was received From: ", freqEmail)

    


    
