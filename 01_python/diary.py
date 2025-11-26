print("----- MCQ Application -----")

while True:
    try:
        print("This application was created by:")
        print("a) Python\tb) Java")
        print("c) HTML\td) JavaScript")

        answer = input("Enter your answer (a/b/c/d) or 'q' to quit: ")

        if answer == "q":
            print("Exiting the application. Goodbye!")
            break

        if answer == "a":
            print("Correct! This application is created using Python.")
        else:
            print("Incorrect! Please enter the correct answer.")


        print("\nWho is the founder of Python?")
        print("a) Brendan Eich\tb) James Gosling")
        print("c) Guido van Rossum\td) Tim Berners-Lee")

        answer = input("Enter your answer (a/b/c/d) or 'q' to quit: ")

        if answer == "q":
            print("Exiting the application. Goodbye!")
            break

        if answer == "c":
            print("Correct! Guido van Rossum is the founder of Python.")
        else:
            print("Incorrect! Please enter the correct answer.")


        print("\nWhich organization manages Python?")
        print("a) Microsoft\tb) Google")
        print("c) Facebook\td) Python Software Foundation")

        answer = input("Enter your answer (a/b/c/d) or 'q' to quit: ")

        if answer == "q":
            print("Exiting the application. Goodbye!")
            break

        if answer == "d":
            print("Correct! Python is managed by the Python Software Foundation.")
        else:
            print("Incorrect! Please enter the correct answer.")
        print("\nWhat is python progaraming language?")
        print("a) High-level programming language\tb) Web development language")
        print("c) Software develpment language\td) App development language")
        answer = input("Enter your answer (a/b/c/d): ")
        if answer == "a":
            print("Correct! Python is a high-level programming language.")
        else:
            print("Incorrect! Please enter the correct answer.")
        print("\nWhich language is inside Python?")
        print("a) SQL\tb) C")
        print("c) Ruby\td) JavaScript")
        answer = input("Enter your answer (a/b/c/d): ")
        if answer == "b":
            print("Correct! C is the language inside Python.")
        else:
            print("Incorrect! Please enter the correct answer.")

    except:
        print("An error occurred. Please try again.")