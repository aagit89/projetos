# Entrada de dados
aparelho = input("Digite o nome do aparelho (ex.: Geladeira): ")
potencia = float(input("Digite a potência do aparelho em watts (W): "))
horas_dia = float(input("Digite o tempo médio de uso diário em horas: "))

# Processamento
consumo_mensal = (potencia * horas_dia * 30) / 1000
custo_estimado = consumo_mensal * 0.75

# Saída de dados
print(f"\nAparelho: {aparelho}")
print(f"Consumo estimado: {consumo_mensal:.2f} kWh/mês")
print(f"Custo estimado: R$ {custo_estimado:.2f} /mês")