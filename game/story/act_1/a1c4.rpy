label a1c4:

    # ------------------------------------------------------------------------------------------------------
    # --- ESCENA 1: Fumando ---
    # ------------------------------------------------------------------------------------------------------

    scene estacionamiento with fade

    # ------------------------------------------------------------------------------------------------------
    # --- PANTALLA DE LA CITA ---
    # ------------------------------------------------------------------------------------------------------

    with Pause(1.5)
    window hide

    # Una cita sobre las máscaras sociales, la identidad y las apariencias
    show text "{i}\"Todos llevamos máscaras, y llega un momento en que no podemos quitárnoslas sin quitarnos nuestra propia piel.\"{/i}\n\n-- André Gide, {i}Los monederos falsos{/i} (1925)." at truecenter with dissolve
    $ renpy.pause()

    hide text with dissolve
    with Pause(1.0)
    window auto
    
    # Salto hacia el siguiente acto, el de Airi (provisional)
    jump a2c1_airi
