import random
import tkinter as tk

from tkcalendar import Calendar
from PIL import Image, ImageTk

# Importing custom widgets
from ExamProject.src.RoundedButton import RoundedButton
from ExamProject.src.GradientFrame import GradientFrame

# Initialize the root window
root = tk.Tk()
root.minsize(width=600, height=800)
root.title('Fitlistic')
root.configure(background="White")

# Variable to store the user's name (used across different GUI screens)
name = tk.StringVar()

# Constants for design elements
BUTTON_WIDTH_BIG = 300
BUTTON_WIDTH_SMALL = 200
BUTTON_HEIGHT_SMALL = 50
BUTTON_HEIGHT_BIG = 75
BUTTON_RADIUS_SMALL = 25
BUTTON_RADIUS_BIG = 35
BUTTON_PADDING = 2

BUTTON_COLOR_GREEN = '#42D742'
BUTTON_COLOR_BLUE = '#0cc0df'

LOGO_SIZE = (300, 300)

# Dictionary to store motivational quotations
quotations = {
    1: "Exercises is king and nutrition is queen. Combine the two and you will have a kingdom.",
    2: "The only bad workout is the one that didn't happen.",
    3: "Fitness is not about being better than someone else. It's about being better than you used to be."
}

# --- Start of first part from Reference 4 (Code used from ChatGPT) ---


# List of image file paths and corresponding descriptions
image_text_pairs = [
    ("../ExamProject/images/Squat.png", "15x3 Squat"),
    ("../ExamProject/images/Dips.png", "10x4 Dips"),
    ("../ExamProject/images/Meditate.png", "3 Minute Breathwork"),
    ("../ExamProject/images/Plank.png", "30 Seconds Plank"),
    ("../ExamProject/images/Stretch.png", "1 Minute Stretch")
]


# --- End of first part from Reference 4 (Code used from ChatGPT) ---

# Function to clear all widgets from the root window
def clear_widgets(root):
    for widget in root.winfo_children():
        widget.destroy()


# Function to set up the introduction GUI screen
def intro_gui(root):
    clear_widgets(root)  # Clear previous widgets

    # Load and display the logo image
    image_file_path = "images/Logo.png"
    image = Image.open(image_file_path)
    image = image.resize(LOGO_SIZE, Image.Resampling.LANCZOS)

    root.logo_image = ImageTk.PhotoImage(image)
    logo_label = tk.Label(root, image=root.logo_image, bg="white")
    logo_label.place(relx=0.5, y=150, anchor="center")  # Position the logo in the center at y=150

    # Display the slogan text below the logo
    slogan_label = tk.Label(root,
                            text="Your holistic fitness journey starts here",
                            font=('Arial', 18, 'bold'),
                            bg="white", fg="black")
    slogan_label.place(relx=0.5, y=250, anchor="center")

    # Entry field label and input for user's name
    entry_label = tk.Label(root,
                           text="Enter your name:",
                           font=('Arial', 20),
                           bg='white')
    entry_label.place(relx=0.5, y=400, anchor='center')

    name_entry = tk.Entry(root, textvariable=name, font=('Arial', 20), bg='grey')
    name_entry.place(relx=0.5, y=450, anchor='center')

    # 'Get Started' button to move to the next screen (overview)
    button = RoundedButton(root,
                           BUTTON_WIDTH_BIG,
                           BUTTON_HEIGHT_BIG,
                           BUTTON_RADIUS_BIG,
                           BUTTON_PADDING,
                           BUTTON_COLOR_GREEN,
                           'white',
                           text="Get Started",
                           text_color="white",
                           command=lambda: overview_gui(root, name.get())  # Pass the user's name to the overview screen
                           )
    button.place(relx=0.5, y=600, anchor="center")


# Helper function to create a workout button and position it
def start_workout_button(root, text, command, y_position):
    button = RoundedButton(
        root,
        BUTTON_WIDTH_BIG,
        BUTTON_HEIGHT_SMALL,
        BUTTON_RADIUS_SMALL,
        1,
        BUTTON_COLOR_GREEN,
        'white',
        text=text,
        text_color="white",
        command=command
    )
    button.place(relx=0.5, y=y_position, anchor="center")  # Position button at specified y-coordinate


