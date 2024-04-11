import tkinter as tk
from tkinter import *
import customtkinter as ctk
from tkinter import font
from customtkinter import *

app = ctk.CTk()

# creating variables with font info to make it easer to style the text

h1 = ctk.CTkFont(family="Abril Display", size=24)
h2 = ctk.CTkFont(family="Abril Display", size=24)
h2 = ctk.CTkFont(family="Abril Display", size=24)
body = ctk.CTkFont(family="Abril Display", size=24)
buttontxt = ctk.CTkFont(family="Abril Display", size=24)

# page that says hello and asks for your name

welcome = Frame(app)
welcome.grid(row=0, column=0, sticky="nsew")

# title of welcome page

welcome_title = ctk.CTkLabel(
    welcome,
    text=("Welcome! What is your name?"),
    font=h1,
    width = 500,
    pady = 20)
welcome_title.place(anchor=tk.CENTER)
welcome_title.pack()

# entry box for username

username = ctk.CTkEntry(
    welcome,
    placeholder_text="Please type your name here...",
    width = 200)
username.pack()
name = username.get()

# function to move to input page

def to_input():
    input.tkraise()

enter = ctk.CTkButton(
    welcome,
    text="Let's get started!",
    command = to_input # run function on button click
)
enter.pack()

# page that welcomes you by name and asks for user input

input = Frame(app)
input.grid(row=0, column=0, sticky="nsew")

# title of input page

input_title = ctk.CTkLabel(
    input,
    text=("Hello " + name + "! What is going on with your plant?"),
    font=h1,
    width = 500,
    pady = 20)
input_title.place(anchor=tk.CENTER)
input_title.pack()

# symptom entry box

symptomentry = ctk.CTkEntry(
    input,
    placeholder_text = "Describe your plant's symptoms here...",
    width = 450
)

# page that displays recommendations based on user input

recommendation = Frame(app)
recommendation.grid(row=0, column=0, sticky="nsew")

welcome.tkraise()
app.geometry("500x400")
app.title("The Plant Doctor by Ethan Jordan")
app.mainloop()