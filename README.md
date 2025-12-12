🏦 Sistema Bancário em Python
Um sistema bancário simples desenvolvido em Python, utilizando funções para organizar operações como depósito, saque e exibição de extrato.

Desenvolvido por Theo Goulart Cardoso Vasconcelos.




👤 Autor
Theo Goulart Cardoso Vasconcelos
GitHub: TheoGoulart333


📌 Funcionalidades:

- Depositar valores
- Realizar saques, com:
- Limite máximo por saque
- Limite de quantidade diária de saques
- Verificação de saldo
- Exibir extrato com todas as movimentações
- Menu interativo executado no terminal

🛠️ Tecnologias utilizadas:

- Python 3.x

  
📂 Estrutura do Código:

O programa é composto pelas seguintes funções:

- depositar(valor, saldo, extrato)
Realiza depósitos e registra no extrato.

- sacar(valor, saldo, extrato, limite, numero_saques, LIMITE_SAQUES)
Processa saques, respeitando limites e saldo.

- mostrar_extrato(saldo, extrato)
Exibe histórico e saldo.

- main()
Controla o menu e a interação com o usuário.


▶️ Como executar:

1- Certifique-se de ter o Python 3 instalado.
2- Baixe ou clone o repositório:
git clone https://github.com/TheoGoulart333/sistema-bancario-python.git
3- Acesse a pasta:
cd sistema-bancario-python
4- Execute o programa:
python sistema_bancario.py


📷 Exemplo de Uso:

=============== MENU ===============

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> d
Informe o valor do depósito: 200

=============== MENU ===============
=> e

========== EXTRATO ==========

Depósito: R$ 200.00
Saldo: R$ 200.00


🚀 Melhorias Futuras: 

- Implementar contas de múltiplos usuários
- Utilizar classes (POO)
- Persistência de dados
- Interface gráfica (Tkinter ou Web)

  
📄 Licença:
Projeto sob a licença MIT.
Criado por Theo Goulart Cardoso Vasconcelos — TheoGoulart333
