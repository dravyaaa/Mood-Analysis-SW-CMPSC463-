import tkinter as tk
import sqlite3

def show_data():
    conn = sqlite3.connect(r'C:\Users\dravy\OneDrive\Desktop\CMPSC 463\FinalProject\mood_data.db') # Replace with your database file path
    c = conn.cursor()
    c.execute("SELECT * FROM user_activities")
    rows = c.fetchall()
    conn.close()

    def update_display():
        listbox.delete(0, tk.END)
        for row in sorted(rows, key=lambda x: x[selected_sort_index].lower()):
            if selected_filter_value in row[selected_filter_index].lower():
                formatted_row = f"Username: {row[0]}\nActivities: {row[1]}\n"
                listbox.insert(tk.END, formatted_row)
                listbox.insert(tk.END, "\n")  # Add an empty line for better separation

    def on_sort_select(*args):
        nonlocal selected_sort_index
        selected_sort_index = sort_option.index(sort_var.get())
        update_display()

    def on_filter_select(*args):
        nonlocal selected_filter_index, selected_filter_value
        selected_filter_index = filter_option.index(filter_var.get())
        selected_filter_value = filter_entry.get().lower()
        update_display()

    def on_search(event):
        search_term = search_entry.get().lower()
        listbox.delete(0, tk.END)
        for row in rows:
            if any(search_term in value.lower() for value in row):
                formatted_row = f"Username: {row[0]}\nActivities: {row[1]}\n"
                listbox.insert(tk.END, formatted_row)
                listbox.insert(tk.END, "\n")  # Add an empty line for better separation

    root = tk.Tk()
    root.title("User Activities")

    selected_sort_index = 0
    selected_filter_index = 0
    selected_filter_value = ''

    sort_option = ["Username", "Activities"]
    sort_var = tk.StringVar(root)
    sort_var.set(sort_option[0])
    sort_var.trace_add("write", on_sort_select)

    filter_option = ["Username", "Activities"]
    filter_var = tk.StringVar(root)
    filter_var.set(filter_option[0])
    filter_var.trace_add("write", on_filter_select)

    search_entry = tk.Entry(root)
    search_entry.pack()
    search_entry.bind("<KeyRelease>", on_search)

    sort_menu = tk.OptionMenu(root, sort_var, *sort_option)
    sort_menu.pack()

    filter_entry = tk.Entry(root)
    filter_entry.pack()

    filter_menu = tk.OptionMenu(root, filter_var, *filter_option)
    filter_menu.pack()

    listbox = tk.Listbox(root, width=60, height=20)
    listbox.pack(padx=20, pady=20)

    update_display()

    root.mainloop()

if __name__ == "__main__":
    show_data()
