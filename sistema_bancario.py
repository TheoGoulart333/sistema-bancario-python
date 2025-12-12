# Sistema Bancário Otimizado com Funções 

saldo = 0
limite = 500 
extrato = "" 
numero_saques = 0 
LIMITE_SAQUES = 3 


def depositar(valor, saldo, extrato):
  if valor > 0: 
    saldo += valor 
    extrato += f"Depósito: R$ {valor:.2f}\n" 
  else: 
    print("Valor de depósito inválido!") 
  return saldo, extrato 
  
  
  def sacar(valor, saldo, extrato, limite, numero_saques, limite_saques): 
    excedeu_saldo = valor > saldo 
    excedeu_limite = valor > limite 
    excedeu_saques = numero_saques >= limite_saques 
    
  if excedeu_saldo: 
    print("Você não tem saldo suficiente!") 
  elif excedeu_limite: 
    print("Valor do saque excede o limite!") 
  elif excedeu_saques: 
    print("Número máximo de saques atingido!") 
  elif valor > 0: 
    saldo -= valor 
    extrato += f"Saque: R$ {valor:.2f}\n" 
    numero_saques += 1 
  else: print("Valor inválido para saque!") 
    
  return saldo, extrato, numero_saques 
  
  def mostrar_extrato(saldo, extrato): 
    print("\n========== EXTRATO ==========") 
    print(extrato if extrato else "Não foram realizadas movimentações.") 
    print(f"Saldo: R$ {saldo:.2f}") 
    print("============================\n") 
    
    
  def main(): global saldo, extrato, numero_saques 
    
  while True: 
    opcao = input(""" =============== MENU =============== 
    [d] Depositar 
    [s] Sacar 
    [e] Extrato 
    [q] Sair
    => """) 
    
       if opcao == "d": 
         valor = float(input("Informe o valor do depósito: ")) 
         saldo, extrato = depositar(valor, saldo, extrato) 
         
       elif opcao == "s": 
         valor = float(input("Informe o valor do saque: ")) 
         saldo, extrato, numero_saques = sacar(valor, saldo, extrato, limite, numero_saques, LIMITE_SAQUES) 
         
       elif opcao == "e": 
         mostrar_extrato(saldo, extrato) 
         
       elif opcao == "q": 
         break 
       else: 
         print("Operação inválida, tente novamente.") 
         
if __name__ == "__main__": main()
