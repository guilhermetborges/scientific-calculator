
'''
from tkinter import *
import math

# Cores
pretofundo = '#212120'
azulnum = '#37b098'

# Criando a Janela
janela = Tk()
janela.title("Calculadora Científica")
janela.geometry("300x420")
janela.configure(bg='white')

# Frames
frame_cima = Frame(janela, bg='white', width=300, height=60)
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela, bg='white', width=300, height=300)
frame_baixo.grid(row=2, column=0)

frame_modo = Frame(janela, bg='white', width=300, height=35)
frame_modo.grid(row=1, column=0)

# Variáveis globais
todos_valores = ''
modo_rad = BooleanVar(value=False)  # False = Graus, True = Radianos
valor_texto = StringVar()

# Função para calcular o resultado
def calcular_resultado():
    global todos_valores
    try:
        expressao = todos_valores
        # Avaliar a expressão com segurança
        resultado = eval(expressao, {"__builtins__": None}, math.__dict__)
        valor_texto.set(str(resultado))
        todos_valores = str(resultado)
    except Exception:
        valor_texto.set("Erro")
        todos_valores = ""

# Função para limpar a entrada
def limpar():
    global todos_valores
    todos_valores = ''
    valor_texto.set("")

# Função para atualizar os números digitados
def calcular_num(valor):
    global todos_valores
    todos_valores += str(valor)
    valor_texto.set(todos_valores)

# Display
app_label = Label(frame_cima, textvariable=valor_texto, width=19, height=2, padx=7,
                  relief=RAISED, anchor="e", justify=RIGHT, font="Ivy 18 bold",
                  bg='gray', fg='white')
app_label.place(x=0, y=0)

# Modo Graus/Radianos
Label(frame_modo, text="Modo:", bg='white', fg='black', font="Ivy 10 bold").pack(side=LEFT, padx=5)
Radiobutton(frame_modo, text="Graus", variable=modo_rad, value=False, bg='white', font="Ivy 10").pack(side=LEFT)
Radiobutton(frame_modo, text="Radianos", variable=modo_rad, value=True, bg='white', font="Ivy 10").pack(side=LEFT)

# Botões matemáticos
botoes = [
    ('tan(', 'sin(', 'cos(', 'sqrt('),
    ('log(', 'log10(', 'e', 'pi'),
    ('**2', '(', ')', '%'),
    ('/', 'C', '*', '-'),
    ('7', '8', '9', '+'),
    ('4', '5', '6', '.'),
    ('1', '2', '3', '='),
    ('0', '0', '', ''),
]

for i, linha in enumerate(botoes):
    for j, texto in enumerate(linha):
        if texto:
            cmd = calcular_resultado if texto == '=' else limpar if texto == 'C' else lambda t=texto: calcular_num(t)
            cor_fundo = pretofundo if texto in "/*-+C.=" else azulnum
            Button(frame_baixo, text=texto, width=8, height=1, bg=cor_fundo, fg='white',
                   command=cmd).grid(row=i, column=j, padx=5, pady=5, columnspan=(2 if texto == '0' else 1))

janela.mainloop()
'''

def recursao(n):
    
    if (n<=0):
        return 0
    else:
        return n * recursao(n-1);
    


print(recursao(5))


i=0
while i <5:
    i+=1
    if i ==3:
        continue
    print(i)