import random 

def generar_simulacion(numero_simulaciones):
    nombres_mascotas=["Flash", "Sasha", "Krilin", "Tanpico", "Katirina"]
    especies=["Mamifero", "Domestico", "Cuadrupedo"]
    razas=["Gato", "Perro", "tortuga"]
    nombres_propietarios=["Jaimito Carter", "Chilindrina Nieves", "Ramon Dones", "Juan Carlos Quicagran", "Juan Jose Gallego", "Andrey Monsalve Villa", "Fannerys Guardia Cuesta"]
    ciudades=["Medellin", "Cali", "Cucuta", "Quibdó", "Paris", "Namekusei"]
    tipos_servicios=["Revision General", "Castrado", "Limpieza", "Desparacitado", "Vacunacion"]
    
    simulaciones=[]
    for _ in range (numero_simulaciones):
        
        simulacion={
            "id_mascota":random.randint(0,200),
            "nombre_mascota":random.choice(nombres_mascotas),
            "especie":random.choice(especies),
            "raza":random.choice(razas),
            "edad(años)":random.randint(10,20),
            "peso(kg)":random.randint(3,7),
            "nombre_propietario":random.choice(nombres_propietarios),
            "ciudad":random.choice(ciudades),
            "tipo_servicio":random.choice(tipos_servicios),
            "costo_serevicio":random.randint(20000,100000)
        }
    
        probabilidad_error=random.random()
    
        if probabilidad_error<0.05:
            simulacion["id_mascota"]=None
        elif probabilidad_error<0.1:
            simulacion["id_mascota"]=random.choice([-22,-33,-3,0])
            simulacion["tipo_servicio"]=random.choice(["tirado por barranco", None])
        elif probabilidad_error<0.15:
            simulacion["ciudad"]="espagueti"
            simulacion["nombre_propietario"]=None
        elif probabilidad_error<0.2:
            simulacion["edad(años)"]=random.choice([None, -1, 999, 222])
            
        simulaciones.append(simulacion)
    
    
    print(simulaciones)