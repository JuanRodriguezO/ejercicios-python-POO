saldo : 0
class CuentaBancaria:
    def __init__(self, titular, numero_cuenta, saldo):
        self.titular = titular
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo
        
        
    def depositar_monto (self, monto):
        if monto <= 0:
            return "no permitido"
        
        else :
          self. saldo += monto
        return "se realizo con exito"
    
    def retirar_monto(self, monto):
        if monto <= 0:
            return "no permitido"
        
        
        
        elif monto > self.saldo:
            return "saldo no disponible"
        
        else :
            
           self.saldo -= monto
            
        return "se realizo con exito"   
cliente = CuentaBancaria("juan rodriguez", 33104, 1000)
while True:
    accion = input ("retirar depositar salir ")
  
    if accion.lower()== "retirar":
    
         monto = float(input("cuanto desea retirar? "))
         cliente.retirar_monto(monto)
         nopermitido = cliente.retirar_monto(monto)
         
         print(nopermitido)
         
    elif accion.lower()== "depositar":
         monto = float(input("cuanto desea depositar? "))
         cliente.depositar_monto(monto)
         nopermitido = cliente.depositar_monto(monto)
         
         
         print(nopermitido)
         
        
    
    elif accion.lower()== "salir":
        break
    
    
    
    