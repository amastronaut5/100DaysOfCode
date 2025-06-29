import tkinter as tk
from tkinter import messagebox
import time
import random

# Sample text list
texts = [
    "The quick brown fox jumps over the lazy dog",
    "Python is a powerful programming language",
    "Typing speed test is fun and useful",
    "Discipline is the bridge between goals and accomplishment"
]

class TypingSpeedTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.geometry("700x400")
        self.text_to_type = random.choice(texts)
        self.start_time = None

        self.setup_widgets()

    def setup_widgets(self):
        self.title_label = tk.Label(self.root, text="Typing Speed Test", font=("Helvetica", 20, "bold"))
        self.title_label.pack(pady=10)

        self.text_display = tk.Label(self.root, text=self.text_to_type, wraplength=600, font=("Helvetica", 14))
        self.text_display.pack(pady=10)

        self.entry = tk.Text(self.root, height=5, font=("Helvetica", 14))
        self.entry.pack(pady=10)
        self.entry.bind("<KeyPress>", self.start_timer)

        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 14))
        self.result_label.pack(pady=10)

        self.check_button = tk.Button(self.root, text="Check Speed", command=self.calculate_speed)
        self.check_button.pack()

        self.reset_button = tk.Button(self.root, text="Reset", command=self.reset_test)
        self.reset_button.pack(pady=5)

    def start_timer(self, event):
        if self.start_time is None:
            self.start_time = time.time()

    def calculate_speed(self):
        end_time = time.time()
        time_taken = end_time - self.start_time
        typed_text = self.entry.get("1.0", tk.END).strip()
        words_typed = len(typed_text.split())
        wpm = round((words_typed / time_taken) * 60)

        correct_words = 0
        for tw, ow in zip(typed_text.split(), self.text_to_type.split()):
            if tw == ow:
                correct_words += 1

        accuracy = round((correct_words / len(self.text_to_type.split())) * 100)

        self.result_label.config(
            text=f"Time: {round(time_taken, 2)}s | WPM: {wpm} | Accuracy: {accuracy}%"
        )

    def reset_test(self):
        self.text_to_type = random.choice(texts)
        self.text_display.config(text=self.text_to_type)
        self.entry.delete("1.0", tk.END)
        self.result_label.config(text="")
        self.start_time = None

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTest(root)
    root.mainloop()
