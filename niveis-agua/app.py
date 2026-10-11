# Descrição: Controle de Níveis de Água

# Importa biblioteca colorama
from colorama import Fore, Style

def definir_alerta(nivel):
    """
    Retorna a mensagem de situação e a cor correspondente
    com base no nível do reservatório informado (1 a 5).
    """
    alertas = {
        1: ("Nível 1: Muito baixo (crítico)", Fore.RED),
        2: ("Nível 2: Baixo", Fore.YELLOW),
        3: ("Nível 3: Médio", Fore.GREEN),
        4: ("Nível 4: Alto", Fore.CYAN),
        5: ("Nível 5: Muito alto (alerta)", Fore.BLUE)
    }
    return alertas.get(nivel, ("Nível desconhecido", Fore.WHITE))

def simular_monitoramento():
    """
    Simula o monitoramento do reservatório de água percorrendo os níveis definidos.
    """
    # Lista armazenando os níveis do reservatório de 1 a 5
    niveis_reservatorio = [1, 2, 3, 4, 5]

    print("SISTEMA DE MONITORAMENTO DE RESERVATÓRIO DE ÁGUA")
    print("Iniciando simulação...\n")

    for nivel in niveis_reservatorio:
        mensagem, cor = definir_alerta(nivel)
        
        # Exibe a situação com a cor correspondente
        print(f"{cor}{mensagem}")
        
        # Restaura o estilo padrão do terminal após a exibição de cada mensagem
        print(Style.RESET_ALL)

    print("Simulação concluída.")

simular_monitoramento()