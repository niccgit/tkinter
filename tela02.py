import tkinter as tk

window = tk.Tk()
window.title("Tela 02")
window.geometry("1920x1080")
window.config(bg="white")

menu_topo = tk.PhotoImage(master=window, file='Menu - Top.png')

menu_label = tk.Label(window, image=menu_topo, bg='white')
menu_label.place(relx=0.3, rely=0.1, anchor='e')

logo_topo = tk.PhotoImage(master=window, file='imagem1.png')

logo_topo_reduzida = logo_topo.subsample(4,4)

logo_label = tk.Label(window, image=logo_topo_reduzida)
logo_label.place(relx=1, rely=0.10, anchor="e")

menu_centro = tk.PhotoImage(master=window, file='Menu- Center.png') 

centro_label = tk.Label(window, image=menu_centro, bg='white')
centro_label.place(relx=0.5, rely=0.5, anchor='center')

texto_label = tk.Label(
    window,
    text="PRECISA DE AJUDA?",
    font=("Arial", 20),
    fg="#2a8fc4",
    bg="white"
)
texto_label.place(relx=0.5, rely=0.9, anchor='center')

window.mainloop()
