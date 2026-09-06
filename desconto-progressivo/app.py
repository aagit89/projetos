# ==============================================================================
# Descrição: Sistema de desconto progressivo para loja online
# ==============================================================================

print("--- Sistema de Desconto Progressivo ---")

# Solicita ao usuário que insira o valor total da compra
# Utiliza float() para permitir valores decimais
valor_compra = float(input("Digite o valor total da compra: R$ "))

# Estrutura de decisão para verificar as regras de desconto aplicáveis
if valor_compra < 200.00:
    # Menor que R$ 199,99: desconto de 5%
    taxa_desconto = 0.05
elif valor_compra >= 200.00 and valor_compra < 300.00:
    # Entre R$ 200,00 e R$ 299,99: desconto de 10%
    taxa_desconto = 0.10
else:
    # Maior ou igual a R$ 300,00: desconto de 15%
    taxa_desconto = 0.15

# Cálculo do valor do desconto e do valor final a ser pago
valor_desconto = valor_compra * taxa_desconto
valor_final = valor_compra - valor_desconto

# Exibe os resultados formatados com duas casas decimais
print("\n--- Resumo da Compra ---")
print(f"Valor original da compra: R$ {valor_compra:.2f}")
print(f"Desconto aplicado ({int(taxa_desconto * 100)}%): R$ {valor_desconto:.2f}")
print(f"Valor total a pagar: R$ {valor_final:.2f}")