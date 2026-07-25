label a1c3:

    # ------------------------------------------------------------------------------------------------------
    # --- ESCENA 1: Fumando ---
    # ------------------------------------------------------------------------------------------------------

    scene estacionamiento with fade

    "El aire de la mañana detrás del edificio principal de DokiWave Entertainment es frío y denso."
    "Un rincón olvidado, rodeado de contenedores de basura y el constante zumbido del aire acondicionado central."
    "Perfecto. Nadie viene aquí."
    "Enciendo un cigarrillo. La primera bocanada de humo llena mis pulmones, trayendo un alivio momentáneo al dolor de cabeza que me dejó la pesadilla de anoche."
    "Miro las volutas de humo gris ascender y disiparse en el cielo."

    mutou "Cinco años fuera y nada cambia realmente..."
    mutou "La misma ambición ciega, el mismo algoritmo devorando vidas..."
    mutou "¿Realmente voy a volver a hacer esto?"

    "El sonido de unos pasos ligeros rompe mi monólogo interno."

    show kaori_basic_neutral

    "Miro de reojo. Una mujer se acerca caminando a paso lento. Lleva una bufanda grande que le cubre parte del rostro y una gorra calada hasta las cejas."
    "Se detiene a un par de metros de mí, buscando algo en sus bolsillos."
    "Extrae un cigarrillo, se lo lleva a los labios y me mira fijamente."

    unknown "Disculpa... ¿tendrás fuego?"

    "Su voz es suave, pero tiene un matiz seco, cansado."
    "Saco el encendedor metálico de mi bolsillo."

    menu:
        "Encenderle el cigarrillo.":
            play sound "audio/UI/Retro5.wav"
            $ pts_kaori += 1
            "Hago chasquear el encendedor, protegiendo la pequeña llama con la palma de mi mano."
            "Ella da un paso adelante, se inclina ligeramente y acerca la punta de su cigarrillo a la llama."
            "Durante un segundo, bajo la sombra de su gorra, alcanzo a notar la mirada penetrante de sus ojos."
            "Da una calada profunda. El extremo del cigarrillo brilla con un rojo intenso."
            unknown "Gracias."
            mutou "No hay de qué."

        "Pasarle el encendedor para que ella misma lo haga.":
            play sound "audio/UI/Retro5.wav"
            "Le extiendo el encendedor de metal en la palma de mi mano."
            "Ella lo toma sin decir nada. Sus dedos rozan los míos por un instante; están fríos."
            "Hace chispear la piedra, enciende su cigarrillo y me devuelve el encendedor."
            unknown "Gracias."
            mutou "..."

    "Ambos nos quedamos de pie en la sombra del edificio, fumando en absoluto silencio."
    "El único sonido entre nosotros es el chisporroteo del tabaco al consumirse."
    "No hay necesidad de charla vacía. Es un acuerdo tácito entre dos personas que solo buscan un momento de anestesia."

    unknown "El aire aquí huele a humedad..."
    
    mutou "Es el mejor lugar del edificio. Nadie molesta."

    hide kaori_basic_neutral
    show kaori_basic_happy

    "Ella suelta una pequeña risa amarga que se pierde en una nube de humo."

    unknown "Tienes razón. Nadie molesta..."

    "Apaga la colilla contra la pared de ladrillo y la tira al basurero."

    unknown "Nos vemos, mánager."

    mutou "...?"

    hide kaori_basic_happy with dissolve

    "Antes de que pueda preguntarle cómo sabe quién soy, la mujer se da la vuelta y camina a paso rápido hacia la salida del callejón, desapareciendo tras la esquina."
    "Me quedo solo, sosteniendo mi cigarrillo a medio consumir."
    "¿Qué demonios fue eso...?"

    # ------------------------------------------------------------------------------------------------------
    # --- ESCENA 2: Formalidad ---
    # ------------------------------------------------------------------------------------------------------

    show yamada_basic_angry with easeinright

    yamada "¡MUTOU!"
    yamada "¡Sabía que te encontraría aquí!"

    "Doy un brinco imperceptible y tiro la colilla de inmediato."

    mutou "Carajo, Yamada... Vas a hacer que me dé un ataque."

    yamada "¡Te dije ayer que la zona de fumadores está prohibida! Aun mas fumar a escondidas detras del edificio principal."
    yamada "Si el director te ve rompiendo las políticas de la empresa en tu primer día oficial, nos meteremos en serios problemas."

    mutou "Nadie nos está viendo..."

    yamada "¡Eso no importa! Además, mírate..."
    yamada "Traes la camisa arrugada y no llevas corbata. Hoy es el día de las evaluaciones de directiva."
    yamada "Por favor, ven conmigo a la oficina de inmediato."

    scene oficina with dissolve

    "Yamada me arrastra hasta su oficina."
    "Rebusca apresuradamente en un perchero detrás de su escritorio y saca un traje oscuro con funda de plástico."

    show yamada_basic_happy with dissolve

    yamada "¡Aquí tienes! Guardé esto por si acaso. Te exigirán formalidad si vas a tomar decisiones sobre los presupuestos de las Angels."

    "Me entrega el saco y la corbata."
    "Suspiro con resignación."

    mutou "Esto se siente como ponerse un uniforme de prisionero."

    yamada "¡Deja de ser tan dramático! Póntelo. La reunión con el departamento administrativo empieza en cinco minutos."

    hide yamada_basic_happy with dissolve

    "Me coloco el saco y me ajusto el nudo de la corbata frente al reflejo del monitor apagado."
    "El ajuste es sofocante, pero supongo que es el precio de encajar en el molde empresarial otra vez."

    # ------------------------------------------------------------------------------------------------------
    # --- ESCENA 3: Administración Empresarial ---
    # ------------------------------------------------------------------------------------------------------

    "Reviso los documentos sobre la mesa antes de la entrevista administrativa."
    "El primer dilema financiero y estratégico para el lanzamiento de las 'Angels' está frente a mí."
    "Tengo que definir la prioridad presupuestaria para el trimestre."

    menu:
        "Invertir la mayor parte del presupuesto en la campaña publicitaria y marketing algorítmico.":
            play sound "audio/UI/Retro5.wav"
            $ pts_airi += 1
            "Si queremos números rápidos, la imagen lo es todo."
            "El algoritmo favorece la visibilidad agresiva sobre la sustancia."
            "Maximizar la presencia en redes desde el día uno."

        "Asignar los recursos a la producción musical y entrenamiento técnico.":
            play sound "audio/UI/Retro5.wav"
            $ pts_kaori += 1
            "La fachada no durará si el producto de fondo es mediocre."
            "Es mejor construir una base artística sólida, aunque el crecimiento sea más lento al principio."

        "Priorizar la seguridad, moderación de comunidad y bienestar de las chicas.":
            play sound "audio/UI/Retro5.wav"
            $ pts_ruka += 1
            "Conozco los riesgos de esta industria. Proteger el entorno del talento evitará crisis a largo plazo."
            "Minimizar la exposición tóxica antes de que el público empiece a consumir sus vidas."

    mutou "Listo. La estrategia está trazada."

    scene black with fade

    "La reunión con los ejecutivos pasa entre gráficos de barras, proyecciones de retención de audiencia y presupuestos fríos."
    "Hago mi trabajo. Respondo con precisión quirúrgica, justo como solía hacerlo hace cinco años."
    "Los ejecutivos asienten satisfechos. Para ellos, solo soy otra pieza funcional del engranaje."

    # ------------------------------------------------------------------------------------------------------
    # --- ESCENA 4: Kaori Sumizome ---
    # ------------------------------------------------------------------------------------------------------

    scene oficina with fade

    "Salgo de la sala de reuniones aflojándome un poco el nudo de la corbata. El dolor de cabeza ha vuelto."

    show yamada_basic_happy with easeinleft

    yamada "¡Mutou! ¡Increíble trabajo allí dentro!"
    yamada "El departamento financiero aprobó la propuesta sin dudarlo."

    mutou "Solo les dije lo que querían escuchar..."

    yamada "¡Como sea, fue fantástico! Y justo a tiempo, porque quiero presentarte oficialmente a una de las chicas del proyecto Angels."
    yamada "Ella estaba ensayando cerca."
    yamada "¡Pasa, por favor!"

    "Escucho pasos acercándose desde el pasillo."
    "Una chica entra a la oficina. Ya no lleva la gorra ni la bufanda alta que le cubría el rostro..."
    "Pero reconozco esa mirada de inmediato."

    hide yamada_basic_happy
    show yamada_basic_happy at left with dissolve
    show kaori_basic_neutral at right with dissolve

    yamada "Mutou, ella es Kaori Sumizome, una de nuestras promesas para el nuevo grupo."
    yamada "Kaori, él es Mutou, el mánager sénior que estará a cargo del proyecto."

    hide kaori_basic_neutral
    show kaori_basic_confused at right

    "Kaori se queda helada al verme. Sus ojos se abren levemente por la sorpresa al conectar las piezas."
    "El hombre con el traje arrugado y el encendedor en el callejón de basura es su posible nuevo mánager."

    mutou "..."
    
    kaori "..."

    "Yo mantengo la cara completamente seria, sin revelar la más mínima emoción."
    "Ella reacciona rápido, recomponiendo su expresión neutral en una fracción de segundo."

    hide kaori_basic_confused
    show kaori_basic_neutral at right

    yamada "¿Eh? ¿Pasa algo? Se quedaron mirándose muy raro..."

    mutou "No, nada. Mucho gusto, Kaori."

    "Kaori da un paso al frente y hace una leve inclinación respetuosa."

    kaori "El gusto es mío... Mánager. Espero que podamos hacer un buen trabajo."

    yamada "¡Excelente! Kaori tiene un talento increíble para la composición, aunque a veces es bastante silenciosa..."

    # Sonido de teléfono sonando
    play sound "audio/sfx/phone_ring.wav"

    "El teléfono celular en el bolso de Kaori empieza a vibrar, interrumpiendo a Yamada."
    "Kaori revisa la pantalla rápidamente. Su ceño se frunce por un instante."

    kaori "Lo siento... tengo que responder esto. Es de... Lo siento."
    kaori "Con su permiso."

    hide kaori_basic_neutral with dissolve

    "Kaori da media vuelta y sale de la oficina a prisa mientras contesta la llamada."

    hide yamada_basic_happy
    show yamada_basic_smile at left

    yamada "Vaya... siempre está tan ocupada."
    yamada "Pero tiene un potencial enorme, ¿no crees?"

    mutou "Sí... Se nota que sabe lo que hace."

    "Miro hacia la puerta por donde se acaba de ir."
    "Así que una de las Angels que debo moldear es la chica que me pidió fuego esta mañana..."
    "El mundo en esta industria es ridículamente pequeño."

    mutou "Yamada, voy a quitarme esta corbata."

    yamada "¡Ah! ¡Espera, Mutou, déjatela puesta para la foto de perfil!"

    scene black
    with fade

    "Día 2 terminado."

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
    
    # Salto hacia el siguiente capitulo
    jump a1c4
