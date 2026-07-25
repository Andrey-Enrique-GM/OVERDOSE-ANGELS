define config.main_menu_music = "audio/bgm/lofi.flac"

# --- EFECTOS VISUALES Y ANIMACIONES ---

transform latido_titulo:
    alpha 0.8
    easein 2.0 alpha 2.0 zoom 2.1
    easeout 2.0 alpha 0.8 zoom 1.8
    repeat

transform btn_crece:
    easein 0.2 zoom 1.15 alpha 1.0
transform btn_achica:
    easein 0.2 zoom 0.85 alpha 0.4
transform btn_reposo:
    easein 0.2 zoom 1.0 alpha 1.0

# --- PANTALLA PRINCIPAL ---

screen main_menu():
    tag menu

    default boton_activo = None

    add Solid("#FFF0F5")

    text "[config.name!t]":
        align (0.5, 0.12) 
        size 100
        bold True
        color gui.accent_color
        drop_shadow [(3, 3)] 
        drop_shadow_color "#00000044"
        at latido_titulo

    vbox:
        align (0.5, 0.65) 
        spacing 15

        textbutton _("Comenzar"):
            action Start()
            hovered SetScreenVariable("boton_activo", "comenzar")
            unhovered SetScreenVariable("boton_activo", None)
            style "estilo_borde_hueco"
            text_style "estilo_texto_glow"
            hover_sound "audio/UI/Retro1.wav"
            activate_sound "audio/UI/Retro8.wav"
            
            if boton_activo == "comenzar":
                at btn_crece
            elif boton_activo != None:
                at btn_achica
            else:
                at btn_reposo

        textbutton _("Cargar"):
            action ShowMenu("load")
            hovered SetScreenVariable("boton_activo", "cargar")
            unhovered SetScreenVariable("boton_activo", None)
            style "estilo_borde_hueco"
            text_style "estilo_texto_glow"
            hover_sound "audio/UI/Retro1.wav"
            activate_sound "audio/UI/Retro8.wav"
            
            if boton_activo == "cargar":
                at btn_crece
            elif boton_activo != None:
                at btn_achica
            else:
                at btn_reposo

        textbutton _("Preferencias"):
            action ShowMenu("preferences")
            hovered SetScreenVariable("boton_activo", "pref")
            unhovered SetScreenVariable("boton_activo", None)
            style "estilo_borde_hueco"
            text_style "estilo_texto_glow"
            hover_sound "audio/UI/Retro1.wav"
            activate_sound "audio/UI/Retro8.wav"
            
            if boton_activo == "pref":
                at btn_crece
            elif boton_activo != None:
                at btn_achica
            else:
                at btn_reposo

        textbutton _("Acerca de"):
            action ShowMenu("about")
            hovered SetScreenVariable("boton_activo", "acerca")
            unhovered SetScreenVariable("boton_activo", None)
            style "estilo_borde_hueco"
            text_style "estilo_texto_glow"
            hover_sound "audio/UI/Retro1.wav"
            activate_sound "audio/UI/Retro8.wav"
            
            if boton_activo == "acerca":
                at btn_crece
            elif boton_activo != None:
                at btn_achica
            else:
                at btn_reposo

        textbutton _("Ayuda"):
            action ShowMenu("help")
            hovered SetScreenVariable("boton_activo", "ayuda")
            unhovered SetScreenVariable("boton_activo", None)
            style "estilo_borde_hueco"
            text_style "estilo_texto_glow"
            hover_sound "audio/UI/Retro1.wav"
            activate_sound "audio/UI/Retro8.wav"
            
            if boton_activo == "ayuda":
                at btn_crece
            elif boton_activo != None:
                at btn_achica
            else:
                at btn_reposo

        textbutton _("Salir"):
            action Quit(confirm=not main_menu)
            hovered SetScreenVariable("boton_activo", "salir")
            unhovered SetScreenVariable("boton_activo", None)
            style "estilo_borde_hueco"
            text_style "estilo_texto_glow"
            hover_sound "audio/UI/Retro1.wav"
            activate_sound "audio/UI/Retro8.wav"
            
            if boton_activo == "salir":
                at btn_crece
            elif boton_activo != None:
                at btn_achica
            else:
                at btn_reposo

    hbox:
        align (0.98, 0.98)
        spacing 10
        text "v1.0" size 16 color "#888888"
        text "|" size 16 color "#888888"
        text "Autor: Andrey" size 16 color "#888888"
        text "|" size 16 color "#888888"
        text "GUI & Audio: Migna" size 16 color "#888888"

# --- ESTILOS ---

style estilo_borde_hueco:
    xalign 0.5
    xpadding 40 
    ypadding 5 
    #no quiero hacer la imagen en un editor en este momento
    # background Frame("gui/borde_redondeado_blanco.png", 15, 15)
    # hover_background At(Frame("gui/borde_redondeado_blanco.png", 15, 15), Transform(matrixcolor=TintMatrix("#ff00ff")))

style estilo_texto_glow:
    xalign 0.5
    size 35 
    idle_color gui.idle_color
    hover_color "#ffffff" 
    hover_outlines [(6, "#ff00ff11", 0, 0), (4, "#ff00ff44", 0, 0), (2, "#ff00ff99", 0, 0), (1, "#ff00ffff", 0, 0)]