class employee:
    # name = "Nitye"
    language = "Python"
    salary = "120K"

    def getInfo(self):
        print("The language is", self.language, "And the salary is", self.salary) ; 

    def greet(self):
        print("Good Morning !!")

Nitye = employee()
Nitye.name = "nitye"
Nitye.language = "JAVA"
print("Name, language and salary are :", Nitye.name, Nitye.language, Nitye.salary)

Devansh = employee()
Devansh.name = "Devansh Bindal"
print(Devansh.name, Devansh.language, Devansh.salary)


print(employee.language)

Nitye.getInfo()
Nitye.greet()