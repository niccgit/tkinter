import tkinter as tk

window = tk.Tk()
window.title("Visualizador de imagem")

image = tk.PhotoImage(master=window, file="imagem1.png")

label = tk.Label(window, image=image)
label.pack()
window.mainloop()

email = tk.Button(window, text="e-mail", )
email.pack()

senha = tk.Button(window, text="senha")
senha.pack()

acesso = tk.Button(window, text="ACESSAR")
acesso.pack()

# eu tentei mt ta leonid mas o problema não estava entre a mesa e a cadeira KKKKKKKKKKK (pelo menos dessa vez)
