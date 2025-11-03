test_list = ["a", "b", "d", "c"]
test_set = {"b", "b", "d", "c"}

test_list.append("e")
test_set.add("a")

print(test_list)
print(test_set)



unpack_list = test_list
unpack_set = test_set

print(*unpack_list)
print(*unpack_set)

