import tkinter
import customtkinter


def generateEnd(score = 0):
    INFOTEXT = [
        f"Congratulations! You achieved a score of {score}!",
        "Did you know there are over 130 million of pieces of space debris?",
        "If these pieces of debris enter our atmosphere, they could burn up and release toxic chemicals!",
        "Thanks for playing, and helping to clean up our corner of the galaxy 😀",
    ]
    customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
    customtkinter.set_default_color_theme(
        "blue"
    )  # Themes: blue (default), dark-blue, green

    app = customtkinter.CTk()  # create CTk window like you do with the Tk window
    app.geometry("800x800")

    i = 0

    def button_function():
        nonlocal i
        if i == len(INFOTEXT) - 1:
            app.destroy()
        else:
            i += 1
            text_var.set(INFOTEXT[i])

    text_var = tkinter.StringVar(value=INFOTEXT[0])

    label = customtkinter.CTkLabel(
        master=app,
        textvariable=text_var,
        width=800,
        height=800,
        fg_color=("white", "#252525"),
        corner_radius=8,
    )
    label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    button = customtkinter.CTkButton(master=app, text="Next", command=button_function)
    button.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)
    app.mainloop()


if __name__ == "__main__":
    generateEnd()
