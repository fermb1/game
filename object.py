from collections import namedtuple 

objecto = namedtuple("objecto",["nombre","id","valor","daño"])


objects = [
    objecto("guadaña",0,200,40),
    objecto("espada",1,100,10),
    objecto("hacha",2,150,20)
]

for obj in objects:
    print(f"nombre: {obj.nombre}, id: {obj.id}, valor: {obj.valor}, daño: {obj.daño}")