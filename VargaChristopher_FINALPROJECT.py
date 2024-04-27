import tkinter as tk
from tkinter import messagebox
import re  # import regex module for email validation

class SurveyApp:
    def __init__(self, master):
        #initialize the main application window with gui components
        self.master = master  # main application window
        master.title("Feedback Survey")

        #section: user feedback input
        #label prompting for user feedback
        self.label_feedback = tk.Label(master, text="Please enter your feedback below:")
        self.label_feedback.pack()
        #entry widget for users to input their feedback
        self.entry_feedback = tk.Entry(master, width=50)
        self.entry_feedback.pack()

        #section: user email input
        #label asking for user's email address for contact purposes
        self.label_email = tk.Label(master, text="Please enter your email address:")
        self.label_email.pack()
        #entry widget for user to input email, which will be validated
        self.entry_email = tk.Entry(master, width=50)
        self.entry_email.pack()

        #section: action buttons
        #button to submit feedback and email. calls submit method when clicked
        self.submit_button = tk.Button(master, text="Submit", command=self.submit)
        self.submit_button.pack()
        #button to exit the application. triggers a confirmation dialog
        self.exit_button = tk.Button(master, text="Exit", command=self.exit_app)
        self.exit_button.pack()

    def submit(self):
        #handle feedback and email submission, checking for non-empty and valid email input
        feedback = self.entry_feedback.get()  # get user feedback from entry
        email = self.entry_email.get()  # get user email from entry
        #validate that feedback is not empty and email is in a proper format
        if feedback.strip() and re.match(r"[^@]+@[^@]+\.[^@]+", email):
            self.open_thank_you_window()
        else:
            messagebox.showwarning("Warning", "Please ensure your feedback is not empty and email is valid.")

    def open_thank_you_window(self):
        #open a new window thanking the user for their feedback and valid email submission
        self.thank_you_window = tk.Toplevel(self.master)
        self.thank_you_window.title("Thank You!")
        #thank you message label displayed to the user
        self.message_label = tk.Label(self.thank_you_window, text="Thank you for your feedback!")
        self.message_label.pack()
        #close button in the thank you window that destroys the window when clicked
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
    #set up and run the main application window
    root = tk.Tk()
    app = SurveyApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
