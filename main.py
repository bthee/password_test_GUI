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
        
        self.welcome.place(x=0, y=0, width=800, height=50)
        self.instruction.place(x=0, y=80, width=800, height=50)

        self.root.mainloop()


def main():
        win = Window(800, 600)


if __name__ == "__main__":
     main()