class employee:
    name = "Default name"
    salary = "120K"
    def showinfo(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

class coder:
    language = "Python"
    def printlanguage(self):
        print(f"The language is {self.language}")
    
class programmer(employee, coder):
    company = "ITC Infotech"
    name = "Default name"
    language = "Python"
    def showlanguage(self):
        print(f"The name is {self.name} and the language is {self.language}")

a = employee()
b = programmer()

a.name = "NItye" ; 
a.salary = "120K"

print(b.company)
a.showinfo()

# b.name = "Nitye"
# b.salary = "120K"

b.showlanguage()
b.showinfo()
