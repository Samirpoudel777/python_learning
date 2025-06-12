import tkinter as tk
import time

def update_time():
    current_time = time.strftime('%H:%M:%S')
    label.config(text=current_time)
    label.after(1000, update_time)  # update every 1 second

# Create the main window
root = tk.Tk()
root.title("Digital Clock")
root.geometry("300x100")
root.resizable(False, False)

# Create and configure the label to show time
label = tk.Label(root, font=('Arial', 40), bg='black', fg='cyan')
label.pack(expand=True)

update_time()  # Start the clock
root.mainloop()  # Run the GUI loop
