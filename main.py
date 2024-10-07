import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkfont
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample dataset for plagiarism check
dataset = [
    "Artificial Intelligence is the simulation of human intelligence processes by machines, especially computer systems.",
    "Machine learning is a method of data analysis that automates analytical model building.",
    "Deep learning is part of a broader family of machine learning methods based on artificial neural networks with representation learning.",
    "Neural networks are a series of algorithms that attempt to recognize underlying relationships in a set of data through a process that mimics the way the human brain operates."
]

# Function to calculate plagiarism percentage
def calculate_plagiarism():
    input_text = input_box.get("1.0", "end-1c")  # Get text from input box

    if not input_text:
        messagebox.showerror("Error", "Please enter some text to check.")
        return

    # Add input text to the dataset for comparison
    texts = [input_text] + dataset

    # Vectorize the texts
    vectorizer = TfidfVectorizer().fit_transform(texts)
    vectors = vectorizer.toarray()

    # Calculate plagiarism percentage with the most similar text from the dataset
    similarity_matrix = cosine_similarity(vectors)
    input_similarity = similarity_matrix[0][1:]  # Skip comparison with itself
    max_similarity = max(input_similarity) * 100

    # Display the result
    result_label.config(text=f"Plagiarism Percentage: {max_similarity:.2f}%")

# Set up Tkinter window
root = tk.Tk()
root.title("Plagiarism Checker")
root.geometry("700x450")  # Set window size
root.config(bg="#f5f5f5")  # Set light background color

# Custom fonts for a more polished look
title_font = tkfont.Font(family="Helvetica", size=22, weight="bold")
label_font = tkfont.Font(family="Helvetica", size=14)
button_font = tkfont.Font(family="Helvetica", size=12, weight="bold")
result_font = tkfont.Font(family="Helvetica", size=16, weight="bold")

# Style enhancements for entry box, buttons, and labels
def style_widget(widget, corner_radius=10, padding=(5, 10)):
    widget.config(relief="flat", highlightbackground="#dddddd", highlightthickness=1, padx=padding[1], pady=padding[0])
    widget.bind("<Enter>", lambda e: widget.config(highlightbackground="#bbbbbb"))  # Hover effect
    widget.bind("<Leave>", lambda e: widget.config(highlightbackground="#dddddd"))

# Add title label
title_label = tk.Label(root, text="Plagiarism Checker", font=title_font, bg="#f5f5f5", fg="#2c3e50")
title_label.pack(pady=20)

# Input Text Box
input_label = tk.Label(root, text="Enter text to check:", font=label_font, bg="#f5f5f5", fg="#34495e")
input_label.pack(pady=5)
input_box = tk.Text(root, height=10, width=65, font=("Helvetica", 12), relief="flat", borderwidth=2, highlightthickness=1, highlightbackground="#ccc")
input_box.pack(pady=5)
style_widget(input_box)

# Button to calculate plagiarism
check_button = tk.Button(root, text="Check Plagiarism", font=button_font, command=calculate_plagiarism, bg="#3498db", fg="white", relief="flat", padx=15, pady=8, borderwidth=0, cursor="hand2")
check_button.pack(pady=20)
check_button.config(activebackground="#2980b9", activeforeground="white")  # Active color for button
style_widget(check_button, padding=(5, 20))

# Label to show result
result_label = tk.Label(root, text="Plagiarism Percentage: ", font=result_font, bg="#f5f5f5", fg="#e74c3c")
result_label.pack(pady=10)

# Adding a shadow effect to the buttons and text box
def add_shadow_effect(widget, offset=3, color="#cccccc"):
    widget.config(borderwidth=0)
    shadow = tk.Label(root, bg=color)
    shadow.place(x=widget.winfo_x()+offset, y=widget.winfo_y()+offset, width=widget.winfo_width(), height=widget.winfo_height())
    widget.lift()

root.update_idletasks()
add_shadow_effect(input_box, offset=2)
add_shadow_effect(check_button, offset=3)

# Run the Tkinter loop
root.mainloop()
