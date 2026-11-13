import tkinter as tk

window = tk.Tk()
window.title("Tela 01")
window.geometry("1200x600")
window.config(bg="white")

image = tk.PhotoImage(master=window, file="imagem1.png")

label = tk.Label(window, image=image)
label.place(relx=0.5, rely=0.17, anchor="center")

email = tk.Entry(window, font=("Arial", 11), bg="#eeeeee", relief="solid", bd=1)
email.insert(0, "e-mail")
email.place(relx=0.5, rely=0.39, anchor="center", width=550, height=50)

senha = tk.Entry(window, font=("Arial", 11), bg="#eeeeee", relief="solid", bd=1)
senha.insert(0, "senha")
senha.place(relx=0.5, rely=0.52, anchor="center", width=550, height=50)

window.mainloop()