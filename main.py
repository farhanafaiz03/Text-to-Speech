import tkinter as tk
from tkinter import *
from tkinter import messagebox
import pyttsx3

try:
    engine = pyttsx3.init()
except Exception as e:
    messagebox.showerror("Initialization Error", f"Failed to initialize TTS engine: {e}")
    raise SystemExit("Engine initialization failed")

def speaknow():
    try:
        text = textv.get()
        if not text.strip():
            raise ValueError("Please enter some text to speak!")
        
        engine.say(text)
        engine.runAndWait()

    except ValueError as ve:
        messagebox.showwarning("Input Error", str(ve))
    except Exception as e:
        messagebox.showerror(f"An error occurred: {e}")

root = Tk()
root.title("Text to Speech")

textv = StringVar()

obj = LabelFrame(root, text="Text to Speech", font=20, bd=1)
obj.pack(fill="both", expand="yes", padx=10, pady=10)

lbl = Label(obj, text="Text", font=30)
lbl.pack(side=tk.LEFT, padx=5)

text = Entry(obj, textvariable=textv, font=30, width=25, bd=5)
text.pack(side=tk.LEFT, padx=10)

btn = Button(obj, text="Speak", font=20, bg="Black", fg="White", command=speaknow)
btn.pack(side=tk.LEFT, padx=10)

try:
    root.mainloop()
except Exception as e:
    messagebox.showerror("Runtime Error", f"Application crashed: {e}")
