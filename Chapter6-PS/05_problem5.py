list = [1, 2, 3, 4, 5, 6] ; 

a = int(input("Enter the no. to find :")) ; 

if(a in list):
    print("found at index", list.index(a)) ; 
else:
    print("No. does not found")

