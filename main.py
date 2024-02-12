from tkinter import Tk, Label, Entry, Button

class Window:
    def __init__(self, width, heigth):
        self.root = Tk()
        self.root.title("Password Strength Test")
        self.root.geometry(f"{width}x{heigth}")
        self.root.configure(bg="white")