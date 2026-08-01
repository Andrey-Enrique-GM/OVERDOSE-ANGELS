label a0c1:

    play music "audio/bgm/BGLF.flac" loop fadein 1.5

    # ------------------------------------------------------------------------------------------------------
    # --- ESCENA 1: Flashback ---
    # ------------------------------------------------------------------------------------------------------

    scene exterior with fade
    
    "El flash de las cámaras. El sonido de la lluvia golpeando los paraguas negros."
    "Los titulares de las noticias decían que fue un 'trágico final', el precio de la fama."
    "Pero yo estuve ahí. Yo construí a esa estrella. Y vi cómo el algoritmo se alimentó de sus restos hasta dejarla vacía."
    "Prometí que nunca volvería a pasar por esto. Prometí que la industria no me quitaría nada más..."
    "Pero..."

    scene black with fade
    with Pause(1.5)
    window hide
    show text "Cinco años después." at truecenter with dissolve
    $ renpy.pause()
    hide text with dissolve
    with Pause(1.0)
    window auto
    
    # ------------------------------------------------------------------------------------------------------
    # --- ESCENA 2: Yamada ---
    # ------------------------------------------------------------------------------------------------------

    scene computadora with fade
    
    "El zumbido del monitor de mi computadora es lo único que llena la pequeña oficina de DokiWave Entertainment."
    "Un espacio pequeño, luces de neón baratas parpadeando en la esquina, y un contrato sobre el escritorio."
    "Alguien interrumpe mi tranquilidad."

    scene oficina with dissolve
    
    show yamada_basic_happy with easeinright
    
    unknown "¡Mutou! ¿De verdad eres tú?"
    unknown "¡No puedo creer que la gran agencia haya conseguido de regreso a Mutou! ¡El hombre que llevó a la cima a la mismísima...!"
    
    hide yamada_basic_happy
    show yamada_basic_smile
    
    "Le hago una seña con la mano para que guarde silencio. No me gusta que mencionen el pasado."
    "Mucho menos ese nombre..."

    unknown "Oh... lo siento. No quise decir nada malo. Solo estaba emocionada de verte."

    mutou "..."
    mutou "No te preocupes... ya pasaron cinco años. No hay nada nuevo que lamentar."

    unknown "Sí, tienes razón. Pero..."
    unknown "¿Qué te trae de vuelta a la industria? ¿Qué te hizo volver?"

    "¿Es en serio?"
    "Esta chica no tiene idea de lo que pasó."
    "No sabe nada de lo que pasó."
    "No sabe nada de lo que me pasó a mí."
    "..."
    "¿Como voy a lidiar con ella?"

    menu:
        "Decirle la verdad.":
            play sound "audio/UI/Retro5.wav"
            "¿Decirle la verdad?"
            "¿En serio?"
            "Si, claro."

        "Mentir y decir que fue por dinero.":
            $ estres += 1
            play sound "audio/UI/Retro5.wav"
            "¿En serio?"
            "¿Desde cuando es que miento si no es necesario?"
            "Bueno, tampoco es que me importe."

    "Mentire."
    "De nuevo, como siempre."

    mutou "Volví por dinero. La industria me necesita, y yo necesito dinero."
    mutou "Ademas... no creo que haya alguien mas apto que yo para esto."

    unknown "¡Eso es genial! ¡Estoy segura de que podemos hacer un gran equipo!"

    mutou "..."
    mutou "Sí, seguro. Pero antes de que empecemos, ¿Quien eres?"

    yamada "¡Oh! ¡Perdón! Me llamo Yamada. Soy una gran admiradora de tu trabajo como manager."

    "Que novedad."

    yamada "También soy la nueva asistente de producción de DokiWave Entertainment."

    "Asistente de producción..."
    "Pero si ese es el trabajo de..."

    mutou "¿La nueva? ¿Qué pasó con Ayame?"

    yamada "Oh... la señorita Ayame..."
    yamada "Se fue hace un par de meses. Dijo que quería dedicarse a algo más personal, y que no podía seguir trabajando en la industria del entretenimiento."
    yamada "O algo así puedo recordar."
    yamada "Pero no te preocupes, estoy aquí para ayudarte en todo lo que necesites."

    "Anotado; esta chica no sabe nada."

    mutou "Bueno, YA-MA-DA. Gracias, pero en mi camino a las oficinas no vi por ningun lado la zona de fumadores."
    mutou "¿Me puedes decir dónde está? Necesito un cigarrillo."

    "Yamada me mira con una sonrisa apenada, algo anda mal."

    yamada "Ehm... la zona de fumadores fue cerrada hace un par de años."
    yamada "La empresa decidió que no era saludable para los empleados y daba una mala imagen para el estreno de la marca 'Angels'."

    "'Angels'... el nuevo gran proyecto de DokiWave Entertainment..."
    "'Nuevo'"
    "Ya todos olvidaron la desgracia en la que termino 'DokiIdols'."
    "Claro. Ya es cosa del pasado, pero..."
    "No me importa la imagen de la marca. No me importa la salud de los empleados. Solo quiero fumar un cigarrillo."

    mutou "Carajo..."

    hide yamada_basic_smile

    scene black with fade

    "Después de unos minutos que se sintieron como horas, Yamada terminó de hablar de la imagen de la marca Angels."
    "Honestamente, no me podría importar menos. Por lo que ignoro sus palabras la mayor parte del tiempo."
    "Aparentemente la empresa a cambiado, bastante."
    "Recuerdo que hace cinco años, la zona de fumadores estaba en el piso 3, justo al lado de la oficina de producción."
    "Ayame y yo pasábamos horas ahí, fumando y hablando de casi cualquier cosa."
    "..."

    # ------------------------------------------------------------------------------------------------------
    # --- ESCENA 3: Airi Shirayuki ---
    # ------------------------------------------------------------------------------------------------------
    
    scene oficina

    show yamada_basic_happy with fade

    yamada "Bueno, creo que eso es todo."
    yamada "Pero antes, quisiera presentarte a alguien..."

    "Me quedo confundido. ¿Alguien? ¿Quién podría ser que yo no conozca de antes?"
    "A menos que sea... claro."

    hide yamada_basic_happy
    show yamada_basic_confused

    yamada "Eh..."
    yamada "Tal parece que ahora mismo no está... disponible."

    mutou "Ya veo... ¿Siempre es así?"

    yamada "No, no, no, para nada... Solo en unas pocas ocasiones..."

    "Pocas ocasiones = Todo el tiempo."

    hide yamada_basic_confused
    show yamada_basic_smile

    yamada "Pero no estamos para hablar de eso. Ella es Airi, Airi Shirayuki."
    yamada "¿Te suena?"

    mutou "Ni un poco."

    hide yamada_basic_smile
    show yamada_basic_confused

    yamada "Oh..."

    hide yamada_basic_confused
    show yamada_basic_smile

    yamada "Bueno, Airi es una gran promesa para el proyecto Angels. Seguro ella podría ser la nueva gran estrella."

    "Yamada me extiende una carpeta de color beige; dentro de esta vienen unos cuantos papeles con cantidades y gráficos."
    "Todo excelente y en un gran crecimiento. Todo respecto al perfil de Airi Shirayuki."

    yamada "Como puedes ver, esta chica tiene un gran perfil ya construido gracias a las redes sociales."
    yamada "A todos les gustan las chicas lindas~"
    yamada "Es una pena terrible que ella no pueda estar presente ahora mismo, pero te aseguro que te caerá bien."

    menu:
        "Debe estar ocupada.":
            $ init_aff_airi += 2
            play sound "audio/UI/Retro5.wav"
            mutou "Entiendo. En otra oportunidad podré conocerla entonces..."
            yamada "Sí, así es..."

        "Que irresponsabilidad.":
            $ init_aff_airi += 1
            play sound "audio/UI/Retro5.wav"
            mutou "Me parece que es una irresponsabilidad que no esté presente. ¿No crees?"
            mutou "Debe ser muy importante para el proyecto, y no se toma la molestia de presentarse."
            hide yamada_basic_smile
            show yamada_basic_confused
            yamada "No es que sea irresponsable... es solo que ella..."
            yamada "Tiene un horario muy apretado, y no siempre puede estar disponible."
            yamada "Pero te aseguro que es una gran chica, y que te caerá bien. Solo... dale tiempo."
            yamada "Y comprende que ella no puede estar presente ahora mismo. No es su culpa."
            "..."
            "Tiene razón. No es su culpa."
            "Así es como es la industria del entretenimiento. No hay tiempo para nada más que no sea trabajo."
            mutou "Si, tienes razón. No es su culpa."
            mutou "Lo siento por haberme alterado. No es mi intención faltarle el respeto a Airi Shirayuki."
            hide yamada_basic_confused
            show yamada_basic_smile
            yamada "No te preocupes, Mutou. Estoy segura de que Airi entenderá."
            
    hide yamada_basic_smile
    show yamada_basic_happy

    yamada "Puedes llevarte la carpeta contigo, tiene bastantes datos que podrían interesarte."

    mutou "De acuerdo, más tarde les daré un vistazo más detenidamente."

    yamada "Muy bien. Pasemos con una pequeña práctica solo para que recuerdes el uso de 'DokiWave OS'."
    yamada "Ahora siéntate e inicia sesión en la computadora."

    # ------------------------------------------------------------------------------------------------------
    # --- ESCENA 4: Tutorial ---
    # ------------------------------------------------------------------------------------------------------

    scene computadora with dissolve

    "Me desplomo en la silla giratoria. El cuero agrietado protesta bajo mi peso."
    "Acerco la mano al botón de encendido del gabinete. El monitor parpadea, arrojando una luz blanca y fría directo a mis ojos cansados."

    # Sonido de inicio de sistema
    play sound "audio/sfx/sys_startup.wav"

    "La pantalla de carga de DokiWave OS se despliega. Interfaces color pastel, tipografías infantiles... clasico."

    yamada "¡Listo! Ese es nuestro panel central. El director hizo que actualizaran el software para que sea más... 'eficiente'."
    yamada "Desde aquí vas a controlar absolutamente todo lo relacionado con tu primer talento."
    yamada "Por ahora el sistema está en modo de simulación. Puedes probarlo para que te acostumbres a la interfaz."

    mutou "Fabuloso. Más números que exprimir..."

    yamada "¡Jeje! Bueno, hablando de números, presentate mañana en mi oficina, te presentare a alguna de las chicas que tenemos en la agencia."
    yamada "Yo me retiro por hoy. Te dejé las credenciales de administrador en el escritorio. ¡Nos vemos mañana, Mutou!"

    "Los pasos de Yamada se alejan por el pasillo."
    "Me quedo solo en la oficina, contemplando el panel de control. Las barras de estadísticas parpadean en un bucle infinito, esperando a su primera víctima."
    "O a su primer milagro. Ya ni siquiera sé qué es lo que busco."

    mutou "Es hora de probar el Angel System..."
    mutou "Quizá haga unas tres pruebas para recordar cómo funciona esto..."

    # Invocamos la pantalla en la carpeta de screens
    call iniciar_angel_system(True)

    # Sonido de cerrado de sistema
    play sound "audio/sfx/sys_off.wav"

    "Bueno, eso fue suficiente."
    "Vaya simulación... me trae recuerdos..."

    scene oficina with dissolve

    mutou "Hora de volver a casa. Mañana será un día largo..."
    mutou "Espero que haya buenas opciones mañana."

    scene black with fade

    "Capítulo 1 terminado."

    # ------------------------------------------------------------------------------------------------------
    # --- PANTALLA DE LA CITA ---
    # ------------------------------------------------------------------------------------------------------

    # Pausa dramática en negro
    with Pause(1.5)
    # Ocultamos la ventana de diálogo por completo
    window hide

    # Muestra la cita centrada en la pantalla usando texto con estilo
    # Una cita sobre la responsabilidad del individuo y la sociedad de Friedrich Nietzsche
    show text "{i}\"Ahí donde el Estado termina, comienza el hombre que no es superfluo; ahí comienza el canto de los necesarios, la melodía única e insustituible.\"{/i}\n\n-- Friedrich Nietzsche, {i}Así habló Zaratustra{/i} (1883)." at truecenter with dissolve
    # El juego se pausa hasta que el jugador presione un botón para continuar
    $ renpy.pause()

    # Desvanecido final para limpiar la pantalla
    hide text with dissolve
    with Pause(1.0)
    # Volvemos a mostrar la ventana
    window auto

    # Salto hacia el siguiente capitulo
    jump a0c2
