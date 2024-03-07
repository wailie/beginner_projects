import pandas
from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)


#Labels
label = Label(font=("Roboto", 20, "bold"))
label.config(text="Application Form")
label.grid(column=0, row=0)

student_info = {}

#Entries
entry = Entry(window, width=30, border=1)
#Add some text to begin with
entry.insert(END, string="Name - ")
entry.grid(column=0, row=3)

#Text
text = Text(height=2, width=30)
#Puts cursor in textbox.
text.focus()
#Adds some text to begin with.
text.insert(END, "Why do you want to attend this school? - ")
text.grid(column=2, row=3)


#label for spinbox
label2 = Label(font=("Roboto", 10, "normal"), text="(Min: 17/ Max: 25)\nAge: ")
label2.grid(column=0, row=5)
#Spinbox

def spinbox_used():
    return int(spinbox.get())
spinbox = Spinbox(from_=17, to=25, width=5, command=spinbox_used)
spinbox.grid(column=2, row=5)


#lable for scale
label3 = Label(font=("Roboto", 10, "normal"), text="Num of Semesters: ")
label3.grid(column=0, row=7)
#Scale
#Called with current scale value.
def scale_used(value):
    return int(value)
scale = Scale(from_=0, to=10, command=scale_used, orient=HORIZONTAL)
scale.grid(column=2, row=7)

yes_or_no = ""
#Checkbutton
def checkbutton_used():
    global yes_or_no
    #Prints 1 if On button checked, otherwise 0.
    if checked_state.get() == 1:
        yes_or_no = "Yes"
    elif checked_state.get() == 0:
        yes_or_no = "No"
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Have Paid? (Yes/No)", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.grid(column=0, row=9)


fresh_or_tran = ""
#Radiobutton
def radio_used():
    global fresh_or_tran
    if radio_state.get() == 1:
        fresh_or_tran = "Fresher"
    elif radio_state.get() == 2:
        fresh_or_tran = "Transfer"

#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Fresher", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Transfer", value=2, variable=radio_state, command=radio_used)
radiobutton1.grid(column=2, row=9)
radiobutton2.grid(column=2, row=10)

subject = ""
#Listbox
def listbox_used(event):
    global subject
    # Gets current selection from listbox
    subject = listbox.get(listbox.curselection())

listbox = Listbox(height=4, width=40)
majors = ["Computer Science", "Physics", "Management", "Chinese Language as a Second Language"]
for major in majors:
    listbox.insert(majors.index(major), major)
    listbox.bind("<<ListboxSelect>>", listbox_used)
    listbox.grid(column=0, row=12)


#Buttons
def action():
    #Gets name in entry
    name = entry.get().replace("Name - ", "")

    #Get's current value in textbox at line 1, character 0 remove question
    reason = text.get("1.0", END).replace("Why do you want to attend this school? - ", "")
    reason = reason.replace("\n", "")

    age = spinbox.get()

    semester = scale.get()

    paid_application_fee = yes_or_no

    student_type = fresh_or_tran

    major = subject

    if name != "":
        student_info.update({"Name": name})

    if reason != "":
        student_info.update({"Reason": reason})

    if age != 0:
        student_info.update({"Age": age})

    if semester != 0:
        student_info.update({"Number of Semesters": semester})

    if paid_application_fee != "":
        student_info.update({"Paid Application Fee?": paid_application_fee})

    if student_type != "":
        student_info.update({"Fresher or Transfer?": student_type})

    if subject != "":
        student_info.update({"Major": major})

    data_frame = pandas.DataFrame([student_info])
    print(data_frame)
    data_frame.to_csv("applicants_information.csv")

#calls action() when pressed
button = Button(text="Submit", command=action)
button.grid(column=3, row=12)


window.mainloop()


