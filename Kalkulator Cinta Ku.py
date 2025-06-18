from tkinter import *
import random
from tkinter import font as tkfont

root = Tk()
# Defining the size
root.geometry('400x300')
root.title('Love Calculator ❤️')
root.configure(bg='#FFE4E1')  # Light pink background

# Custom fonts
title_font = tkfont.Font(family="Helvetica", size=16, weight="bold")
label_font = tkfont.Font(family="Helvetica", size=10)
result_font = tkfont.Font(family="Helvetica", size=24, weight="bold")
button_font = tkfont.Font(family="Helvetica", size=12)

def calculate_love():
    # Get names from entries
    name1_val = name1.get().strip()
    name2_val = name2.get().strip()
    
    if not name1_val or not name2_val:
        result.config(text="Masukkan kedua nama!", fg="red")
        return
    
    # Create a "deterministic random" result based on names
    combined = (name1_val + name2_val).lower()
    random.seed(sum(ord(c) for c in combined))
    percentage = random.randint(50, 100)  # Love percentage between 50-100%
    
    # Set different colors based on percentage
    if percentage >= 80:
        color = "#FF1493"  # Deep pink
        message = "Soulmates! ❤️"
    elif percentage >= 60:
        color = "#FF69B4"  # Hot pink
        message = "Good match! 💕"
    else:
        color = "#DB7093"  # Pale violet red
        message = "Not bad! 💘"
    
    result.config(text=f"{percentage}%", fg=color)
    message_label.config(text=message, fg=color)

# Heading on Top
heading = Label(root, text='Love Calculator ❤️', font=title_font, bg='#FFE4E1', fg='#FF1493')
heading.pack(pady=10)

# Input frame
input_frame = Frame(root, bg='#FFE4E1')
input_frame.pack(pady=5)

# Slot/input for the first name
slot1 = Label(input_frame, text="Nama Kamu:", font=label_font, bg='#FFE4E1')
slot1.grid(row=0, column=0, padx=5, pady=5, sticky='w')
name1 = Entry(input_frame, border=3, font=label_font)
name1.grid(row=0, column=1, padx=5, pady=5)

# Slot/input for the partner name
slot2 = Label(input_frame, text="Nama Pasangan:", font=label_font, bg='#FFE4E1')
slot2.grid(row=1, column=0, padx=5, pady=5, sticky='w')
name2 = Entry(input_frame, border=3, font=label_font)
name2.grid(row=1, column=1, padx=5, pady=5)

# Button
bt = Button(root, text="Hitung Cinta", height=1, width=15, 
            command=calculate_love, font=button_font, 
            bg='#FF69B4', fg='white', relief=RAISED, bd=3)
bt.pack(pady=10)

# Result frame
result_frame = Frame(root, bg='#FFE4E1')
result_frame.pack()

# Text on result slot
Label(result_frame, text='Kecocokan:', font=label_font, bg='#FFE4E1').pack()
result = Label(result_frame, text='?', font=result_font, bg='#FFE4E1')
result.pack()
message_label = Label(result_frame, text='', font=label_font, bg='#FFE4E1')
message_label.pack()

# Footer
Label(root, text="❤️ Cinta itu indah ❤️", font=label_font, bg='#FFE4E1', fg='#DB7093').pack(side=BOTTOM, pady=10)

# Starting the GUI
root.mainloop()