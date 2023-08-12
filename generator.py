
#! Using Normal Function
def square(num):
    result = []
    for i in num:
       result.append(i * i)
    return result


      
list1 = [1,  2, 3, 4, 5]
print(square(list1))

#! Using List comprehension
list2 = [i * i for i in list1]

print(list2)


#! Using Generators

def generators(num):
    for i in num:
        yield i * i #* yield is used to define generators 

geneLis = generators([2, 4, 6, 8, 10])

# print(next(geneLis))
# print(next(geneLis))
# print(next(geneLis))
# print(next(geneLis))
# print(next(geneLis))

for i in geneLis:
    print(i)

#! Generator are great to use list in an efficient manner as it doesn't take memory and is used only when got called. 
#! Making it better choice to use while working with large sets of datas. 