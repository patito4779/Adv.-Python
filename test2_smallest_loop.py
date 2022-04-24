# make the code to find smallest number

smallest_so_far = None
print("berfore", smallest_so_far)
for num in [9, 41, 12, 3, 74, 15]:
    if smallest_so_far is None:
        smallest_so_far = num
    elif num < smallest_so_far:
        smallest_so_far = num

    print(smallest_so_far, num)
print("After", smallest_so_far)



mystring = "Here in this string you will find my personal email address which is patrick.okwe@gmail.com and that is it"
# get the email domain name and concat it with another username email address.
at = mystring.find("@")
print("@ is located in position", at)

domain = mystring.find(" ",at)   # This line gets gmail.com before the space in front of it
print("space after domain is at position", domain)

print(mystring[at+1:domain])
new_email = "mudiokwe" + mystring[at:domain]  # This line prints a new email with mudiokwe concatenated with gmail.com
print(new_email)



