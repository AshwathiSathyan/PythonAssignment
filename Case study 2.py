#!/usr/bin/env python
# coding: utf-8

# q1

# In[1]:


def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


user_input = input("Enter a list of numbers separated by spaces: ")
numbers = [int(num) for num in user_input.split()]


result = sum_list(numbers)


print("The sum of the list is:", result)


# q2

# In[2]:


def is_palindrome(string):
    
    string = string.lower().replace(" ", "")
    
    
    for i in range(len(string)//2):
        if string[i] != string[-i-1]:
            return False
    return True


user_input = input("Enter a string: ")


if is_palindrome(user_input):
    print("The string is a palindrome!")
else:
    print("The string is not a palindrome.")


# q3

# In[3]:


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

limit = int(input("Enter the limit for the Fibonacci series: "))

for i in range(limit):
    print(fibonacci(i), end=" ")


# q4

# In[4]:



def multiplication_table(n, i=1):
    if i > 10:
        return
    print(f"{n} x {i} = {n*i}")
    multiplication_table(n, i+1)


number = int(input("Enter a number: "))


multiplication_table(number)


# q5

# In[5]:


def count_vowels_consonants(word):
    vowels = 0
    consonants = 0
    for letter in word:
        if letter.lower() in 'aeiou':
            vowels += 1
        else:
            consonants += 1
    return vowels, consonants

# example usage
word = input("enter the word:")
vowels, consonants = count_vowels_consonants(word)
print(f"Number of vowels: {vowels}")
print(f"Number of consonants: {consonants}")


# q6

# In[6]:


def uppercase_word(word):
    return word.upper()


word =input("enter the word")
uppercase = uppercase_word(word)
print(uppercase)


# q7

# In[7]:


input_list = [12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]
output_list = list(filter(lambda x: x is not None, input_list))
print(output_list)


# q8

# In[8]:


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
    
    def area(self):
        return self.length * self.width
    
    def display(self):
        print(f"Length of rectangle: {self.length}")
        print(f"Width of rectangle: {self.width}")
        print(f"Perimeter of rectangle: {self.perimeter()}")
        print(f"Area of rectangle: {self.area()}")

class Parallelepiped(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height
    
    def volume(self):
        return self.length * self.width * self.height
    
    def display(self):
        super().display()
        print(f"Height: {self.height}")
        print(f"Volume: {self.volume()}")

rectangle = Rectangle(5, 10)
rectangle.display()

parallelepiped = Parallelepiped(5, 10, 3)
parallelepiped.display()


# q9

# In[9]:


class BankAccount:
    
    def __init__(self, accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance
    
    def Deposit(self, amount):
        self.balance += amount
        print("Deposit successful. New balance is: ${}".format(self.balance))
        
    def Withdrawal(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal successful. New balance is: ${}".format(self.balance))
        else:
            print("Insufficient balance.")
    
    def bankFees(self):
        fee = self.balance * 0.05
        self.balance -= fee
        print("Bank fees applied. New balance is: ${}".format(self.balance))
    
    def display(self):
        print("Account Number:", self.accountNumber)
        print("Account Name:", self.name)
        print("Account Balance: ${}".format(self.balance))
        


# create a bank account
my_account = BankAccount(123456, "John Smith", 1000)

# make a deposit
my_account.Deposit(500)

# make a withdrawal
my_account.Withdrawal(200)

# apply bank fees
my_account.bankFees()

# display account details
my_account.display()


# q10

# In[11]:


class Rectangle:
    
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    
    def area(self):
        return self.length * self.breadth
    
    def perimeter(self):
        return 2 * (self.length + self.breadth)



class Parallelepiped(Rectangle):
    
    def __init__(self, length, breadth, height):
        super().__init__(length, breadth)
        self.height = height
    
    def volume(self):
        return self.length * self.breadth * self.height

    
    
rectangle = Rectangle(4, 5)
print("Rectangle area:", rectangle.area())
print("Rectangle perimeter:", rectangle.perimeter())

parallelepiped = Parallelepiped(3, 4, 5)
print("Parallelepiped area:", parallelepiped.area())
print("Parallelepiped perimeter:", parallelepiped.perimeter())
print("Parallelepiped volume:", parallelepiped.volume())


# In[ ]:





# In[ ]:




