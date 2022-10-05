
questions = {
    "what is the color of an apple?\n(a)black or blue.\n(b)red or green.\n(c)pink or white.": "b",
    "what is the sum of 20+35-15?\n(a)25.\n(b)65.\n(c)40.": "c",
    "Does cat have nine live?\n(a)True.\n(b)false.\n(c)Maybe.": "b",
    "A Noun is a part of speech?\n(a)false.\n(b)maybe.\n(c)ture": "c",
    "which of this is not a football club?\n(a)chelsea.\n(b)man u.\n(c)closeup": "c"
    }

game_count = 5
user_life = 3
game_prompt = """hello user
press s or start to start the game
press q or quit to quit the game
press h or help to recive help
"""
game_rules = """
you have 3 chances and 5 question
Good luck!
"""

game_questions = None
print(game_prompt)
while True:
    decision = input("enter a command: ").lower()
    if decision == "h" or decision == "help":
        print(game_rules)
    elif decision =="q" or decision == "quit":
        print("Thanks for playing \nGood bye ('-')")
        break
    elif decision == "s" or decision == "start":
        score = 0
        for question in questions.keys():
            print(question)
            answer = input("Enter answer: ")
            if answer == questions[question]:
                print("Correct Answer")
                score += 1
            else:
                print("wrong answer")
        print(f"You scored {score}")
    else:
        print("invaild input")
