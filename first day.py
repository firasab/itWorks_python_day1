# Exercise (Easy)
# Ask the user for his name, and then print a greeting message
print("write your name please!")
def ask():
    name = input()
    print("My name is:", name )
ask()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Exercise (Easy)
# Ask two users for their names, and then tell them who got the longest name.
print("write your name's please!")
def ask():

    name1 = input()
    print("nice to meet you ", name1 , "!")
    print("write your name's please!")
    name2 = input()
    print("nice to meet you ", name2 , "!")
    if name1 > name2:
        print( name1 ,"your name is longer than " , name2 ," name :D")
    elif name1 == name2:
        print("you both has the same name leneght XD")
    else:
        print( name2 ,"your name is longer than ", name1 ," name :D")
   
ask()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Exercise (Easy)
# Ask a user for his name, and if it starts with a vowel, greet him
print("write your name's please!")
def ask():
    name1 = input()
    if "A" in name1[0] or "I" in name1[0] or "O" in name1[0] or "E" in name1[0] or "U" in name1[0] or "Y" in name1[0] :
        print("wow your name has a vowel O.O , nice to meet you ", name1 , "!")
    elif "a" in name1[0] or "i" in name1[0] or "o" in name1[0] or "e" in name1[0] or "u" in name1[0] or "y" in name1[0] :
        print("wow your name has a vowel O.O , nice to meet you ", name1 , "!")
    else:
        print("nice to meet you" , name1 , "!")
        
ask()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Exercise (Easy)
# Ask the user for his name, and tell him if the last letter is a vowel or a consonant
print("write your name's please!")
def ask():
    name1 = input()
    if "a" in name1[-1] or "i" in name1[-1] or "o" in name1[-1] or "e" in name1[-1] or "u" in name1[-1] or "y" in name1[-1] :
        print("Your name last letter is a vowel , nice to meet you ", name1 , "!")
    else:
        print("Your name last letter is a consonant , nice to meet you ", name1 , "!")
   
        
ask()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Exercise (Easy)
# Ask the user for two numbers (one after the other) and then print their sum
print("please enter a number!")
def ask():
    num1 = int(input())
    print("please enter another number!")
    num2 = int(input())
    num3 = num1 + num2
    print(f"the sum of the 2 numbers =" , num3)
   
   
        
ask()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Exercise (Medium)
#Challenge the user to print the longest sentence 
#without any “A”, if he achieves it, tell him how many letters he wrote, else, print a fail message. 
print("write a sentence without ( A ) letter in it please!")
def ask():
    name = str(input())
    if "a" in name:
        print(" You LOST!")
    else:
        count = len(name)
        print(" GOOD JOB ,we have " , count , "letter in this sentence !")

        
   
        
ask() 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Exercise (Medium)
#Ask the user for his full name (example: “John Doe”), and check the validity of his answer:
#The name should contain only letters.
#The name should contain only one space.
#The first letter of each name should be upper cased.
print("Write your full name please!")
def ask():
    name = str(str(input()))
    count=0
    for i in name:
        if(i.isspace()):
            count=count+1
                  
    bola = name[0].isupper()
    
    if  any(char.isdigit() for char in name):
        print("This is not your name , there is numbers in this name!")
    elif count != 1 :
        print("This is not your real name !")
    elif  bola == False:
    	print("This name is not in uppercase.")
    else :
        print("thanks for your real name" , name)
ask()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Exercise (Medium)
# Ask the user for a sentence, and then tell him how many words are in it.
print("Write a sentenc please!")
def ask():
    sen = str(str(input()))
    count = len(sen.split())
    print("we have " , count , "words in this sen")
ask()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Exercise (Medium)
# Write a python program to get a string made of the first 2 and the last 2 chars from a given string, if the string length is less than 2, return instead the empty string.
# For example: "Helloworld" output "Held", while "Sik" returns ""
print("Enter a word please!")
def ask():
    word = input()
    if len(word) < 4 :
        print(" ''  '' ")
    else :
        first = word[0] + word[1]
        sec = word[-2] + word[-1]
        print(first + sec)
