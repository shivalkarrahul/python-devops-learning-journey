print ("Table upto 10")
table = 0
for i in range(1,10):
    print("table of ", i)
    for j in range(1, 10):
        print ("i = ", i ,"j = ", j)
        
        table = i*j
        print ("table", table)


print ("Print Square Pattern")
for i in range(1, 5):
    for j in range(1, 5):
        print("*", end=" ")
    print()    

print ("Triangle Pattern")
for i in range(1, 5):
    for j in range (i):
        print("*", end=" ")
    print()
    

