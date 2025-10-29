i = 0
while i < 5 :
    print(f"{i} is less than 5")
    i = i + 1

def sum_of_squares_upto_limit(limit):
    i = 1
    sum = 0
    while i * i <= limit:
        sum += i * i
        i += 1
    return sum

def sum_of_cubes_upto_limit(limit):
    i = 1
    sum = 0
    while i * i * i <= limit:
        sum += i * i * i
        i += 1
    return sum

def get_number_of_digits(number):
    number_of_digits = 0
    if number < 1:
        return -1
    if number == 0:
        return 1
    while number > 0:
        #print (f"\nNumber  = {number}")
        number = number // 10
        number_of_digits = number_of_digits + 1
    return number_of_digits
    

def test_break_with_for_loop(number):
    print("\ntest_break")
    for i in range(1, number+1):
        if i == 5:
            break
        print(f"{i} ", end = " ")
    print(f"\non {i} ")
        
def test_continue_with_for_loop(number):
    print("\ntest_continue")
    for i in range(1, number+1):
        if i % 2 == 0:
            print(f",skipping {i}")
            continue
        print(f"{i}", end = " ")
    print("")

def test_break_with_while_loop(number):
    print("\ntest_break_with_while_loop")
    i = 0
    while i < number:
        if i == 5:
            print(f"Break on {i}")
            break
        i = i + 1
        

def test_continue_with_while_loop(number):
    print("\ntest_continue_with_while_loop")
    i = 1
    while i < number+1:
        if i % 2 == 0:
            print(f",skipping {i}")
            i = i + 1
            continue
        print(f"{i} ", end = "")
        i = i + 1
    print("")
    

print("\nsum_of_squares_upto_limit =", sum_of_squares_upto_limit(10))  # Output: 55
print("\nsum_of_cubes_upto_limit =", sum_of_cubes_upto_limit(10))  # Output: 55
number_of_digits = get_number_of_digits(123)
print("")
print(f"Number of digit = {number_of_digits}")
test_break_with_for_loop(10)
test_continue_with_for_loop(10)
test_break_with_while_loop(10)
test_continue_with_while_loop(10)


