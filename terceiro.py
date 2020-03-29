#Saludo

convidado = "Convidado"
nome = input(str("Digite seu nome: "))

if(nome == ""):
    nome = convidado
    
print(f'Bem-vindo {nome}')