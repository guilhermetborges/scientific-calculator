from tkinter import *
from tkinter import ttk
import math

pretofundo = '#212120';  brancofundo = '#b5b5b5' ; azulnum ='#37b098'

janela = Tk()
janela.title("Calculadora Científica") 
janela.geometry("300x390")
janela.configure(bg='white')


frame_cima = Frame(janela, bg='white', width=300, height=60)
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela, bg='white', width=300, height=300)
frame_baixo.grid(row=2, column=0)

frame_modo = Frame(janela, bg='#ffffff', width=300, height=35)
frame_modo.grid(row=1, column=0)

# Entrada para os números


global todos_valores
todos_valores = ''
valor_texto = StringVar()

# Variável para alternar entre graus e radianos
modo_rad = BooleanVar(value=False)  # Padrão: Radianos


# Funções
def calcular_resultado_(event):
    global todos_valores
    try:
        expressao = todos_valores

        if not modo_rad.get():  # Se estiver em graus
            expressao = expressao.replace("sin(", "math.sin(math.radians(")
            expressao = expressao.replace("cos(", "math.cos(math.radians(")
            expressao = expressao.replace("tan(", "math.tan(math.radians(")
            expressao = expressao.replace(")", "))")
            resultado = eval(expressao, {"__builtins__": None, "math": math})
        else:  # Se estiver em radianos
            expressao = expressao.replace("sin(", "sin(")
            expressao = expressao.replace("cos(", "cos(")
            expressao = expressao.replace("tan(", "tan(")
            resultado = eval(expressao, {"__builtins__": None}, math.__dict__)
        # Avaliar a expressão de forma segura
        valor_texto.set(str(resultado))
        todos_valores = str(resultado)
    except Exception:
        valor_texto.set("Erro")
        todos_valores = ""

def limpar_(event):
    global todos_valores    
    todos_valores=''
    valor_texto.set("")





def calcular_num(event):
    global todos_valores  
    todos_valores= todos_valores + str(event)
    valor_texto.set(todos_valores)





app_label = Label(frame_cima,textvariable=valor_texto ,width=19,height=2,padx=7,anchor=E,relief=RAISED,justify=RIGHT,font="Ivy 18 bold",bg='gray',fg='white')
app_label.place(x=0,y=0)




# Botões
b_tangente = Button(frame_baixo,command=lambda:calcular_num("tan("), text="tan", width=8, height=1, bg=pretofundo, fg='white' )
b_tangente.grid(row=0, column=0, padx=5, pady=5)

b_sin = Button(frame_baixo,command=lambda:calcular_num("sin("), text="sin", width=8, height=1, bg=pretofundo, fg='white' )
b_sin.grid(row=0, column=1, padx=5, pady=5)

b_cos = Button(frame_baixo,command=lambda:calcular_num("cos("), text="cos", width=8, height=1, bg=pretofundo, fg='white')
b_cos.grid(row=0, column=2, padx=5, pady=5)

b_sqrt = Button(frame_baixo,command=lambda:calcular_num("sqrt("), text="√", width=8, height=1, bg=pretofundo, fg='white')
b_sqrt.grid(row=0, column=3, padx=5, pady=5)

b_log = Button(frame_baixo,command=lambda:calcular_num("log("), text="log", width=8, height=1, bg=pretofundo, fg='white')
b_log.grid(row=1, column=0, padx=5, pady=5)


b_log10 = Button(frame_baixo,command=lambda:calcular_num("log10("), text="log10", width=8, height=1, bg=pretofundo, fg='white')
b_log10.grid(row=1, column=1, padx=5, pady=5)

b_e = Button(frame_baixo,command=lambda:calcular_num("e"), text="e", width=8, height=1, bg=pretofundo, fg='white')
b_e.grid(row=1, column=2, padx=5, pady=5)

b_pi = Button(frame_baixo,command=lambda:calcular_num("pi"), text="π", width=8, height=1, bg=pretofundo, fg='white')
b_pi.grid(row=1, column=3, padx=5, pady=5)

b_quadrado = Button(frame_baixo,command=lambda: calcular_num('**2'), text="x²", width=8, height=1, bg=pretofundo, fg='white')   
b_quadrado.grid(row=2, column=0, padx=5, pady=5)

b_elevado = Button(frame_baixo,command=lambda: calcular_num('**'), text="xʸ", width=8, height=1, bg=pretofundo, fg='white')
b_elevado.grid(row=2, column=3, padx=5, pady=5)

