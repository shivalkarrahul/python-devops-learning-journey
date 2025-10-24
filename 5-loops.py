print("First for loop: range with start and end")
for i in range(1, 11):
    print(i)

print("Second for loop: range with start, end and step")
for j in range(1, 11, 2):
    print(j)

print("Third for loop: range with end")
for k in range(11):
    print(k)

print("Fourth for loop: range with start and end and print square of each number ")
for l in range(1, 11):
    print(l*l)    

print("Fifth for loop: range with start and end and sum of range")
sum = 0
for m in range(1, 11):
    sum = sum + m
    print("Sum of numbers from 1 to", m ,"=", sum)

print("Sixth for loop: range with start and end and table of 5")
for i in range(1, 11):
    print("5 * ", i ,"=", 5*1)




