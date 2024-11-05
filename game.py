import random

def start_game():
    print("\nBienvenido al juego")
    new_game = input("¿Crear nueva partida? (si/no): ")
    
    if new_game == "si":
        global personaje
        personaje = Player()
        global abrirInventario
        abrirInventario = abrir_inventario() 
        choose_action()
    else:
        print("Saliendo del juego.")
class Player:
    def __init__(self):
        self.name = input("¿Cuál es tu nombre? ")
        self.stats = {
            "nivel": 1,
            "vida": 100,
            "monedas": 50000,
            "hierro": 0,
            "punto de encantamiento": 0,
            "elemento": 0
        }
        print(f"{self.name} nivel: {self.stats['nivel']} vida: {self.stats['vida']} monedas: {self.stats['monedas']}")

    def get_coins(self):
        return self.stats["monedas"]

    def restar_coins(self, cantidad):
        self.stats["monedas"] -= cantidad

    def show_stats(self):
        print(f"""
{self.name} 
nivel: {self.stats['nivel']} 
vida: {self.stats['vida']} 
monedas: {self.stats['monedas']} 
hierro: {self.stats['hierro']} 
punto de encantamiento: {self.stats['punto de encantamiento']}
""")

itemPosition = 1
class abrir_inventario():
    def __init__(self):
        self.inventario = {
            "item1":None,
            "item2":None,
            "item3":None,
            "item4":None,
            "item5":None,
            "item6":None,
            "item7":None,
            "item8":None,
            "item9":None,
            "item10":None,
        }
        self.inventario_magico = {
            "item1":None,
            "item2":None,
            "item3":None,
            "item4":None,
            "item5":None,
            "item6":None
        }
    def agregarItem1(i):
        claveAmodificar = list(self.inventario())[{itemPosition}]
        abrirInventario[claveAmodificar] = i

def inventario():
    print(abrirInventario.inventario)
    x = input("""
        que quieres hacer ahora?
            1.abrir el segundo inventario
            2.salir
            """)
    if x=="1":
        inventarioMagico()
    elif x=="2":
        choose_action()
    else:
        print("opcion no valida")
        inventario()
            
def inventarioMagico():
    print(abrirInventario.inventario_magico)
    y = input("""
            que quieres hacer ahora?
                      1.salir
                      """)
    if y=="1":
        choose_action()
    else:
        print("opcion no valida")
        inventarioMagico()
        

class WeaponInventory:
    def __init__(self):
        self.multiplicador = random.randint(10, 20)

class Enemies:
    def __init__(self, player_level):
        if player_level <= 4:
            self.level = random.randint(1, 3)
        else:
            self.level = random.randint(4, 10)
        
        self.hormiga = {
            "ataque1": 10,
            "ataque2": 15,
            "ataque3": 20,
            "vida": 40
        }
        self.hormiga_leon = {
            "ataque1": 40,
            "ataque2": 60,
            "ataque3": 80,
            "vida": 100
        }
        

        self.avispa = {
            "ataque1": 30,
            "ataque2": 45,
            "ataque3": 50,
            "vida": 70
        }
        self.arana = {
            "ataque1": 20,
            "ataque2": 35,
            "ataque3": 45,
            "vida": 60
        }
        self.escorpion = {
            "ataque1": 50,
            "ataque2": 70,
            "ataque3": 90,
            "vida": 120
        }
        self.oso = {
            "ataque1": 80,
            "ataque2": 100,
            "ataque3": 120,
            "vida": 200
        }
        self.dragon = {
            "ataque1": 150,
            "ataque2": 200,
            "ataque3": 250,
            "vida": 500
        }

def choose_action():
    action = input(
        """
    ¿Qué quieres hacer?  
        1.tienda
        2.bosque
        3.mina
        4.stats           
        5.inventario
        6.tienda de encantamientos           
                   """)
    global fuerzaTotal
    fuerzaTotal = WeaponInventory()
    
    if action == "1":
        tienda = Shop()
        tienda.enter_shop(personaje)
    elif action == "2":
        enter_forest()
    elif action == "3":
        cave = EnterCave()
        cave.accion_mina()
    elif action == "4":
        personaje.show_stats()
        print(f"Daño actual: {fuerzaTotal.multiplicador}")
        choose_action()
    elif action == "5":
        print("abriendo inventario")
        inventario()
    elif action == "6":
        print("entrando a la tienda de encantamientos")
        sala_de_encantamientos()
    


