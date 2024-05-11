class Student :
    No_of_leaves = 10
    x= "BEST"
    
    def __init__(self, name, std, sec ):
        self.name = name
        self.std = int(std)
        self.sec = sec
    
    def detail(self):
        return "Student's name is {}, studies in standard {}, in section {}".format(self.name, self.std, self.sec)
    
    @classmethod
    def insert(cls, all):                              #alternate constructor
        return cls(*all.strip().split())        
    
    @staticmethod
    def warning():                                        #Since it doesn't depend on object and class and will remain same, 
        print("Warning : Fees will not be refunded.")            #no matter what, that's why its called static method
    
    def __add__(self, other):                    #This is Operator Overloading and ofcourse dunder method too
        return self.std + other.std
    
    def __truediv__(self, other):                #This is Operator Overloading
        return self.std/other.std
    
    def __and__(self, other):                    #This is Operator Overloading
        return self.sec == other.sec
    
    def __repr__(self):                          #its simply dunder method
        return f"Student('{self.name}', {self.std}, '{self.sec}') or Student('{self.name} {self.std} {self.sec}')"
    
    def __str__(self):                          ### IMPORTANT : If str is not present but repr is present then program   
        return self.detail()                    ###             Calls repr method when str called but not vice versa
                                                ##              
    
Shrey = Student("Shrey", 10, "B")
Rudra = Student.insert("Rudra 10 B")

print("Add: ", Shrey+Rudra)
print("Divide: ", Shrey/Rudra)
print("Check: ",Shrey & Rudra)
print("repr: ",repr(Shrey))
print("str: ",str(Rudra))
print(Shrey)                     ### Previously it gives address of instance but now it gives str method also if str not 
                                 ### present then gives repr
    