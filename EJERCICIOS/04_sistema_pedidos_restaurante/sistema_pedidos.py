listaMenu = list()
listaPedidos = list ()
from datetime import datetime

class Producto :
    def __init__(self, nombre, tamaño, precio):
        self.nombre = nombre
        
        self.tamaño = tamaño
        self.precio = precio
        
        
class Pedido :
    def __init__(self,):
        
        self.fecha_compra = datetime.now().date()
        self.lista_productos = list()
        
    def agregarProducto (self, producto) :
        
      self.lista_productos.append(producto)
            
    def totalProductos (self,) :
        total = 0
        for producto in self.lista_productos:
                
                total += producto.precio
            
        return total
    
pizzGarande = Producto ("pizza", "grande", 350) 
pizzaMediana =Producto ("pizza", "mediana", 250)
pizzaChica= Producto ("pizza", "chica", 150)
hamburguesa= Producto ("hamburguesa", "estandar", 120)
refresco= Producto ("coca", " estandar", 50) 
 

listaMenu = [pizzGarande, pizzaMediana, pizzaChica, hamburguesa, refresco]


cierre = input("fin de la jornada o crear pedido:  ").strip().lower()
while True : 
    
    if cierre != "fin de la jornada" and cierre !="crear pedido":
        print("opcion no valida intente de nuevo")
        cierre = input("fin de la jornada o crear pedido:  ").strip().lower()
        
    if cierre == "fin de la jornada":
        break  
    
        
    elif cierre == "crear pedido":      
        print("MENU: ")
        for numero, producto in enumerate(listaMenu, start=1) :
                print(numero, producto.nombre,   producto.tamaño,"precio: ", producto.precio,)
                
    pedido= Pedido()
    eleccion =input("eligue el numero de lo que desea:. O escriba salir  ").strip().lower()
    while True :
        
        if eleccion == "salir":
            break  
        elif eleccion.isdigit() :
            eleccion= int(eleccion)
            
            if 1 <= eleccion <= len(listaMenu):
                producto_elegido= listaMenu[eleccion -1]       
                pedido.agregarProducto(producto_elegido)
                total = pedido.totalProductos()

            else:   
                    print("el numero no es valido intentelo de nuevo ")
                
        else:
            print("dato incorrecto. escribe un numero o salir: ")
        eleccion = input("agrega el nuemro de lo que desea:  O escriba salir  ") 
    listaPedidos.append(pedido)
    print("total a pagar: ", total)   
    print("fecha de compra", pedido.fecha_compra)      
    cierre = input("fin de la jornada o crear pedido: ")
    