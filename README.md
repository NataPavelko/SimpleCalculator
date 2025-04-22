🧮 Tkinter Calculator GUI
A simple calculator built using Python's tkinter module. This GUI-based app allows users to perform basic arithmetic operations in a user-friendly interface.

📦 Features
Graphical User Interface (GUI) using Tkinter

Basic arithmetic operations: +, -, *, /

Support for parentheses and decimal points

Real-time result calculation using the = button

Delete last character (DEL)

Clear entire input (DELETE EVERYTHING)

Fixed-size window layout using Grid System

🖥️ Requirements
Python 3.x

This app uses only standard libraries (tkinter), so no additional installations are needed.

🚀 How to Run
Save the code to a .py file, e.g., calculator.py

Open terminal or command prompt

Run the file using:

bash
Kopieren
Bearbeiten
python calculator.py
📄 Code Overview
tk.Tk() initializes the root window

Entry widget for displaying input/output

Button widgets to input digits and operators

eval() is used to evaluate the input string

Layout is managed using .grid() and responsive resizing with rowconfigure() and columnconfigure()

⚠️ Notes
The eval() function is used to compute the result. While it's convenient, be cautious with user input if extending this calculator to more complex or shared environments.

The window size is fixed using .resizable(False, False) and .minsize().

📸 Preview
markdown
Kopieren
Bearbeiten
----------------------------
|        Entry Field       |
|--------------------------|
| 7 | 8 | 9 | ( | )        |
| 4 | 5 | 6 | * | /        |
| 1 | 2 | 3 | + | -        |
| 0 | . |DEL| = (= spans)  |
|  DELETE EVERYTHING       |
----------------------------
🛠️ To-Do / Ideas
Add keyboard input support

Add advanced functions (sin, cos, log, etc.)

Add result history

Input validation to avoid eval() error
