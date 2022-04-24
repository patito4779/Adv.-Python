with open("file.txt", "r") as file:
    count = 0
    for line in file:
        count += 1
        line = line.rstrip()  # This line in the code just helps to remove the extra lines created by the print statement.
        print(line)
print("Line Count is", count)

filename = input("Enter the file name: ")
try:
    fname = open(filename)
except:
    print("file cannot be opened check that the filename is correct", filename)
    quit()

count = 0
for line in fname:
    if line.startswith("Subject"):
        count += 1
print("There were ", count, "subject lines in", filename)

    
# Note that we can use a delimeter such as ; for a split case scenario as shown below
line = 'Patrick;JAmes;Paul;Jude'
line = line.split(';')
print(line)