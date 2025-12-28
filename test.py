questions = ("How many elements are in the periodic table?: ",
             "Which animals lays the largerst eggs: ",
             "What is the most abundant gas in Earth's atmostphere?: ",
             "How many bones are in the human body?: ",
             "Which planet in the solar system is the hottest?: ")

options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
           ("A. Nitrogetn", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
           ("A. 206", "B. 207","C. 208","D. 209"),
           ("A. Mercury","B. Venus", "C.Earth", "D.Mars"))
answers = ("C","D","A","A","B")
guesses = []
score = 0
question_num = 0
for question in questions:
    print("----------------")
    print(question)
    for option in options[question_num]:
        print (option)

    guess = input("Enter your answer (A,B,C,D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("You got it!")
    else:
        print("Sorry, you did not answer")
        print(f"The option {answers[question_num]} is the correct answer")
    question_num += 1
    print("-------------------")
    print("      RESULTS      ")
    print("--------------------")
    print("anwers: " ,end="")
for answer in answers:
    print(answer,end=" ")
print("guesses: ",end="")
for guess in guesses:
    print(guess,end=" ")
print()
score = int (score / len(questions)*100)
print(f"Your Score is : {score}%")

