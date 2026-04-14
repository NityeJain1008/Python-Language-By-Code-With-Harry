import random

'''
1 for snake 
2 for water
3 for gun
'''

dict = {1:"Snake", 2:"Water", 3:"Gun"} ; 

computer_choice = random.choice([1, 2, 3])
your_choice = int(input("Enter 1 for snake " \
"2 for water " \
"3 for gun ")) ; 
 
you = dict[your_choice] ; 
computer = dict[computer_choice] ; 

print("Computeer chooses", computer)
print("YOu choose", you) ;

if (computer == you): 
    print("It's a draw")

elif(your_choice == 1 and computer_choice == 2) or (your_choice == 2 and computer_choice == 3) or (your_choice == 3 and computer_choice == 1): 
    print("YOU WIN")

else:                                
    print("YOU LOOSE")

