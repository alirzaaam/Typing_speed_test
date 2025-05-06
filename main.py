import tkinter as  tk
import time
import random


SENTENCE = ["I live in a house near the mountains",
            "We do lots of things together",
            "Police officers are law enforcement professionals",
             "Farmers maintain fields of crops",
             "London is a famous and historic city",
             "It goes without saying that humans",
             "I take classes at the local university"]

WORD_COUNT = 0
SCORE = 0
COUNTER = 0
WPM = 0
TIME = 0
START_TIME = 0
random.shuffle(SENTENCE)

def reset_color():
    txt_box.config(bg="white")

def elapsed_time():
    global TIME
    global GAME

    TIME += 1
    lbl_time.config(text=f"Time: {TIME}")
    lbl_time.after(1000, elapsed_time)


def clear_text():
    txt_box.delete(0, tk.END)

def play(event):
    txt_box.config(bg="green")
    global WORD_COUNT
    global SCORE
    global SENTENCE
    global COUNTER
    global WPM

    if COUNTER + 1 > len(SENTENCE):
        txt_box.config(state="disabled")
        label_text.config(state="disabled")
        lbl_time.destroy()
        lbl_result.config(text=f"WPM: {WPM:.2f}")


    label_text['text'] = SENTENCE[COUNTER]

    
    if txt_box.get() == label_text['text']:
        WORD_COUNT +=len(label_text['text'])
        clear_text()
        SCORE += 1
        # print("Correct")
        COUNTER += 1
        elapsed_time = time.time() - START_TIME
        WPM  = WORD_COUNT / (elapsed_time / 60)
        play(event)
    else:
        txt_box.config(bg="red")
        txt_box.after(500, reset_color)
        # print("Wrong")



def game():
    global START_TIME
    
    elapsed_time()
    lbl_time.grid(row=0, column=0, padx=0, pady=10)
    label_text.grid(row=3, column=1, padx=0, pady=10)
    txt_box.grid(row=1, column=1, padx=0, pady=10)
    game_btn.destroy()
    lbl_start.destroy()
    START_TIME = time.time() 

window = tk.Tk()
window.geometry("500x400")
window.title("Typing Speed Test")
font=('Times', 12, "bold")

lbl_time = tk.Label(window, text=f"Time: {TIME}", font=font)

label_text = tk.Label(window, text=SENTENCE[COUNTER])

txt_box = tk.Entry(window, bg='white', font=font, width=40)

lbl_result = tk.Label(window, font=font)
lbl_result.grid(row=4, column=1,padx=10, pady=10)

lbl_start = tk.Label(window, text="After typing each sentence, press ENTER", font=font)
lbl_start.grid(row=5, column=1, padx=100)
game_btn = tk.Button(window, text="START", command=game, height=4, width=10, font=font)
game_btn.grid(row=6, column=1, padx=110, pady=110)

window.bind("<Return>", play)


window.mainloop()