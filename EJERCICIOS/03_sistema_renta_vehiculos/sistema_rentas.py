from datetime import datetime
listaVehiculos = list()
listarentas = list()

class vehiculo ():
    
    def __init__(self, id, modelo, año, color, precio_por_dia, marca, transmision, capacidad_de_pasajeros):
        self.id = id 
        self.modelo = modelo 
        self.año = año
        self.color = color
        self.precio_por_dia = precio_por_dia
        self.disponibilidad = True
        self.marca = marca
        self.transmision = transmision
        self.capasidad_de_pasajeros = capacidad_de_pasajeros
        
    def devolver (self):
        if self.disponibilidad == False :
          self.disponibilidad = True   
          return "vehiculo devuelto"  
    
        else :
            
            return "vehiculo disponible"
        
            
    def rentar (self):
        if self.disponibilidad == True :
            self.disponibilidad = False
            
            return "vehiculo rentado"    
        else :
            
            return "vehiculo no disponible" 
        
    
        
        
class automovil (vehiculo) :
  def __init__(self, id, modelo, año, color, precio_por_dia, marca, transmision, capacidad_de_pasajeros, numero_puertas):
      super().__init__(id, modelo, año, color, precio_por_dia, marca, transmision, capacidad_de_pasajeros)
      self.numero_puertas =  numero_puertas
      
      
class motocicleta (vehiculo):
    def __init__(self, id, modelo, año, color, precio_por_dia, marca, transmision, capacidad_de_pasajeros, cilindraje):
        super().__init__(id, modelo, año, color, precio_por_dia, marca, transmision, capacidad_de_pasajeros)
        self.cilindraje= cilindraje
        
class camioneta (vehiculo):
    def __init__(self, id, modelo, año, color, precio_por_dia, marca, transmision, capacidad_de_pasajeros, capacidad_carga):
        super().__init__(id, modelo, año, color, precio_por_dia, marca, transmision, capacidad_de_pasajeros)
        self.capacidad_carga = capacidad_carga
        
class renta ():
    def __init__(self, cliente, vehiculo, fecha_inicio,  ):
        self.cliente = cliente
        self.vehiculo = vehiculo
        self.fecha_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d")
       
        
    def fecha_de_devolucion(self, fecha_devolucion, ):
        self.fecha_devolucion = datetime.strptime(fecha_devolucion, "%Y-%m-%d")
        
        total= self.fecha_devolucion -self.fecha_inicio 
        self.dias = total.days
        self.total = self.vehiculo.precio_por_dia * self.dias
        
        return self.total
        
class cliente ():
    def __init__(self, id_cliente, nombre, telefono, identificacion, licencia_conducir):
        self.idcliente = id_cliente
        self.nombre= nombre
        self.telefono = telefono
        self.identificacion = identificacion
        self.licencia = licencia_conducir
        
        
        
        
Automovil = automovil( 1,55, 2024, "rojo", 8000, "jac", "automatica", 5, 4)       
 
Motocicleta = motocicleta(2, 22, 2026, "blanco", 4500, "yamaha", "estadar", 2, 600 )

Camioneta = camioneta (3, 88, 2023, "negro", 15000, "toyota", "estandar", 2, "15 tls")




listaVehiculos = [Automovil, Motocicleta, Camioneta]       

while True :
    accion = input ("devolver o  rentar: ")
    idVehiculo = int( input("escribe el ID del vehiculo : "))

    if accion == "rentar":
        encontrado = False
        for vehiculo in listaVehiculos:
            if vehiculo.id == idVehiculo :
                fechaInicio= input("fecha de renta: aaaa-mm-dd: ")
            
                print("desea rentar el ", vehiculo.modelo, vehiculo.marca, vehiculo.transmision)
                decision = input("si / no: ")
        
                if decision == "si" :
                   Cliente = cliente(input("ID cliente: "), input("Nombre cliente: "), int(input("numero de celular: ")), int(input("No. de identificacion")), int(input("No. de licencia de conducir: ")),)
               
                   disponible = vehiculo.rentar()
                   print(disponible)  
                   encontrado = True
                   break
                elif decision == "no":
                    print ("vehiculo no rentado")
                    break
            
        if encontrado == False:
            print ("id incorrecto intentelo de nuevo")
            
        devolucion = renta( Cliente, vehiculo, fechaInicio)
        listarentas.append(devolucion)
        print(listarentas)
    
    elif accion == "devolver" :
        encontrado = False
        for rentaActual in listarentas :
            if rentaActual.vehiculo.id == idVehiculo :
            
                fechadevolucion = input("fecha de devolucion aaaa-mm-aa: ")
                total= rentaActual.fecha_de_devolucion(fechadevolucion)
                regreso = rentaActual.vehiculo.devolver()
                print ("se devolvio", rentaActual.vehiculo.modelo, rentaActual.vehiculo.marca, "total a pagar: ", total)
            
                encontrado = True
            
        if encontrado == False :
            print ("vehiculo no encontrado intente de nuevo")
        