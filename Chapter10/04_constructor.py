class employee:
    # name = "Nitye" ; 
    language = "Python" ; 
    salary = "120K" ; 

    def getInfo(self):
        print("The language is", self.language, "And the salary is", self.salary) ; 

    def greet(self):
        print("Good Morning !!") ; 

    def __init__(self, name, salary, language):
        self.name = name ; 
        self.language = language ; 
        self.salary = salary ; 


harry = employee("Harry", "120K", "Python") ; 

print(harry.name, harry.language, harry.salary) ; 