ask()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Exercise (Medium)
# Ask a user for his birthdate (specify the format, for example: DD/MM/YYYY) and then tell him how old he turnt/will turn this year.
def ageCal():
    print("please enter your year birth")
    birthYear = input()
    print("please enter your month birth")
    birthMonth = input()
    print("please enter your Day birth")
    birthDay = input()
    
    today = date.today() 
    
    year = today.year() - birthYear +1
    month = today.month() - birthMonth
    day = today.day() - birthDay
    print("his age will be next year " , year  , " years and " , month , "months and " , day , "days")
ageCal()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Exercise (Hard)
# Ask a user for his birthdate (specify the format, for example: DD/MM/YYYY) and then tell him how old he is today.
from datetime import date

def ageCal():
    print("please enter your year birth")
    birthYear = input()
    print("please enter your month birth")
    birthMonth = input()
    print("please enter your Day birth")
    birthDay = input()
    
    today = date.today() 
    
    year = today.year() - birthYear
    month = today.month() - birthMonth
    day = today.day() - birthDay
    print("his age is " , year  , " years and " , month , "months and " , day , "days")
ageCal()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# For Loops
# Exercise (Easy)
# Write a program that counts the number of element for a list, without the len function.
def countMem():
    name=['Alex','Mike','Dylan','Yossi']
    count = 0
    for i in name:
         count +=1
    print("we have " , count , "members")
countMem()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Exercise (Easy)
# Write a program that print every name that starts by ‘a’
def countMem():
    name=['Alex','Mike','Dylan','yossi','Alan']
    for i in range(0,len(name)):
        if "a" in name[i][0]:
             print("the name is :" , name[i])
countMem()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Exercise (Easy)
# Write a Python program that prints all the numbers from 0 to 10 except 3 and 6.
def countem():
    list_num =[0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]
    for item in list:
        if item == 3 or item == 6:
             continue
        else:
            print(item)
countem()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Exercise (Easy)
# You have a list of users, and you want to remove every user that is below 16 years old.
# Write a program that ask every user their age, and if they are less than 16 years old, remove them from the list.
# At the end, print the final list.
# Example list:
# names = ['Rick', 'Morty', 'Beth', 'Jerry', 'Summer']
def countem():
    names = ['Rick', 'Morty', 'Beth', 'Jerry', 'Summer']
    for item in list:
        print("how old are you ?")
        age = int(input())
        if age < 16:
            names.remove(item)
             
        
    print(names)
countem()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Exercise (Easy)
# You have a list of users, and you want to remove every user that is below 16 years old.
# Write a program that ask every user their age, and if they are less than 16 years old, remove them from the list.
# At the end, print the final list.
# Example list:
# names = ['Rick', 'Morty', 'Beth', 'Jerry', 'Summer']
def countem():
    names = ['Rick', 'Morty', 'Beth', 'Jerry', 'Summer']
    for item in names:
        print("how old are you ?")
        age = input()
        if age < 16:
            names.remove(item)
        else:    
            print(item)
    
countem()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Exercise (Easy)
# Use a for loop to print the numbers from 1 to 20, inclusive.
def printo():
    numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    for num in numbers:  
        print(num)
printo()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Exercise (Easy)
# Make a list of the numbers from one to one million, and then use a for loop to print the numbers.
# (If the output is taking too long, stop it by pressing ctrl-C or by closing the output window.)
def printo():
    mill = list(range(1,1000001))
    for num in mill:  
        print(num)
printo()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Exercise (Easy)
# Make a list of the numbers from one to one million, and then use min() and max() to make sure your
# list actually starts at one and ends at one million. Also, use the sum() function to see how quickly Python can add a million numbers.
def printo():
    mill = list(range(1,1000001))
    index1 = vowels.index(1)
    index2 = vowels.index(1000000)
    for num in mill:  
        print(num)
    
    if index1 == 1:
        print("The index of 1:", index1)
    elif index2 == 1:
        print("The index of 1000000:", index2)
        
    mill_sum = sum(mill)
    print(mill_sum)
