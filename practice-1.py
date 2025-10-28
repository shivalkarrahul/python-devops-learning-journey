print("\nPrint 1 to 10 using a loop")
for i in range(1, 11):
    print(i)

print("\nSum of first 50 numbers")
sum = 0
for i in range(1, 51):
    sum = sum + i
print("Sum of first 50 numbers = ", sum)

print("\nCheck if a number is even or odd")
input_number = 11
if input_number % 2 == 0:
    print(input_number ,"Number is even")
else:
    print(input_number ,"Number is odd")

input_number = 10
if input_number % 2 == 0:
    print(input_number ,"Number is even")
else:
    print(input_number ,"Number is odd")    

print("Take user input and reverse a string")

user_string = input("Enter a string to reverse ")
reversed_string = ""

for s in user_string:
    reversed_string = s+ reversed_string
print("Reversed String = ", reversed_string)

print("Find the largest of three numbers")
number1 = int(input("Enter the first number "))
number2 = int(input("Enter the second number "))
number3 = int(input("Enter the third number "))

if number1 > number2 and number1 > number3:
    print(number1, "is greater")
elif number2 > number1 and number2 > number3:
    print(number2 ,"is greater")
else:
    print(number3 ,"is greater")

print("Count vowels in a string")
user_string = input("Enter a string to count vowels ")
vowel_count = 0
for s in user_string:
    if s == 'a' or s == 'e' or s == 'i' or s == 'o' or s == 'u':
        vowel_count = vowel_count + 1
print("Vowel in ", user_string, " = ", vowel_count)

#Print multiplication table of any number (e.g., 5)
print("Print multiplication table of any number (e.g., 5)")
result = 0
for i in range(1, 11):
    result = (5 * i)
    print("5 *", i, "=", result)


#Find factorial of a number
print("Find factorial of a number")
number = 10
print("Factorial of", number)
factorial = 1
for i in range(1, number+1):
    factorial = factorial * i
print("Factorial of", number, "=", factorial)

#Check if a string is a palindrome
user_string = input("Enter a string to check if it is palindrome ")
reversed_string = ""
for s in user_string:
    reversed_string = s + reversed_string
if user_string.lower() == reversed_string.lower():
    print("String", user_string ,"is a palindrome")
else:
    print("String", user_string ,"is not a palindrome")


#Generate Fibonacci Series up to 10 Terms
#0 1 1 2 3 5 8 13 21 34
print("Generate Fibonacci Series up to 10 Terms")
first = 0
next = 1
for i in range(0, 11):
    print(first)
    first, next  = next, first + next 
#Print 1 to 10 using a loop





