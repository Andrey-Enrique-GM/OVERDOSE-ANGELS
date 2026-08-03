# ==============================================================================
# ROAD.RPY - Sistema de Decisión y Control de Rutas (Gestor de Capítulos)
# ==============================================================================
# Este archivo es el encargado de tomar decisiones, evaluarlas y guiar al
# jugador por las distintas rutas a través de los capítulos.
# ==============================================================================

label evalue_a0c5:

    if init_aff_airi >= init_aff_ruka and init_aff_airi >= init_aff_kaori:
        $ pts_airi += 1
        jump a1c1_airi

    elif init_aff_ruka >= init_aff_airi and init_aff_ruka >= init_aff_kaori:
        $ pts_ruka += 1
        jump a1c1_ruka

    else:
        $ pts_kaori += 1
        jump a1c1_kaori
