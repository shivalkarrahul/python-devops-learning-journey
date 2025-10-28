file_to_read = "2-operators-and-expressions.py"
mode = "r"
print("\nReading file", file_to_read ,"in", mode ,"mode")
with open(file_to_read, mode) as file:
    content = file.read()
    print(content)

print("\nReading file", file_to_read ,"in", mode ,"mode line by line" )
with open(file_to_read, mode) as file:
    for linenumber, line in enumerate(file, start=1):
        print("line = ", linenumber ,": ", line.strip())


file_to_write = "test_file_to_write.txt"
mode = "w"
print("\nWriting to file", file_to_write ,"in", mode ,"mode")
with open(file_to_write, mode) as file:
    file.write("Test")

with open(file_to_write, "r") as file:
    content = file.read()
    print(content)


file_to_append = "test_file_to_append"
mode ="a"
print("\nAppending to file", file_to_write ,"in", mode ,"mode")
with open(file_to_append, mode) as file:
    file.write("Test")
with open(file_to_append, "r") as file:
    content = file.read()
    print(content)


import os
check_file_exists = "no_file.txt"
if os.path.exists(check_file_exists):
    print("File", check_file_exists ,"exists")
else:
    print("File", check_file_exists ," does not exist")


