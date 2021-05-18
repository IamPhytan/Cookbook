import tkinter as tk


class SimpleGUI:
    def __init__(self, master) -> None:
        self.master = master
        master.title("Hello")
        master.geometry("500x200")

        # Examples of buttons
        self.b1 = tk.Button(master=root, text="My button", command=self.my_callback)
        self.b1.pack()

        self.b2 = tk.Button(master=root, text="My second button", command=lambda: self.my_callback("Hello"))
        self.b2.pack()

        # Examples of OptionMenu with an activation of another OptionMenu (categories / sub-categories)
        # String Var in Menu
        self.choice = tk.StringVar()
        # Options to show in the menu
        options = [chr(i) for i in range(85, 90)]
        # OptionMenu, callback for when we change option
        self.om = tk.OptionMenu(root, self.choice, *options, command=self.choice_callback)
        self.om.pack()
        # Default value
        self.choice.set("A")

        self.choice2 = tk.StringVar()
        options2 = [chr(i) for i in range(75, 90)]
        self.om2 = tk.OptionMenu(root, self.choice2, *options2, command=self.choice2_callback)
        self.om2.pack()
        self.om2.config(state="disabled")
        self.choice2.set("T")

    def my_callback(self, *args):
        print(args)

    def choice_callback(self, choice):
        print(f"[FIRST CALLBACK] : {choice}")
        if choice == "U":
            self.om2.config(state="active")
        else:
            self.om2.config(state="disabled")

    def choice2_callback(self, choice):
        print(f"[SECOND CALLBACK] : {choice}")


root = tk.Tk()
app = SimpleGUI(root)
root.mainloop()
