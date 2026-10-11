# Controle de Níveis de Água

Simulador desenvolvido em Python para o monitoramento de níveis de água em um reservatório, executado diretamente no terminal com suporte a alertas coloridos via biblioteca `colorama`.

## 📋 Descrição da Atividade
O objetivo é aplicar conceitos de programação estruturada, utilizando listas, funções, controle de fluxo e manipulação de pacotes externos no terminal.

## 🎚️ Níveis de Alerta
O sistema avalia os cinco níveis para o reservatório:
1. **Nível 1:** Muito baixo (crítico) — 🔴 Vermelho
2. **Nível 2:** Baixo — 🟡 Amarelo
3. **Nível 3:** Médio — 🟢 Verde
4. **Nível 4:** Alto — 🔵 Ciano
5. **Nível 5:** Muito alto (alerta) — 🔵 Azul

## 🛠️ Tecnologias Utilizadas
- **Python 3.x**
- **Biblioteca Colorama** (para estilização de texto no terminal)

## 📦 Instalação e Execução

1. Certifique-se de ter o Python instalado em sua máquina.
2. Instale a biblioteca `colorama` através do terminal/prompt de comando:
   ```bash
   pip install colorama