from functools import reduce

#MAP
def cube(x):
    return x*x*x


# print(cube(2))


# newl = []
l = [1, 2, 4, 6, 8, 4, 3]
# for item in l:
#   newl.append(cube(item))

newl = list(map(lambda x: x*x*x, l))

print(newl)

#FILTER
filter_func = lambda a: a>=4
newnewl = list(filter(lambda a: a>=4, l))
print(newnewl)


#REDUCE

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Calculate the sum of the numbers using the reduce function
sum = reduce(lambda x, y: x + y, numbers)

# Print the sum
print(sum)