def factorial(n):
    fact = 1 ; 
    for i in range(1, n+1):
        fact = fact * i
    print("The factorial is :", fact) ; 

def fact(n):
    if(n ==1 or n==0):
        return 1 ; 
    return n * fact(n-1)


n = int(input("Enter the no. :"))
factorial(n) ; 

print(fact(5))

