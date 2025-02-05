import sys
import tkinter as tk
from dense_retrieval_system import DenseRetrievalSystem
from gui import DarkThemeGUI

# Initialize the Dense Retrieval System
rag = DenseRetrievalSystem()


def on_enter_callback(sentence):
    results = rag.search(sentence, k=10)
    app.sample_data = results
    app.update_list()

# Initialize the GUI
root = tk.Tk()
app = DarkThemeGUI(root, on_enter_callback=on_enter_callback)
app.show_loading()  # Initially show loading
root.update()
root.update_idletasks()

if len(sys.argv) > 1:
    input_variable = sys.argv[1]
    print(f"Input file name passed into program: {input_variable}")
else:
    print("No input file name provided. Using default prayers.txt")
    input_variable = "prayers.txt"

# Load contents of file as newline separated strings
with open(input_variable, 'r') as file:
    lines = file.readlines()

for index, line in enumerate(lines):
    app.update_loading_text("Loading data " + str(index+1) + " of " + str(len(lines)))
    root.update()
    root.update_idletasks()
    print("Loading data " + str(index+1) + " of " + str(len(lines)))
    rag.push(line)


app.sample_data = rag.search("test", k=10)
app.hide_loading_and_update_list()
root.mainloop()