"""print("Hello python")

name = "John"
name2= "John"
num = 25
balance = 159.258
flag = True
"""
# print(type(name))
# print(type(num))
"""print(type(balance))
print(type(flag))"""

"""print("Using Range")

for i in range(2, 18, 2):
    print(i)"""
# never reaches max value(max-1)

"""for i in range(18):
    if i ==17:
        print(i)     """
  
# print(id(name)) 
# print(id(name2)) 

# items = [1,2,3,4,5,6,7,8]
# for item in items:
#   print(item)
  
import random

def max_min(numbers):
    minimum=numbers[0]
    for num in numbers:
        if num<minimum:
            minimum=num
        #print(f"Current min {minimum}")
    return minimum
    
    
def getValues():
    list = random.sample(range(50, 100), 10)   
    # list=[5,4,3,2,1]
    print(list)
    result = max_min(list)
    print(f"value is {result}")

getValues()

lists=random.sample(random(10),5)
print(lists)
print(f"Start at index 2 lists[2:]") #start at index 2
print(f"Stop at 3{list[:3]}")# stop at index 3
list.append(5)

list_a=lists[-1]#get last index
print(list_a)