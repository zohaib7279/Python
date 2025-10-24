import random
item_list = ["Rock","Paper","Scissor"]
user_choise = input("Enter your move = Rock, Paper, Scissor = ")
comp_choise = random.choice(item_list)
print(f"User choice = {user_choise}, computer choice = {comp_choise}")
if user_choise == comp_choise:
    print("both Chooses same")
elif user_choise == "Rock":
    if comp_choise == "Paper":
        print("Paper cover Rock = Computer")
    else:
        print("Rock smashes Scissor = You win")
elif user_choise == "Paper":
    if comp_choise == "Scissor":
        print("Scissor cuts paper, Computer Win")
    else:
        print("Paper cover Rocks,You Win")
elif user_choise == "Scissor":
    if comp_choise == "Paper":
        print("Scissor cuts paper, You Win")
    else:
        print("Rock smashes scissor, Computer Win")