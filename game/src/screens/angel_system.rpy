# Variables, Estilos y Flujo Lógico
# Estilos barras verticales
style bar_mental:
    bar_vertical True
    xsize 25
    ysize 150
    left_bar Solid("#00ffcc") # Color de la salud mental
    right_bar Solid("#333333")

style bar_stress:
    bar_vertical True
    xsize 25
    ysize 150
    left_bar Solid("#ff4d4d") # Color del estres
    right_bar Solid("#333333")

# call iniciar_angel_system(True)   ///   call iniciar_angel_system()
label iniciar_angel_system(is_prologo=False):
    # Numero aleatorio del 1 al 3
    if is_prologo:
        $ turnos_restantes = 3
    else:
        $ turnos_restantes = renpy.random.randint(1, 3)

    # Mientras haya turnos, sigue en el sistema
    while turnos_restantes > 0:
        
        # Seleccionar personaje
        call screen angel_system_selection(turnos_restantes)
        $ char_elegida = _return 
        
        # Pantalla de accion
        call screen angel_system_action(char_elegida)
        $ accion_elegida = _return

        # Procesar la eleccion
        if accion_elegida == "volver":
            # El ciclo simplemente se repite sin restar turnos
            pass
        else:
            # Se aplica la accion y se gasta un turno
            call aplicar_accion_angel(char_elegida, accion_elegida)
            $ turnos_restantes -= 1

    # Cuando los turnos llegan a 0, termina y regresa a la historia normal
    return

# Logica de las acciones
label aplicar_accion_angel(personaje, accion):
    python:
        # Define que hace cada accion
        if personaje == "airi":
            if accion == "trabajar":
                fans_airi += 500
                stress_airi += 25
                mental_airi -= 15
            elif accion == "practicar":
                fans_airi += 100
                stress_airi += 10
            elif accion == "descansar":
                stress_airi = max(0, stress_airi - 30)
                mental_airi = min(100, mental_airi + 20)
                
        elif personaje == "ruka":
            if accion == "trabajar":
                fans_ruka += 500
                stress_ruka += 25
                mental_ruka -= 15
            elif accion == "practicar":
                fans_ruka += 100
                stress_ruka += 10
            elif accion == "descansar":
                stress_ruka = max(0, stress_ruka - 30)
                mental_ruka = min(100, mental_ruka + 20)
                
        elif personaje == "kaori":
            if accion == "trabajar":
                fans_kaori += 500
                stress_kaori += 25
                mental_kaori -= 15
            elif accion == "practicar":
                fans_kaori += 100
                stress_kaori += 10
            elif accion == "descansar":
                stress_kaori = max(0, stress_kaori - 30)
                mental_kaori = min(100, mental_kaori + 20)
    
    play sound "audio/UI/Retro5.wav"
    return





# Pantalla de Selección
transform carta:
    on idle:
        easein 0.15 zoom 1.0
    on hover:
        easein 0.15 zoom 1.05

