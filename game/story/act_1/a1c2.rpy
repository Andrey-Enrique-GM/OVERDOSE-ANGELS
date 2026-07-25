label a1c2:

    # ------------------------------------------------------------------------------------------------------
    # --- ESCENA 1: Presentación de los nuevos talentos ---
    # ------------------------------------------------------------------------------------------------------

    scene oficina with fade

    "El sol de la mañana se filtra malamente a través de las persianas polvorientas de DokiWave Entertainment."
    "Mi cuerpo resiente la falta de sueño, pero el café barato de la máquina ayuda a mantener los ojos abiertos."

    show yamada_basic_happy with easeinleft

    yamada "¡Buenos días, Mutou! ¡Llegas justo a tiempo!"
    yamada "El director me pidió que te entregara esto de inmediato. Son los perfiles de los nuevos talentos de la agencia."

    "Yamada me extiende otra carpeta de color beige. Pesa más de lo que me gustaría."

    hide yamada_basic_happy
    show yamada_basic_smile

    yamada "Son tres chicas en total. Las llaman el 'Angels Proyect'."
    yamada "El director dice que tienen un potencial masivo para el algoritmo actual, pero necesitan un mánager con mano de hierro para moldearlas."

    mutou "Mano de hierro... Entiendo."

    hide yamada_basic_smile

    "Abro la carpeta sobre el escritorio. Tres fotografías, tres nombres, tres vidas resumidas en hojas de datos estadísticos."
    "Tres chicas cuyos nombres apenas registro en este momento."
    "Las miro fijamente."
    "¿Angels? Qué maldito chiste."
    "Miro sus rostros sonrientes en las fotos. Inocentes. Ambiciosas. Ignorantes del matadero al que acaban de entrar."
    "Me pregunto... ¿A quién de ellas le voy a desgraciar la vida esta vez?"
    "¿A quién voy a exprimir hasta que no quede nada más que una carcasa vacía en nombre del maldito dinero?"

    # ------------------------------------------------------------------------------------------------------
    # --- ESCENA 2: Ruka Kurogane ---
    # ------------------------------------------------------------------------------------------------------

    "Soy interrumpido por la plática de Yamada detrás de mí."

    yamada "Claro, aquí está el..."
    yamada "¿Eh? ¿Lo quieres ver? ¿Justo ahora?"
    yamada "Eh... no sé si sea un buen momento, justo ahora él está revisando tu expediente..."

    "Suficiente. Está hablando de mí, pero ¿con quién?"
    "Rápidamente cierro la carpeta y me pongo de pie, dándome la vuelta en el proceso."
    "Justo al hacerlo, noto que hay alguien más fuera de la oficina."

    show yamada_basic_confused at left
    show ruka_basic_neutral at right

    "Tiene un aspecto bastante llamativo, ¿será que ella es...?"

    ruka "¿Qué tal? Soy Ruka."

    "Sí, es Ruka Kurogane."

    mutou "Por lo que veo ya me conoces, ¿me equivoco?"

    hide ruka_basic_neutral
    show ruka_basic_happy at right
    hide yamada_basic_confused
    show yamada_basic_happy at left

    yamada "Ella es Ruka Kurogane. Quizá alcanzaste a darle un vistazo a su perfil."
    yamada "Tiene una gran trayectoria construida por su cuenta. Ella es..."

    hide yamada_basic_happy
    show yamada_basic_confused at left

    ruka "Soy streamer. Bueno, quizá no como las chicas con las que tú sueles trabajar..."

    "¿Tú? Tiene demasiada confianza o un nulo respeto por sus superiores."

    hide ruka_basic_happy
    show ruka_basic_neutral at right

    ruka "Yo hago streams de videojuegos, no me grabo maquillándome o haciendo ASMR o... bueno..."

    hide ruka_basic_neutral
    show ruka_basic_angry at right

    ruka "Tuve una etapa."

    "Impresionante."
    "¿Acaso todas las streamers tuvieron esa 'etapa'?"

    hide ruka_basic_angry
    show ruka_basic_happy at right

    ruka "Pero eso no importa, ahora soy una nueva Ruka Kurogane."
    ruka "Bueno... mis amigos me dicen 'KuroRage'."

    "¿Sus amigos? Según su expediente, se refiere como 'amigos' a sus fans."

    mutou "Bueno... Ruka, fue un gusto conocerte."
    mutou "Pero ahora mismo quisiera hablar con Yamada. A solas."

    hide ruka_basic_happy
    show ruka_basic_neutral at right

    yamada "Oh... no sabía que tenían ese tipo de relación..."

    with hpunch # Sacudida de pantalla

    mutou "¡NO ES ESO!"

    yamada "Bueno... creo que es mejor dejar la conversación por hoy, Ruka..."

    hide yamada_basic_confused
    show yamada_basic_happy at left

    yamada "Puedes tomarte el resto del día libre."
    yamada "Siéntete libre de jugar videojuegos con tus amigos."

    hide ruka_basic_neutral
    show ruka_basic_happy at right

    ruka "¡Genial!"
    ruka "Nos vemos, señorita Yamada... Mánager."

    hide ruka_basic_happy

    "Con eso, finalmente se va y nos deja a solas de nuevo."

    yamada "Como puedes ver... ella es un tanto... especial de tratar."
    yamada "Tenle paciencia, es muy amigable y gentil."
    yamada "Además, es de las favoritas para el proyecto Angels."
    yamada "Podría ser la nueva gran estrella si sabes manejar correctamente su pasión por los videojuegos."

    mutou "Entiendo..."

    "A veces lo olvido: a esta industria solo le importan las posibilidades de éxito."
    "No los culpo. Yo fui uno de ellos, después de todo."
    "..."
    "¿O sigo siéndolo?"
    "No importa."
    "Ya no importa. No creo que exista algo como la redención para mí."
    "..."
    "....."
    ".........."

    yamada "¿Seguimos entonces?"

    "Me olvidé completamente de Yamada."
    "Quedé totalmente sumido en mis pensamientos."

    mutou "Claro, sigamos..."

    # ------------------------------------------------------------------------------------------------------
    # --- ESCENA 3: Ayame ---
    # ------------------------------------------------------------------------------------------------------

    "Tomo la carpeta y continúo donde me quedé."
    "De fondo escucho a Yamada diciéndome datos de la empresa que claramente no me importan y olvidaré mañana mismo."
    "El peso de los papeles me oprime el pecho. De repente, el olor a encierro de la oficina me transporta a otro lugar..."
    
    scene black with dissolve
    
    with Pause(0.5)
    
    # Flashback con Ayame
    "Recuerdo el piso 3. El frío de la barandilla de metal en la zona de fumadores."
    "El humo del cigarrillo flotando en el aire de la noche, disipándose lentamente bajo la luna."
    "Ayame estaba a mi lado, mirando el horizonte de la ciudad con esos ojos cansados pero extrañamente pacíficos."
    
    show ayame_basic_neutral with dissolve
    
    ayame "Mutou... sé que esta industria te vuelve loco."
    ayame "Sé que a veces sientes que solo destruimos cosas."
    ayame "Pero recuerda: el monstruo solo tiene el poder que tú le otorgues. Al final del día, cuando apagas el monitor, tú decides quién eres en la oscuridad."
    
    #hide ayame_basic_neutral with dissolve
    
    with Pause(0.5)

    # Regreso al presente
    scene oficina with dissolve
    show yamada_basic_smile

    "El recuerdo de sus palabras actúa como un freno de mano en mi cabeza. Mi respiración se estabiliza. Cierro la carpeta de golpe."

    yamada "¿Mutou? ¿Te encuentras bien? Te pusiste un poco pálido..."

    mutou "Estoy bien, Yamada. Solo... necesito analizar esto con calma."
    mutou "Me llevaré estos documentos a casa. Los revisaré esta noche y mañana te daré mi decisión sobre con quién empezaremos a trabajar."

    yamada "Oh, entiendo. ¡Los genios necesitan su espacio! Está bien, llévatelos. ¡Descansa, Mutou!"

    hide yamada_basic_smile with easeoutleft

    # ------------------------------------------------------------------------------------------------------
    # --- ESCENA 4: En casa ---
    # ------------------------------------------------------------------------------------------------------

    scene black with fade
    "El trayecto a casa es un borrón de luces y rostros anónimos en el metro."
    
    # Fondo para el casa de Mutou
    # scene casa_mutou with fade
    "Mi casa está en silencio. Dejo las llaves en la mesa, enciendo una lámpara tenue y me sirvo un trago."
    "Extiendo los tres expedientes frente a mí."
    "Tengo que ser meticuloso. Debo elegir basándome en lo que realmente busco en este regreso..."

    label escena_reclutamiento:
    
    call screen seleccion
    
    if _return == "airi":
        "Airi... Shirayuki..."
        "Ya tiene una base estética impecable... justo lo que buscaba."
        "Tiene buena cara, ahorrará tiempo en producción, directo a generar ingresos."
        
    elif _return == "ruka":
        "Ruka... ¿Kurogane?"
        "Parece algo... extraña, aunque sus numeros..."
        "Tiene un buen perfil, no sera un problema que obtenga fans."
        
    elif _return == "kaori":
        "Kaori Sumizome..."
        "Segun su perfil parece algo problematica para controlar..."
        "Solamente quiere crear arte, no le parece importar mucho la industria..."

    menu:
        "Estaría bien que tuviera ya un buen perfil, alguien que ya tenga cierta fama. (Ruka)":
            play sound "audio/UI/Retro5.wav"
            $ pts_ruka += 1
            "Ruka... ¿Kurogane?"
            "Parece algo... extraña, aunque sus números..."
            "Tiene un buen perfil, no será un problema que obtenga fans."

        "Prefiero un perfil más reservado, alguien que requiera control absoluto. (Kaori)":
            play sound "audio/UI/Retro5.wav"
            $ pts_kaori += 1
            "Kaori Sumizome..."
            "Según su perfil parece algo problemática para controlar..."
            "Solamente quiere crear arte, no le parece importar mucho la industria..."
            
            
    mutou "Suficiente..."

    "Cierro los ojos, frotándome las sienes. El alcohol y el cansancio acumulado finalmente ganan la batalla."
    "Me arrastro hasta la cama..."
    "Me siento jodidamente agotado..."

    # ------------------------------------------------------------------------------------------------------
    # --- ESCENA 5: Recuerdos del pasado ---
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

    # Sonido de latidos
    play sound "audio/sfx/heart_echo.wav"
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