# Function to set up the overview GUI screen
def overview_gui(root, user_name):
    clear_widgets(root)  # Clear previous widgets

    # Add a gradient background frame
    gradient_frame = GradientFrame(root, "lightgreen", "green", bg_color="white")
    gradient_frame.pack(fill="both", expand=True)

    # Display welcome message with user's name
    welcome_label = tk.Label(root,
                             text=f"Welcome back, {user_name}",
                             font=('Arial', 18, 'bold'),
                             bg="white", fg="black")
    welcome_label.place(relx=0.5, y=100, anchor="center")

    # Display 'Wellbeing Score' label
    score_label = tk.Label(root,
                           text="Wellbeing Score",
                           font=('Arial', 18, 'bold'),
                           bg="white", fg="black")
    score_label.place(relx=0.5, y=230, anchor="center")

    # Load and display the score image
    image_score_file_path = "../ExamProject/images/Score.png"

    image_score = Image.open(image_score_file_path)
    image_score = image_score.resize((335, 177))

    root.score_image = ImageTk.PhotoImage(image_score)
    score_image_label = tk.Label(root, image=root.score_image, bg="white")
    score_image_label.place(relx=0.5, y=335, anchor="center")

    # Display 'Start a Session' label
    start_label = tk.Label(root,
                           text="Start a Session",
                           font=('Arial', 18, 'bold'),
                           bg="white", fg="black")
    start_label.place(relx=0.5, y=475, anchor="center")

    # Use of the helper function to create the buttons
    start_workout_button(root, "Fullbody Workout", lambda: exercise_gui(root, name.get()), 540)
    start_workout_button(root, "Upperbody Workout", lambda: exercise_gui(root, name.get()), 600)
    start_workout_button(root, "Power Recovery", lambda: exercise_gui(root, name.get()), 660)

    reminder_gui_button = RoundedButton(root,
                                        BUTTON_WIDTH_BIG,
                                        BUTTON_HEIGHT_SMALL,
                                        BUTTON_RADIUS_SMALL,
                                        BUTTON_PADDING,
                                        BUTTON_COLOR_BLUE,
                                        'white',
                                        text="Set a workout reminder",
                                        text_color="white",
                                        command=lambda: reminder_gui(root, name.get())
                                        )
    reminder_gui_button.place(relx=0.5, y=750, anchor="center")


# Function to set up the reminder GUI screen
def reminder_gui(root, user_name):
    clear_widgets(root)  # Clear previous widgets

    # Add a gradient background frame
    gradient_frame = GradientFrame(root, "lightgreen", "green", bg_color="white")
    gradient_frame.pack(fill="both", expand=True)

    # Display header label
    reminder_label = tk.Label(root,
                              text="Choose a date to be reminded to workout",
                              font=('Arial', 18, 'bold'),
                              bg="white", fg="black")
    reminder_label.place(relx=0.5, y=100, anchor="center")

    # Create and display the calendar widget
    cal = Calendar(root, selectmode='day', year=2024, month=8, day=19)
    cal.place(relx=0.5, y=350, anchor="center")

    # Using the date from the calendar to display the selected date
    def on_date_select():
        selected_date = cal.get_date()
        reminder_label = tk.Label(root,
                                  text=f"You will be reminded to do a workout on the {selected_date}",
                                  font=('Arial', 15, 'italic'), bg="white", fg="black", wraplength=550)
        reminder_label.place(relx=0.5, y=575, anchor="center")


    # Button to confirm the selected date
    set_reminder_button = RoundedButton(root,
                                        BUTTON_WIDTH_BIG,
                                        BUTTON_HEIGHT_SMALL,
                                        BUTTON_RADIUS_SMALL,
                                        BUTTON_PADDING,
                                        BUTTON_COLOR_BLUE,
                                        'white',
                                        text="Set Reminder",
                                        text_color="white",
                                        command=on_date_select
                                        )
    set_reminder_button.place(relx=0.5, y=500, anchor="center")

    # Button to return to the overview screen
    button = RoundedButton(root,
                           BUTTON_WIDTH_BIG,
                           BUTTON_HEIGHT_BIG,
                           BUTTON_RADIUS_BIG,
                           BUTTON_PADDING,
                           BUTTON_COLOR_GREEN,
                           'white',
                           text="Back home",
                           text_color="white",
                           command=lambda: overview_gui(root, name.get())
                           )
    button.place(relx=0.5, y=675, anchor="center")


