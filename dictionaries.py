lsit = ["paul", "game", "paul", "jude", "lucky", "lucky", "paul"]
count = {}

for name in lsit:
    # if name not in count:
    #     count[name] = 1
    # else:
    #     count[name] += 1
    count[name] = count.get(name, 0) + 1   # This is an alternative of one line of code to the commented out code above.

print(count)

with open("file.txt") as file:
    for line in file:
        line = line.rstrip()
        line = line.split()
        for name in line:
            count[name] = count.get(name, 0) + 1
print(count)

