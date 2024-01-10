strawberry = 1000
oranges = 1978
cherries = 1980
hasAnswered = False 

print("Welcome to out shop! We have strawberries, oranges, and cherries.") #string
selection = input("what would you like to eat? ").lower()


if selection== 'strawberry' or selection == 'strawberries': 
    strawberry -=1 
    print(f"There are {strawberry} strawberries left!") #string
    hasAnswered= True 
    print("Your strawberries will arrive shortly!")#string

elif selection== 'oranges': 
    oranges-=1 
    print(f"There are {oranges} oranges left!")#string
    hasAnswered = True 
    print("Your oranges will arrive shortly!")#string


elif selection== 'cherries': 
    cherries -=1 
    print(f"There are {cherries} cherries left!")
    hasAnswered = True 
    print("Your cherries will arrive shortly!")
elif selection == 'thats all': 
        print("Thank you for shopping!")
        hasAnswered == False 
else:
    print("You bald fat man we do not have that leave now!")
    hasAnswered == False 

while hasAnswered == True:
    selection = input ("What else would you like today? ")

    if selection== 'strawberry': 
        strawberry -=1 
        print(f"There are {strawberry} strawberries left!")
        hasAnswered= True 

    elif selection== 'oranges': 
        oranges-=1 
        print(f"There are {oranges} oranges left!")
        hasAnswered = True 


    elif selection== 'cherries': 
        cherries -=1 
        print(f"There are {cherries} cherries left!")
        hasAnswered = True 
    elif selection == 'Thats all': 
        print("Thank you for shopping!")
        hasAnswered == False 
    else: 
        print("You bald fat man we do not have that leave now!")
        hasAnswered == False