def sala_de_encantamientos():
    while True:
        print(f"""
        Bienvenido a la tienda de encantamientos
        ¿Qué desea?
            Encantamientos de espada:
            1. Espada de fuego: 200 monedas (doble de daño)
            2. Espada de viento: 250 monedas (mayor probabilidad de esquivar el ataque)
            3. Espada de elemento: 1 de elemento (probabilidad de dar veneno)
            4. Cambiar de página
            5. Salir
        """)
        
        x = input("¿Qué quieres hacer? ")
        
        if x == "1" and personaje.stats["monedas"] >= 200:
            personaje.restar_coins(200)
            if abrirInventario.agregar_item("atributo de fuego"):
                print("Compraste el atributo de fuego y se agregó al inventario.")
            else:
                print("El inventario está lleno. No se pudo agregar el objeto.")
        
        elif x == "2" and personaje.stats["monedas"] >= 250:
            personaje.restar_coins(250)
            if abrirInventario.agregar_item("atributo de viento"):
                print("Compraste el atributo de viento y se agregó al inventario.")
            else:
                print("El inventario está lleno. No se pudo agregar el objeto.")
        
        elif x == "3" and personaje.stats["elemento"] >= 1:
            personaje.stats["elemento"] -= 1  # Suponiendo que el atributo "elemento" se gasta
            if abrirInventario.agregar_item("atributo de elemento"):
                print("Compraste el atributo de elemento y se agregó al inventario.")
            else:
                print("El inventario está lleno. No se pudo agregar el objeto.")
        
        elif x == "4":
            print("Cambiando de página...")
            segunda_pagina()
            break  # Salir de esta función ya que vamos a la segunda página
        
        elif x == "5":
            print("Saliendo de la sala de encantamientos.")
            choose_action()
            break  # Salir del bucle y de la función
        
        else:
            print("Opción no válida o fondos insuficientes. Inténtalo de nuevo.")



multi = 1

def continues():
    print("¿Qué haces ahora?")
    camino = input("volver/seguir caminando: ")
    if camino == "volver":
        choose_action()
    else:
        print("Sigues caminando...")
        enter_forest()

def spawn_enemy(enemy_type):
    enemy = Enemies(personaje.stats["nivel"])
    if enemy_type == "hormiga":
        hormiga_attack = random.choice([enemy.hormiga["ataque1"], enemy.hormiga["ataque2"], enemy.hormiga["ataque3"]])
        attack_total = hormiga_attack * enemy.level
        enemy_life = enemy.hormiga["vida"] * enemy.level
        print(f"Te encontraste con una hormiga agresiva, nivel {enemy.level}")
    elif enemy_type == "hormiga_leon":
        hormiga_attack = random.choice([enemy.hormiga_leon["ataque1"], enemy.hormiga_leon["ataque2"], enemy.hormiga_leon["ataque3"]])
        attack_total = hormiga_attack * enemy.level
        enemy_life = enemy.hormiga_leon["vida"] * enemy.level
        print(f"Te encontraste con una hormiga leon agresiva, nivel {enemy.level}")
    elif enemy_type == "dragon":
        hormiga_attack = random.choice([enemy.dragon["ataque1"], enemy.dragon["ataque2"], enemy.dragon["ataque3"]])
        attack_total = hormiga_attack * enemy.level
        enemy_life = enemy.dragon["vida"] * enemy.level
        print(f"Te encontraste con un dragon, nivel {enemy.level}")
    elif enemy_type == "oso":
        hormiga_attack = random.choice([enemy.oso["ataque1"], enemy.oso["ataque2"], enemy.dragon["ataque3"]])
        attack_total = hormiga_attack * enemy.level
        enemy_life = enemy.oso["vida"] * enemy.level
        print(f"Te encontraste con un oso, nivel {enemy.level}")


    while enemy_life > 0:
        personaje_fuerza = fuerzaTotal.multiplicador * multi
        accion = input(f"Vida de enemigo: {enemy_life}\n\n1. Atacar\n2. Ver inventario\n3. No hacer nada\n")
        defensa = random.randint(1, 25)

        if accion == "1":
            if defensa <= 5:
                print("¡El enemigo falló el ataque!")
            else:
                personaje.stats["vida"] -= attack_total
                print(f"El golpe fue efectivo, pero el enemigo te atacó, tu vida es de: {personaje.stats['vida']}")
            
            enemy_life -= personaje_fuerza
            if enemy_life <= 0:
                print("¡Has derrotado al enemigo!")
                continues()

        elif accion == "2":
            print("Mostrando inventario...")
        elif accion == "3":
            print("No haces nada. El enemigo te observa...")

class EnterCave:
    def __init__(self):
        self.picos = {
            "pico basico": 200,
            "pico doble": 150,
            "pico triple": 100
        }
        self.pico_seleccionado = None  
        self.pico = False 

    def accion_mina(self):    
        print("Has entrado a la cueva, ¿qué quieres hacer?")
        accion_minar = input("1. Minar\n2. Salir\n3. Tienda de picos\nElige una opción: ")

        if accion_minar == "1":
            if self.pico:
                if self.pico_seleccionado == "pico basico":
                    self.minar_dificil()
                elif self.pico_seleccionado == "pico doble":
                    self.minar_mediano()
                elif self.pico_seleccionado == "pico triple":
                    self.minar_facil()
            else:
                print("No tienes un pico para minar. Ve a la tienda de picos.")
                self.tienda_picos()           
        elif accion_minar == "2":
            print("Saliendo de la cueva...")
            choose_action()
        elif accion_minar == "3":
            self.tienda_picos()

    def tienda_picos(self):
        print("Bienvenido a la tienda de picos")
        for i, (nombre, precio) in enumerate(self.picos.items(), start=1):
            print(f"{i}. {nombre} ({precio} monedas)")

        seleccion = input("Elige un pico para comprar (1, 2 o 3): ")
        try:
            seleccion = int(seleccion) - 1
            nombre_pico, precio_pico = list(self.picos.items())[seleccion]
            
            if personaje.get_coins() >= precio_pico:
                personaje.restar_coins(precio_pico)
                self.pico = True
                self.pico_seleccionado = nombre_pico
                print(f"Has comprado {nombre_pico}.")
            else:
                print("No tienes suficientes monedas para este pico.")
        except (ValueError, IndexError):
            print("Selección no válida. Inténtalo de nuevo.")

    def minar_dificil(self):
        prop = random.randint(1, 2000)
        if prop <= 10:
            print("encontraste un diamante de valor: 100")
            personaje.stats["monedas"] += 100

    def minar_mediano(self):
        print("Minando en modo mediano...")

    def minar_facil(self):
        print("Minando en modo fácil...")

