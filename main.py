from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
stop = False
check_marks = ""
reps = 0
# ---------------------------- TIMER RESET ------------------------------- # 


def reset():
    global stop
    global check_marks
    global reps
    canvas.itemconfig(timer_text, text="25:00")
    title_label.config(text="Timer", fg=GREEN)
    stop = True
    reps = 0
    check_marks = ""
    check_mark.config(text=check_marks)
# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        title_label.config(text="Break", fg=RED)
        count_down(LONG_BREAK_MIN*60)
    elif reps % 2 == 0:
        title_label.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_MIN*60)
    else:
        title_label.config(text="Work", fg=GREEN)
        count_down(WORK_MIN*60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    global stop
    global check_marks
    mins = "{:02d}".format(count // 60)
    secs = "{:02d}".format(count % 60)
    canvas.itemconfig(timer_text, text=f"{mins}:{secs}")

    if count > 0:
        counting_down = window.after(1000, count_down, count - 1)
        count -= 1
    elif count == 0:
        if reps in [1, 3, 5, 7]:
            check_marks += "✔"
            check_mark.config(text=check_marks)
        start_timer()

    if stop:
        reset()
        window.after_cancel(counting_down)
        stop = False


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

tomato_png = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_png)
timer_text = canvas.create_text(100, 130, text="25:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=2)

title_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
title_label.grid(row=0, column=2)

check_mark = Label(text=check_marks, bg=YELLOW, fg=GREEN, font=(FONT_NAME, 18, "bold"))
check_mark.grid(row=3, column=2)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=1)

reset_button = Button(text="Reset", highlightthickness=0, command=reset)
reset_button. grid(row=2, column=3)

window.mainloop()
