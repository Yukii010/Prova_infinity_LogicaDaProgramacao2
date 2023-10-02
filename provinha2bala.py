# Solicita a velocidade do carro ao usuário
velocidade = float(input("Digite a velocidade do carro em km/h: "))

# Verifica se a velocidade é superior a 80 km/h
if velocidade > 80:
    # Calcula a quantidade de quilômetros acima de 80 km/h
    quilometros_acima = velocidade - 80
    
    # Calcula o valor da multa, que é R$20,00 por cada km acima de 80 km/h
    valor_multa = quilometros_acima * 20
    
    # Exibe a mensagem de multa e o valor
    print(f"Você foi multado! A velocidade estava {quilometros_acima:.2f} km/h acima do limite de 80 km/h.")
    print(f"O valor da multa é de R${valor_multa:.2f}")
else:
    print("Você está dentro do limite de velocidade. Dirija com segurança!")
