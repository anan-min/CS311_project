
def forget_all_frames(parent_frame):
    for frame in frame.winfo_children():
        frame.grid_forget()

# set frame grid on parent at the default position


def set_frame(parent_frame, frame, position):
    row, column =  position 
    forget_all_frames(parent_frame)
    frame.grid(row=row, column=column)


def fetch_data(page_number, item_per_page):
    off_set = (page_number - 1) * item_per_page
    limit = item_per_page
    sql_command = f"SELECT * FROM table_name ORDER BY your_ordering_column LIMIT {limit} OFFSET {off_set}"
    # this will fetch data depending on page number and iterm per page


# so we can forget every frames and set frame we wanted with 2 functions
# note you can pass product id or other data in config and can retrieve it late using a function
