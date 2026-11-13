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
logo_label.place(relx=0.97, rely=0.10, anchor="e")

menu_voltar = tk.PhotoImage(master=window, file='Back.png')

voltar_label = tk.Label(window, image=menu_voltar, bg='white')
voltar_label.place(relx=0.18, rely=0.2, anchor='e')

container_tabela = tk.Frame(window, bg="#1e272e")
container_tabela.place(relx=0.5, rely=0.5, anchor="center")

categorias = ['Palestra', 'Data', 'Local', 'Valor', 'Duração']
colunas = 8

for index_coluna, cat in enumerate(categorias):
    label_cat = tk.Label(container_tabela, text=cat, font=("Arial", 14, "bold"), fg="#ffffff", bg="#53d7ec", width=15,)
    label_cat.grid(row=0, column=index_coluna, padx=10, pady=15)

    for index_linha in range(1, colunas + 1):
        texto_lorem = f"Lorem {index_linha}"

        label_dado = tk.Label(container_tabela, text=texto_lorem, font=("Arial", 12), fg="white", bg="#2c3e50", width=15, relief="solid", bd=1)
        label_dado.grid(row=index_linha, column=index_coluna, padx=5, pady=5)

window.mainloop()