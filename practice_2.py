#Function Definition
def print_message(message: str) -> None:
    print("\nFunction = print_message")
    print(message)


def sum_of_numbers(number: int) -> None:
    print("\nFunction = sum_of_numbers")
    total = 0
    for i in range(number+1):
        print(total ,"+", i)
        totalt = total + i        
    print("Sum of numbers upto ", number, " = ", total)

def check_even_odd(number: int) -> None:
    print("\nFunction = check_even_odd")
    if number % 2 == 0:
        print("Number", number ,"is even")
    else:
        print("Number", number ,"is odd")

def reverse_string(user_string: str) -> None:
    print("\nFunction = reverse_string ")
    reversed_string = ""
    for c in user_string:
        reversed_string = c + reversed_string
    print("User String = ", user_string)
    print("Reversed String = ", reversed_string)

def largest_of_three_numbers(number1: int, number2: int, number3: int) -> None:
    print("\nFunction = largest_of_three_numbers")
    if number1 > number2 and number1 > number3:
        print("number1 =", number1, "is greater than number2 =", number2 ,"and number3 =", number3)
    elif number2 > number1 and number2 > number3:
        print("number2 =", number2 ,"is greater than number1 =", number1, "and number3 =", number3)
    elif number3 > number1 and number3 > number2:
        print("number3 =", number3 ,"is greater than number1 =", number1 ,"and number2 =", number2)
    else:
        print("number1 =", number1 ,"number2 =", number2 ,"number3 =", number3 ,"are all equal")
        
def count_vowels(input_string: str) -> None:
    print("\nFunction = count_vowels")
    total_vowels = 0
    for c in input_string:
        if c.lower() in "aeiou":
            total_vowels = total_vowels + 1
    print("Total Vowels in ", input_string , "=", total_vowels)

def table(number: int) -> None:
    print("\nFunction = table")
    result = 0
    for i in range(1, 11):
        result = number * i
        print(number ,"*", i ,"=", result)

def factorial_of_number(number: int) -> None:
    print("\nFunction = factorial_of_number")
    factorial = 1
    for i in range(1, number+1):
        factorial = factorial * i
    print("Factorial of ", number ,"=", factorial)

def check_palindrome(user_string: str) -> None:
    print("\nFunction = check_palindrome")
    reversed_string = ""
    for c in user_string:
        reversed_string = c + reversed_string
    if user_string.lower() == reversed_string.lower():
        print("String ", user_string ,"is a Palindrome")
    else:
        print("String", user_string ,"is not a Palindrome")

def fibonacci_series(number: int) -> None:
    # 0 1 1 2 3 5
    print("\nFunction = fibonacci_series")
    first = 0
    next = 1
    for i in range(1, number+1):
        print(first, end=" ")
        first, next = next, first + next
    print("")


if __name__ == "__main__":
    #Function Call
    print_message("Hello")
    sum_of_numbers(2)
    check_even_odd(10)
    check_even_odd(11)
    reverse_string("rahul")
    largest_of_three_numbers(10, 9, 5)
    largest_of_three_numbers(8, 11, 7)
    largest_of_three_numbers(6, 2, 12)
    largest_of_three_numbers(2, 2, 2)
    count_vowels("Rahul")
    count_vowels("rahul")
    count_vowels("aeiou")
    table(5)
    table(10)
    factorial_of_number(4)
    factorial_of_number(6)
    check_palindrome("Rahul")
    check_palindrome("AbA")
    fibonacci_series(10)
