class empleados ():
    def __init__(self, ID, nombre, puesto, salario, antiguedad):
        self.id = ID
        self.nombre = nombre
        self.puesto = puesto
        self.salario = salario
        self.antiguedad = antiguedad
    
    def descansar (self):
        print("hora de descansar")
        
        
class programador (empleados):
    def __init__(self, ID, nombre, puesto, salario, antiguedad):
        super().__init__(ID, nombre, puesto, salario, antiguedad)
        
        
    def trabajar (self):
        print( f"hola soy: ", self.nombre, " y estoy programando")
        
       
class diseñador (empleados):
    def __init__(self, ID, nombre, puesto, salario, antiguedad):
        super().__init__(ID, nombre, puesto, salario, antiguedad)
        
    
    def trabajar (self):
        print(f"hola soy: ", self.nombre, " y estoy diseñando")
        
        
        
class soporte (empleados):
    def __init__(self, ID, nombre, puesto, salario, antiguedad):
        super().__init__(ID, nombre, puesto, salario, antiguedad)
        
        
    def trabajar (self):
        print(f"hola soy: ", self.nombre, " y estoy en soporte")
        
        
        
        
        
empleado1 = programador(34750, "JUAN", "PROGRAMADOR", 45000, "2 AÑOS")
empleado2 = diseñador (34751, "PEDRO", "DISEÑADOR",2000, "6 MESES")
empleado3 = soporte (34752, "HECTOR", "SOPORTE", 25000, "5 AÑOS")

empleado1.trabajar()
empleado2.trabajar()
empleado3.trabajar()
empleado1.descansar()
empleado2.descansar()
empleado3.descansar()
