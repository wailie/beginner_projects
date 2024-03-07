from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=200)
window.config(padx=20, pady=20)


#row 0
user_input = Entry(width=10, border=3)
user_input.grid(column=1, row=0)

measure = ""
def listbox_used(event):
    global measure
    # Gets current selection from listbox
    measure = listbox.get(listbox.curselection())
    update_label4_text()


def update_label4_text():
    if measure == "Mile":
        label4.config(text="Km")
    elif measure == "Km":
        label4.config(text="Mile")


listbox = Listbox(height=2, width=10)
measurements = ["Mile", "Km"]
for measurement in measurements:
    listbox.insert(measurements.index(measurement), measurement)
measure = listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.grid(column=2, row=0)



#row 1
label2 = Label(text="is equal to", font=("Roboto", 10, "normal"))
label2.grid(column=0, row=1)
label2.config(padx=10, pady=10)

label3 = Label(text=f"{0}", font=("Roboto", 10, "normal"))
label3.grid(column=1, row=1)
label3.config(padx=10, pady=10)

label4 = Label(text="Km", font=("Roboto", 10, "normal"))
label4.grid(column=2, row=1)
label4.config(padx=10, pady=10)
if measure == "Km":
    label4.config(text="Mile")


def convert():
    if measure == "Mile":
        try:
            mile = int(user_input.get())
        except ValueError:
            mile = 0 
        km = round(mile * 1.609344)
        label3.config(text=f"{km}")
    elif measure == "Km":
        try:
            km = int(user_input.get())
        except ValueError:
            km = 0
        mile = round(km / 1.609344)
        label3.config(text=f"{mile}")

#row 2
button = Button(text="Calculate", command=convert)
button.grid(column=1, row=2)
button.config(padx=5, pady=5)


window.mainloop()
