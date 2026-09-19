# ==============================================================================
# Pesquisa de Opinião - TudoWeb
# ==============================================================================

# Variáveis para armazenar as quantidades solicitadas
qtd_excelente = 0
qtd_ruim = 0

# Variáveis para quantidade de repetições
num_entrevistados = 50

print("="*40)
print("   PESQUISA DE SATISFAÇÃO - TUDOWEB")
print("="*40)
print("Opções: 1 - EXCELENTE | 2 - BOM | 3 - RUIM\n")

# Estrutura de repetição (for)
for i in range(num_entrevistados):
    print(f"--- Entrevistado {i + 1} de {num_entrevistados} ---")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    opiniao = int(input("Opinião (1, 2 ou 3): "))
    
    # Estrutura de decisão para verificar a opinião
    if opiniao == 1:
        qtd_excelente += 1
    elif opiniao == 2:
        # A opção BOM não é utilizada
        pass 
    elif opiniao == 3:
        qtd_ruim += 1
    else:
        print("Atenção: Opção inválida digitada. Considere apenas 1, 2 ou 3.")
    
    print("-" * 40)

# Exibição dos resultados finais
print("\n" + "="*40)
print("      RESULTADO FINAL DA PESQUISA")
print("="*40)
print(f"a) Quantidade de respostas 'EXCELENTE': {qtd_excelente}")
print(f"b) Quantidade de respostas 'RUIM': {qtd_ruim}")
print("="*40)