import tkinter as tk
from tkinter import *
import customtkinter as ctk
from tkinter import font
from customtkinter import *
from PIL import Image
from PIL import Image, ImageTk

##################### FUNCTION #####################
# defining a dictionary of keywords with associated recommendations
care_recommendations = {
    'yellow': [
        "Yellow leaves at the base may indicate overwatering. Try reducing the frequency of watering and ensure proper drainage.",
        "Yellow leaves at the tip may indicate nutrient deficiency. Consider fertilizing the plant with a balanced fertilizer."
    ],
    'brown': [
        "Brown spots may indicate a fungal infection. Consider trimming affected areas and applying a fungicide."
    ],
    'wilt': [
        "Wilting can be a sign of underwatering. Make sure the plant is receiving adequate water, and adjust watering frequency as needed."
    ],
    'leggy': [
        "Leggy growth often occurs in low light conditions. Move the plant to a brighter location and consider pruning to encourage bushier growth."
    ]
}

# creating primary function, plant_doctor
def plant_doctor(user_input):
    keywords = []
    for word in user_input.split():
        found_keyword = False
        for keyword in care_recommendations.keys():
            if keyword.lower() in word.lower() or word.lower() in keyword.lower():
                keywords.append(keyword)
                found_keyword = True
                break
        if not found_keyword:
            keywords.append(word.lower())
    recommendations = []
    for keyword in keywords:
        recommendations.extend(care_recommendations.get(keyword, []))
    return recommendations

##################### GUI #####################
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

# creating variable to use as the bg image on the WELCOME page; not working but im saving it just in case
welcome_bg_img = CTkImage(
    Image.open("logo-pngs/bg-img.jpg"),
    size=(800,600)
)
welcome_bg_img_label = ctk.CTkLabel(app, image=welcome_bg_img)

# creating page that says hello and asks for your name
welcome = ctk.CTkFrame(
    app,
    width = 800,
    height = 600,
    fg_color = 'transparent')
welcome.grid(row=0, column=0, sticky="nsew")

# creating page that welcomes you by name and asks for user input
input = ctk.CTkFrame(
    app,
    fg_color = tan)
input.grid(row=0, column=0, sticky="nsew")

# creating page that displays recommendations based on user input
recommendation_page = ctk.CTkFrame(
    app,
    fg_color = tan)
recommendation_page.grid(row=0, column=0, sticky="nsew")

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
recommendation_logo_label = ctk.CTkLabel(recommendation_page, image=recommendation_logo, text = "")

# WELCOME PAGE
welcome_logo_label.grid(
    pady = (120,0)
) # the plant doctor logo

# title of welcome page
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
    text_color=lgreen,
    width=800,
    wraplength=600
)
input_title.grid(pady=(100, 10))

# entry box to accept user's input
symptomentry = ctk.CTkEntry(
    input,
    placeholder_text="Describe your plant's symptoms here...",
    width=450,
    height=200,
    corner_radius=10,
    fg_color=tan,
    placeholder_text_color=dtan,
    text_color=lgreen,
    font=body,
    border_width=1,
    border_color=lgreen
)
symptomentry.grid()

# button that goes to next page
to_rec_button = ctk.CTkButton(
    input,
    text="GET RECOMMENDATIONS",
    font=buttontxt,
    text_color=tan,
    command=lambda: submit_symptoms(),
    fg_color=lgreen,
    width=265,
    height=40,
    corner_radius=10,
    border_width=0,
    hover_color=dgreen
)
to_rec_button.grid(pady=10)

def submit_symptoms():
    print(symptomentry.get())

def to_recommendation():
    recommendation_page.tkraise()

# RECOMMENDATION PAGE
# Recommendation page content
recommendations_title = ctk.CTkLabel(
    recommendation_page,
    text="Here are some recommendations:",
    font=h1,
    text_color=lgreen,
    width=800,
    pady=20,
    wraplength=600
)
recommendations_title.grid(row=0, column=0)

# text box that displays recommendations
recommendation_text = ctk.CTkTextbox(
    recommendation_page,
    wrap='word',
    state='disabled',
    width=450,
    height=430,
    corner_radius=10,
    fg_color=tan,
    text_color=lgreen,
    font=body,
    border_width=1,
    border_color=lgreen
)
recommendation_text.grid(row=1, column=0)

#setting up the scrollbar
scrollbar = tk.Scrollbar(recommendation_page, command=recommendation_text.yview)
scrollbar.grid(row=1, column=1, sticky='ns')
recommendation_text.configure(yscrollcommand=scrollbar.set)

# function to move to input page and update the input title
def to_input():
    input_title.configure(text="Hello, " + name_var.get().capitalize() + "!\nWhat is going on with your plant?")
    input.tkraise()

# function to submit symptoms and display recommendations
def submit_symptoms():
    user_input = symptomentry.get()
    recommendations =plant_doctor(user_input)
    recommendation_text.configure(state='normal')  # Enable text widget for editing
    recommendation_text.delete('1.0', END)  # Clear previous recommendations
    if recommendations:
        for recommendation in recommendations:
            recommendation_text.insert(END, "- " + recommendation + "\n\n")
    else:
        recommendation_text.insert(END, "No matching recommendations found. Please try different keywords or describe the issue in more detail.")
    recommendation_text.configure(state='disabled')  # Disable text widget after editing
    recommendation_page.tkraise()

# button that takes user back to the input page to ask another question
back_to_input_button = ctk.CTkButton(
    recommendation_page,
    text="ASK ANOTHER QUESTION",
    font=buttontxt,
    text_color=tan,
    command=lambda: back_to_input(),
    fg_color=lgreen,
    width=265,
    height=40,
    corner_radius=10,
    border_width=0,
    hover_color=dgreen
)
back_to_input_button.grid(pady=10)

# function for the above the button to take user back to the last page
def back_to_input():
    input.tkraise()

welcome.tkraise()
app.geometry("800x600")
app.title("The Plant Doctor by Ethan Jordan")
app.mainloop()