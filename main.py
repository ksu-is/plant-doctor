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
    'monstera' : [
        "Monstera are popular houseplants with unique, fenestrated leaves. Here are some essential care tips for your monstera:",
        "Monsteras like chunky soil with lots of perlite, bark, and nutrients. Make sure that the soil drains thorgouly with every water.",
        "Monsteras like to dry out between waterings. Make sure that the top 1-2 inches of soil are dry before watering again. Too much water can lead to root rot, so be sure to test the soil before watering.",
        "Be sure to give your monstera bright, indirect light. A south- or west-facing window is perfect. If the light is too direct, try adding a sheer curtain to diffuse the light.",
        "For best results, add a support pole to your monstera. These tropical plants like to climb, and a support pole will allow them to produce larger leaves with more fenestrations."
    ],
    'snake' : [
        "Snake plants, also called mother in law's tongue, are popular houseplants for beginners with tall, pointy leaves. Here are some essential care tips for your snake plant:",
        "Snake plants like very chunky soils--similar to what you would use for a cactus. Be sure to include lots of perlite and bark for quick drainage.",
        "Snake plants don't need very much water, which makes them great for beginners. These plants only need water 2-3 times per month and should be watered when the soil is almost entirely dry.",
        "Snake plants can handle nearly any lighting conditions. They will do well in low-medium light, and they can handle bright, direct sunlight.",
        "Snake plants produce 'pups,' or baby plants that come off the main plant. These pups can be divided and planted into their own pot. Or leave them in the pot for an extra full plant!"
    ],
    'pothos' : [
        "Pothos are fast-growing, vine plants with bright green foliage. They come in many varieties, such as the marble queen or golden pothos. Here are some essential care tips for your pothos plant:",
        "Pothos like a medium-draining soil that retains some moisture. Use a balanced blend of coco coir, perlite, and bark.",
        "Water your pothos every 1-2 weeks or when the top 2 inches of soil are dry. These plants don't need much to grow quickly!",
        "Pothos will do well in medium- to bright-light environments. The brighter the light, the more dramatic their markings will be.",
        "Pothos are one of the easiest plants to propagate. Simply cut the vine below a leaf and place in water. Once the leaf has grown several inches of roots, pot into soil and water very thoroughly. Soon, you will have a whole new plant!"
    ],
    'ZZ' : [
        "ZZ plants are low-maintenance plants with unique growth patterns. Here are some essential care tips for your ZZ plant:",
        "Pot your ZZ plant into well draining soil, similar to what you would use for a cactus. Make sure that the soil drains thoroughly with every water.",
        "ZZ plants don't need much water. In fact, you can get away with only watering these plants 1-2 times per month.",
        "ZZ plants can handle nearly all lighting conditions. The brighter the light, the quicker the growth and the more intense the color variations.",
    ],
    'rubber' : [
        "Rubber plants, or ficus elastica, are tree-like plants with shiny, dark green leaves. They come in many varieties, such as the ficus rubra or ficus tineke. Here are some essential care tips for your rubber plant:",
        "Rubber plants do well in a medium-draining soil that retains some moisture. Use a balanced blend of coco coir, perlite, and bark.",
        "Rubber plants do well with weekly waterings or when the top 1 inch of soil has dried out.",
        "Rubber plants like medium- to bright-light environments, but can do well in lower light situations. For variegated varieties, place in a brighter spot to see more vibrant pink and white leaves."
    ],
    'philodendron' : [
        "Philodendrons are fast-growing, vine plants with varying leaf shapes. Some species of philodendrons climb and produce large leaves, while others trail and have smaller leaves. Here are some essential care tips for your philodendrons:",
        "Philodendrons do well in a well-draining soil. Use a balanced mix of coco coir, perlite, and bark. For larger varieties, consider adding some coco bark for the roots to grab onto.",
        "Water your philodendron when the top 1-2 inches of soil have dried out. Philodendron leaves may curl when they have dried out too much.",
        "Philodendrons do well in medium- to bright-light environments. Climbing philodendrons will grow facing the light source. Try rotating these plants after every watering to encourage even growth.",
        "For climbing varieties, add a support pole for best results. These tropical plants like to climb, and a support pole will allow them to produce larger leaves."
    ],
    'fiddle' : [
        "Fiddle-leaf figs are tree-like ficuses with rounded leaves. They are known for being quite temperamental. Here are some essential care tips for your fiddle-leaf fig:",
        "Fiddle-leaf figs, or FLFs, like a medium-draining soil with lots of perlite and bark.",
        "Water your FLF when the top 1-2 inches of soil are dry. These plants are sensitive to water, so be sure to check the soil frequently.",
        "FLFs like lots of bright light. Place this plant near a south- or west-facing window that receives 6+ hours of bright light every day.",
        "Fiddle-leaf figs are sensitive to cold air and may drop several leaves when exposed to drafts. Keep these plants away from air conditioning vents and drafty windows in the winter time."
    ],
    'anthurium' : [
        "Anthurium are tropical plants with varying, heart-shaped foliage. Some varieties of anthuriums produce colorful flowers, while others may never produce flowers as a houseplant. Here are some essential care tips for your anthurium:",
        "Consider making a special soil mix for your anthurium including sphagnum moss, perlite, and coco bark. The soil should be light and airy for the thick roots while also retaining some moisture.",
        "These plants like to remain consistently moist, so water when the top 1 inch of soil mix is dry. Consider bottom watering to ensure that the sphagnum moss is thoroughly moistened.",
        "These plants like medium or bright, indirect light. Too much direct sunlight may burn their velvety leaves.",
        "Most varieties of anthuriums have velvety, rich green leaves. Try placing them near a humidifier to keep the leaves extra healthy. Most anthuriums need to stay above 65% humidity for best results, but they will be okay with humidity above 45%."
    ],
    'palm' : [
        "Palms are dramatic plants with fan-shaped leaves. Here are some essential care tips for your palm trees:",
        "Palms like very retentive soil. Consider mixing coco coir with some perlite and bark. Add some earthworm castings for extra retention.",
        "Palms need lots of water and will benefit from weekly waterings. Be sure to water thoroughly until water comes out of the drainage holes.",
        "These plants need bright light. Consider placing in a south- or west-facing window, or even on a sunny back porch.",
        "Palms are prone to getting thrips and several other common pests. Wipe your palm tree down with a neem oil mixture at least once per month. Add peppermint essential oil for extra strength."
    ],
    'hoya' : [
        "Hoyas are beautiful, vine plants that come in many different varieties. These aroids are great for beginners, as well as seasoned plant parents. Here are some essential care tips for your hoyas:",
        "Hoyas like a chunky, well-draining soil. Consider creating a mix of coco bark and perlite. For added moisture retention add a small amount of coco coir to the soil.",
        "These tropical plants don't need water very often. Water them very thoroughly and ensure that there is no standing water in the drainage tray.",
        "Hoyas thrive in bright, direct sunlight. Many hoyas also produce bright red or pink leaves under bright lights. Consider investing in some grow lights for these plants.",
        "Hoyas produce beautiful clusters of flowers with strong, sweet fragrances. Place these plants under bright lights to encourage flowering. Once the plant has produced a peduncle, be sure not to cut it off--more flowers will grow from the same spot!"
    ],
    'cactus' : [
        "Cacti are desert plants that thrive with minimal care. Here are some essential care tips for your cactus:",
        "Cacti need a very well-draining soil consisting of perlite, bark, and pumice. Cactus soil can be found easily at grocery stores and hardware stores.",
        "These desert plants need water 1-2 times per month. You may notice some wrinkles on the cactus; this indicates that it is time for water. If you notice any mushy spots, reduce watering frequency.",
        "Cacti need bright, direct sunlight."
    ],
    'yellow': [
        "Yellow leaves at the base may indicate overwatering. Try reducing the frequency of watering and ensure proper drainage.",
        "Yellow leaves at the tip may indicate nutrient deficiency. Consider fertilizing the plant with a balanced fertilizer."
    ],
    'brown': [
        "A brown leaf can often be a sign of over- or underwatering. Make sure that the plant is in a pot with drainage holes and well-draining soil. If you have a hard time watering often enough, try mixing a handul of earthworm castings into your soil to add extra moisture retention."
    ],
    'wilt': [
        "Wilting can be a sign of underwatering. Make sure the plant is receiving adequate water, and adjust watering frequency as needed."
    ],
    'leggy': [
        "Leggy growth often occurs in low light conditions. Move the plant to a brighter location and cut back leggy growth to encourage fuller growth. If you don't have a bright window, consider investing in some grow light bulbs or strips."
    ],
    'spot' : [
        "Spots on a plant's leaves can be caused by several factors, but the most common cause is fungal diseases from overwatering. Try wiping the plant down with a neem oil mixture to eliminate and fungus or pests. Also, mix a small amount of hydrogen peroxide into the can before your next watering to remove fungus on the roots."
    ],
    'bugs' : [
        "Bugs are normal, but some types are more harmful than others. Try mixing a tablespoon of neem oil into a spray bottle full of water. For extra strength, add a few drops of peppermint essential oil. Spray leaves, stems, and soil thoroughly to kill most bugs and any eggs they may have laid."
    ],
    'pale' : [
        "Pale yellow-green growth is a sign of nutrient deficiency. Try investing in a high-quality liquid fertilizer. Mixing pellet fertilizer into your soil also makes it easy to keep the soil full of nutrients."
    ],
    'mushy' : [
        "A mushy stem can be caused by excessive water in the soil. Try mixing perlite or pumice into your soil to add extra drainage. Mushy stems are also common to plants that grow from bulbs, like alocasias. In this case, you have nothing to worry about!"
    ],
    'soil' : [
        "There is a lot to be said about soil. There are three main components to a good soil: moisture retention, drainage, and nutrients. A common mix is coco coir for moisture retention, perlite, pumice, or orchid bark for drainage, and a fertilzer of some sort for nutrients. For bonus points, add in coconut bark or horicultural charcoal for added benefits. The ratio of ingredients depends on the plant."
    ],
    'compact' : [
        "As soil ages, it is common for it to become compacted. Try using a wooden chopstick to gently poke holes into the soil. For plants in plastic pots, squeeze the pot to loosen the soil. If these tips do not add enough aeration, it may be time for a repot."
    ],
    'smell' : [
        "If you notice a bad smell coming from your plant, it likely indicates root rot or another fungal infection. Try mixing some hydrogen peroxide into the can during your next watering. If the issue persists, try repotting into a potting soil with added drainage."
    ],
    'root' : [
        "Roots coming out of the pot indicate a 'rootbound' plant, which means it has outgrown its pot. Repot the plant into a pot that is 1-2 inches larger than its current pot. For example, if its current pot is 4 inches in diameter, upgrade to a pot 6 inches in diameter or smaller. If necessary, carefully trim any excessive roots during the repot process."
    ],
    'rott' : [
        "Root rot is commonly caused by too much moisture in the soil. Try mixing perlite or pumice into the soil for added drainage. If the root rot is bad, remove the plant from its pot, gently remove as much soil as possible, and trim any brown or soft roots. Spray the root ball with a mixture of 1:10 hydrogen peroxide to water. Rinse thoroughly with clean water before repotting into a chunkier soil mix."
    ],
    'webs' : [
        "Fine, white webs on a plant come from spider mites. Try mixing a tablespoon of neem oil into a spray bottle full of water. For extra strength, add a few drops of peppermint essential oil. Spray leaves, stems, and soil thoroughly to kill most bugs and any eggs they may have laid."
    ],
    'mold' : [
        "Mold on the soil's surface is a result of inadequate air flow. This can also be caused by soil that does not dry out quickly enough. Use a clean spoon to remove the top inch of soil from the plant. Try placing a small fan near the plant to increase air flow. If the mold comes back again, try repotting into a chunkier soil mix."
    ],
    'burn' : [
        "Burns on a plants leaves can come from 2 things: too much sun or too much fertilizer. If your plant is receiving too much sunlight, try moving it or hanging a sheer curtain in the window to filter the light. If the plant is receiving too much fertilizer, try flushing the soil thoroughly with clean water. Use a lower concentration of fertilizer. Often, using 1/4 of what the manufacturer's instructions recommend at every water should help avoid nutrient burn."
    ],
    'overwater' : [
        "Overwatering happens! If you are afraid you overwatered your plant, try gently removing the soil from the pot, keeping it all in one piece. Wrap the soil ball in several layers of newspaper. If you are afraid to overwater again, try mixing perlite or pumice into your soil. For added benefits, add extra drainage holes to the plant's pot."
    ],
    'dying' : [
        "A dying leaf is not always cause for alarm. Many plants will simply drop one leaf to make room for new growth. However, if you notice many leaves dying rapidly, that may indicate your plant is not receiving the care it needs. Try going back and provide more details so that the Plant Doctor can provide recommendations."
    ],
    'red spot' : [
        "Red spots on a plant, or oedema, are caused by excess moisture. These dots form when the plant takes up more water than can be transpired through the leaves. As a result, the cell burst and turn an orange-red color. Try watering less frequently or mixing perlite/pumice into your plant's soil mixture."
    ],
    'crisp' : [
        "Crispy leaves are caused by too little moisture. Leaves may turn completely brown and crispy when the plant is not receiving enough water. On the other hand, brown, crunchy tips may be seen when the plant is not receiving enough humidity. Try watering the plant more often or using a more retentive soil mix. To add humidity, place a humidifier or essential oil diffuser near the plant. Be careful that the mist does not accumulate as drops on the leaves."
    ],
    'gnat' : [
        "Try mixing a tablespoon of neem oil into a spray bottle full of water. For extra strength, add a few drops of peppermint essential oil. Spray leaves, stems, and soil thoroughly to kill most bugs and any eggs they may have laid."
    ],
}

