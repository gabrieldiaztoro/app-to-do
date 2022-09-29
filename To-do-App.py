from ast import Delete
from cProfile import label  # adicionou sozinho
from tkinter import *
from tkinter import ttk  # adicionou sozinho
from dbd import *

# ------CORES

cor0 = "#000000"  # preta
cor1 = "#59656F"  # Cinza?
cor2 = "#feffff"  # branca
cor3 = "#0074eb"  # azul
cor4 = "#f04141"  # vermelho
cor5 = "#59b356"  # verde
cor6 = "#cdd1cd"  # cizenta


# ---------CRIANDO JANELA PRINCIPAL-----(PASSO 1)
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

# (PASSO 2) criando função para os botoes NOVO E ATUALIZAR


def main(a):
    # NOVO
    if a == "novo":
        for widget in frame_e_baixo.winfo_children():
            widget.destroy()

        def adicionar():
            tarefa_entry = entry.get()
            inserir([tarefa_entry])
            mostrar()

        lb = Label(frame_e_baixo, text="Insira nova tarefa", width=42, height=5, pady=15,
                   anchor=CENTER)  # removeu esta parte e deixou o fundo da cor oriinal do  bg.  fg=cor0, bg=cor2)
        lb.grid(row=0, column=0, sticky=NSEW)
        # ADD ENTRY (CAIXA DE TEXTO QUE IRA MANDAR PARA TAREFAS)
        entry = Entry(frame_e_baixo, width=15)
        entry.grid(row=1, column=0, sticky=NSEW)

        # ADICIONANDO BOTAO PARA (ADICIONAR TAREFA)
        b_adicionar = Button(frame_e_baixo, text="ADICIONAR", width=10, pady=11, height=1,
                             bg=cor6, fg=cor0, font="8", anchor="center", relief=RAISED, command=adicionar)
        b_adicionar.grid(row=2, column=0, sticky=NSEW, pady=15)


# ATUALIZAR
    if a == "atualizar":
        for widget in frame_e_baixo.winfo_children():
            widget.destroy()

        def on():

            lb = Label(frame_e_baixo, text="Atualize a tarefa", width=42, height=5, pady=15,
                       anchor=CENTER)  # removeu esta parte e deixou o fundo da cor oriinal do  bg.  fg=cor0, bg=cor2)
            lb.grid(row=0, column=0, sticky=NSEW)

            # ADD ENTRY (CAIXA DE TEXTO QUE IRA MANDAR PARA TAREFAS)
            entry = Entry(frame_e_baixo, width=15)
            entry.grid(row=1, column=0, sticky=NSEW)

            v_selecionado = listbox.curselection()[0]
            palavra = listbox.get(v_selecionado)
            entry.insert(0, palavra)

            tarefas = selecionar()

            def alterar():
                for item in tarefas:
                    if palavra == item[1]:
                        nova = [entry.get(), item[0]]
                        atualizar(nova)
                        entry.delete(0, END)
                mostrar()

            # ADICIONANDO BOTAO PARA (ATUALIZAR TAREFA)
            b_alterar = Button(frame_e_baixo, text="ATUALIZAR", width=10, pady=11, height=1,
                               bg=cor6, fg=cor0, font="8", anchor="center", relief=RAISED, command=alterar)
            b_alterar.grid(row=2, column=0, sticky=NSEW, pady=15)

        on()

# ADICIONANDO FUNCAO REMOVER


def remover():
    v_selecionado = listbox.curselection()[0]
    palavra = listbox.get(v_selecionado)
    tarefas = selecionar()

    for item in tarefas:
        if palavra == item[1]:
            deletar([item[0]])
    mostrar()


# ----CRIANDO BOTOES
b_novo = Button(frame_e_cima, text="NOVO", width=10, height=1,  # frame_e_cima# foi colocado ao vez da freme principal
                relief=RAISED, command=lambda: main("novo"), bg=cor3, fg="white", anchor="center", overrelief='ridge', font=("Arial 10 bold"))  # foi usado grid para criar botao ao vez de place
# adicionado  command=lambda:main("novo"), depois do PASSO 2
b_novo.grid(row=0, column=0, sticky=NSEW, pady=1)

b_remover = Button(frame_e_cima, text="REMOVER", width=10, height=1,  # frame_e_cima# foi colocado ao vez da freme principal
                   relief=RAISED, command=remover, bg=cor4, fg="white", anchor="center", overrelief='ridge', font=('Arial 10 bold'))  # foi usado grid para criar botao ao vez de place
b_remover.grid(row=0, column=1, sticky=NSEW, pady=1)
b_atualizar = Button(frame_e_cima, text="ATUALIZAR", width=10, height=1,  # frame_e_cima# foi colocado ao vez da freme principal
                     relief=RAISED, command=lambda: main("atualizar"), bg=cor5, fg="white", anchor="center", overrelief='ridge', font=("Arial 10 bold"))  # foi usado grid para criar botao ao vez de place
# adicionado  command=lambda:main("atualizar"), depois do PASSO 2
b_atualizar.grid(row=0, column=2, sticky=NSEW, pady=1)
# ----LABEL TAREFAS
label = Label(frame_direita, text="Tarefas", width=37, height=1, pady=7,
              padx=30, relief="flat", anchor=W, font=("Courier 20 bold"), fg=cor0, bg=cor2)
label.grid(row=0, column=0, sticky=NSEW, pady=1)
# ------Criando Caixa de listas
listbox = Listbox(frame_direita, font=("Courier 9 bold"), width=1)
listbox.grid(row=1, column=0, sticky=NSEW, pady=5)
# ----Adicionando tarefas na listbox

"""
tarefas = ["pagar contas", "assistir one piece",
           "encontrar o mundial do palmeiras"]
for item in tarefas:
    listbox.insert(END, item)
# PROXIMO PASSO, CRIAR BANCO DE DADOS, SEGUIR OS PASSOS NA ABA DBD
"""
# PROXIMO PASSO, APOS RETORNAR DA OUTRA JANELA, IMPORTAR O BANCO DE DADOS LA EM CIMA

# configurando para mostrar somente os nomes, sem os numeros e ()
"""
tarefas = selecionar()
for item in tarefas:
    listbox.insert(END, item[1])
"""


def mostrar():
    listbox.delete(0, END)
    tarefas = selecionar()
    for item in tarefas:
        listbox.insert(END, item[1])


mostrar()

# prox passo definir funcao dos botoes novo e atualizar, adicionado PASSO 2 LA EM CIMA
# (CONTINUACAO DO PASSO 1)


janela.mainloop()
