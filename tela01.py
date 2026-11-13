import tkinter as tk

window = tk.Tk()
window.title("Tela 01")
window.geometry("1920x1080")
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

botao_acessar = tk.Button(window, text="ACESSAR", font=("Arial", 11, "bold"), fg="white", bg="#2a8fc4", relief="raised", bd=1,)
botao_acessar.place(relx=0.5, rely=0.65, anchor="center", width=550, height=60)

botao_primeiro_acesso = tk.Button(window, text="PRIMEIRO ACESSO", font=("Arial", 10, "bold"), fg="#2a8fc4", bg="white", bd=0,)
botao_primeiro_acesso.place(relx=0.5, rely=0.77, anchor="center")

window.mainloop()