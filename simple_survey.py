import tkinter as tk
from tkinter import messagebox, PhotoImage, Label
import re  # import regex module for email validation

class SurveyApp:
    def __init__(self, master):
        self.master = master
        master.title("Feedback Survey")

        # Adding an image with alternative text as a label (Image 1)
        self.image1 = PhotoImage(file="image1.png")
        self.image_label1 = Label(master, image=self.image1, text="A Pond In The Berkshires In The Spring", compound="top")
        self.image_label1.pack()

        self.label_feedback = tk.Label(master, text="Please enter your feedback below:")
        self.label_feedback.pack()
        self.entry_feedback = tk.Entry(master, width=50)
        self.entry_feedback.pack()

        # Adding another image (Image 2)
        self.image2 = PhotoImage(file="image2.png")
        self.image_label2 = Label(master, image=self.image2, text="Asenema Waterfall, Ghana", compound="bottom")
        self.image_label2.pack()

        self.label_email = tk.Label(master, text="Please enter your email address:")
        self.label_email.pack()
        self.entry_email = tk.Entry(master, width=50)
        self.entry_email.pack()

        self.submit_button = tk.Button(master, text="Submit", command=self.submit)
        self.submit_button.pack()
        self.exit_button = tk.Button(master, text="Exit", command=self.exit_app)
        self.exit_button.pack()

    def submit(self):
        feedback = self.entry_feedback.get()
        email = self.entry_email.get()
        if not feedback.strip() and not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            messagebox.showwarning("Warning", "Please ensure your feedback is not empty and email is valid.")
        elif not feedback.strip():
            messagebox.showwarning("Warning", "Please ensure your feedback is not empty")
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            messagebox.showwarning("Warning", "Please ensure your email is valid.")
        else:
            self.open_thank_you_window()

    def open_thank_you_window(self):
        self.thank_you_window = tk.Toplevel(self.master)
        self.thank_you_window.title("Thank You!")
        self.message_label = tk.Label(self.thank_you_window, text="Thank you for your feedback!")
        self.message_label.pack()
        self.close_button = tk.Button(self.thank_you_window, text="Close", command=self.close_thank_you_window)
        self.close_button.pack()

    def close_thank_you_window(self):
        #close the thank you window, safely destroying it
        self.thank_you_window.destroy()

    def exit_app(self):
         #securely exit the application after confirming the user's intent
        response = messagebox.askyesno("Exit", "Are you sure you want to exit?")
        if response:
            self.master.quit()

def main():
    root = tk.Tk()
    app = SurveyApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
