import tkinter as tk

def calculate_result():
    try:
        ai = int(bishop_entry.get())
        bi = int(god_entry.get())
        ci = (((ai * 4) ** 4) / 2) + bi

        result_label.config(text=get_result_sequence(ci),font=("Helvetica", 25))
    except ValueError:
        result_label.config(text="Please enter valid numbers")

def get_result_sequence(ci):
    if ci + 17 == 80017:
        return "D O N ' T  R U I N  M Y  S T O R Y  W I T H  Y O U R  L O G I C"
    elif ci + 17 == 32785:
        return "O F T H  E T Q S  H I  O B C D A  V Y X P  Z U W G  J I O K A"
    elif ci + 17 == 32786:
        return "W Q R U  O B S A  D J  P L K M Z  X C V B  N Y I G  H I Y J Q"
    else:
        return "K S J H  U Y E T  A K  M N O U I  W S X V  E D F R  T G H J K"

# Create the main window
window = tk.Tk()
window.geometry("1600x1000")
window.title("A Step")

# Create input fields for bishops and gods with adjusted text size
bishop_label = tk.Label(window, text="Enter the no. of bishops:", font=("Georgia", 20))
bishop_label.pack()
bishop_entry = tk.Entry(window, font=("Georgia", 20))  # Adjust the font size here
bishop_entry.pack()

god_label = tk.Label(window, text="Enter the no. of gods:", font=("Times New Roman", 20))
god_label.pack()
god_entry = tk.Entry(window, font=("Times New Roman", 20))  # Adjust the font size here
god_entry.pack()

# Create a button to trigger the calculation
calculate_button = tk.Button(window, text="Calculate", command=calculate_result,font=("Arial", 20))
calculate_button.pack()

# Create a label to display the result or error message
result_label = tk.Label(window, text="", font=("Helvetica", 20))  # Adjust the font size here
result_label.pack()

# Start the GUI event loop
window.mainloop()
