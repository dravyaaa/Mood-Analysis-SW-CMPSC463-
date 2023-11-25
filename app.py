import tkinter as tk
import sys
from tkinter import messagebox
from google.cloud import language_v1
from google.oauth2 import service_account
from PIL import Image, ImageTk
import csv
import sqlite3
import requests
from io import BytesIO
from textblob import TextBlob
from datetime import datetime
from data_processing import (
    handle_missing_values,
    add_temporal_features,
    calculate_activity_frequency,
    add_sentiment_scores,
    aggregate_similar_activities,
    add_weather_condition,
)


active_user = ""
users = {}
user_activities_file = r'C:\Users\dravy\OneDrive\Desktop\CMPSC 463\FinalProject\mood_data.db'

def create_table():
    conn = sqlite3.connect(user_activities_file)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS user_activities
                 (username TEXT, activities TEXT)''')
    conn.commit()
    conn.close()

def write_user_activities_to_db():
    conn = sqlite3.connect(user_activities_file)
    c = conn.cursor()
    try:
        c.execute("DELETE FROM user_activities")
        for user, activities in users.items():
            c.execute("INSERT INTO user_activities VALUES (?, ?)", (user, activities))
        conn.commit()
        print("Data written to database successfully.")
    except sqlite3.Error as e:
        conn.rollback()
        print(f"Database Error occurred: {str(e)}")
        # Logging the error message can also be helpful:
        # logger.error(f"Database Error occurred: {str(e)}")
        messagebox.showerror("Database Error", f"An error occurred: {str(e)}")
    finally:
        conn.close()

def read_user_activities_from_db():
    conn = sqlite3.connect(user_activities_file)
    c = conn.cursor()
    try:
        c.execute("SELECT * FROM user_activities")
        rows = c.fetchall()
        for row in rows:
            users[row[0]] = row[1]
        print("Data read from database successfully.")
    except sqlite3.Error as e:
        print(f"Database Error occurred: {str(e)}")
        # logger.error(f"Database Error occurred: {str(e)}")
        messagebox.showerror("Database Error", f"An error occurred: {str(e)}")
    finally:
        conn.close()

# (Other functions such as add_user, collect_user_activities, get_mood_suggestion, etc.)
def add_user():
    global active_user
    user_name = entry_username.get()
    if user_name:
        active_user = user_name
        users[user_name] = ""
        messagebox.showinfo("User Added", f"User '{user_name}' added successfully!\nActive User: {active_user}")
        update_active_user_label()
        update_users_listbox()
        write_user_activities_to_db()  # Update the database after adding a user



def collect_user_activities():
    global active_user
    if active_user:
        activities_data = entry_activities.get("1.0", tk.END)
        users[active_user] = activities_data
        handle_missing_values(users)  # Handle missing values after collecting activities
        messagebox.showinfo("Activities Submitted", f"User activities for '{active_user}' submitted successfully!")
        # Add additional processing functions as needed
        add_temporal_features(users, active_user)
        calculate_activity_frequency(users, active_user)
        add_sentiment_scores(users, active_user)
        # Call other data processing functions here
        aggregate_similar_activities(users, active_user)
        add_weather_condition(users, active_user)
        write_user_activities_to_db()  # Update the database after collecting activities


def get_mood_suggestion(score):
    if score >= 0.5:
        return "positive"
    elif -0.5 <= score < 0.5:
        return "neutral"
    else:
        return "negative"

def show_mood_and_suggestion(score, mood):
    global active_user
    if active_user:
        if mood == "positive":
            messagebox.showinfo("Sentiment Analysis Result",
                                f"Sentiment score: {score}\nMood: Positive\nSuggested Activity: Great! Be grateful and continue the good work.\nUser Activities: {users[active_user]}")
        elif mood == "neutral":
            messagebox.showinfo("Sentiment Analysis Result",
                                f"Sentiment score: {score}\nMood: Neutral\nSuggested Activity: Hmm...maybe watch Netflix? or Relax in a pool?\nUser Activities: {users[active_user]}")
        else:
            messagebox.showinfo("Sentiment Analysis Result",
                                f"Sentiment score: {score}\nMood: Negative\nSuggested Activity: Don't stress! Treat yourself to your favourite food.\nUser Activities: {users[active_user]}")
    else:
        messagebox.showwarning("No Active User", "Please select an active user before analyzing sentiment.")

def update_active_user_label():
    label_active_user.config(text=f"Active User: {active_user}")

def update_users_listbox():
    listbox_users.delete(0, tk.END)
    for user in users:
        listbox_users.insert(tk.END, user)


root = tk.Tk()
root.geometry("850x638")
root.title("Data Collection")



def analyze_sentiment():
    global active_user
    if active_user:
        text = entry_sentiment.get("1.0", tk.END)

        if not text.strip():
            messagebox.showerror("Error", "Please enter some text.")
            return

        try:
            key_path = "silicon-park-405804-7b680b962dcf.json"
            credentials = service_account.Credentials.from_service_account_file(key_path)
            client = language_v1.LanguageServiceClient(credentials=credentials)

            document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
            response = client.analyze_sentiment(request={'document': document})

            sentiment = response.document_sentiment
            score = sentiment.score

            mood_suggestion = get_mood_suggestion(score)
            show_mood_and_suggestion(score, mood_suggestion)
            show_mood_image(mood_suggestion)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    else:
        messagebox.showwarning("No Active User", "Please select an active user before analyzing sentiment.")


def delete_user():
    global active_user
    selected_user = listbox_users.get(tk.ACTIVE)
    if selected_user:
        del users[selected_user]
        if active_user == selected_user:
            active_user = ""
            update_active_user_label()
        update_users_listbox()

def exit_program():
    root.destroy()


create_table()
read_user_activities_from_db()


background_color = "#00000000"
accent_color = "#4CAF50"
button_color = "#333"
text_color = "#111"
background_image_path = "bg.png"

background_image = Image.open(background_image_path)
background_photo = ImageTk.PhotoImage(background_image)

root.configure(bg='black')

background_label = tk.Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

mood_label = tk.Label(root)  # This is an example; the actual initialization could be different
mood_label.pack()  # Example placement; actual placement might differ

def show_mood_image(mood):
    img_path = None
    suggestion = None

    if mood == "positive":
        img_path = 'sun.png'
    elif mood == "neutral":
        img_path = 'clouds.png'
    else:
        img_path = 'rain.png'

    if img_path:
        img = Image.open(img_path)
        img = img.resize((300, 300), resample=Image.LANCZOS)
        photo = ImageTk.PhotoImage(img)

        # Assuming mood_label is a Label widget in your GUI
        mood_label.config(image=photo, text=f"Mood: {mood.capitalize()}\nSuggested Activity: {suggestion}",
                          compound=None, font=("Arial", 14, "bold"), fg="#000000", padx=20, pady=20)
        mood_label.image = photo  # Ensure the image reference is retained to prevent garbage collection


frame_exit_button = tk.Frame(root, bg=None)
frame_exit_button.pack()

button_exit = tk.Button(frame_exit_button, text="Exit", command=root.destroy, bg="#FF6347", fg="white",
                        font=("Arial", 12))
button_exit.pack(pady=10)

# (Other GUI components and their configurations)
title_label = tk.Label(root, text="Data Collection", bg=None, fg=button_color,
                       font=("Garamond", 22, "bold"))
title_label.pack(pady=10)

label_active_user = tk.Label(root, text="Active User: ", bg=None, font=("Arial", 12), fg="black", highlightbackground=None)
label_active_user.pack()

entry_username = tk.Entry(root, width=30, font=("Arial", 10))
entry_username.pack(pady=5)

button_add_user = tk.Button(root, text="Add User", command=add_user, bg=accent_color, fg="white",
                            font=("Arial", 12))
button_add_user.pack(pady=5)

label_users = tk.Label(root, text="Users", bg=None, font=("Arial", 12), fg=button_color)
label_users.pack()

listbox_users = tk.Listbox(root, width=30, height=5, font=("Arial", 10))
listbox_users.pack(pady=5)
update_users_listbox()

button_delete_user = tk.Button(root, text="Delete User", command=delete_user, bg="#FF6347", fg="white",
                               font=("Arial", 12))
button_delete_user.pack(pady=5)

label_activities = tk.Label(root, text="User Activities:", bg=None, font=("Arial", 12), fg=button_color)
label_activities.pack()
entry_activities = tk.Text(root, width=40, height=5, font=("Arial", 10))
entry_activities.pack(pady=5)

button_activities = tk.Button(root, text="Submit Activities", command=collect_user_activities, bg=accent_color,
                               fg="white", font=("Arial", 12))
button_activities.pack(pady=5)

label_sentiment = tk.Label(root, text="Sentiment Analysis:", bg=None, font=("Arial", 12),
                            fg=button_color)
label_sentiment.pack()
entry_sentiment = tk.Text(root, width=40, height=5, font=("Arial", 10))
entry_sentiment.pack(pady=5)

button_sentiment = tk.Button(root, text="Analyze Sentiment", command=analyze_sentiment, bg=accent_color, fg="white",
                             font=("Arial", 12))
button_sentiment.pack(pady=5)

button_exit = tk.Button(root, text="Exit", command=exit_program, bg="#FF6347", fg="white", font=("Arial", 12))
button_exit.place(relx=0.5, rely=0.9, anchor=tk.CENTER)


root.mainloop()
