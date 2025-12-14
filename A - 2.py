import random
option=["Rock","Paper","Scissors"]
user_choice=input("Enter your choice (Rock, Paper, Scissors): ")
computer_choice=random.choice(option)
print(f"Computer Choice: {computer_choice}")
print(f"Your choice: {user_choice}")

if user_choice==computer_choice :
    print("Its a tie")
elif user_choice=="Rock" and computer_choice=="Scissors":
    print("Rock Smashes Scissors! You Win!")

elif user_choice=="Paper" and computer_choice=="Rock":
    print("Paper covers rock! You win!")

elif user_choice=="Scissors" and computer_choice=="Paper":
    print("Scissors cut paper! You Win!")

elif user_choice=="Scissors" and computer_choice=="Rock":
    print("Rock Smashes Scissors! Computer Wins! ")

elif user_choice=="Rock" and computer_choice=="Paper":
    print("Paper covers Rock! Computer Wins!")

elif user_choice=="Paper" and computer_choice=="Scissors":
    print("Scissors cut paper! Computer Wins! ")