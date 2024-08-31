import tkinter as tk
from tkinter import ttk, messagebox
import speech_recognition as sr
from googletrans import Translator, LANGUAGES

# Initialize the translator
translator = Translator()

def translate_text():
    try:
        input_text = input_textbox.get("1.0", "end-1c")
        dest_language = language_combobox.get()

        if not input_text:
            messagebox.showwarning("Input Error", "Please enter text to translate.")
            return

        # Perform translation
        translation = translator.translate(input_text, dest=dest_language)
        output_textbox.delete("1.0", "end")
        output_textbox.insert("end", translation.text)
    except Exception as e:
        messagebox.showerror("Translation Error", str(e))

def recognize_speech():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        messagebox.showinfo("Voice Recording", "Please speak now...")
        audio = recognizer.listen(source)
        messagebox.showinfo("Voice Recorded", "Voice recorded successfully. Converting to text...")

        try:
            text = recognizer.recognize_google(audio)
            input_textbox.delete("1.0", "end")
            input_textbox.insert("end", text)
            messagebox.showinfo("Select Language", "Please select the target language from dropdown...")
        except sr.UnknownValueError:
            messagebox.showerror("Speech Error", "Could not understand the audio.")
        except sr.RequestError as e:
            messagebox.showerror("Speech Error", f"Could not request results; {e}")

# Initialize Tkinter window
root = tk.Tk()
root.title("Language Translator")
root.geometry("500x500")
root.configure(bg="#f0f0f0")  # Set background color

# Input text label and textbox
input_label = ttk.Label(root, text="Input Text:", font=("Helvetica", 12, "bold"), background="#f0f0f0")
input_label.pack(pady=10)
input_textbox = tk.Text(root, height=5, width=50, font=("Helvetica", 10))
input_textbox.pack(pady=10)

# Recognize speech button
speech_button = ttk.Button(root, text="🎤 Speak", command=recognize_speech, style="Accent.TButton")
speech_button.pack(pady=10)


# Language selection combobox
language_label = ttk.Label(root, text="Select Language:", font=("Helvetica", 12, "bold"), background="grey")
language_label.pack(pady=10)

language_combobox = ttk.Combobox(root, values=list(LANGUAGES.values()), font=("Helvetica", 10))
language_combobox.set("Spanish")  # Default language
language_combobox.pack(pady=10)

# Translate button
translate_button = ttk.Button(root, text="🔄 Translate", command=translate_text, style="Accent.TButton")
translate_button.pack(pady=10)

# Output text label and textbox
output_label = ttk.Label(root, text="Translated Text:", font=("Helvetica", 12, "bold"), background="#f0f0f0")
output_label.pack(pady=10)
output_textbox = tk.Text(root, height=5, width=50, font=("Helvetica", 10))
output_textbox.pack(pady=10)

# Style configuration for buttons
style = ttk.Style()
style.configure("Custom.TButton", background="color_code", foreground="color_code")
style.map("Custom.TButton", background=[("active", "color_code")])

# Start Tkinter main loop
root.mainloop()
