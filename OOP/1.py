# class
class Person:
    pass
    # class attributes
    
    #constructor (yapıcı method)
    def __init__(self,name,year):
    # object attributes
        self.name = name
        self.year = year
    
      
    # instance methods
    def calculateAge(self):
        return 2020-self.year

#object
p1 = Person('erdi',1996)
p2 = Person('ahmet',1999)
print(f'name : {p1.name} year : {p1.year}')
print(f'name : {p2.name} year :  {p2.year}') 

print(f'my name is {p1.name} and age {p1.calculateAge()}')
print(f'my name is {p2.name} and age {p2.calculateAge()}')


