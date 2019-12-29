from source import *
from tkinter import *
from PIL import ImageTk, Image
import webbrowser

# Basic Window for GUI
root = Tk()
root.title("Maple")
root.iconbitmap("maple.ico")
root.geometry("400x400")

# Maple Banner
banner = ImageTk.PhotoImage(Image.open("maple_banner.png"))
Label(image=banner).grid(row=0, column=0)


def app():      # Button function
    if var.get() == "ZERO":
        gain_crystals()
    else:
        pass


def callback(event):        # Function for callable URL
    webbrowser.open_new(event.widget.cget("text"))


# Contents of GUI
var = StringVar()
var.set("ZERO")
Radiobutton(root, text="GAIN CRYSTALS BY FOLLOWING", variable=var, value="ZERO").grid(row=1, padx=120, sticky=W)
Radiobutton(root, text="GAIN CRYSTALS BY LIKING", variable=var, value="ONE", fg="grey").grid(row=2, padx=120, sticky=W)
Button(root, text="START", width=20, command=app).grid(row=3, pady=10)
Button(root, text="END", width=20, command=root.quit()).grid(row=4,pady=5)
Label(root, text="Join the community and learn how to setup the bot").grid()
URL = Label(root, text=r"http://bit.ly/39haqEi-maple", fg="blue", cursor="hand2")
URL.grid()
URL.bind("<Button-1>", callback)
Label(root, text="").grid(pady=10)
Label(root, text="Visit My GitHub for more projects").grid()
URL2 = Label(root, text=r"https://github.com/AVIXASH", fg="blue", cursor="hand2")
URL2.grid()
URL2.bind("<Button-1>", callback)

# End loop
root.mainloop()
