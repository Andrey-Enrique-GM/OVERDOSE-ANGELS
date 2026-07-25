#migna estuvo aqui favor de no tocar
#falta asignar los retratos/imagenes
# GG

transform carta:
    on idle:
        easein 0.15 zoom 1.0
    on hover:
        easein 0.15 zoom 1.05

screen seleccion():
    add Solid("#000000B3") 
    
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
            
            hovered Play("sound", "audio/UI/Retro7.wav")
            action [Play("sound", "audio/UI/Retro5.wav"), SetVariable("pts_airi", pts_airi + 1), Return("airi")]
            
            vbox:
                align (0.5, 0.0)
                spacing 15
                
                
                # Placeholder temporal (caja gris)
                add Solid("#333333") xysize(280, 250) xalign 0.5 
                # despcomentar despues
                # add "images/portraits/airi.png" xalign 0.5 xysize(280, 250)
                
                # provicional (Airi: Rosa/Rojo)
                text "Airi" xalign 0.5 bold True size 34 idle_color "#FFFFFF" hover_color "#FF77A8"
                
                text "Fachada perfecta, lista para empezar a trabajar." text_align 0.5 size 20 idle_color "#cccccc" hover_color "#ffffff"

        # --- Columna 2: Ruka ---
        button:
            at carta
            xysize (320, 500)
            padding (20, 20)
            background Solid("#1e1e24")
            hover_background Solid("#2b2b36")
            
            hovered Play("sound", "audio/UI/Retro7.wav")
            action [Play("sound", "audio/UI/Retro5.wav"), SetVariable("pts_ruka", pts_ruka + 1), Return("ruka")]
            
            vbox:
                align (0.5, 0.0)
                spacing 15
                
                
                add Solid("#333333") xysize(280, 250) xalign 0.5 
                # despcomentar despues y comentar el placeholder
                # add "images/portraits/ruka.png" xalign 0.5 xysize(280, 250)
                
                # provicional (Ruka: Azul/Cian)
                text "Ruka" xalign 0.5 bold True size 34 idle_color "#FFFFFF" hover_color "#77CCFF"
                
                text "Buen perfil, alguien que ya tenga cierta fama." text_align 0.5 size 20 idle_color "#cccccc" hover_color "#ffffff"

        # --- Columna 3: Shiori ---
        button:
            at carta
            xysize (320, 500)
            padding (20, 20)
            background Solid("#1e1e24")
            hover_background Solid("#2b2b36")
            
            hovered Play("sound", "audio/UI/Retro7.wav")
            action [Play("sound", "audio/UI/Retro5.wav"), SetVariable("pts_shiori", pts_shiori + 1), Return("shiori")]
            
            vbox:
                align (0.5, 0.0)
                spacing 15
                
                # cambiar despues por la silueta de Shiori
                add Solid("#333333") xysize(280, 250) xalign 0.5 
                # add "images/portraits/shiori.png" xalign 0.5 xysize(280, 250)
                
                # provicional (Shiori: Morado/Lila)
                text "Shiori" xalign 0.5 bold True size 34 idle_color "#FFFFFF" hover_color "#C277FF"
                
                text "Perfil reservado, requiere control absoluto." text_align 0.5 size 20 idle_color "#cccccc" hover_color "#ffffff"