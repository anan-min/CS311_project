import tkinter as tk


def create_drop_shadow(widget, offset=3, color='gray'):
    # Create top shadow
    shadow_top = tk.Frame(widget.master, bg=color)
    shadow_top.place(x=widget.winfo_x(), y=widget.winfo_y() -
                     offset, width=widget.winfo_width(), height=offset)

    # Create bottom shadow
    shadow_bottom = tk.Frame(widget.master, bg=color)
    shadow_bottom.place(x=widget.winfo_x(), y=widget.winfo_y(
    ) + widget.winfo_height(), width=widget.winfo_width(), height=offset)

    # Create left shadow
    shadow_left = tk.Frame(widget.master, bg=color)
    shadow_left.place(x=widget.winfo_x() - offset, y=widget.winfo_y(),
                      width=offset, height=widget.winfo_height())

    # Create right shadow
    shadow_right = tk.Frame(widget.master, bg=color)
    shadow_right.place(x=widget.winfo_x() + widget.winfo_width(),
                       y=widget.winfo_y(), width=offset, height=widget.winfo_height())


root = tk.Tk()
root.geometry('300x300')

# Create the box
box = tk.Frame(root, width=200, height=200, bg='white')
box.pack(pady=20)

# Create drop shadow for the box
create_drop_shadow(box, offset=3, color='gray')

root.mainloop()
