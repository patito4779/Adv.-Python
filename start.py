# let us write some codes that we can understand
# what is a list in python it is simply a collection of data that we can read.

list = ["Patrick", "Lucky", "Many", True]
# how do i check if an item is inside of my list?
list2 = list.copy()
print(list2)

# clear() can actually clear the contents of a list

numbers = [1, 2, 4, 5, 7]
times = [u*u for u in numbers]

print(numbers)
print(times)


def hi(name):
    return "Hi " + name + " how are you"

print(hi("patrick"))