print(type(5))
print(type(2.5))
print(type("Rahul"))
print(type(True))
print(type(None))
print(type([1,2,3]))
print(type((1, 2, 3)))
print(type({1, 2, 3}))
print(type({'name': 'Rahul'}))
print(type(5+2j))
print(type(5j))
print(type(range(5)))


def calculate_simple_interest(principal, interest, duration):
    total_amount = principal + (principal * interest * 0.01 * duration)
    return total_amount
print(calculate_simple_interest(900000, 7.4, 2)) 

i = 1
i = i + 1
print("i = ", i)

j = 1
j += 1 #Shorthand Operator
print("j = ", j)


print(5 ** 3) #Exponentiation operator
print(pow(5, 3))


i = 2
print(type(i))

i = i / 1.5
print(type(i))


i = 5.6
print(int(i))

j = 5
print(float(j))

k = 5.6
print(round(k))

l = 5.4
print(round(l))


print (4.5 - 3.2)


import decimal

value1 = decimal.Decimal('4.5')
value2 = decimal.Decimal('3.2')
result = value1 - value2    
print(result)

#from math import e
#from math import pi
import math

print(math.e)
print(math.pi)

print(True)
print(False)

print(True and False)

i = 10
print(i < 5)
print(i <= 5)


def can_access_library(age):
    if age < 18:
        return False
    if age >= 18:
        return True
permission = can_access_library(15)
print(permission)
permission = can_access_library(20)
print(permission)

def is_eligible_for_race(max_speed):
    if max_speed < 200:
        return False
    if max_speed >= 200:
        return True
    
result_speed = is_eligible_for_race(150)
print(result_speed)
result_speed = is_eligible_for_race(250)    
print(result_speed)