# Function to set up the exercise session GUI screen
def exercise_gui(root, user_name):
    clear_widgets(root)  # Clear previous widgets

    # Add a gradient background frame
    gradient_frame = GradientFrame(root, "lightblue", "blue", bg_color="white")
    gradient_frame.pack(fill="both", expand=True)

    # Display exercise session header
    exercise_label = tk.Label(root,
                              text="Exercise Session",
                              font=('Arial', 18, 'bold'),
                              bg="white", fg="black")
    exercise_label.place(relx=0.5, y=75, anchor="center")

    # Display exercise details
    details_label = tk.Label(root,
                             text="5 Exercises | 15 Minutes | 150 Calorie Burn",
                             font=('Arial', 14,),
                             bg="black", fg="white")
    details_label.place(relx=0.5, y=125, anchor="center")

    # 'Workout completed' button to end the session
    button = RoundedButton(root,
                           BUTTON_WIDTH_BIG,
                           BUTTON_HEIGHT_BIG,
                           BUTTON_RADIUS_BIG,
                           BUTTON_PADDING,
                           BUTTON_COLOR_GREEN,
                           'white',
                           text="Workout completed",
                           text_color="white",
                           command=lambda: finish_gui(root, name.get())
                           )
    button.place(relx=0.5, y=675, anchor="center")

    # Load and display the cancel button image
    photo = Image.open("images/X.png")
    photo = photo.resize((30, 30), Image.Resampling.LANCZOS)
    photo_image = ImageTk.PhotoImage(photo)

    cancel_button = tk.Button(root, bg="white", font="Helvetica", image=photo_image, compound=tk.LEFT,
                              command=lambda: overview_gui(root, user_name))
    cancel_button.image = photo_image  # Keep a reference to avoid garbage collection
    cancel_button.place(relx=0.05, rely=0.04, anchor="center")

    # Set up container for exercise images and descriptions
    screen_height = root.winfo_screenheight()
    top_margin_height = int(screen_height * 0.22)

    container = tk.Frame(gradient_frame, bg="white")
    container.pack(pady=(top_margin_height, 20), fill="x")

    # --- Start of second part from Reference 4 (Code used from ChatGPT) ---
    # Code that displays the exercises with the given image and text
    for image_path, description in image_text_pairs:
        frame = tk.Frame(container, bg="white")
        frame.pack(pady=10, padx=20, anchor="center")

        image = Image.open(image_path)
        image = image.resize((50, 50), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        image_label = tk.Label(frame, image=photo, bg="white")
        image_label.image = photo  # Keep a reference to prevent garbage collection
        image_label.pack(side="left", padx=10)

        text_label = tk.Label(frame, text=description, bg="white", font=('Arial', 14), anchor="w")
        text_label.pack(side="left", padx=10)
    # --- End of second part from Reference 4 (Code used from ChatGPT) ---


# Function to set up the completion screen after an exercise session
def finish_gui(root, user_name):
    clear_widgets(root)  # Clear previous widgets

    # Load and display the finish image
    image_finish_file_path = "../ExamProject/images/Finish.png"
    image_finish = Image.open(image_finish_file_path)
    image_finish = image_finish.resize((255, 327), Image.Resampling.LANCZOS)

    root.finish_image = ImageTk.PhotoImage(image_finish)
    finish_image_label = tk.Label(root, image=root.finish_image, bg="white")
    finish_image_label.place(relx=0.5, y=200, anchor="center")

    # Selecting one of the quotes with the random library
    motivational_quote = random.choice(list(quotations.values()))

    # Display completion message with user's name
    completed_label = tk.Label(root,
                               text=f"Congratulations {user_name}, you have completed your session!",
                               font=('Arial', 18, 'bold'), bg="white", fg="black", wraplength=500)
    completed_label.place(relx=0.5, y=450, anchor="center")

    # Display a motivational quote
    quote_label = tk.Label(root,
                           text=motivational_quote,
                           font=('Arial', 14, 'italic'),
                           bg="white", fg="black", wraplength=500)
    quote_label.place(relx=0.5, y=525, anchor="center")

    # Button to return to the overview screen
    button = RoundedButton(root,
                           BUTTON_WIDTH_BIG,
                           BUTTON_HEIGHT_BIG,
                           BUTTON_RADIUS_BIG,
                           BUTTON_PADDING,
                           BUTTON_COLOR_GREEN,
                           'white',
                           text="Back home",
                           text_color="white",
                           command=lambda: overview_gui(root, name.get())
                           )
    button.place(relx=0.5, y=675, anchor="center")


# Setting intro_gui as the initial screen
intro_gui(root)

root.mainloop()
