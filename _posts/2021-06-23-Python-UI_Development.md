---
layout: post
title:  "Python GUI Development: Tkinter"
date:   2021-06-23 03:52:38
categories: Tech
hidden: true
tags: [Coding, DIY]
image:
  background: witewall_3.png
---

[Main Course Link](https://www.linkedin.com/learning/python-gui-development-with-tkinter-2)

This Series is a part of [30 Days of Learning](https://www.notion.so/yogeshpandey/June-30-Days-of-Learning-65a60adfdd504eb2b989649fef13e6d2).

- tkinter is tool for GUI development in Python.

- Provides UI elements like buttons, widgets etc.

- Tk GUI can run on most common OS.

- TK 8.0 can match the theme of your OS.

- Basic tk UI 

```

# Importing all functions
from tkinter import *

# Create a constructor
root = Tk()

# Pack the geometry
Label(root, text="Hello, Tkinter!").pack()

# Run the main loop
root.mainloop()

```

- Creating and Configuring Widgets, Each Widget is a class. All widgets exits after root. The widgets have heirarchy and the parent is the geometry manager of its child.

```
from tkinter import *

# Library for the widgets

from tkinter import ttk

# Create Constructer
root = Tk()

# Add a button Widget, pass the parent widget 
button = ttk.Button(root, text = 'Click Me')

# Add to the window
button.pack()

# Configuring button widget

button['text'] = 'Click Me'
button.config(text = 'Push Me')

# Get all the propoerties with the widget object
print(button.config())

# Get UID of widget
print(str(button))


print(str(root))

ttk.Label(root, text ='Hello, Tkinter!').pack()

# mainloop() add
root.mainloop()


```

- How to manage widget placement. We can do this using Geometry management. There are different Geometry managers. Each is created for diffrent uses.

- Event handling.  Using command property or event bindings