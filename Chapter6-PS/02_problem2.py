s1 = int(input("Enter the marks of subject 1"))
s2 = int(input("Enter the marks of subject 2"))
s3 = int(input("Enter the marks of subject 3"))

total = (s1 + s2 + s3)/3 ; 

if(s1 >= 33 and s2 >= 33 and s3 >= 33 and total >= 40):
    print("Congrats !! You passed in all subjects" )

else:
    print("sorry ! you failed !!")

