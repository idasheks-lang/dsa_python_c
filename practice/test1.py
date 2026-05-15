import random
# print("Hello python")

# name = "John"
# name2= "John"
# num = 25
# balance = 159.258
# flag = True 

# # print(type(name))
# # print(type(num))
# """print(type(balance))
# print(type(flag))"""

# print("Using Range")

# for i in range(2, 18, 2):
#     print(i)
# # never reaches max value(max-1)

# for i in range(18):
#     if i ==17:
#         print(i)     
  
# # print(id(name)) 
# # print(id(name2)) 

# # items = [1,2,3,4,5,6,7,8]
# # for item in items:
# #   print(item)

 #direct recursion and tail
# def basic(n):
#     if n<0:
#         return n
      
#     print(n)
#     return basic(n -1)
# # also am instance of tail recursion since the recursive call is the last thing being done
  
# basic(5) 

# #indirect recursion

# def a(n):
#     if n>0:
#         print(f"Inside a {n}")
#         return b(n -1)
    
#     #  or
    
#     if n < 1:
#         return n
#     else:
#         print(f"Inside a {n}")
#         return b(n -1)
#     # both the first and the second do the same thing
    
    
# def b(n):
#     if n>0:
#         print(f"Inside b {n}")
#         return a(n -1)
    
# a(5)

# def head_recursion(n):
#     if n<1:
#         return n
      
#     head_recursion(n -1)
#     print(n)
# # is a stack
# head_recursion(5)

def linear_search(values,target):
    for item in range(len(values)):
        if values[item] == target:
            return item
        
    return -1

def get_values():
    values = random.sample(range(10,20),5)
    print(f"The list is {values}")
    target=int(input("Enter value to search "))
    result = linear_search(values, target)
    if result != -1:
        print(f"The value at index {result} is {values[result]}")
    else:
        print(f"Not Found")
        
get_values()

def binary_recursion(values,target,low,high):
    if low>high:
        return
    mid=(low + high)// 2
    print(f"{low}{mid}{high}")
    if values[mid] == target:
        return mid
    elif values[mid] > target:
        return binary_recursion(values, target,low,mid -1)
    else :
        return binary_recursion(values, target,mid + 1 ,high)
    