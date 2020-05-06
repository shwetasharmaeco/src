# limited guess game
from random import randint
name = input("What is your name > ").title()
print ("Hi" + " " + name)

print ("I am thinking a number between 1 to 100 \n Can you guess it?")


comp_num= randint(1,101)
comp_num_lst=[]
count=1

while True:
    try:
        guess= int(input("What is your guess > "))
        if guess==comp_num :
            comp_num_lst.append(count)
            print (comp_num_lst)
            print(f"Well done {name}! You found my number in {count} tries")
            if count==min(comp_num_lst):
                    print("CONGRATULATIONS!, you have the lowest score")

        elif guess<1 or guess>100:
            print("Only numbers between 1-100 allowed")

        elif guess < comp_num  :
            print("Your guess is too low, try again.")
            if count>5:
                print("Sorry! You are out of guesses")
            else:
                count+=1
                continue
               
        elif guess > comp_num:
            print("Your guess is too high, try again.")
            if count>5:
                print("Sorry! You are out of guesses")
            else:
                count+=1
                continue
                
        restart = "Z" 
       
        while (restart != "Y" and restart != "N"):
            restart=input("would you like to play again: Y or N> ").upper()
            

        if  restart=="Y":
            count=1
            print("Okay! I am ready with a new number")
            comp_num= randint(1,101)
            continue
            
        
        elif restart=="N":
            print("Thanks for playing, see you next time")
            break   
        elif count>5:
            print("Sorry! you are out of guesses :(")
            continue      
    except:
        print("Only numbers between 1-100 allowed")

    

