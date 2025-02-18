import math

modo_rad = False  # Simulando que o usuário está em graus
expressao = "sin(30) + cos(60) + tan(45)"

if not modo_rad:  # Se estiver em graus, converter
    expressao = expressao.replace("sin(", "math.sin(math.radians(")
    expressao = expressao.replace("cos(", "math.cos(math.radians(")
    expressao = expressao.replace("tan(", "math.tan(math.radians(")

# Fechar corretamente os parênteses abertos pelo replace
expressao = expressao.replace(")", "))")

print("Expressão final:", expressao)

# **Correção no eval**
resultado = eval(expressao, {"__builtins__": None, "math": math})
print("Resultado:", resultado)

