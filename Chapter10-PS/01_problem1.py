class programmer:
    company = "microsoft"
    salary = "120K"
    language = "Python"

    def __init__(self, name, company, salary, language):
        self.name = name ; 
        self.company = company ; 
        self.salary = salary ; 
        self.language = language ; 

    def getInfo(self):
        print(self.name, self.company, self.salary, self.language)

# nitye = programmer()
# nitye.name = "Nitye"
# print(nitye.name, nitye.company, nitye.salary) ; 

devansh = programmer("devansh", "microsof", "120K", "Python") ; 
devansh.getInfo()
# programmer.getInfo(devansh)