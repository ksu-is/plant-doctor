import tkinter as tk
from tkinter import *
import customtkinter as ctk
from tkinter import font
from customtkinter import *
from PIL import Image

tan = '#DDD0B6'
lgreen = '#3D5535'
dgreen = '#2F3D2A'

app = ctk.CTk(fg_color = tan)

# creating variables with font info to make it easer to style the text

h1 = ctk.CTkFont(family="Blue_Cashews", size=32)
h2 = ctk.CTkFont(family="Abril Display", size=28)
h2 = ctk.CTkFont(family="Abril Display", size=24)
body = ctk.CTkFont(family="DM Sans", size=16)
buttontxt = ctk.CTkFont(family="DM Sans", size=16)

# page that says hello and asks for your name

welcome = Frame(
    app,
    bg = tan)
welcome.grid(row=0, column=0, sticky="nsew")

# page that welcomes you by name and asks for user input
input = Frame(
    app,
    bg = tan)
input.grid(row=0, column=0, sticky="nsew")

# page that displays recommendations based on user input

recommendation = Frame(
    app,
    bg = tan)
recommendation.grid(row=0, column=0, sticky="nsew")

# defining logo variables for whole app

welcome_logo = CTkImage(
    light_image=Image.open("logo-pngs/PlantDoctor_Logo-06.png"),
    dark_image=Image.open("logo-pngs/PlantDoctor_Logo-06.png"),
    size=(300,200)
    )
welcome_logo_label = ctk.CTkLabel(welcome, image=welcome_logo, text = "")

input_logo = CTkImage(
    light_image=Image.open("logo-pngs/PlantDoctor_Logo-06.png"),
    dark_image=Image.open("logo-pngs/PlantDoctor_Logo-06.png"),
    size=(300,200)
    )
input_logo_label = ctk.CTkLabel(input, image=input_logo, text = "")

recommendation_logo = CTkImage(
    light_image=Image.open("logo-pngs/PlantDoctor_Logo-06.png"),
    dark_image=Image.open("logo-pngs/PlantDoctor_Logo-06.png"),
    size=(300,200)
    )
recommendation_logo_label = ctk.CTkLabel(recommendation, image=recommendation_logo, text = "")

# WELCOME PAGE
# title of welcome page

welcome_title = ctk.CTkLabel(
    welcome,
    text=("Welcome to The Plant Doctor!\nWhat is your name?"),
    font=h1,
    text_color = lgreen,
    width = 800,
    pady = 20,
    wraplength=600)
welcome_title.place(anchor=tk.CENTER)
welcome_title.pack()

# entry box for username

name_var = tk.StringVar()

username = ctk.CTkEntry(
    welcome,
    textvariable = name_var,
    placeholder_text="Please type your name here...",
    width = 200)
username.pack()

# function to update the input_title variable to include the user's name

def update_input_title():
    input_title.configure(text="Hello, " + name_var.get().capitalize() + "! What is going on with your plant?")

# function to move to input page & update the input_title variable

def to_input():
    update_input_title()
    input.tkraise()

# Define the button to move to the input page
enter = ctk.CTkButton(
    welcome,
    text="Let's get started!",
    font = buttontxt,
    command=to_input
)
enter.pack()

welcome_logo_label.pack()

# INPUT PAGE
# title of input page

input_title = ctk.CTkLabel(
    input,
    text="",
    font=h1,
    text_color = lgreen,
    width=800,
    pady=20,
    wraplength=600)
input_title.pack()

# symptom entry box

symptomentry = ctk.CTkEntry(
    input,
    placeholder_text = "Describe your plant's symptoms here...",
    width = 450,
    height = 200,
)
symptomentry.pack()

def submit_symptoms():
    print(symptomentry.get())

def to_recommendation():
    recommendation.tkraise()

to_rec_button = ctk.CTkButton(
    input,
    text = "Get Recommendations",
    font = buttontxt,
    command = to_recommendation
)
to_rec_button.pack()

# RECOMMENDATION PAGE
# recommendations page title

recommendations_title = ctk.CTkLabel(
    recommendation,
    text=("Here are some recommendations:"),
    font=h1,
    text_color = lgreen,
    width = 800,
    pady = 20,
    wraplength=600)
recommendations_title.place(anchor=tk.CENTER)
recommendations_title.pack()

welcome.tkraise()
app.geometry("800x600")
app.title("The Plant Doctor by Ethan Jordan")
app.mainloop()