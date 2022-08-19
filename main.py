from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="../flash-card-project-start/images/card_back.png")

canvas = Canvas(width=800, height=526)
canvas.create_image(400, 263, image=card_front_img)
canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)
#
# right_button_img = PhotoImage(file="../flash-card-project-start/images/right.png")
# wrong_button_img = PhotoImage(file="../flash-card-project-start/images/wrong.png")
# right_button = Button(image=right_button_img, highlightthickness=0)
# right_button.grid(column=1, row=1)
# wrong_button = Button(image=wrong_button_img, highlightthickness=0)
# wrong_button.grid(column=0, row=1)


window.mainloop()