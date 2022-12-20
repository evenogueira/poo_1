class Conta:
  def __init__(self,saldo, agencia):
    self.saldo = saldo
    self.agencia = agencia


minha_conta = Conta(1000.00,1234)

teste_conta = Conta(22000.00,1111)


print("o saldo da minha conta é: ",minha_conta.saldo)
print("a agencia da minha conta é: ",minha_conta.agencia)

print("o saldo da teste conta é: ", teste_conta.saldo)
print("a agencia da teste conta é: ",teste_conta.agencia)