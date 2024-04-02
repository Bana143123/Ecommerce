class Product:
    def __init__(self, name, price, deal_price, rating):
        self.name = name
        self.price = price
        self.deal_price = deal_price
        self.rating = rating
        self.you_saved = price - deal_price 
    

    def display_productdetails(self):
        print("Product name : {}".format(self.name))
        print("Price : {}".format(self.price))
        print("Deal_price : {}".format(self.deal_price))
        print("rating : {}".format(self.rating))
        print("you_saved : {}".format(self.you_saved))

class Electronicitem(Product):
    def __init__(self, name, price, deal_price, rating, warranty_in_months):
        super().__init__(name, price, deal_price, rating)
        self.warranty_in_months = warranty_in_months
    
    def display_productdetails(self):
        super().display_productdetails()
        print("warranty : {} months ".format(self.warranty_in_months))

class Groceryitem(Product):
    def __init__(self, name, price, deal_price, rating, expiry_date):
        super().__init__(name, price, deal_price, rating)
        self.expiry_date = expiry_date
    
    def display_productdetails(self):
        super().display_productdetails()
        print("Expirydate : {} ".format(self.expiry_date))
class Order:
    delivery_charges = {
        "Normal" : 0,
        "Prime_delivery" : 99
    }
    def __init__(self, delivery_method, delivery_address):
        self.items_in_cart = []
        self.delivery_method = delivery_method
        self.delivery_address = delivery_address

    def add_item(self, product, quantity):
        item = (product, quantity)
        self.items_in_cart.append(item)
        print(self.items_in_cart)
    
    def display_order_details(self):
        print("Delivery method : {}".format(self.delivery_method))
        print("Delivery_address : {}".format(self.delivery_address))
        print("Products")
        print("==============================================================")
        for product, quantity in self.items_in_cart:
            product.display_productdetails()
            print("Quantity : {}".format(quantity))
            print(" ")

    def tot_bill(self):
        Total_B = 0
        for product, quantity in self.items_in_cart:
            Bill = product.deal_price*quantity
            Total_B+=Bill
            print(f"Totalbill for your {product}  : {Total_B}")



p = Electronicitem("Washing machine", 50000, 30000, 4.8, 50)
#p.display_productdetails()
g = Groceryitem("Maggie", 200, 150, 4.5, 2023)
#g.display_productdetails()
A = Order("Normal","Tadipatri")
A.add_item(p, 3)
A.add_item(g, 2)
A.display_order_details()
A.tot_bill()

'''n=list(input("enter input :",))
def reddy(n):
    x=len(n)
    #print(x)
    if x%2==0:
        n1=int(n[(x//2)-1])
        print(type(n1))
        n2=int(n[(x//2)])
        print(type(n2))
        print((n1+n2)/2)
        
    else:
        print(n[x//2])
reddy(n)'''
''#------------------------------------------------
'''from collections import Counter
s="loving some one is injurious to life"
print(Counter(s))
print(s.count("o"))'''
#-------------------------------------------------
'''list=[1,0,2,0,4,6]
for item in list:
    if item==0:
        list.remove(item)
        list.append(item)
print(list)'''
#===========================================

'''s="loving some one is injurious to life"
from collections import Counter
print(Counter(s))
print(s.count('l'))'''
'''class v:
    def __init__(self,value):
        self.value=value




    def __str__(self):
        s=f"MyClass instance with value: {self.value}"
        return s
    
if __name__=="__main__":
   obj= v(20)
   print(type(obj))
   string=str(obj)
   print(string)'''




'''import requests

re=requests.get("https://www.google.com")
if re.status_code==200:
    print(re.text)
else:
    print(re.status_code)'''


#===========================
'''import math
print(math.factorial(5))
print(math.floor(4.0))
print(math.ceil(4.1))
print(math.sqrt(4))'''
'''import random
print(random.randint(1,6))
#print(random.choice(["d","y","23"]))'''
#-------------------------------------
#python Built in functions
# print() len() min() max()......
#map(function,sequence)  filter(function,sequence) reduce(function,sequence)
#Reduce function
from functools import reduce

def sum(a,b):
    return a+b

list_a = [1,2,3,4,5,6]
Total_sum = reduce(sum,list_a)
print(Total_sum)   

# Filter method filters the elements in the sequence based on the result of a function and return values

def positive_num(n):
    return n>0
li = [1,-2,7,-7,9]
pos = filter(positive_num,li)
print(list(pos))
# Map applies a given function to each item of the sequence and return a sequence of the result.

def square(n):
    return n*n

lis = [1,2,3,4,5]
out = map(square,lis)
print(list(out))

#================
line = list(map(int,input().split()))
print(line)

# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
#print("Try programiz.pro")


'''a = " i am narendra kumar reddy"
s=a.split()
print(s)
rev=[]
for i in range(len(s)):
    rev.append(s[-i-1])                  
rev_string = " ".join(rev)
print(rev_string)
print(type(rev_string))'''
'''
L= ["python","java","c"]
dic={}
for i,j in enumerate(L):
    dic.update({i:j})
print(dic)'''

'''L  = [1,34,67,"a",54,"v",2]
sum=0
for i in L:
    if isinstance(i,int):
        sum+=i
print(sum)'''

'''L=[1,34,67,"a",54,"v",2]
sum=0
for i in L:
    if isinstance(i,int):
        for digit in str(i):
            sum+=int(digit)
print(sum)'''
'''def pri(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
n=20
if pri(n):
    print(f"{n} : Prime number")
else:
    print(f"{n} : Not a prime")'''
'''l= [2,4,6,8,4,1,45]
for i in range(len(l)-1):
    for j in range(len(l)-1):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
print(l)'''

'''def fibn(n):
    fib=[0,1]
    for i in range(2,n):
        next=fib[i-1]+fib[i-2]
        fib.append(next)
    return fib
res=fibn(10)
print(res)'''
'''def increment(a):
    while True:
        a+=1
        yield a
a=5
res=increment(a)
print(next(res))
print(next(res))
print(next(res))'''
'''def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)

n=int(input())
re=fact(n)
print(re)'''
'''import time

# Define the decorator
def calculate_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record the start time
        result = func(*args, **kwargs)  # Call the original function
        end_time = time.time()  # Record the end time
        execution_time = end_time - start_time  # Calculate the execution time
        print(f"Execution time of '{func.__name__}': {execution_time} seconds")
        return result
    return wrapper

# Apply the decorator to the function
@calculate_execution_time
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

# Call the function
result = factorial(5)
print("Factorial:", result)'''


'''
L = [1,[3,5],4,[5,7,0]]
flat=[]
for i in L:
    if isinstance(i,list):
        flat.extend(i)
    else:
        flat.append(i)
print(flat)'''

L= ['1','3','5','6']
res=[int(i) for i in L]
print(res)
