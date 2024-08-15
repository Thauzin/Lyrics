import time 

v1 = "O destino deve estar nos olhando" 
v2 = "Com aquela cara de quem diz" 
v3 = "Eu tentei juntar vocês dois" 
v4 = "O destino deve estar nos olhando" 
v5 = "Decepcionado"
v6 = "Que pena, que pena" 

def imprimir_com_ritmo1(frase, delay=0.4):
    palavras = frase.split()  
    for palavra in palavras:
        print(palavra, end=' ', flush=True) 
        time.sleep(delay)
    print() 


def criar_letra():
    imprimir_com_ritmo1(v1)
    time.sleep(1)  
    imprimir_com_ritmo1(v2)
    time.sleep(2)  
    imprimir_com_ritmo1(v3)
    time.sleep(3)  
    imprimir_com_ritmo1(v4)
    time.sleep(2)
    imprimir_com_ritmo1(v5)
    time.sleep(2)
    imprimir_com_ritmo1(v6)



# Executa a função para criar a letra da música
if __name__ == "__main__":
    criar_letra()