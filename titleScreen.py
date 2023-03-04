import tkinter
import customtkinter


def generateTitle():
    INFOTEXT = ["Welcome to Gravity Invaders!",
                "The object of this game is to collect space garbage!",
                "Watch out for asteroids! If you get too close, the gravitational field may pull you in!",
                "You will start with three lives.",
                "If you get yourself into a sticky situation, press spacebar to temporarily accelerate!"]
    customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
    customtkinter.set_default_color_theme(
        "blue"
    )  # Themes: blue (default), dark-blue, green

    app = customtkinter.CTk()  # create CTk window like you do with the Tk window
    app.geometry("600x600")
    
    i = 0
    def button_function():
        nonlocal i
        if i == len(INFOTEXT) - 1:
            app.destroy()
        else:
            i += 1
            text_var.set(INFOTEXT[i])


    text_var = tkinter.StringVar(value= INFOTEXT[0])

    label = customtkinter.CTkLabel(
        master=app,
        textvariable=text_var,
        width=500,
        height=500,
        fg_color=("white", "#252525"),
        corner_radius=8,
    )
    label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    button = customtkinter.CTkButton(master=app, text="CTkButton", command=button_function)
    button.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)
    app.mainloop()


if __name__ == "__main__":
    generateTitle()
