message = "hello world"
print(f"Type of message = {type(message)}")
print(f"Character at index 6 = {message[6]}")
for c in message:
    print(f"Character = {c}")

string1 = "hello"
string2 = "Hello"

if string1.lower() == string2.lower():
    print(f"String1 and String2 -> {string1.lower()} {string2.lower()} are equal")
else:
    print(f"String1 and String2 -> {string1.lower()} {string2.lower()} are  not equal")


character = "a"
vowel_string = "aeiouAEIOU"
if character in vowel_string:
    print(f"Character {c} is a vowel")
else:
    print(f"Character {c} is not a vowel")


def check_vowel(ch):
    vowel_string = "aeiouAEIOU"
    if ch in vowel_string:
        return True 
    else:
        return False
vowel = check_vowel("p")
print(f"Is Character {c} a vowel ? {vowel}")


def count_uppercase_letters(string: str) -> str:
    count = 0
    for c in string:
        if c.isupper():
            count = count + 1
    print(f"Number of uppercase letters in {string} = {count}")

count_uppercase_letters("RahUL")
count_uppercase_letters("RAHUl")