def enter_forest():
    scene = random.randint(1,5)
    if scene==1 or scene ==3:
        accion1()
    elif scene==2:
        accion2()
    elif scene==4 or scene==5:
        accion3()
    

def accion3():
    found = random.randint(1,20)
    if found >= 15:
        print("encontraste una moneda")
        foundMonedas = random.randint(1,30)
        personaje.stats["monedas"] += foundMonedas
    elif found == 14:
        hierroFound: random.randint(1,4)
        print(f"encontraste {hierroFound} de hierro")
        personaje.stats["hierro"] += hierroFound
    elif found == 13:
        print("encontraste 1 orbe de encantamiento")
        personaje.stats["hierro"] += 1
    elif found <= 12 and found >=10 :
        print("encontraste una piedra de union")
        if personaje.stats["piedra de union"] == 0:
            personaje.stats["piedra de union"] +=1
        else:
            print("ya tienes una piedra de union, el limite es 1")
            print("se te dara 100 monedas por venderlo")
            personaje.stats["monedas"] +=100

def accion2():
    print("no encontraste nada")
    continues()


def accion1():
    number = random.randint(1, 10)
    if number == 2:
        spawn_enemy("hormiga")
    elif number ==4:
        spawn_enemy("hormiga_leon")
    elif number == 5:
        spawn_enemy("dragon")
    elif number == 6:
        spawn_enemy("oso")
    else:
        accion1()

class abrir_inventario:
    def __init__(self):
        self.inventario = {f"item{i}": None for i in range(1, 11)}
        self.inventario_magico = {f"item{i}": None for i in range(1, 7)}

    def agregar_item(self, item):
        for key in self.inventario:
            if self.inventario[key] is None:
                self.inventario[key] = item
                print(f"{item} agregado al inventario.")
                return True
        print("El inventario está lleno.")
        return False

def inventario():
    print("Inventario actual:", abrirInventario.inventario)
    x = input("""
        ¿Qué quieres hacer ahora?
        1. Abrir el segundo inventario
        2. Salir
    """)
    if x == "1":
        inventarioMagico()
    elif x == "2":
        choose_action()
    else:
        print("Opción no válida")
        inventario()
            
def inventarioMagico():
    print("Inventario mágico actual:", abrirInventario.inventario_magico)
    y = input("""
        ¿Qué quieres hacer ahora?
        1. Salir
    """)
    if y == "1":
        choose_action()
    else:
        print("Opción no válida")
        inventarioMagico()

class Shop:
    def __init__(self):
        self.paginas_items = [
            {
                "espada básica": 40,
                "arco básico": 60,
                "guadaña básica": 100,
            },
            {
                "armadura de plástico": 50,
                "armadura de hierro": 100,
                "armadura de pinchos": 150
            },
            {
                "poción pequeña": 40,
                "poción mediana": 60,
                "poción grande": 120
            }
        ]
        self.pagina_actual = 0

    def mostrar_items(self):
        items = self.paginas_items[self.pagina_actual]
        print("Artículos disponibles en esta página:")
        for i, (nombre, precio) in enumerate(items.items(), start=1):
            print(f"{i}. {nombre} ({precio} monedas)")

    def enter_shop(self, personaje):
        while True:
            print("\nBienvenido a la tienda")
            self.mostrar_items()
            print("4. Salir")
            print("0. Cambiar de página\n")

            purchase = input("¿Qué quieres comprar? Ingresa el número de la opción: ")

            if purchase == "0":
                self.pagina_actual = (self.pagina_actual + 1) % len(self.paginas_items)
            elif purchase == "4":
                print("Saliendo de la tienda.")
                choose_action()
                break
            else:
                try:
                    purchase_index = int(purchase) - 1
                    item_name, item_price = list(self.paginas_items[self.pagina_actual].items())[purchase_index]
                    
                    if personaje.get_coins() >= item_price:
                        personaje.restar_coins(item_price)
                        if abrirInventario.agregar_item(item_name):
                            print(f"Has comprado {item_name}.")
                        else:
                            print("No se pudo agregar el objeto al inventario.")
                    else:
                        print("No tienes suficientes monedas para este objeto.")
                except (ValueError, IndexError):
                    print("Selección no válida. Inténtalo de nuevo.")

start_game()
