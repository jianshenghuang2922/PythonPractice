import random 

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num,highest_num)

guesses = 0
is_running = True

print("Python Number Guessing Game")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:
    guess =(float) (input ("Enter your guess:"))
    if guess == answer:
        print("Your answer is correct")
        is_running = not is_running
      
    elif guess > answer:
        print("Your guess is too big")
        
    else:
        print("Your guess is too small")
    guesses += 1
print(f"Your total guess numbers is {guesses}")   
