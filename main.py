from tkinter import Tk, Label, Entry, Button

class Window:
    def __init__(self, width, heigth):
        self.root = Tk()
        self.root.title("Password Strength Test")
        self.root.geometry(f"{width}x{heigth}")
        self.root.configure(bg="white")

        self.welcome = Label(self.root,
                             text="Welcome!",
                             font=("", 16),
                             bg="lightblue"
                            )
        
        self.instruction = Label(self.root,
                                 text="To test your password, just enter it in the field below and press 'enter' or hit the test button.",
                                 font=("", 12),
                                 padx=10,
                                 anchor="w",
                                 bg="white"
                                )

        self.user_input = Entry(self.root,
                           font=("", 14)
                           )

        self.output = Label(self.root,
                            font=("", 12),
                            padx=10,
                            anchor="w",
                            bg="lightgray"
                            )
        
        self.test_button = Button(self.root,
                                  text="Check your password!"
                                  )


        self.welcome.place(x=0, y=0, width=800, height=50)
        self.instruction.place(x=0, y=80, width=800, height=50)
        self.user_input.place(x=200, y=200, width=400, height=50)
        self.output.place(x=100, y=280, width=600, height=200)
        self.test_button.place(x=300, y=500, width=200, height=50)

        self.root.mainloop()


    def get_input(self):
         self.output.config(text= self.user_input.get(), 
                            font= ('Helvetica 13')
                            )


def main():
        win = Window(800, 600)


if __name__ == "__main__":
     main()