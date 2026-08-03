# Aqui se definen los personajes del juego, con sus nombres y colores de texto
define mutou = Character("Mutou", color="#787878")
define yamada = Character("Yamada", color="#f95d5d")
define ayame = Character("Ayame", color="#ff46cb")
define sato = Character("Sato", color="#787878")

define airi = Character("Airi", color="#7febfc")
define ruka = Character("Ruka", color="#c551f3")
define kaori = Character("Kaori", color="#b34343")

define unknown = Character("???", color="#787878")



#Aqui se definen las variables del juego, que se usan para controlar el flujo de la historia
default dinero = 1000
default estres = 0

# Aqui se definen las variables de puntos de los personajes para manejar el flujo y final del prologo
# Esto servira como un multiplicador (bono) al empezar el acto 1
default init_aff_airi = 0
default init_aff_ruka = 0
default init_aff_kaori = 0

# Aqui se definen las variables de puntos de los personajes para manejar el flujo de la historia
# Estos seran los puntos que se iran sumando
default aff_airi = 0
default aff_ruka = 0
default aff_kaori = 0

# Aqui se definen las variables de puntos de cada personaje
# Estos 'pts' seran acumulados en +1 por cada capitulo de su respectiva ruta que se juegue (logros)
default pts_airi = 0
default pts_ruka = 0
default pts_kaori = 0

# Salud mental (0 = Colapso / 100 = Estable)
# Eventos especiales
default mental_airi = 50
default mental_ruka = 50
default mental_kaori = 50

# Nivel de estres (0 = Relajada / 100 = Limite)
# Eventos del trabajo
default stress_airi = 0
default stress_ruka = 0
default stress_kaori = 0

# Seguidores individuales
# Eventos especiales
default fans_airi = 1000
default fans_ruka = 800
default fans_kaori = 300

# Reputación o Nivel de la Agencia / Proyecto
default agency_fame = 0

# Eventos clave
default know_airi_secret = False
default reveal_ruka_fear = False
default made_promise_kaori = False

# Logros y persistencia (Definidos en src/achievements.rpy)




# Aqui se define la fuente que se usará en el juego
define gui.playtime_font = "gui/fonts/playtime.ttf" 



# Aqui empieza el juego
label start:

    # Saltamos al Acto 1
    jump a0c1
