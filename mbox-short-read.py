filename = input("Enter the name of the file: ")
try:
    fname = open(filename)
except:
    print("the filename is not correct ")
    quit()

with fname as file:
    for line in file:
        line = line.rstrip()
        line = line.split()
        if len(line) < 3 or line[0] != "From": continue
        print(line[2])
        
