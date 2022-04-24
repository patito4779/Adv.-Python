filename = input("Enter a file:")
if len(filename) < 1 : filename = "clown.txt"

dict = {}
with open(filename) as file:
    for line in file:
        line = line.rstrip()
        line = line.split()
        for word in line:
            dict[word] = dict.get(word, 0) + 1

print(dict)

# The line below returns the maximum that appears in the dictionary.
frqCount = max(dict.values())
frqWord = None
for key, value in dict.items():
    if value == frqCount:
        frqWord = key

print(frqWord)


