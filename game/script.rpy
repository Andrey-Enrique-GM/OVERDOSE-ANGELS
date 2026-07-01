# Aqui se definen los personajes del juego, con sus nombres y colores de texto
define akira = Character("Akira", color="#00aec9")


#Aqui se definen las variables del juego, que se usan para controlar el flujo de la historia
default pts_akira = 0



# Aqui empieza el juego
label start:

    # Saltamos al Acto 1
    jump a1c1
