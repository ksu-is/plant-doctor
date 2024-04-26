import tkinter as tk
from tkinter import *
import customtkinter as ctk
from tkinter import font
from customtkinter import *
from PIL import Image
from PIL import Image, ImageTk


# defining color varialbes
tan = '#DDD0B6'
dtan = '#BFAF94'
lgreen = '#3D5535'
dgreen = '#2F3D2A'

app = ctk.CTk(fg_color = tan)

#configuring the grid
app.columnconfigure(0, weight=1) # row 1
app.columnconfigure(1, weight=1) # row 2
app.columnconfigure(2, weight=1) # row 3

# creating variables with font info to make it easer to style the text
h1 = ctk.CTkFont(family="Blue_Cashews", size=32)
h2 = ctk.CTkFont(family="Abril Display", size=28)
h2 = ctk.CTkFont(family="Abril Display", size=24)
body = ctk.CTkFont(family="DM Sans Medium", size=16)
buttontxt = ctk.CTkFont(family="DM Sans Bold", size=16)

# page that says hello and asks for your name
welcome = ctk.CTkFrame(
    app,
    width = 800,
    height = 600,
    fg_color = 'transparent')
welcome.grid(row=0, column=0, sticky="nsew")

# creating variable to use as the bg image on the WELCOME page; not working but im saving it just in case
welcome_bg_img = CTkImage(
    Image.open("logo-pngs/bg-img.jpg"),
    size=(800,600)
)
welcome_bg_img_label = ctk.CTkLabel(app, image=welcome_bg_img)

# page that welcomes you by name and asks for user input
input = ctk.CTkFrame(
    app,
    fg_color = tan)
input.grid(row=0, column=0, sticky="nsew")

# page that displays recommendations based on user input
recommendation = ctk.CTkFrame(
    app,
    fg_color = tan)
recommendation.grid(row=0, column=0, sticky="nsew")

# defining logo variables for whole app
welcome_logo = CTkImage(
    light_image=Image.open("logo-pngs/PlantDoctor_Logo-06.png"),
    dark_image=Image.open("logo-pngs/PlantDoctor_Logo-06.png"),
    size=(200,105),
    )
welcome_logo_label = ctk.CTkLabel(
    welcome,
    image=welcome_logo,
    text = "")

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
welcome_logo_label.grid(
    pady = (120,0)
) # the plant doctor logo

welcome_title = ctk.CTkLabel(
    welcome,
    text=("Welcome to The Plant Doctor!\nWhat is your name?"),
    font=h1,
    text_color = lgreen,
    width = 800,
    pady = 20,
    wraplength=600)
welcome_title.grid()

# entry box for username
name_var = tk.StringVar()
username = ctk.CTkEntry(
    welcome,
    textvariable = name_var,
    placeholder_text="Please type your name here...",
    width = 230,
    height = 40,
    corner_radius = 10,
    fg_color = tan,
    placeholder_text_color = dtan,
    text_color = lgreen,
    font = body,
    border_width = 1,
    border_color = lgreen)
username.grid()

# function to update the input_title variable to include the user's name
def update_input_title():
    input_title.configure(text="Hello, " + name_var.get().capitalize() + "!\nWhat is going on with your plant?")

# function to move to input page & update the input_title variable
def to_input():
    update_input_title()
    input.tkraise()

# Define the button to move to the input page
enter = ctk.CTkButton(
    welcome,
    text="LET'S GET STARTED!",
    font = buttontxt,
    text_color = tan,
    command=to_input,
    fg_color = lgreen,
    width = 230,
    height = 40,
    corner_radius = 10,
    border_width = 0,
    hover_color = dgreen
)
enter.grid(
    pady = 10
)

# INPUT PAGE
# title of input page
input_title = ctk.CTkLabel(
    input,
    text="",
    font=h1,
    text_color = lgreen,
    width=800,
    wraplength=600)
input_title.grid(
    pady=(100, 10)
)

# symptom entry box
symptomentry = ctk.CTkEntry(
    input,
    placeholder_text = "Describe your plant's symptoms here...",
    width = 450,
    height = 200,
    corner_radius = 10,
    fg_color = tan,
    placeholder_text_color = dtan,
    text_color = lgreen,
    font = body,
    border_width = 1,
    border_color = lgreen)
symptomentry.grid()

def submit_symptoms():
    print(symptomentry.get())

def to_recommendation():
    recommendation.tkraise()

to_rec_button = ctk.CTkButton(
    input,
    text = "GET RECOMMENDATIONS",
    font = buttontxt,
    text_color = tan,
    command=to_recommendation,
    fg_color = lgreen,
    width = 265,
    height = 40,
    corner_radius = 10,
    border_width = 0,
    hover_color = dgreen
)
to_rec_button.grid(
    pady = 10
)

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
recommendations_title.grid()

welcome.tkraise()
app.geometry("800x600")
app.title("The Plant Doctor by Ethan Jordan")
app.mainloop()