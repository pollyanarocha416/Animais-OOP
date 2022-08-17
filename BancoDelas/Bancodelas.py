class Banco:
    def __init__(self,numero, titular, saldo):
          numero = numero 
          titular = titular 
          saldo = saldo
                 
class Cliente_mulher(Banco):
    def __init__(self, numero, titular, saldo, limite, sexo):
        
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.sexo = sexo
    
    def extrato(self): 
        
        print(f'Saldo atual: {self.saldo}') 
         
    def deposita(self, valor):
        self.saldo += valor
        print(f"Você depositou: {valor}") 
    def saca(self, valor):
        self.saldo -= valor
        print(f"Você sacou: {valor}")
    def exibir_dados_conta(self):
        direito = None
        self.limite += self.limite 
        if self.sexo == "masculino":
              direito = False
        else:
             direito = True
        print(f"Conta: {self.numero}, {self.titular}, renda mensal: {self.saldo}, limite: {self.limite}, {self.sexo}, tem direito a cheque especial? {direito}")
        

class Cliente_homem(Banco):
    def __init__(self, numero, titular, saldo, limite, sexo):
        
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.sexo = sexo
    def extrato(self): 
        
        print(f'Saldo atual: {self.saldo}') 
         
    def deposita(self, valor):
        self.saldo += valor
        print(f"Você depositou: {valor}") 
    def saca(self, valor):
        self.saldo -= valor
        print(f"Você sacou: {valor}")
    def exibir_dados_conta(self):
        direito = None
        if self.sexo == "masculino":
              direito = False
        else:
             direito = True
        print(f"Conta: {self.numero}, {self.titular}, renda mensal: {self.saldo}, limite: {self.limite}, {self.sexo}, tem direito a cheque especial? {direito}")

mulher = Cliente_mulher("555-333", "Julia", 1500, 1500, "feminino")       
mulher.exibir_dados_conta()    
mulher.saca(100)
mulher.extrato()
mulher.deposita(1000)
mulher.extrato()
homem = Cliente_homem("222-555", "felipe", 1500, 1500, "masculino")       
homem.exibir_dados_conta()
