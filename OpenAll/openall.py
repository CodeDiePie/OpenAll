########################################################################################################################
############################################ OpenAll Created 12/20/2020 ################################################
################################################# By: Joshua Bishop ####################################################
########################################################################################################################


#resources
import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
apps = []


#reads the save.txt file
if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]


#adds executable programs and removes duplicate input
def addApp():

    for widget in frame.winfo_children():
        widget.destroy()

    filename= filedialog.askopenfilename(initialdir="/", title="Select File",
                                         filetypes=(("executables","*.exe"),("all files","*.*")))
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="white")
        label.pack()


#runs selected programs
def runApps():
    for app in apps:
        os.startfile(app)


#  GUI formating
canvas = tk.Canvas(root, height=500, width=500, bg= "black")
canvas.pack()

frame = tk.Frame(root, bg="grey")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(root, text="Select Program", padx=10, pady=6, fg="white", bg="black", command=addApp)
openFile.pack()

runApps = tk.Button(root, text="Run", padx=10, pady=6, fg="white", bg="black", command=runApps)
runApps.pack()


Label = tk.Label(root, text="OpenAll Ver.0.0.1 Alpha - by: J.Bishop")
Label.pack()

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()


#keeps program open until manually closed
root.mainloop()


#writes the save.txt file
with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')