b_parenteseEsq = Button(frame_baixo,command=lambda: calcular_num("("), text="(", width=8, height=1, bg=pretofundo, fg='white')    
b_parenteseEsq.grid(row=2, column=1,)

b_parenteseDir = Button(frame_baixo,command=lambda: calcular_num(")"), text=")", width=8, height=1, bg=pretofundo, fg='white')
b_parenteseDir.grid(row=2, column=2, )

b_sobra = Button(frame_baixo,command=lambda: calcular_num('%'), text="resto", width=8, height=1, bg='black', fg='white')
b_sobra.grid(row=4, column=3, padx=5, pady=5)

b_div = Button(frame_baixo, command=lambda: calcular_num('/'), text="/", width=8, height=1, bg='black', fg='white')
b_div.grid(row=4, column=0, padx=5, pady=5)

b_limpar = Button(frame_baixo, command=lambda: limpar_(""), text="C", width=13, height=1, bg='#561959', fg='white',relief=RAISED)
b_limpar.grid(row=4, column=1, columnspan=2, padx=5, pady=5)

b_mult = Button(frame_baixo, command=lambda: calcular_num('*'), text="x", width=8, height=1, bg='black', fg='white')
b_mult.grid(row=5, column=3, padx=5, pady=5)

b_7 = Button(frame_baixo, command=lambda: calcular_num('7'), text="7", width=8, height=1, bg=azulnum, fg='white')
b_7.grid(row=5, column=0, padx=5, pady=5)

b_8 = Button(frame_baixo, command=lambda: calcular_num('8'), text="8", width=8, height=1, bg=azulnum, fg='white')
b_8.grid(row=5, column=1, padx=5, pady=5)

b_9 = Button(frame_baixo, command=lambda: calcular_num('9'), text="9", width=8, height=1, bg=azulnum, fg='white')
b_9.grid(row=5, column=2, padx=5, pady=5)

b_sub = Button(frame_baixo,command=lambda: calcular_num('-'), text="-", width=8, height=1, bg='black', fg='white')
b_sub.grid(row=6, column=3, padx=5, pady=5)

b_4 = Button(frame_baixo, command=lambda: calcular_num('4'), text="4", width=8, height=1, bg=azulnum, fg='white')
b_4.grid(row=6, column=0, padx=5, pady=5)

b_5 = Button(frame_baixo, command=lambda: calcular_num('5'), text="5", width=8, height=1, bg=azulnum, fg='white')
b_5.grid(row=6, column=1, padx=5, pady=5)

b_6 = Button(frame_baixo, command=lambda: calcular_num('6'), text="6", width=8, height=1, bg=azulnum, fg='white')
b_6.grid(row=6, column=2, padx=5, pady=5)

b_soma = Button(frame_baixo,command=lambda: calcular_num('+'), text="+", width=8, height=1, bg='black', fg='white')
b_soma.grid(row=7, column=3, padx=5, pady=5)

b_1 = Button(frame_baixo, command=lambda: calcular_num('1'), text="1", width=8, height=1, bg=azulnum, fg='white')
b_1.grid(row=7, column=2, padx=5, pady=5)

b_2 = Button(frame_baixo, command=lambda: calcular_num('2'), text="2", width=8, height=1, bg=azulnum, fg='white')
b_2.grid(row=7, column=1, padx=5, pady=5)


b_3 = Button(frame_baixo, command=lambda: calcular_num('3'), text="3", width=8, height=1, bg=azulnum, fg='white')
b_3.grid(row=7, column=0, padx=5, pady=5)

b_ponto = Button(frame_baixo, command=lambda: calcular_num('.'), text=".", width=8, height=1, bg='black', fg='white')
b_ponto.grid(row=8, column=3, padx=5, pady=5)

b_0 = Button(frame_baixo, command=lambda: calcular_num('0'), text="0", width=8, height=1, bg=azulnum, fg='white')
b_0.grid(row=8, column=0, padx=5, pady=5)

b_igual = Button(frame_baixo, command= lambda: calcular_resultado_("="), text="=", width=13, height=1, bg='blue', fg='white')
b_igual.grid(row=8, column=1, columnspan=2, padx=5, pady=5)


# label modo


label = Label(frame_modo, text="Modo: ", bg='white', fg='black', font="Ivy 10 bold ").pack(side=LEFT, padx=5)
Radiobutton(frame_modo, text="Graus",variable=modo_rad, value=False, bg='white',font="Ivy 10 bold ").pack(side=LEFT)
Radiobutton(frame_modo, text="Radianos", variable=modo_rad, value=True, bg='white',font="Ivy 10 bold ").pack(side=LEFT)


janela.mainloop()