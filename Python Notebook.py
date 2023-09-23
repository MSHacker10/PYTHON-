#!/usr/bin/env python
# coding: utf-8

# In[1]:


x = 2
print(x == 2) # prints out True
print(x == 3) # prints out False
print(x < 3) # prints out True


# In[2]:


name = "Eesha"
age = 21
if name == "Eesha" and age == 21:
    print("Your name is Eesha, and you are also 21 years old.")

if name == "Eesha" or name == "Aliza":
    print("Your name is either Eesha or Aliza.")


# In[7]:


statement = False
another_statement = True
if statement is True:
    # do something
    pass
elif another_statement is True: # else if
    # do something else
    pass
else:
    # do another thing
    pass


# In[8]:


x = 2
if x == 2:
    print("x equals two!")
else:
    print("x does not equal to two.")


# In[9]:


x = [1,2,3]
y = [1,2,3]
print(x == y) # Prints out True
print(x is y) # Prints out False


# In[10]:


print(not False) # Prints out True
print((not False) == (False)) # Prints out False


# In[11]:


# change this code
number = 16
second_number = 0
first_array = [1,2,3]
second_array = [1,2]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")


# In[12]:


primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)


# In[13]:


# Prints out the numbers 0,1,2,3,4
for x in range(5):
    print(x)

# Prints out 3,4,5
for x in range(3, 6):
    print(x)

# Prints out 3,5,7
for x in range(3, 8, 2):
    print(x)


# In[14]:


# Prints out 0,1,2,3,4

count = 0
while count < 5:
    print(count)
    count += 1  # This is the same as count = count + 1


# In[15]:


# Prints out 0,1,2,3,4

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

# Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)


# In[16]:


# Prints out 0,1,2,3,4 and then it prints "count value reached 5"

count=0
while(count<5):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))

# Prints out 1,2,3,4
for i in range(1, 10):
    if(i%5==0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")


# In[17]:


numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]

# your code goes here
for number in numbers:
    if number == 237:
        break

    if number % 2 == 1:
        continue

    print(number)


# In[20]:


block_head:
    1st block line
    2nd block line
    ...


# In[21]:


def my_function():
    print("Hello From My Function!")


# In[22]:


def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))


# In[23]:


def sum_two_numbers(a, b):
    return a + b


# In[25]:


# Define our 3 functions
def my_function():
    print("Hello From My Function!")

def my_function_with_args(username, greeting):
    print("Hello, %s, From My Function!, I wish you %s"%(username, greeting))

def sum_two_numbers(a, b):
    return a + b

# print(a simple greeting)
my_function()

#prints - "Hello, Eesha Alam, From My Function!, I wish you a great year!"
my_function_with_args("Eesha Alam", "a great year!")

# after this line x will hold the value 3!
x = sum_two_numbers(1,2)


# In[26]:


# Modify this function to return a list of strings as defined above
def list_benefits():
    return []

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    return ""

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()


# In[27]:


class MyClass:
    variable = "eesha"

    def function(self):
        print("This is a message inside the class.")


# In[28]:


class MyClass:
    variable = "eesha"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()


# In[31]:


class MyClass:
    variable = "eesha"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()

myobjectx.variable


# In[32]:


class MyClass:
    variable = "eesha"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()

print(myobjectx.variable)


# In[33]:


class MyClass:
    variable = "eesha"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()
myobjecty = MyClass()

myobjecty.variable = "alam"

# Then print out both values
print(myobjectx.variable)
print(myobjecty.variable)


# In[34]:


class MyClass:
    variable = "eesha"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()

myobjectx.function()


# In[35]:


class NumberHolder:

   def __init__(self, number):
       self.number = number

   def returnNumber(self):
       return self.number

var = NumberHolder(10)
print(var.returnNumber()) #Prints '10'


# In[38]:


# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

# your code goes here
car1 = Vehicle()
car1.name = "Fortuner"
car1.color = "black"
car1.kind = "convertible"
car1.value = 60000.00

car2 = Vehicle()
car2.name = "Cultas"
car2.color = "white"
car2.kind = "van"
car2.value = 10000.00

# test code
print(car1.description())
print(car2.description())

