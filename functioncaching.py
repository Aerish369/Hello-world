import time
from functools import lru_cache #* This is built-in module for managing cache in the complex functions of python.

@lru_cache(maxsize=3) #* This decorator is used to invoke the function caching in python.
def complex_work(n):  #* The maxsize helps to determine cache storing for how many time of calling the function. 
    time.sleep(n)
    return n

# if __name__ == '__main__':
#     print("Initializing complex work.")
#     complex_work(5) #! Takes 5 secs to execute. 
#     print("Completed complex work. Calling it again for more work.")
#     complex_work(5) #! Takes no time to execute as it is stored as cache in the temp memory by function-caching. 
#     print("Completed second work. Time for 3rd time. ")
#     complex_work(5) #! Takes no time. 
#     print("Completed the third execution.")


#! Understanding Maxsize of @lru_cache:

#* As the maxsize value is 3. It only saves latest 3 executions of the function(complex_work.)
if __name__ == '__main__':
    print("Initializing complex work.")
    complex_work(5) #! Takes 5 secs to execute. It is not saved in the memory. 
    print("1st exe")
    complex_work(3) #? Latest third save of the function
    print("2nd exe")
    complex_work(2) #? Latest second save of the function
    print("3rd exe")
    complex_work(4) #? Latest first save of the function
    print("4th exe")
    print("Completed 4 complex work. Calling it again for complex_work(5) which is not saved. ")
    complex_work(5) #! Takes 5 seconds to execute as it is not saved.  
    print("Completed after 5 secs")
    
    
