class Student:

    def __init__(self, fname, lname, id, energy_level=10):
        self.fname = fname
        self.lname = lname
        self.id = id
        self.energy_level=energy_level

    def __str__(self):
        return self.lname + ":" + self.id
    
    def greeting(self,fname,lname): 
        return f"{self.fname},{self.lname} says Hi"

    def take_exam(self,energy_level):
        self.energy_level-1
    
    def get_energy_level(self,energy_level):
        return self.energy_level
        