printo()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Exercise (Easy)
# Write a program that returns the index of the first occurrence of an item in a list.


# i am sorry but i didnt understand the question , first item in the list will always be in index 0 so why we have to check where is it .
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Exercise (Easy)
# Write a little program that concatenate two lists together without using the + sign.
list1 = [1 , 2 , 3]
list2 = [4 , 5 , 6]

for i in list2:
  list1.append(i)

print(list1)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Exercise (Medium)
# Create a board as following by using for loops:
print("enter how many rows u want")
num = int(input())
for i in range(0,num):
    for j in range(0,num-i-1):
        print(end="")
    for j in range(0,i+1):
        print("*",end="")


        
    
        
    print()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Exercise (Medium)
# Make a list of the multiples of 3 from 3 to 30. Use a for loop to print the numbers in your list.
def math():
    for i in range(0,11):
        print(3*i)
        
math()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Exercise (Medium)
# Write a program that insert an item at a defined index.
def add_num():
    list1 = [ 1, 2, 3, 4, 5, 6, 7 ] 
    print("what number you want to add to the list")
    num = int(input())
    print("where you want to add it ")
    index = int(input())
    list1.insert(index, num)  
    print(list1)  
add_num()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Exercise (Medium)
#Draw the following pattern using for loops:

#     *
#    **
#   ***
#  ****
# *****
print("please enter how many rows u want!")
rows = int(input())
for row in range(1, rows):
    num = 1
    for j in range(rows, 0, -1):
        if j > row:
            print(" ", end=' ')
        else:
            print("*", end=' ')
            num += 1
    print("")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Exercise (Medium)
#What is the output of the following?¶#
#    x = ['ab', 'cd']
#    for i in x:
#        i.upper()
#    print(x)

answer :
         AB , CD
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Exercise (Medium)
# What is the output of the following?¶

#   x = ['ab', 'cd']
#   for i in x:
#       x.append(i.upper())
#   print(x)

answer :
        ab , cd , AB , CD 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Exercise (Easy)
#Draw the following pattern using for loops:
# *
# **
# ***
# ****
# *****
print("please enter the rows u want")
rows = int(input())
i = 1
while i <= rows:
    j = 1
    while j <= i:
        print(("*"), end=" ")
        j = j + 1
    i = i + 1
    print()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Exercise (Hard)
#Draw the following pattern using for loops:

 #     *
 #    ***
 #   *****
 size = 3
m = (2 * size) - 3
for i in range(0, size):
    for j in range(0, m):
        print(end=" ")
    m = m - 1 
    for j in range(0, i + 1):
        print("* ", end=' ')
    print(" ")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Exercise (Hard)
#Execute this program manually (without the help of your computer), write the value of each
#variable and their changes, and add the final output. Try to understand the purpose of this program.
#my_list = [2, 24, 12, 354, 233]
#for i in range(len(my_list) - 1):
#    minimum = i
#   for j in range( i + 1, len(my_list)):
#        if my_list[j] < my_list[minimum]:
#           minimum = j
#            if(minimum != i):
#                my_list[i], my_list[minimum] = my_list[minimum], my_list[i]
# print(my_list) 
asnwer :
[2, 12, 24, 233, 354]
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# While Loops
# Exercise (Easy)
# Write a loop that prompts the user to enter a series of pizza toppings until they enter a ‘quit’ value.
# As they enter each topping, print a message saying you’ll add that topping to their pizza .
need = "quit"
while need != quit :
    if need == quit :
        break
    print("add what you want to ur pizza")
    need = input()
    print("we will add" , need , "to your pizza")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Exercise (Easy)
# A movie theater charges different ticket prices depending on a person’s age .
#  If a person is under the age of 3, the ticket is free; if they are between 3 and 12,
#  the ticket is $10; and if they are over age 12, the ticket is $15 .

