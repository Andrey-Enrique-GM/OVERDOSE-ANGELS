# Aqui se definen los personajes del juego, con sus nombres y colores de texto
define mutou = Character("Mutou", color="#787780")
define yamada = Character("Yamada", color="#f95d5d")
define ayame = Character("Ayame", color="#ff46cb")
define akira = Character("Akira", color="#00d6f7")

#Aqui se definen las variables del juego, que se usan para controlar el flujo de la historia
default dinero = 1000
default estres = 0

# Aqui se definen las variables de puntos de los personajes, que se usan para controlar el flujo de la historia
default pts_akira = 0
default pts_akira2 = 0
default pts_akira3 = 0

# Aqui se define la fuente que se usará en el juego
define gui.playtime_font = "gui/fonts/playtime.ttf" 



# Aqui empieza el juego
label start:

    # Saltamos al Acto 1
    jump a1c1
