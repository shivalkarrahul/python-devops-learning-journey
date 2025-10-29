#Class
class Country():
    pass

#Objects
india =  Country()
usa = Country()
germany = Country()

#Attributes
india.name = "India"
usa.name = "USA"
germany.name = "Germany"

#Print values
print(f"Name of India = {india.name}")
print(f"Name of USA = {usa.name}")
print(f"Name of German = {germany.name}")



####

class Motorbike:
    pass

honda = Motorbike()
hyundai = Motorbike()

honda.speed = 100
hyundai.speed = 150

print(f"Speed of Honda = {honda.speed}")
print(f"Speed of Hyndai = {hyundai.speed}")



###

class Book:
    pass

first_book = Book()
second_book = Book()
third_book = Book()

first_book.name = "DevOps"
second_book.name = "AWS"
third_book.name = "Python"

print(f"First Book = {first_book.name}")
print(f"Second Book = {second_book.name}")
print(f"Third Book = {third_book.name}")


###
class Dimension:
    def __init__(self, inches):
        self.feet = inches // 12
        self.inches = inches % 12

input_inches = 25
dim = Dimension(input_inches)

print(f"{input_inches} inches = {dim.feet} feet {dim.inches} inches")




class Car:
    def __init__(self, speed):
        self.speed = speed

    def increase_speed(self, how_much):
        self.speed = self.speed + how_much

    def decrease_speed(self, how_much):
        self.speed = self.speed - how_much
    
    
    

i20 = Car(100)
print(f"Speed = {i20.speed}")

i20.increase_speed(50)
print(f"Speed = {i20.speed}")


i20.decrease_speed(10)
print(f"Speed = {i20.speed}")