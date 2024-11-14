import random
user_value=int(input("enter user value 0 is for rock ,1 is for paper, 2 is for scissors:"))
if user_value >=3 or user_value <0:
    print("you enter a invalid number")
else:
     computer_value=random.randint(0,2)
     print(f"computer value:{computer_value}")
     if computer_value == user_value :
        print("draw")
     elif user_value==0 and computer_value==2:
                print("user_value wins")
     elif user_value==2 and computer_value==0:
                   print("computer_value wins")
     elif computer_value > user_value :
            print("computer wins")
     elif user_value >computer_value :
                print("user wins")



