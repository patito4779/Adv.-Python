# This program gets the Hours in the message log and gets the Hour with the most mail messages"
import re

filename = input("Enter a file name which you want to analyse: ")
if len(filename) < 1 : filename = "mbox-short.txt"

with open(filename) as file:
    new_list = []
    for line in file:
        target = re.findall("^From .*@.*  ([\d+]+):", line)
        if len(target) < 1 : continue
        #print(target)
        new_num = int(target[0])
        new_list.append(new_num)
    print(new_list)
    counts = {}
    for num in new_list:
        counts[num] = counts.get(num, 0) + 1
    print(counts)
    for keys, values in sorted(counts.items()):
        results = (keys, values)


        print(results)
        

        
        
