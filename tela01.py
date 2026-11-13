import tkinter as tk

window = tk.Tk()
window.title("Tela 01")
window.geometry("1200x600")
window.config(bg="white")

image = tk.PhotoImage(master=window, file="imagem1.png")

label = tk.Label(window, image=image)
label.place(relx=0.5, rely=0.17, anchor="center")

window.mainloop()