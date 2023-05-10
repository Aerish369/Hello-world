# #User input factorial
# def factorial_iter(a):
#         a = int(input("Enter a number: ")) #Prompting user for integer input.
#         n = a
#         product = 1
#         for i in range(n): #Range would be 0 to n. 
#             product = product * (i+1) #So 1 is added in i to start counting one above. Further Explanation: 1*1=1,1*2=2,2*3=6,6*4=24,24*5=120.
#         return product

# print(factorial_iter(1))

# #Not User input factorial
# def factorial_iter(n):
#         product = 1
#         for i in range(n): #Range would be 0 to n. 
#             product = product * (i+1) #So 1 is added in i to start counting one above. Further Explanation: 1*1=1,1*2=2,2*3=6,6*4=24,24*5=120.
#         return product

# print(factorial_iter(4))

def factorial_recursive(n):
      if n == 1 or n==0:
            return 1 
      return n * factorial_recursive(n-1)

f = factorial_recursive(4)
print(f)