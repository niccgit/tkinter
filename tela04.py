import tkinter as tk

window = tk.Tk()
window.title("Tela 04")
window.geometry("1920x1080")
window.config(bg="white")

menu_topo = tk.PhotoImage(master=window, file='Menu - Top.png')

menu_label = tk.Label(window, image=menu_topo, bg='white')
menu_label.place(relx=0.3, rely=0.1, anchor='e')

logo_topo = tk.PhotoImage(master=window, file='imagem1.png')

logo_topo_reduzida = logo_topo.subsample(4,4)

logo_label = tk.Label(window, image=logo_topo_reduzida)
logo_label.place(relx=0.97, rely=0.10, anchor="e")

menu_voltar = tk.PhotoImage(master=window, file='Back.png')

voltar_label = tk.Label(window, image=menu_voltar, bg='white')
voltar_label.place(relx=0.18, rely=0.2, anchor='e')

texto_label = tk.Label(
    window,
    text="EDITAR CONSULTA",
    font=("Arial", 20, "bold"),
    fg="#2a8fc4",
    bg="white"
)
texto_label.place(relx=0.5, rely=0.2, anchor='center')

window.mainloop()
