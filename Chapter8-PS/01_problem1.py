def greatest():
    
    num1 = int(input("Enter the first no."))
    num2 = int(input("Enter the first no."))
    num3 = int(input("Enter the first no."))

    list = [num1, num2, num3] ; 

    great = max(list) ; 

    print("The highest no. is :", great) ; 

    return great ; 


a =  greatest()
print(a) ; 