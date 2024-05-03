import tkinter as tk


def convert_text_to_anchor_left(text):
    lines = text.split("\n")
    return "\n".join([f"{line.strip()}" for line in lines])


def switch_main_frame(self, parent_frame, child_frame):
    # Forget all other child frames
    for frame in parent_frame.winfo_children():
        if frame != child_frame:
            frame.grid_forget()

    # Grid the selected child frame
    child_frame.grid(row=0, column=0, sticky="news")


def fetch_data(page_number, item_per_page):
    off_set = (page_number - 1) * item_per_page
    limit = item_per_page
    sql_command = f"SELECT * FROM table_name ORDER BY your_ordering_column LIMIT {limit} OFFSET {off_set}"
    # this will fetch data depending on page number and iterm per page


# def create_drop_shadow(widget, offset=(2, 2), color='gray'):
#     shadow = tk.Frame(widget.master, bg=color)
#     shadow.place(x=widget.winfo_x() + offset[0], y=widget.winfo_y(
#     ) + offset[1], width=widget.winfo_width(), height=widget.winfo_height())


# so we can forget every frames and set frame we wanted with 2 functions
# note you can pass product id or other data in config and can retrieve it late using a function
