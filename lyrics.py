import time 

v1 = "Please, don't see" 
v2 = "Just a boy caught up in dreams and fantasies" 
v3 = "Please, see me" 
v4 = "Reaching out for someone I can't see" 
v5 = "Take my hand"
v6 = "Let's see where we wake up tomorrow" 

def imprimir_com_ritmo1(frase, delay=0.9):
    palavras = frase.split()  # Divide a frase em palavras
    for palavra in palavras:
        print(palavra, end=' ', flush=True)  # Imprime a palavra na mesma linha
        time.sleep(delay)  # Pausa entre as palavras
    print()  # Pula para a linha seguinte após a frase completa

def imprimir_com_ritmo2(frase, delay=0.4):
    palavras = frase.split()  # Divide a frase em palavras
    for palavra in palavras:
        print(palavra, end=' ', flush=True)  # Imprime a palavra na mesma linha
        time.sleep(delay)  # Pausa entre as palavras
    print()  # Pula para a linha seguinte após a frase completa


def criar_letra():
    imprimir_com_ritmo1(v1)
    time.sleep(2)  # Pausa entre versos
    imprimir_com_ritmo2(v2)
    time.sleep(3)  
    imprimir_com_ritmo1(v3)
    time.sleep(3)  
    imprimir_com_ritmo2(v4)
    time.sleep(2)
    imprimir_com_ritmo2(v5)
    time.sleep(1)
    imprimir_com_ritmo2(v6)



# Executa a função para criar a letra da música
if __name__ == "__main__":
    criar_letra()