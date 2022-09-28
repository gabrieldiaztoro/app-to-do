from cProfile import label
from tkinter import *
from tkinter import ttk

# ------CORES

cor0 = "#000000"  # preta
cor1 = "#59656F"  # Cinza?
cor2 = "#feffff"  # branca
cor3 = "#0074eb"  # azul
cor4 = "#f04141"  # vermelho
cor5 = "#59b356"  # verde
cor6 = "#cdd1cd"  # cizenta


# ---------CRIANDO JANELA PRINCIPAL-----
janela = Tk()
janela.resizable(width=False, height=False)
janela.geometry("500x225")
janela.title('To-Do')
janela.configure(background=cor2)

# ----CRIANDO FRAMES DENTRO DA JANELA
frame_esquerda = Frame(janela, width=300, height=200,
                       bg=cor2, relief="flat")
frame_esquerda.grid(row=0, column=0, sticky=NSEW)
# Sticky=NSEW, para preencher todo espaco, norte, sul, este oeste

frame_direita = Frame(janela, width=200, height=250,
                      bg=cor2, relief="flat")
frame_direita.grid(row=0, column=1, sticky=NSEW)

# ----frame esquerda dividida em duas partes
frame_e_cima = Frame(frame_esquerda, width=300, height=50,  # copiou de cima e mudou a janela, colocou o frame recem criada = frame_esquerda
                     bg=cor2, relief="flat")
frame_e_cima.grid(row=0, column=0, sticky=NSEW)

frame_e_baixo = Frame(frame_esquerda, width=300, height=150,
                      bg=cor2, relief="flat")
frame_e_baixo.grid(row=1, column=0, sticky=NSEW)


# ----CRIANDO BOTOES

b_novo = Button(frame_e_cima, text="NOVO", width=10, height=1,  # frame_e_cima# foi colocado ao vez da freme principal
                relief=RAISED, bg=cor3, fg="white", anchor="center", overrelief='ridge', font=("Arial 10 bold"))  # foi usado grid para criar botao ao vez de place
b_novo.grid(row=0, column=0, sticky=NSEW, pady=1)


b_remover = Button(frame_e_cima, text="REMOVER", width=10, height=1,  # frame_e_cima# foi colocado ao vez da freme principal
                   relief=RAISED, bg=cor4, fg="white", anchor="center", overrelief='ridge', font=('Arial 10 bold'))  # foi usado grid para criar botao ao vez de place
b_remover.grid(row=0, column=1, sticky=NSEW, pady=1)


b_atualizar = Button(frame_e_cima, text="ATUALIZAR", width=10, height=1,  # frame_e_cima# foi colocado ao vez da freme principal
                     relief=RAISED, bg=cor5, fg="white", anchor="center", overrelief='ridge', font=("Arial 10 bold"))  # foi usado grid para criar botao ao vez de place
b_atualizar.grid(row=0, column=2, sticky=NSEW, pady=1)


# ----LABEL TAREFAS

label = Label(frame_direita, text="Tarefas", width=37, height=1, pady=7,
              padx=30, relief="flat", anchor=W, font=("Courier 20 bold"), fg=cor0, bg=cor2)
label.grid(row=0, column=0, sticky=NSEW, pady=1)

# ------Criando Caixa de listas

listbox = Listbox(frame_direita, font=("Courier 9 bold"), width=1)
listbox.grid(row=1, column=0, sticky=NSEW, pady=5)


# ----Adicionando tarefas na listbox

tarefas = ["pagar contas", "assistir one piece",
           "encontrar o mundial do palmeiras"]
for item in tarefas:
    listbox.insert(END, item)


janela.mainloop()
