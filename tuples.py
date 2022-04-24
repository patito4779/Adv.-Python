# using tuples to sort items
# Note that the items function for dictionaries turns a dictionary into a list of tuples as in line 5
from pyparsing import alphanums


d = {'a':10, 'b':1, 'c':22}
t = sorted(d.items())
print(t) 
for key, value in sorted(d.items()):
    print(key, value)

counts = {}
with open("intro.txt") as file:
    for line in file:
        line = line.rstrip()
        l = ""
        for letter in line:
            
            if letter.isalnum() or letter == " ":
                l += letter
            continue
                
            
        line = l.split()
        for word in line:
            counts[word] = counts.get(word, 0) + 1
print(counts)

lst = []
for keys, values in counts.items():
    newtuple = (keys, values)
    lst.append(newtuple)

lst = sorted(lst, reverse=True)  # This arranges  the keys in reverse alphabetical order from z down to a
print(lst)
for keys, values in lst[:10]:
    print(values, keys)