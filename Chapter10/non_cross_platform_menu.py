import tkinter as tk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.geometry("300x200")
menu = tk.Menu(root)


smile = tk.PhotoImage(file='smile.gif')
smile_menu = tk.Menu(menu, tearoff=False)
smile_menu.add_command(
  image=smile,
  command=lambda: showinfo(message="Smile!")
)
smile_menu.add_command(label='test')

# The image is cut off in MacOS
# In Windows, only the text "(image)" appears
menu.add_cascade(image=smile, menu=smile_menu)


# configure colors
menu.configure(foreground='white', background='navy')
smile_menu.configure(foreground='yellow', background='red')

# Doesn't appear on any platform
menu.add_separator()

# Doesn't appear on MacOS at all
menu.add_command(
  label='Top level command',
  command=lambda: showinfo(message='By your command!')
)


boolvar = tk.BooleanVar()
# Doesn't appear on MacOS at all
# Appears in Windows, but without checkbox
menu.add_checkbutton(label="It is true", variable=boolvar)

root.config(menu=menu)
root.mainloop()
