label a1c2:

    # ------------------------------------------------------------------------------------------------------
    # --- ESCENA 1: Presentación de los nuevos talentos ---
    # ------------------------------------------------------------------------------------------------------

    scene oficina
    with fade

    "El sol de la mañana se filtra malamente a través de las persianas polvorientas de DokiWave Entertainment."
    "Mi cuerpo resiente la falta de sueño, pero el café barato de la máquina ayuda a mantener los ojos abiertos."

    show ayame-bien with easeinleft

    yamada "¡Buenos días, Mutou! ¡Llegas justo a tiempo!"
    yamada "El director me pidió que te entregara esto de inmediato. Son los perfiles de los nuevos talentos que acaban de firmar con la agencia."

    "Yamada me extiende una carpeta de color beige. Pesa más de lo que me gustaría."

    hide ayame-bien
    show ayame-neutral

    yamada "Son tres chicas en total. Las llaman el 'Angels Proyect'."
    yamada "El director dice que tienen un potencial masivo para el algoritmo actual, pero necesitan un mánager con mano de hierro para moldearlas."

    mutou "Mano de hierro... Entiendo."

    "Abro la carpeta sobre el escritorio. Tres fotografías, tres nombres, tres vidas resumidas en hojas de datos estadísticos."
    "Tres chicas cuyos nombres apenas registro en este momento."
    "Las miro fijamente."
    "¿Angeles? Qué maldito chiste."
    "Miro sus rostros sonrientes en las fotos. Inocentes. Ambiciosas. Ignorantes del matadero al que acaban de entrar."
    "Me pregunto... ¿A quién de ellas le voy a desgraciar la vida esta vez?"
    "¿A quién voy a exprimir hasta que no quede nada más que una carcasa vacía en nombre del maldito dinero?"

    # ------------------------------------------------------------------------------------------------------
    # --- ESCENA 2: Ayame ---
    # ------------------------------------------------------------------------------------------------------

    "El peso de los papeles me oprime el pecho. De repente, el olor a encierro de la oficina me transporta a otro lugar..."
    
    scene black with dissolve
    with Pause(0.5)
    
    # Flashback con Ayame
    "Recuerdo el piso 3. El frío de la barandilla de metal en la zona de fumadores."
    "El humo del cigarrillo flotando en el aire de la noche, disipándose lentamente bajo la luna."
    "Ayame estaba a mi lado, mirando el horizonte de la ciudad con esos ojos cansados pero extrañamente pacíficos."
    
    show ayame-neutral with dissolve
    
    ayame "Mutou... sé que esta industria te vuelve loco."
    ayame "Sé que a veces sientes que solo destruimos cosas."
    ayame "Pero recuerda: el monstruo solo tiene el poder que tú le otorgues. Al final del día, cuando apagas el monitor, tú decides quién eres en la oscuridad."
    
    hide ayame-neutral with dissolve
    with Pause(0.5)

    # Regreso al presente
    scene oficina with dissolve
    show ayame-neutral

    "El recuerdo de sus palabras actúa como un freno de mano en mi cabeza. Mi respiración se estabiliza. Cierro la carpeta de golpe."

    yamada "¿Mutou? ¿Te encuentras bien? Te pusiste un poco pálido..."

    mutou "Estoy bien, Yamada. Solo... necesito analizar esto con calma."
    mutou "Me llevaré estos documentos a casa. Los revisaré esta noche y mañana te daré mi decisión sobre con quién empezaremos a trabajar."

    yamada "Oh, entiendo. ¡Los genios necesitan su espacio! Está bien, llévatelos. ¡Descansa, Mutou!"

    hide ayame-neutral with easeoutleft

    # ------------------------------------------------------------------------------------------------------
    # --- ESCENA 3: En casa ---
    # ------------------------------------------------------------------------------------------------------

    scene black with fade
    "El trayecto a casa es un borrón de luces y rostros anónimos en el metro."
    
    # Fondo para el casa de Mutou
    # scene casa_mutou with fade
    "Mi casa está en silencio. Dejo las llaves en la mesa, enciendo una lámpara tenue y me sirvo un trago."
    "Extiendo los tres expedientes frente a mí."
    "Tengo que ser meticuloso. Debo elegir basándome en lo que realmente busco en este regreso..."

    menu:
        "Me atrae el carisma enérgico y la disposición a destacar. (Perfil: Chica 1)":
            $ pts_akira += 1
            "La primera chica... Su perfil dice que no le teme a las cámaras y busca atención desesperadamente."
            "Es el lienzo perfecto para crear un fenómeno de masas... o una tragedia comercial."

        "Prefiero un perfil más reservado, alguien que requiera control absoluto. (Perfil: Chica 2)":
            $ pts_akira2 += 1
            "La segunda chica... Parece moldeable."
            "Menos resistencia al principio, más fácil de dirigir bajo mis propios términos."

        "Busco a alguien que ya tenga una fachada perfecta, lista para ser explotada. (Perfil: Chica 3)":
            $ pts_akira3 += 1
            "La tercera opción... Ya tiene una base estética impecable."
            "Ahorrará tiempo en producción, directo a generar ingresos."

    mutou "Suficiente..."

    "Cierro los ojos, frotándome las sienes. El alcohol y el cansancio acumulado finalmente ganan la batalla."
    "Me arrastro hasta la cama..."
    "Me siento jodidamente agotado..."

    # ------------------------------------------------------------------------------------------------------
    # --- ESCENA 4: Recuerdos del pasado ---
    # ------------------------------------------------------------------------------------------------------

    scene black with fade
    with Pause(2.0)

    "El silencio de la noche es interrumpido por un eco ensordecedor."
    "El sonido distorsionado de miles de notificaciones en un teléfono."
    "¡Ping! ¡Ping! ¡Ping!"
    "Voces susurrando a través de la estática de un micrófono roto."
    "''¿Por qué lo hiciste? ¿Por qué no la salvaste? Mánager... Mánager...''"
    "De repente, visualizo una silueta en el suelo. Un vestido de idol blanco, ahora manchado de una oscuridad pastosa."
    "El destello incesante de las cámaras fotográficas ilumina su rostro sin vida. Aquel 'Angel' que una vez estuvo en la cima."
    "Sus ojos abiertos, completamente vacíos, mirándome directamente a mí."
    "Todo es mi culpa."
    "El algoritmo sigue hambriento."

    # Sonido de golpe
    # play sound "audio/sfx/despertar_golpe.wav"
    scene black with hpunch # Sacudida de pantalla por el susto
    
    "¡...!"
    "Me incorporo de golpe en la cama, con el corazón golpeando violentamente contra mis costillas."
    "Jadeo, buscando aire desesperadamente en la penumbra de mi habitación. El sudor frío me empapa la frente."
    "Miro a mi alrededor."
    "Solo es mi departamento."
    "Solo es la maldita noche de siempre."
    "Paso mis manos por mi rostro, obligándome a respirar lento... inhalar... exhalar..."
    "La calma regresa a cuentagotas, pero el frío en mi pecho no se va."

    with Pause(2.0)
    "Día 1 terminado."

    # ------------------------------------------------------------------------------------------------------
    # --- PANTALLA DE LA CITA ---
    # ------------------------------------------------------------------------------------------------------

    with Pause(1.5)
    window hide

    # Una cita real sobre la manipulación, el poder y la naturaleza humana maleable de Nicolás Maquiavelo
    show text "{i}\"Los hombres son tan simples, y se someten hasta tal punto a las necesidades presentes, que quien engaña encontrará siempre quien se deje engañar.\"{/i}\n\n-- Nicolás Maquiavelo, {i}El príncipe{/i} (1513)." at truecenter with dissolve
    $ renpy.pause()

    hide text with dissolve
    with Pause(1.0)
    window auto
    
    # Salto hacia el siguiente capitulo
    jump a1c3
