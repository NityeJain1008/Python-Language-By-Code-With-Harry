class employee:
    def showinfo(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

# class programmer:
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")

#     def showlanguage(self):
#         print(f"The name is {self.name} and the language is {self.language}")

    
class programmer(employee):
    company = "ITC Infotech"
    def showlanguage(self):
        print(f"The name is {self.name} and the language is {self.language}")

a = employee()
b = programmer()

a.name = "NItye" ; 
a.salary = "120K"

print(b.company)
a.showinfo()