# Write a loop in which you ask users their age, and then tell them the cost of their movie ticket .
need = "notend"
while need != "end" :
    print("please enter your age")
    age = int(input())
    if age < 3 :
        print("you can enter for free")
    elif age >= 3 and age < 12:
        print("ypu have to pay $10")
    elif age > 12 :
        print("you have to pay $15")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Exercise (Easy)
# Given a list, use a while loop to print out every elements from the end to the beginning.
list = [1, 3, 5, 7, 9]
i = len(list) -1
while i >= 0:
    print(list[i])
    i -= 1
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Exercise (Easy)
# Without your computer, guess the output of this piece of code:

# i = 1
# while True:    
#   if i == 3: 
#       break
#   print(i) 
#   i + = 1
answer :
        it will print 1 , 2 then do break 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Exercise (Easy)
# Use a while loop to print every number from 5 to 100
i = 5
while i <= 100:
    print(i)
    i += 1
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Exercise (Easy)
# What is the purpose of this program:

# user_input = input("> ")
# while user_input != "p4ssw0rd":
#   print("Access denied.")
#   user_input = input("> ")
# print("Access granted!")
answer :
        to check if the word that user enter is p4ssw0rd , if it is that then it print Access granted! else it print Access denied.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Exercise (Easy)
# What is the problem in this program:
# user_input = input("Password: ")
# while user_input != "my_password":
#   print("Access denied")
# print("Access granted")
answer :
        the user can try just one time , there is no input method in the while loop here
        we can fix it by adding a input method inside the while loop
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Exercise (Medium)
# Take the last exercise, and apply it to a family, ask every member of the family their age,
# and at the end of the loop, tell them the cost of the tickets for the whole family.
count = 0
need = "-1"
while need != -1 :
    if need == -1 :
        break
    print("please enter your age")
    age = int(input())
    if age < 3 :
        print("you can enter for free")
    elif age >= 3 and age < 12:
        print("ypu have to pay $10")
        count += 10
    elif age > 12 :
        print("you have to pay $15")
        count += 15
print(count)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Exercise (Medium)
# Given a list, use a while loop to print out every element which his index is even.
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
lenegth = 0
while lenegth <= len(thislist):
    print(thislist[lenegth])
    lenegth += 2
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Exercise (Medium)
#A group of teenagers is coming to your movie theater and want to see a movie that is restricted for people between 16 and 21 years old.
#Write a program that ask every user their age, and then tell them which can see the movie.
#Try to add the allowed ones to a list.
need = "notend"
while need != "end" :
    print("please enter your age")
    age = int(input())
    if age < 16 :
        print("you cant watch the movie , sorry!")
    elif age >= 16 and age < 21:
        print("you can watch the movie :D")
    elif age > 21 :
        print("you are too old for this movie")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Exercise (Medium)
# Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700.
num = 1500
while num <= 2700:
    if num % 5 == 0 and num % 7 == 0:
        print(num)
        num += 1
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Exercise (Medium)
# Count the number of spaces in a string.
str=input("Enter the string: \n")
spaces=0
for i in range(0,len(str)):
  if(str[i]==' '):
    spaces=spaces+1
print("The number of spaces are: ",spaces)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Exercise (Medium)
# Count the number of words in a string.
test_string = "my name is firas aby sneneh"
print ("The original string is : " +  test_string) 
res = len(test_string.split()) 
print ("The number of words in string are : " +  str(res)) 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Exercise (Medium)
# Write a program that calculate the number of upper case letters and lower case letters in a string.
def string_test(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           d["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", s)
    print ("Number of Upper case characters : ", d["UPPER_CASE"])
    print ("Number of Lower case Characters : ", d["LOWER_CASE"])

string_test('My Name Is Firas')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Exercise (Medium)
# Without your computer, guess the output of this program:
# index = 0
# my_list = [321, 312, 123, 434, 1235]
# while index < len(my_list):
#   s = str(my_list[index])
#  print(s[-1])
#   index += 1
answer :
1
2
3
4
5
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
