import customtkinter as ctk
from PIL import Image

# Fonction pour afficher un frame donné
def show_frame(frame):
    frame.tkraise()


#app window config
app = ctk.CTk()
app.title("HandSign Learning App")
#Screen max size
screen_height = app.winfo_screenheight()
screen_width = app.winfo_screenwidth()
app.geometry(f"{screen_width}x{screen_height}")

# Container for all pages
container = ctk.CTkFrame(app, width=screen_width, height=screen_height)
container.pack(fill="both", expand=True)

# Create pages
home_page = ctk.CTkFrame(container, fg_color="lightgray", width=800, height=600)
lrn_page = ctk.CTkFrame(container, fg_color="white", width=800, height=600)
page3 = ctk.CTkFrame(container, fg_color="lightgray", width=800, height=600)

# Placement de toutes les pages dans le conteneur
for frame in (home_page, lrn_page, page3):
    frame.grid(row=0, column=0, sticky="nsew")

# expanding row and columns' container
container.grid_rowconfigure(0, weight=1)
container.grid_columnconfigure(0, weight=1)

# Add widget to each page

# Home page
##Frame for text
txt_frame = ctk.CTkFrame(home_page)
txt_frame.grid(row=0, column=1, sticky="nsew")

##Text
hometxt1 = ctk.CTkLabel(txt_frame, text="WELCOME", text_color="#AD4933",font=("Century Gothic", 55))
hometxt1.pack(padx=0, pady=90)
hometxt2 = ctk.CTkLabel(txt_frame, text="Let's learn sign language together !", text_color="#AD4933",font=("Century Gothic", 25))
hometxt2.pack(padx=180, pady=90, anchor="e")

##Buttons
#b1
train_btn = ctk.CTkButton(txt_frame, text="Learning",text_color="black", font=("Century Gothic", 20), command=lambda: show_frame(lrn_page), corner_radius=75, height=40, width=155, fg_color="#AD4933", hover_color="white")
train_btn.pack()
#b2
pract_btn = ctk.CTkButton(txt_frame, text="Exercise", text_color="black", font=("Century Gothic", 20), command=lambda: show_frame(page3), corner_radius=75, height=40, width=155, fg_color="#AD4933", hover_color="white")
pract_btn.pack(pady=20)

##Frame for image
img_frame = ctk.CTkFrame(home_page)
img_frame.grid(row=0, column=0, sticky="nsew")
##image for home page
hands_image = ctk.CTkImage(light_image=Image.open("/home/rolyster/Documents/EnglishProject/hands.png"),
                                  dark_image=Image.open("/home/rolyster/Documents/EnglishProject/hands.png"),
                                  size=(screen_width/2, screen_height))

image_label = ctk.CTkLabel(img_frame, image=hands_image, text="", compound="left")
image_label.pack()




# Learning page

## Sidebar
sidebar = ctk.CTkFrame(lrn_page, width=300)
sidebar.pack(side="left", fill="y")

bartxt = ctk.CTkLabel(sidebar, text="LEARNING", text_color="#AD4933",font=("Century Gothic", 30))
bartxt.pack(padx=50, pady=40)

##btns
number_btn = ctk.CTkButton(sidebar, text="Numbers",text_color="#AD4933", font=("Century Gothic", 20), command=lambda: show_frame(lrn_page), height=40, width=300, fg_color="white", hover_color="gray")
number_btn.pack()

alpha_btn = ctk.CTkButton(sidebar, text="Alphabet",text_color="#AD4933", font=("Century Gothic", 20), command=lambda: show_frame(lrn_page), height=40, width=300, fg_color="white", hover_color="gray")
alpha_btn.pack(pady=20)

others_btn = ctk.CTkButton(sidebar, text="Others",text_color="#AD4933", font=("Century Gothic", 20), command=lambda: show_frame(lrn_page), height=40, width=300, fg_color="white", hover_color="gray")
others_btn.pack()





# Page 3
label3 = ctk.CTkLabel(page3, text="Ceci est la page 3", font=("Helvetica", 16))
label3.pack(pady=10)
button3_to_1 = ctk.CTkButton(page3, text="Retour à la page 1", command=lambda: show_frame(home_page))
button3_to_1.pack()
button3_to_2 = ctk.CTkButton(page3, text="Retour à la page 2", command=lambda: show_frame(lrn_page))
button3_to_2.pack()

# Affichage de la première page au démarrage
show_frame(home_page)

# Lancer la boucle principale de l'application
app.mainloop()

