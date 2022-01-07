class Gamers():
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    @property
    def username(self):
        if (self.fname == None or self.lname == None):
            return "Mr_Unknown"
        return f"{self.fname}_{self.lname}"
    
    @username.setter
    def username(self,string):
        self.fname = string.split('_')[0]
        self.lname = string.split('_')[1]
        
    @username.deleter
    def username(self):
        self.fname = None
        self.lname = None   
        
a = Gamers("Shrey","Jain")
print(a.username)

a.lname = 'Chanderia'
print(a.username)

a.username = "Fuck_Off"
print(a.fname + "\t" + a.lname )

del a.username
print(a.username)