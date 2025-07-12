"""
nome = input("Digite seu nome:")
tamanho_nome = len(nome)
print(f"Seu nome é {nome} e possui {tamanho_nome} letras.")
num1 = int(input("Digite um numero: "))
num2 = int(input("Digite um numero: "))
soma = num1+num2
print(f"A soma do {num1} + {num2} = {soma}")
"""
#Desafio Calculo de KPI
CONSTANTE_BONUS = 1000
nome = (input("Digite seu nome: "))
salario = float(input("Digite seu salário: "))
bonus = float(input("Digite a porcentagem do bonus: "))
kpi = CONSTANTE_BONUS + salario * bonus

print(f"{nome.capitalize()} o valor do seu kpi bônus 2025 é {kpi}")
