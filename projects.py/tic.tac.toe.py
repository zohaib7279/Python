import tkinter as tk
from tkinter import messagebox
def check_winner():
    for combo in [[0,1,2],[3,4,5],[6,7,8]]:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] !="":
            buttons[combo[0]].config(bg= "green")
            buttons[combo[1]].config(bg= "green")
            buttons[combo[2]].config(bg= "green")
            messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[combo[0]]['text']} wins!")
            root.quit()
           
def button_click(index):
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = curent_palyer
        check_winner()
        toogle_player()

def toogle_player():
    global curent_palyer
    curent_palyer = "X" if curent_palyer == "O" else "O"
    label.config(text=f"player {curent_palyer}'s turn")

root = tk.Tk()
root.title("Tic-Tac-Toe")
buttons = [tk.Button(root, text="", font=("normal",25), width=6 , height=2 , command=lambda i=i:  button_click(i))for i in range(9)]
for i,button in enumerate(buttons):
    button.grid(row=i //3 , column=i % 3)
curent_palyer ="X"
winner = False
label = tk.Label(root , text=f"Player {curent_palyer}'s turn " , font=("normal" , 16))
label.grid(row=3 , column=0, columnspan=3)
root.mainloop()