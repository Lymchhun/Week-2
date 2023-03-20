import random

PC = random.randint(1,3)
print("\nEnter 1 to choose rock")
print("\nEnter 2 to choose paper")
print("\nEnter 3 to choose scissors")
Users = int(input("\nEnter Your option here: "))
if PC==1 and Users ==1 or PC==2 and Users == 2 or PC ==3 and Users == 3:
    print("\n draw")
elif PC==1 and Users==2 or PC==2 and Users ==3 or PC==3 and Users == 1:
    print("\n Users WIN")
elif PC==2 and Users==1 or PC==3 and Users ==2 or PC==1 and Users == 3:
    print("\n PC wiin")
else:
    print("\n Invalid Input")
print("Users: ",Users)
print("PC: ", PC)