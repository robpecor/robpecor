# Simple GUI

from tkinter import *

# Create the Window
root = Tk()

# Modify root window
root.title("Labeler")
root.geometry("800x400")

# Create a frame and put in root
app = Frame(root)

# Add app to the grid
app.grid()
# Create a label
label = Label(app, text = "This is a label")

# Add the label to a grid
label.grid()

# Create Buttons
# Button 1 is a button with text placed in the button
button1 = Button(app, text = "Button1 Here")
# Button 2 is a blank button, text to be added later
button2 = Button(app)
# Button 3 is blank, text to be added later
button3 = Button(app)

# Put button on the grid
button1.grid()
button2.grid()
button3.grid()
# Add text to Button 2
button2.configure(text = "Button2 Here")

# Different way to add text
button3["text"] = "Button3 Here"

# Start the event loop
root.mainloop()

mySet = {1, 2, 'a'}
type(mySet)
mySet.