# Usamos una screen para diseñar el monitor del Angel
screen angel_system_panel(nombre_angel):

    # Forzamos a que el jugador interactúe con el panel y no avance el texto por error
    modal True 

    # Fondo del monitor
    add "images/bgs/computadora.png"


    # --- BARRA SUPERIOR DE ESTADO (Métricas del Angel) ---
    hbox:
        xalign 0.5
        ypos 50
        spacing 40 

        # Presupuesto de la Agencia (Global)
        frame:
            background "#1a1a24" padding (15, 10)
            text "Presupuesto: $[dinero]" color "#00ffcc" size 20

        # Barra de Estrés Dinámica (Usa la variable global 'estres')
        frame:
            background "#1a1a24" padding (15, 10)
            hbox:
                spacing 10
                # Ahora muestra dinámicamente el nombre del Ángel activo
                text "Estrés [nombre_angel]:" color "#ffffff" size 20
                bar:
                    value AnimatedValue(estres, 100, delay=1.0)
                    xmaximum 200
                    ymaximum 20


    # --- PANEL CENTRAL: ACCIONES ---
    vbox:
        xalign 0.5
        yalign 0.6
        spacing 20

        text "ANGEL SYSTEM v1.0.4" xalign 0.5 color "#fff" size 18

        # Acción 1: Stream Masivo
        textbutton "Iniciar Stream de 12 Horas":
            xminimum 400 yminimum 50
            action [
                SetVariable("estres", estres + 30),
                SetVariable("dinero", dinero + 800),
                Return("stream") 
            ]
            style "angel_sys_button"

        # Acción 2: Descanso
        textbutton "Asignar Día de Descanso":
            xminimum 400 yminimum 50
            action [
                SetVariable("estres", max(0, estres - 25)),
                SetVariable("dinero", dinero - 200),
                Return("descanso")
            ]
            style "angel_sys_button"


# --- Estilos Visuales del Panel ---
style angel_sys_button:
    background "#00aec9"
    hover_background "#00ffcc" 
    padding (10, 10)

style angel_sys_button_text:
    color "#ffffff"
    hover_color "#000000"
    xalign 0.5