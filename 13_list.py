#help(list)
marks = [10, 20, 30, 40]
marks.append(50)
marks.insert(3, 35)
marks.remove(40)
print(marks)
total = sum(marks)
print(f"Total marks = {total}")

lenght = len(marks)
average = total / lenght
print(f"Average Marks = {average} ")


#help(list.empty())

def has_greater_element(numbers: list, value: int) -> bool:
    print(f"List  = {numbers}")
    print(f"Value = {value}")
    length = 0      
    length = len(numbers)
    print(f"Length of List = {length}")

    if lenght <= 0:
        print(f"List is emptry")
        return False
    else:
        for i in numbers:
            if i > value:
                return True
        return False

result = has_greater_element([10,2,3], 1)
print(f"Result = {result}")

def are_sums_equal(list1: list, list2: list):
    sum1 = sum(list1)
    sum2 = sum(list2)

    if not list1 or not list2:
        print(f"Either list1 or list2 is empty, where list1 = {list1} and list2 = {list2}")
        return False

    if sum1 == sum2:
        print(f"Sum of two list are equal, where list1 = {list1} and list2 = {list2}")
        return True
    elif sum1 > sum2:
        print(f"Sum of list is greater that sum of list 2, where list1 = {list1} and ")
        return False

    elif sum1 < sum2:
        print(f"Sum of list is less that sum of list 2, where list1 = {list1} and list2 = {list2}")
        return False    


result = are_sums_equal([], [3,2,1])
print(f"Result = {result}")


list_strings = ["one", "two", "three"]
reversed_list = list_strings.reverse()
print(f"Reversed List in place = {list_strings}")

list_strings = ["one", "two", "three"]
for number in reversed(list_strings):
    print(number, end = " ")
print("")

print(f"Reversed Numbers = {list(reversed(list_strings))}")


list_digit = [1, 2 ,5, 4]
list_digit.sort()
print(f"Sorted List in place = {list_digit}")

list_digit = [1, 2 ,5, 4]
print(f"Sorted List = {sorted(list_digit)}")
print(f"Original List = {list_digit}")

