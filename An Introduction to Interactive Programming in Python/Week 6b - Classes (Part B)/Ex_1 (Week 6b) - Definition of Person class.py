# Implementation of Person class


#################################################
# Student adds code where appropriate

# definition of Person class
class Person:
    
    def __init__(self, first, last, year):
        self.first_name = first
        self.last_name = last
        self.birth_year = year
        
    def full_name(self):
        full_name = self.first_name + " " + self.last_name
        return full_name
    
    def age(self, current_year):
        return current_year - self.birth_year
    
    def __str__(self):
        string = "\nFirst Name : " + self.first_name + "\nLast Name  : " + self.last_name + "\nBirth year : " + str(self.birth_year)
        return string
 
    
###################################################
# Testing code

joe = Person("Joe", "Warren", 1961)
john = Person("John", "Greiner", 1966)
stephen = Person("Stephen", "Wong", 1960)
scott = Person("Scott", "Rixner", 1987)  

print joe
print john
print stephen
print scott

print joe.age(2013)
print scott.age(2013)   # yeah, right ;)
print john.full_name()
print stephen.full_name()


####################################################
# Output of testing code - results of __str__ method may vary

#The person's name is Joe Warren. Their birth year is 1961
#The person's name is John Greiner. Their birth year is 1966
#The person's name is Stephen Wong. Their birth year is 1960
#The person's name is Scott Rixner. Their birth year is 1987
#52
#26
#John Greiner
#Stephen Wong