# Descrição: Sistema de Classificação de Consumo de Água
print("--- Sistema de Análise de Consumo de Água ---")

# Solicita o tipo de imóvel ao usuário
tipo_imovel = input("Digite o tipo de imóvel (comercial, casa ou apartamento): ").strip().lower()

# Solicita o consumo mensal convertendo diretamente para número decimal (float)
consumo = float(input("Digite o consumo mensal de água em m³ (ex: 15.5): "))

# Aplica as regras de negócio usando estruturas condicionais
if tipo_imovel == "comercial":
    print("\nResultado: Tarifa comercial aplicada – consulte o plano corporativo.")
    
elif tipo_imovel == "apartamento" and consumo < 10:
    print("\nResultado: Consumo econômico – excelente controle de água!")
    
elif (tipo_imovel == "apartamento" and consumo <= 25) or (tipo_imovel == "casa" and consumo <= 25):
    print("\nResultado: Consumo moderado – dentro do padrão residencial.")
    
else:
    print("\nResultado: Consumo excessivo – adote medidas de economia e verifique vazamentos.")