import tkinter as tk # Modul 8: GUI
import random
import time
from threading import Thread

class TypingTest: # Modul 5 :OOP
    def __init__(self, master):
        self.master = master
        self.master.title("Typing Test")
        self.master.geometry("1000x400")
        
        self.time_limit = 60
        self.start_time = None
        self.running = False
        # Modul 1: Array
        self.word_list = ["sebuah", "jangan", "bunga", "beberapa", "fungsi", "mungkin", "suatu", "kondisi", "perulangan", "metode", "melainkan", "dapat", "kelas", "walaupun", "hadiah", "mengapa", "dimana", "nyata", "akan", "saat"]
        self.words_to_type = random.sample(self.word_list, 10)
        self.typed_words = []
        
        self.setup_gui()

    def setup_gui(self): 
        self.label = tk.Label(self.master, text="Type the following words:", font=("Helvetica", 16))
        self.label.pack(pady=20)
        
        self.word_display = tk.Label(self.master, text=" ".join(self.words_to_type), font=("Helvetica", 16))
        self.word_display.pack(pady=20)
        
        self.entry = tk.Entry(self.master, font=("Helvetica", 16), width=75) 
        self.entry.pack(pady=20)
        self.entry.bind("<KeyRelease>", self.start_typing)
        
        self.button_frame = tk.Frame(self.master)
        self.button_frame.pack(pady=20)

        self.restart_button = tk.Button(self.button_frame, text="Restart", command=self.restart, font=("Helvetica", 16))
        self.restart_button.grid(row=0, column=0, padx=10)
        
        self.exit_button = tk.Button(self.button_frame, text="Exit", command=self.master.quit, font=("Helvetica", 16))
        self.exit_button.grid(row=0, column=1, padx=10)
        
        self.result_label = tk.Label(self.master, text="", font=("Helvetica", 16))
        self.result_label.pack(pady=20)

    def start_typing(self, event): 
        if not self.running: # Modul 2: Pengkondisian
            self.start_time = time.time()
            self.running = True
            Thread(target=self.update_timer).start()
        
        typed_text = self.entry.get().split()
        if len(typed_text) >= len(self.words_to_type):
            if typed_text[-1] == self.words_to_type[-1]: 
                self.entry.insert(tk.END, ".") 
                self.calculate_results()
    
    def update_timer(self):
        while self.running:
            elapsed_time = time.time() - self.start_time
            if elapsed_time >= self.time_limit:
                self.calculate_results()
                break
            time.sleep(0.1)
    
    def calculate_results(self):
        self.running = False
        self.entry.config(state='disabled')
        
        typed_text = self.entry.get().split()
        correct_words = 0
        for i, word in enumerate(self.words_to_type):
            if i < len(typed_text) and word == typed_text[i]:
                correct_words += 1
        
        accuracy = (correct_words / len(self.words_to_type)) * 100
        elapsed_time = time.time() - self.start_time
        wpm = (correct_words / 5) / (elapsed_time / 60)
        
        self.result_label.config(text=f"Accuracy: {accuracy:.2f}%, WPM: {wpm:.2f}")
    
    def restart(self): # Modul 4: Function dan Method, Modul 3: Perulangan (tombol restart)
        self.running = False
        self.start_time = None
        self.words_to_type = random.sample(self.word_list, 10)
        self.typed_words = []
        
        self.entry.config(state='normal')
        self.entry.delete(0, tk.END)
        self.word_display.config(text=" ".join(self.words_to_type))
        self.result_label.config(text="")
        
if __name__ == "__main__": 
    root = tk.Tk()
    app = TypingTest(root)
    root.mainloop()