screen angel_system_selection(turnos):
    modal True
    add "images/bgs/computadora.png" # Fondo de sistema
    add Solid("#000000B3") # Filtro oscuro

    # Variable local para detectar a quien esta haciendo hover
    default char_hover = None

    text "ANGEL SYSTEM - v2.3.2" xalign 0.5 ypos 30 size 40 color "#00ffcc" bold True
    text "Turnos: [turnos]" xalign 0.5 ypos 80 size 25 color "#ffffff"

    hbox:
        align (0.5, 0.5) 
        spacing 40 

        # --- Columna 1: Airi ---
        button:
            at carta
            xysize (320, 500)
            padding (20, 20)
            background Solid("#1e1e24") 
            hover_background Solid("#2b2b36") 
            
            # Control del hover para mostrar stats
            hovered [Play("sound", "audio/UI/Retro7.wav"), SetScreenVariable("char_hover", "airi")]
            unhovered SetScreenVariable("char_hover", None)
            action Return("airi")
            
            vbox:
                align (0.5, 0.0)
                spacing 15
                add Solid("#333333") xysize(280, 200) xalign 0.5 # Placeholder sin imagen unu
                text "Airi" xalign 0.5 bold True size 34 idle_color "#FFFFFF" hover_color "#FF77A8"
                
                # Si el cursor esta encima, muestra las barras
                if char_hover == "airi":
                    hbox:
                        xalign 0.5
                        spacing 20
                        vbox:
                            text "Mental" size 14 xalign 0.5
                            bar value mental_airi range 100 style "bar_mental"
                        vbox:
                            text "Estrés" size 14 xalign 0.5
                            bar value stress_airi range 100 style "bar_stress"
                else:
                    text "Fachada perfecta, lista para empezar a trabajar." text_align 0.5 size 20 idle_color "#cccccc"

        # --- Columna 2: Ruka ---
        button:
            at carta
            xysize (320, 500)
            padding (20, 20)
            background Solid("#1e1e24")
            hover_background Solid("#2b2b36")
            
            hovered [Play("sound", "audio/UI/Retro7.wav"), SetScreenVariable("char_hover", "ruka")]
            unhovered SetScreenVariable("char_hover", None)
            action Return("ruka")
            
            vbox:
                align (0.5, 0.0)
                spacing 15
                add Solid("#333333") xysize(280, 200) xalign 0.5
                text "Ruka" xalign 0.5 bold True size 34 idle_color "#FFFFFF" hover_color "#77CCFF"
                
                if char_hover == "ruka":
                    hbox:
                        xalign 0.5
                        spacing 20
                        vbox:
                            text "Mental" size 14 xalign 0.5
                            bar value mental_ruka range 100 style "bar_mental"
                        vbox:
                            text "Estrés" size 14 xalign 0.5
                            bar value stress_ruka range 100 style "bar_stress"
                else:
                    text "Buen perfil, alguien que ya tiene cierta fama." text_align 0.5 size 20 idle_color "#cccccc"

        # --- Columna 3: Kaori ---
        button:
            at carta
            xysize (320, 500)
            padding (20, 20)
            background Solid("#1e1e24")
            hover_background Solid("#2b2b36")
            
            hovered [Play("sound", "audio/UI/Retro7.wav"), SetScreenVariable("char_hover", "kaori")]
            unhovered SetScreenVariable("char_hover", None)
            action Return("kaori")
            
            vbox:
                align (0.5, 0.0)
                spacing 15
                add Solid("#333333") xysize(280, 200) xalign 0.5 
                text "Kaori" xalign 0.5 bold True size 34 idle_color "#FFFFFF" hover_color "#C277FF"
                
                if char_hover == "kaori":
                    hbox:
                        xalign 0.5
                        spacing 20
                        vbox:
                            text "Mental" size 14 xalign 0.5
                            bar value mental_kaori range 100 style "bar_mental"
                        vbox:
                            text "Estrés" size 14 xalign 0.5
                            bar value stress_kaori range 100 style "bar_stress"
                else:
                    text "Perfil reservado, requiere control absoluto." text_align 0.5 size 20 idle_color "#cccccc"





# Pantalla de Acción
screen angel_system_action(personaje):
    modal True
    add "images/bgs/computadora.png"
    add Solid("#000000E6") # Fondo oscuro

    # Extrae las variables segun quien eligio
    python:
        if personaje == "airi":
            p_nombre = "Airi"
            p_color = "#FF77A8"
            p_mental = mental_airi
            p_stress = stress_airi
            p_fans = fans_airi
        elif personaje == "ruka":
            p_nombre = "Ruka"
            p_color = "#77CCFF"
            p_mental = mental_ruka
            p_stress = stress_ruka
            p_fans = fans_ruka
        elif personaje == "kaori":
            p_nombre = "Kaori"
            p_color = "#C277FF"
            p_mental = mental_kaori
            p_stress = stress_kaori
            p_fans = fans_kaori

    hbox:
        align (0.5, 0.5)
        spacing 80

        # PANEL IZQUIERDO: Retrato
        vbox:
            # Retrato del personaje
            add "images/portraits/" + personaje + "_portrait.png"
        
        # PANEL DERECHO: Informacion y Acciones
        vbox:
            spacing 25
            yalign 0.5

            text p_nombre size 60 color p_color bold True
            text "Seguidores Activos: [p_fans]" size 24 color "#ffffff"
            
            # Barras horizontales
            hbox:
                spacing 15
                text "Estabilidad Mental" size 20 xminimum 180
                bar value p_mental range 100 xsize 300 ysize 25 left_bar Solid("#00ffcc") right_bar Solid("#444")
            hbox:
                spacing 15
                text "Nivel de Estrés" size 20 xminimum 180
                bar value p_stress range 100 xsize 300 ysize 25 left_bar Solid("#ff4d4d") right_bar Solid("#444")

            null height 30 # Espaciador

            # BOTONES DE ACCION
            # Si 'estres' esta a 100, no puede trabajar ni practicar, se inhabilitan
            
            textbutton "Trabajar":
                style "angel_sys_button"
                text_style "angel_sys_button_text"
                xminimum 400 yminimum 50
                action Return("trabajar")
                sensitive (p_stress < 90 and p_mental > 10) # Se desactiva si esta a punto de colapsar

            textbutton "Practicar":
                style "angel_sys_button"
                text_style "angel_sys_button_text"
                xminimum 400 yminimum 50
                action Return("practicar")
                sensitive (p_stress < 100)

            textbutton "Descansar":
                style "angel_sys_button"
                text_style "angel_sys_button_text"
                xminimum 400 yminimum 50
                action Return("descansar")

            null height 20

            # BOTON VOLVER
            textbutton "<< Volver":
                action Return("volver")
                text_size 20 text_color "#aaaaaa" text_hover_color "#ffffff"