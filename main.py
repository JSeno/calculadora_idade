# Importando a biblioteca tkinter
from tkinter import *
from tkinter import ttk


from tkcalendar import Calendar, DateEntry
from dateutil.relativedelta import relativedelta
from datetime import date, datetime


# -- Criação da janela principal --
janela = Tk()  # Criando a janela principal
janela.title("Calculadora de Idade")  # Titulo da janela
janela.geometry("310x400")  # Tamanho da janela
janela.resizable(False, False)  # Bloqueando o redimensionamento da janela


# Cores
cor1 = '#000000'  # Cor preta bem escura
cor2 = '#3b3b3b'  # Cor preta mais clara
cor3 = '#ffffff'  # Cor branca
cor4 = '#f7d00c'  # Cor dourada

# -- Criando função para calcular a idade --	
def calcular_idade():
    inicial = cal_1.get()
    termino = cal_2.get()
    
    dia, mes, ano = [int(f) for f in inicial.split('/')]
    data_inicial = date(ano, mes, dia)

    dia2, mes2, ano2 = [int(f) for f in termino.split('/')]
    data_nascimento = date(ano2, mes2, dia2)

    anos = relativedelta(data_inicial, data_nascimento).years
    meses = relativedelta(data_inicial, data_nascimento).months
    dias = relativedelta(data_inicial, data_nascimento).days

    l_app_anos['text'] = anos
    l_app_meses['text'] = meses
    l_app_dias['text'] = dias


# -- Criando Frames --
frame_cima = Frame(janela, width=310, height=140, pady=0, padx=0, relief=FLAT, bg=cor1)
frame_cima.grid(row=0, column=0)
frame_baixo = Frame(janela, width=310, height=260, pady=0, padx=0, relief=FLAT, bg=cor2)
frame_baixo.grid(row=1, column=0)

# -- Criando Labels para o frame cima --
l_calculadora = Label(frame_cima, text="Calculadora", width=25, height=1, padx=3, relief='flat', bg=cor1, font=('Ivy', 15, 'bold'), anchor='center', fg=cor3)
l_calculadora.place(x=0, y=30)
l_idade = Label(frame_cima, text="DE IDADE", width=11, height=1, padx=0, relief='flat', bg=cor1, font=('Arial', 35, 'bold'), anchor='center', fg=cor4)
l_idade.place(x=0, y=70)

# -- Criando Labels para o frame baixo --
l_data_inicial = Label(frame_baixo, text="Data inicial: ", height=1, padx=0, pady=0, relief='flat', bg=cor2, font=('Ivy', 11), anchor=NW, fg=cor3)
l_data_inicial.place(x=20, y=30)
cal_1 = DateEntry(frame_baixo, width=13, bg='darkblue', fg=cor3, borderwidth=2, date_pattern='dd/mm/yyyy', y=2022)
cal_1.place(x=170, y=30)

l_data_nascimento = Label(frame_baixo, text="Data de nascimento: ", height=1, padx=0, pady=0, relief='flat', bg=cor2, font=('Ivy', 11), anchor=NW, fg=cor3)
l_data_nascimento.place(x=20, y=70)
cal_2 = DateEntry(frame_baixo, width=13, bg='darkblue', fg=cor3, borderwidth=2, date_pattern='dd/mm/yyyy')
cal_2.place(x=170, y=70)

l_app_anos = Label(frame_baixo, text=" ", height=1, padx=0, pady=0, relief='flat', bg=cor2, font=('Ivy 25 bold'), anchor='center', fg=cor3)
l_app_anos.place(x=60, y=135)
l_app_anos_nome = Label(frame_baixo, text="Anos", height=1, padx=0, pady=0, relief='flat', bg=cor2, font=('Ivy 11 bold'), anchor='center', fg=cor3)
l_app_anos_nome.place(x=60, y=175)

l_app_meses = Label(frame_baixo, text=" ", height=1, padx=0, pady=0, relief='flat', bg=cor2, font=('Ivy 25 bold'), anchor='center', fg=cor3)
l_app_meses.place(x=140, y=135)
l_app_meses_nome = Label(frame_baixo, text="Meses", height=1, padx=0, pady=0, relief='flat', bg=cor2, font=('Ivy 11 bold'), anchor='center', fg=cor3)
l_app_meses_nome.place(x=140, y=175)

l_app_dias = Label(frame_baixo, text=" ", height=1, padx=0, pady=0, relief='flat', bg=cor2, font=('Ivy 25 bold'), anchor='center', fg=cor3)
l_app_dias.place(x=220, y=135)
l_app_dias_nome = Label(frame_baixo, text="dias", height=1, padx=0, pady=0, relief='flat', bg=cor2, font=('Ivy 11 bold'), anchor='center', fg=cor3)
l_app_dias_nome.place(x=220, y=175)

# -- Criando botão para calcular a idade --
b_calcular = Button(frame_baixo, command=calcular_idade, text="Calcular", width=20, height=1, relief='raised', overrelief='ridge', bg=cor2, font=('Ivy 10 bold'), fg=cor3)
b_calcular.place(x=70, y=225)







janela.mainloop()  # Loop infinito da janela
