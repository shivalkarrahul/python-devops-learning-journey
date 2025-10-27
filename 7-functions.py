#Function Definition
def print_function():
    print("Hello from print_function()!!")


#Function Call
print_function()


def input_to_function(number_of_times):
    print("Number of Times = ", number_of_times)
    for i in range(number_of_times):
        print(i, "Times")

input_to_function(6)          


def parameter_function(parameter1, parameter2):
    print("Parameter 1=", parameter1)
    print("Parameter 2=", parameter2)

parameter_function(1, 2)

def add_two_numbers(number1, number2):
    addition = number1 + number2
    return addition
result = add_two_numbers(10, 5)
print("Addition = ", result)

for i in range(result):
    print("i = ", i)


def cube_of_number(number):
    return number*number*number

cube = cube_of_number(3)
print("Cube = ", cube)

def calculate_third_angle(first_angle, second_angle):
    third_angle = 180 - (first_angle + second_angle)
    return third_angle
result_third_angle = calculate_third_angle(50, 100)
print("Third Angle = ", result_third_angle)


#Calculate the Sum of Squares of First n Even Number
def sum_of_squares(n):
    sum = 0
    for i in range(1, n+1):
        sum =sum + (2*i)*(2*i)
    return sum
input = 5
sum = sum_of_squares(input)
print("Sum of Squares of First", input ,"Even Number = ", sum)


def function_with_default_parameter_value(msg="Hello", number_of_times=5):
    for i in range(number_of_times):
        print(msg)
function_with_default_parameter_value() #No Arguments, will use default values
function_with_default_parameter_value("Hi", 10) #With Arguments



def calculate_factorial(n):
    factorial = 1
    for i in range(1, n+1):
        factorial = factorial * i
    return factorial
input = 5
result_fact = calculate_factorial(input)
print("Factorial of", input ," = ", result_fact)



