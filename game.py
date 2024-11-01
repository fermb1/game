import random

def start_game():
    print("\nBienvenido al juego")
    new_game = input("¿Crear nueva partida? (si/no): ")
    
    if new_game == "si":
        global personaje
        personaje = Player()
        choose_action()
    else:
        print("Saliendo del juego.")

class Player:
    def __init__(self):
        self.name = input("¿Cuál es tu nombre? ")
        self.stats = {
            "nivel": 1,
            "vida": 100,
            "monedas": 50000
        }
        print(f"{self.name} nivel: {self.stats['nivel']} vida: {self.stats['vida']} monedas: {self.stats['monedas']}")

    def get_coins(self):
        return self.stats["monedas"]

    def restar_coins(self, cantidad):
        self.stats["monedas"] -= cantidad

    def show_stats(self):
        print(f"{self.name} nivel: {self.stats['nivel']} vida: {self.stats['vida']} monedas: {self.stats['monedas']}")

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
    action = input("¿Qué quieres hacer? (tienda/bosque/stats/mina): ")
    global fuerzaTotal
    fuerzaTotal = WeaponInventory()
    
    if action == "tienda":
        tienda = Shop()
        tienda.enter_shop(personaje)
    elif action == "bosque":
        enter_forest()
    elif action == "mina":
        cave = EnterCave()
        cave.accion_mina()
    elif action == "stats":
        personaje.show_stats()
        print(f"Daño actual: {fuerzaTotal.multiplicador}")
        choose_action()
        
multi = 1

def continues():
    print("¿Qué haces ahora?")
    camino = input("volver/seguir caminando: ")
    if camino == "volver":
        choose_action()
    else:
        print("Sigues caminando...")

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


    while enemy_life > 0:
        personaje_fuerza = fuerzaTotal.multiplicador * multi
        accion = input(f"Vida de enemigo: {enemy_life}\n\n1. Atacar\n2. Ver inventario\n3. No hacer nada\n")
        defensa = random.randint(1, 50)

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
    number = random.randint(1, 10)
    if number > 2:
        spawn_enemy("hormiga")
    elif number ==4:
        spawn_enemy("hormiga_leon")
    elif number == 5:
        spawn_enemy("dragon")

class Shop:
    def __init__(self):
        self.paginas_items = [
            {
                "espada básica": 40,
                "arco básico": 60,
                "guantes básicos": 20,
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
        global multi
        while True:
            print("\nBienvenido a la tienda")
            self.mostrar_items()
            print("4. Salir")
            print("0. Cambiar de página\n")

            purchase = input("¿Qué quieres comprar? Ingresa el número de la opción: ")

            if purchase == "0":
                self.pagina_actual = (self.pagina_actual + 1) % len(self.paginas_items)
                print("\nPágina cambiada.")
                continue
            elif purchase == "4":
                print("Saliendo de la tienda.")
                choose_action()
                break
            else:
                try:
                    index = int(purchase) - 1
                    item_actual = list(self.paginas_items[self.pagina_actual].items())[index]
                    nombre_item, precio_item = item_actual

                    if personaje.get_coins() >= precio_item:
                        print(f"Compraste {nombre_item}.")
                        multi = precio_item // 10
                        personaje.restar_coins(precio_item)
                    else:
                        print("No tienes suficiente dinero para esa compra.")
                except (ValueError, IndexError):
                    print("Opción no válida. Inténtalo de nuevo.")

start_game()
