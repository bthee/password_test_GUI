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
                            pady=10,
                            anchor="nw",
                            justify="left",
                            bg="lightgray"
                            )
        
        self.test_button = Button(self.root,
                                  text="Check your password!",
                                  command=self.display_output,
                                  font=("", 12, "bold")
                                  )


        self.welcome.place(x=0, y=0, width=800, height=50)
        self.instruction.place(x=0, y=80, width=800, height=50)
        self.user_input.place(x=200, y=200, width=400, height=50)
        self.output.place(x=50, y=280, width=700, height=175)
        self.test_button.place(x=285, y=500, width=230, height=50)

        self.root.mainloop()


    def display_output(self):
        input_text = self.user_input.get()
        length = len(input_text) >= 12
        number = any(char.isnumeric() for char in input_text)
        upper_ch = any(char.isupper() for char in input_text)
        lower_ch = any(char.islower() for char in input_text)
        special_ch = any(not char.isalnum() for char in input_text)

        count = sum([length, number, upper_ch, lower_ch, special_ch])

        if count == 5:
            output_text = "Your password is strong!\n"
        elif count == 4 and length:
            output_text = "Your password is good! Here is an improvement you should make.\n"
        elif count == 4 and not length:
            output_text = "Your password would be strong if you increase its length to 12 characters.\n"
        elif count == 3 and length:
            output_text = "Your password is okay. Here are some improvements you should make.\n"
        elif count == 3 and not length:
            output_text = "Your password is weak! You should make the following improvements!\n"
        elif count <= 2:
            output_text = "Your password is very weak! You should make the following improvements!\n"
        
        imp_length = "- Increase the length of your password to at least 12 characters.\n"
        imp_num = "- Include at least one number character like '1, 2, 3 ...'\n"
        imp_up = "- Include at least one uppercase character like 'A, B, C ...'\n"
        imp_low = "- Include at least one lowercase character like 'a, b, c ...'\n"
        imp_sp = "- Include at least one special character like '@, !, $ ...'\n"

        if not length and count <= 3:
            output_text += imp_length
        if not number:
            output_text += imp_num
        if not upper_ch:
            output_text += imp_up
        if not lower_ch:
            output_text += imp_low
        if not special_ch:
            output_text += imp_sp
        
        self.output.config(text=output_text)


def main():
        win = Window(800, 600)


if __name__ == "__main__":
     main()