from tkinter import *
import math


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


# -----------------------#
reps = 0
num_of_check = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def timer_reset():
    global timer_text, reps
    window.after_cancel(timer)
    canva.itemconfig(timer_text, text="00:00")
    title.config(text="Timer", fg=GREEN)
    ticks.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_second = WORK_MIN * 60
    short_break_second = SHORT_BREAK_MIN * 60
    long_break_second = LONG_BREAK_MIN * 60
    
    if reps % 8 == 0:
        title.config(text="Break", fg=RED)        
        count_down(long_break_second)
    elif reps % 2 == 0:
        title.config(text="Break", fg=PINK)
        count_down(short_break_second)
    else:
        title.config(text="Work", fg=GREEN)
        count_down(work_second)
        

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global num_of_check, timer
    count_minute = count // 60
    count_second = count % 60
    # Dynamic typing python
    if count_second < 10:
        count_second = f"0{count_second}"
    canva.itemconfig(timer_text, text=f"{count_minute}:{count_second}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    # Start timer for next session (e.g. work => break => work ...)
    elif count == 0:
        start_timer()
        num_of_check = math.floor(reps/2)
        ticks.config(text=f"{'✔' * num_of_check }")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.minsize(width=200, height=224)
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW, highlightthickness=0)


title = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
title.config(padx=10, pady=10)
title.grid(column=1, row=0)


canva = Canvas(width=200, height=224, bg=YELLOW)
tomato_img = PhotoImage(file="tomato.png")
canva.create_image(102, 112, image=tomato_img)
timer_text = canva.create_text(103, 130, text="00:00", font=(FONT_NAME, 25, "bold"), fill="white")
canva.grid(column=1, row=1)


start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)


reset_button = Button(text="Reset", command=timer_reset)
reset_button.grid(column=2, row=2)


ticks = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
ticks.grid(column=1, row=3)


window.mainloop()