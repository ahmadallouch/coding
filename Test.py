# Hello World

print("Hello World")

# Variable and Types

string = "This is a string with double quotes"
string2 = 'This is a string with single quotes' #Quotes will make no difference to strings, as long as you use either.
integer = 12
integer2 = -245
float1 = 3.4
float2 = -3.6

# Lists

string_list = ['item1','item2','item3','item4','item5']
integer_list = [1, -2 ,3 ,4 , -5]
float_list = [1.2, -2.3 ,3.4 ,-4.5, 5.6]
mixed_list = ['item3', -4, 98.9, -56,8, 23, "item4"]

# Basic Operators

addition = 1 + 1 #This also supports strings but it will only combine the words.
subtraction = 4 - 2 #This will output 2.
multiplication = 4 * 5 #This will output 20.
division = 4 / 2 #This will output 2.
remainder = 11 / 3 #This will give a remainder of a division, 2 in this case.
exponent = 11 ** 2 #This will make 11 to the power of 2.
string_mutiply = 'Hello World' * 11 #This will give you 11 of the string, you can also do the same with addition.
#You can also use all of these operators with lists.

# String Formating

name = "John"
print("Hello, %s!" % name) #This prints out "Hello, John!".
#The %s will replace what comes after the % with a string formatted variable.
name = "John"
age = 23
print("%s is %d years old." % (name, age))
#This %d will replace itself with the nearest integer it detects, int this case age which equals to 23.

# Basic String Operations

len(string) #This will tell you how many characters are in a string.
string.index("T") #This will tell me where 'T' is in the variable called "string".
string.count('a') #This will count how many occurance there are of 'a' in the variable "string".

