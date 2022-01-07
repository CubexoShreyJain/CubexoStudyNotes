from abc import ABC, abstractmethod

class Shape(ABC):                #ABC bole toh abstracat base class
    @abstractmethod              #necessary decorator
    def area(self):
        return 0
    
class Rectangle(Shape):
    def __init__(self,length, breadth):
        self.length = length
        self.breadth = breadth
        
    def area(self):                           #Shows error witihout this function
        return self.length*self.breadth
        
Box  = Rectangle(10,5)
print(Box.area())
# adsf = Shape()                      # Error : Can't initiate abc directly 