# creating primary function, plant_doctor
def plant_doctor(user_input):
    keywords = set()  # initialize a set of keywords
    recommendations = []  # initialize list of recommendations
    for word in user_input.split():
        # check to see if user's entry is 4+ letters; prevents app from detecing non-keywords in the user's input, for example: detecting 'i' and displaying irrelevant recommendations for all keywords that include the letter 'i'
        if len(word) >= 4:
            for keyword in care_recommendations.keys():
                if keyword.lower() in word.lower() or word.lower() in keyword.lower():
                    if keyword not in keywords:  # check to see if the recommendation has already been used; only display recommendations once
                        keywords.add(keyword)  # add keyword to set
                        recommendations.extend(care_recommendations[keyword])  # add recommendations for keyword
                    break
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
symptomentry = ctk.CTkTextbox( # ctk textbox used in place of entry allow better formatting, like wrap
    input,
    width=450,
    height=200,
    corner_radius=10,
    fg_color=tan,
    text_color=lgreen,
    font=body,
    border_width=1,
    border_color=lgreen,
    wrap='word'
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
    border_color=lgreen,
    scrollbar_button_color=tan,
    scrollbar_button_hover_color=tan
)
recommendation_text.grid(row=1, column=0)

# setting up the scrollbar
scrollbar = Scrollbar(
    recommendation_page,
    command=recommendation_text.yview)
scrollbar.grid(row=1, column=1, sticky='ns')
recommendation_text.configure(yscrollcommand=scrollbar.set)

# function to move to input page and update the input title
def to_input():
    input_title.configure(text="Hello, " + name_var.get().capitalize() + "!\nWhat is going on with your plant?")
    input.tkraise()

# function to submit symptoms and display recommendations
def submit_symptoms():
    user_input = symptomentry.get("1.0", "end-1c")  # retrieve all text from the textbox
    recommendations = plant_doctor(user_input)
    recommendation_text.configure(state='normal')  # enable text widget for editing
    recommendation_text.delete('1.0', 'end')  # clear previous recommendations
    if recommendations:
        for recommendation in recommendations:
            recommendation_text.insert('end', "- " + recommendation + "\n\n")
    else:
        recommendation_text.insert('end', "No matching recommendations found. Please try different keywords or describe the issue in more detail.")
    recommendation_text.configure(state='disabled')  # disable text widget after editing
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
    symptomentry.delete('1.0', 'end')  # remove previous entry
    input.tkraise()  # go back to input page

welcome.tkraise()
app.geometry("800x600")
app.title("The Plant Doctor by Ethan Jordan")
app.mainloop()