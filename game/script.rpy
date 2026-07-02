# Aqui se definen los personajes del juego, con sus nombres y colores de texto
define mutou = Character("Mutou", color="#787780")
define yamada = Character("Yamada", color="#f95d5d")
define akira = Character("Akira", color="#00d6f7")

#Aqui se definen las variables del juego, que se usan para controlar el flujo de la historia
default dinero = 1000
default estres = 0

default pts_akira = 0



# Aqui empieza el juego
label start:

    # Saltamos al Acto 1
    jump a1c1
