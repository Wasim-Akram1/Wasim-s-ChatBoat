from tkinter import *

# main chatbot window
root = Tk()
root.title("Chatbot")

#colors and fonts
BG_GRAY = "#abb2b9"
BG_COLOR = "#87CEEB"
TEXT_COLOR = "#EAECEE"
FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

# user input and bot responses
def send():
    user_input = e.get().lower()
    response = ""

    if user_input == "hello":
        response = "Hi there, how can I help?"
    elif user_input in ["hi", "hii", "hiiii"]:
        response = "Hi there, what can I do for you?"
    elif user_input == "how are you":
        response = "Fine! And you?"
    elif user_input=="are you a roboat?":
        response="Yes, I am a roboat, but i am a good one,How can i help you."
    else:
        response="I dont have enough Knowledge"
    # Add more responses here...

    # Display bot's response
    txt.insert(END, "\nBot -> " + response)
    e.delete(0, END)

# UI elements
lable1 = Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text="Welcome", font=FONT_BOLD, pady=10, width=20, height=1)
lable1.grid(row=0)

txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
txt.grid(row=1, column=0, columnspan=2)
scrollbar = Scrollbar(txt)
scrollbar.place(relheight=1, relx=0.974)

e = Entry(root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)
e.grid(row=2, column=0)

send_button = Button(root, text="Send", font=FONT_BOLD, bg=BG_GRAY, command=send)
send_button.grid(row=2, column=1)

# GUI event loop
root.mainloop()
