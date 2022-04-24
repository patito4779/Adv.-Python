
import sys
filename = input("Enter a file name: ")
if len(filename) < 1 : filename = "mbox-short.txt"
with open(filename) as file:
    newstring = ""
    for line in file:
        line = line.rstrip()
        line = line.lower()
        for letter in line:
            if letter.isalpha():
                newstring += letter
            else:
                continue
    #print(newstring)
    newstring = " ".join(newstring)
    newstring = newstring.split()
    #print(newstring)
    
    counts = {}
    for letters in newstring:
        counts[letters] = counts.get(letters, 0) + 1
    print(counts)

    
    sorted_values = sorted([(values, keys) for keys, values in counts.items()], reverse=True)
    for v, k in sorted_values:
        print(v, k)
    freqCount = max(counts.values())
    freqLetter = None
    for keys, values in counts.items():
        if values == freqCount:
            freqLetter = keys
    print("So finally the most frequent occuring letter in the txt file " + sys.argv[0] + " is: ", freqLetter)
    

