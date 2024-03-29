from tkinter import Tk, Label, Entry, Button

class Window:
    def __init__(self, width, heigth):
        # Initialize the window
        self.root = Tk()
        self.root.title("Password Strength Test")
        self.root.geometry(f"{width}x{heigth}")
        self.root.configure(bg="white")

        # Create labels, entry, and buttons
        # Set their properties and bind events
        self.welcome_label = Label(self.root,
                             text="Welcome!",
                             font=("", 16),
                             bg="lightblue"
                            )
        
        self.instruction_label = Label(self.root,
            text="To test your password, just enter it in the field below and press 'enter' or hit the test button.",
            font=("", 12),
            padx=10,
            anchor="w",
            bg="white"
            )

        self.user_input = Entry(self.root,
                                font=("", 14),
                                show="*"
                                )
        
        self.user_input.focus_set()
        
        self.user_input.bind("<Return>", self.display_output)
        self.user_input.bind("<Control-KeyRelease-a>", self.select_all)
        self.user_input.bind("<Control-x>", self.cut_text)
        self.user_input.bind("<Control-c>", self.copy_text)
        self.user_input.bind("<Control-v>", self.delete_for_paste)

        self.show_hide_button = Button(self.root,
                                       text="Show/Hide",
                                       font=("", 12, "bold"),
                                       command=self.toggle_show_hide
                                      )
        
        self.clear_button = Button(self.root,
                                   text="Clear",
                                   font=("", 12, "bold"),
                                   command=self.clear_entry)

        self.output_field = Label(self.root,
                                  font=("", 12),
                                  padx=10,
                                  pady=10,
                                  anchor="nw",
                                  justify="left",
                                  bg="lightgray"
                                )
        
        self.check_pw_button = Button(self.root,
                                      text="Check your password!",
                                      command=self.display_output,
                                      font=("", 12, "bold")
                                    )


        self.welcome_label.place(x=0, y=0, width=800, height=50)
        self.instruction_label.place(x=0, y=80, width=800, height=50)
        self.user_input.place(x=200, y=160, width=400, height=50)
        self.output_field.place(x=50, y=240, width=700, height=175)
        self.check_pw_button.place(x=285, y=460, width=230, height=50)
        self.show_hide_button.place(x=625, y=160, width=125, height=50)
        self.clear_button.place(x=625, y=460, width=120, height=50)

        # Display the window
        self.root.mainloop()


    def display_output(self, event=None):
        # Evaluate password strength based on criteria
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
        
        self.output_field.config(text=output_text)

    def select_all(self, event=None):
        self.user_input.select_range(0, 'end')
    
    def cut_text(self, event=None):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.user_input.get())
        if self.user_input.selection_present():
            self.user_input.delete("sel.first", "sel.last")
    
    def copy_text(self, event=None):
        self.user_input.selection_clear()
        self.root.clipboard_clear()
        self.root.clipboard_append(self.user_input.get())
    
    def delete_for_paste(self, event=None):
        if self.user_input.selection_present():
            self.user_input.delete("sel.first", "sel.last")

    def toggle_show_hide(self):
        if self.user_input['show'] == '*':
            self.user_input['show'] = ''
        else:
            self.user_input['show'] = '*'

    def clear_entry(self):
        self.user_input.delete(0, "end")
        self.output_field.config(text="")

def main():
        # Initialize window object
        win = Window(800, 600)


if __name__ == "__main__":
     main()