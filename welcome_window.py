import tkinter as tk

class WelcomeWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Begrüßung")
        self.root.geometry("300x200")

    def show_welcome_window(self):
        self.label = tk.Label(self.root, text="Willkommen zum Energy Balance Game!")
        self.label.pack(pady=20)

        self.button = tk.Button(self.root, text="Start", command=self.root.destroy)
        self.button.pack(pady=20)

        self.root.mainloop()
