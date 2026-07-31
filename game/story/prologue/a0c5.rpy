label a0c5:

    # ------------------------------------------------------------------------------------------------------
    # --- ESCENA 1: Fans ---
    # ------------------------------------------------------------------------------------------------------

    # Falta el fondooo
    # scene lobby_evento with fade
    scene pasillo_pilares with fade

    "El vestíbulo principal de DokiWave Entertainment está repleto de flashes, murmullos emocionados y un mar de fanáticos."
    "Banners gigantes con los rostros de las integrantes de Angels cuelgan del techo."
    "La atmósfera rebosa entusiasmo fingido y devoción comercial."
    "Observo la escena desde una distancia prudente, manteniendo los brazos cruzados."
    "Las chicas están distribuidas en mesas individuales firmando autógrafos y posando con sonrisas perfectamente ensayadas para las cámaras."

    show yamada_basic_happy with dissolve

    "Diviso a Yamada a unos metros."
    "Está reunida con dos hombres de traje oscuro e insignias corporativas doradas en la solapa: ejecutivos de alto rango."
    "Me acerco a ellos a paso lento."

    mutou "Yamada."

    hide yamada_basic_happy
    show yamada_basic_smile

    yamada "¡Ah, Mutou! Qué bueno que te acercas."
    yamada "Estaba comentándole a los directivos sobre la excelente recepción del evento de hoy."
    yamada "Los números de interacción en vivo están superando todas las proyecciones del trimestre."

    mutou "Me alegra escuchar eso..."

    "Echó una mirada discreta hacia los lados antes de bajar el tono de voz, dirigiéndome directamente a Yamada."

    mutou "Oye, Yamada... sobre el asunto de ayer. El señor problemático..."
    mutou "¿Cómo va esa situación?"

    hide yamada_basic_smile
    show yamada_basic_happy

    "Yamada no pestañea. Su sonrisa no flaquea ni un solo milímetro; al contrario, se vuelve extrañamente más brillante y relajada."

    yamada "¡Ah, eso! No te preocupes en absoluto, Mutou. Ya está bien."
    yamada "Ya está todo perfectamente arreglado."
    yamada "La directiva y el equipo especializado ya se encargaron por completo de ese problema."

    "Frunzo ligeramente el ceño. La respuesta me toma por sorpresa."

    mutou "Vaya... Deben tener programadores francamente brillantes en el área de sistemas para haber erradicado el botting y las publicaciones tan rápido."

    hide yamada_basic_happy
    show yamada_basic_confused

    yamada "...¿Programadores?"

    "Yamada se me queda viendo con una expresión de desconcierto genuino, ladeando la cabeza como si hubiera dicho una insensatez."

    mutou "...¿Sí? Me refiero a la limpieza de redes y los servidores. ¿No?"

    hide yamada_basic_confused
    show yamada_basic_smile

    "El desconcierto de Yamada dura solo una fracción de segundo antes de disolverse en esa misma serenidad inquebrantable."

    yamada "Ah... claro, las redes. No te preocupes por los detalles técnicos, Mutou."
    yamada "Te aseguro que ya todo está bien. El asunto está cerrado."

    "Esa calma... esa tranquilidad desmedida y casi robótica hace que se me revuelva el estómago."
    "Hay algo en su tono de voz que no encaja. Una frialdad oculta tras una capa de amabilidad corporativa."

    # ------------------------------------------------------------------------------------------------------
    # --- ESCENA 2: Cena ---
    # ------------------------------------------------------------------------------------------------------

    # Falta el fondooo
    # scene comedor_elegante with fade
    scene maceta with fade

    "El evento público concluye sin contratiempos."
    "Nos trasladamos a un restaurante exclusivo a pocas calles de la agencia. Un comedor privado de iluminación cálida, maderas nobles y cristalería de lujo."
    "Un lugar reservado únicamente para la élite de la empresa y sus proyectos prioritarios."
    "Todas las chicas de Angels ya están sentadas en la mesa principal, conversando en voz baja entre ellas."
    "Sin embargo, la inquietud dentro de mi pecho no ha hecho más que crecer."
    "¿'Ya se encargaron de ese problema'?"
    "Esa frase no deja de repetirse en mi cabeza como un eco distante."
    "Algo no está bien... Algo pasó. Tengo que comprobarlo ahora mismo."

    show yamada_basic_happy

    "Me dirijo hacia Yamada antes de tomar asiento."

    mutou "Yamada, disculpa un momento. Voy al sanitario, no tardo."

    yamada "Claro, Mutou. No te demores, ya van a servir la cena."

    # Falta el fondooo
    # scene baño_elegante with dissolve
    scene pasillo_vacio with dissolve

    "Entro al baño del restaurante, me acerco al lavabo y abro el grifo para que el ruido del agua disimule cualquier sonido."
    "Saco rápidamente mi teléfono celular de la bolsa del saco."
    "Mis dedos se mueven con prisa sobre la pantalla."
    "Tecleo en el buscador: 'Kenjiro Sato' 'DokiWave' 'Detención' 'Protesta'."
    "Nada. Cero resultados recientes. Ni arrestos, ni notas sobre un manifestante afuera del edificio."
    "Borro los filtros de búsqueda y pruebo con términos más amplios de noticias locales de las últimas cuarenta y ocho horas."
    "Paso varios titulares irrelevantes hasta que un artículo de una nota roja local llama mi atención:"

    "{i}\"Hallazgo en distrito residencial: Hombre es encontrado sin vida en su departamento. Presunto suicidio.\"{/i}"

    "Leo el cuerpo de la noticia con frialdad analítica."
    "El artículo no menciona ningún nombre completo. Solo se refiere a la víctima como {i}'S' (47 años){/i}."
    "Reviso rápidamente los datos: la hora estimada del deceso coincide con la noche posterior a mi encuentro con él en el estacionamiento."
    "La zona es el mismo barrio humilde que figuraba en la dirección del antiguo expediente de Saori."
    "Recuerdo las palabras desoladas de Sato ayer..."
    "Recuerdo la sonrisa impecable de Yamada hace unos minutos al decir {i}'ya nos encargamos'{/i}."

    play sound "audio/sfx/heart_echo.wav"

    mutou "Lo mataron..."

    "No fue un suicidio. Lo eliminaron para proteger la imagen del proyecto Angels y silenciar las difamaciones antes del lanzamiento."
    "Aprieto el teléfono con tanta fuerza que mis nudillos se vuelven blancos."
    "La bilis me vuelve a subir por la garganta."

    with hpunch # Sacudida de pantalla

    "Un mareo repentino me obliga a sujetarme del borde del lavabo."
    "El sonido de la puerta del baño abriéndose me hace guardar el teléfono de un tirón."

    # Ejecutivo de DokiWave
    "Un ejecutivo de alto nivel de DokiWave entra al sanitario."
    "Se me queda mirando al notar mi rostro pálido y las gotas de sudor frío en mi frente."

    unknown "Vaya, Mutou... Te ves pésimo. ¿Estás bien? Te ves blanco como un papel."

    mutou "Solo... un poco de mareo."
    mutou "Por el cansancio acumulado..."

    unknown "Esta industria nos agota a todos."
    unknown "Toma, estas pastillas son excelentes para la migraña y la presión."

    "El ejecutivo saca un pequeño frasco y me ofrece dos comprimidos."

    mutou "Gracias..."

    "Tomo las pastillas."
    "Me llevo la mano a la boca simulando tragarlas con un sorbo de agua del grifo, pero con un movimiento rápido y practicado las dejo caer disimuladamente por el drenaje."
    "Seco mis manos y mi rostro con una toalla de papel. Aprieto los dientes, me compongo el saco frente al espejo y salgo del sanitario."

    # ------------------------------------------------------------------------------------------------------
    # --- ESCENA 3: Angels ---
    # ------------------------------------------------------------------------------------------------------

    # Falta el fondooo
    # scene comedor_elegante with fade
    scene maceta with fade

    "Regreso al comedor privado."
    "Yamada me ve entrar y me hace una seña entusiasmada desde la cabecera de la gran mesa de caoba."

    show yamada_basic_happy at left with dissolve

    yamada "¡Aquí estás, Mutou! Ven, guardé el asiento de honor justo aquí para ti."

    hide yamada_basic_happy with dissolve

    "Me siento en el lugar indicado."
    "A mi alrededor están todas las integrantes del proyecto 'Angels'."

    show ruka_basic_neutral at left with dissolve
    show airi_basic_smile at center with dissolve
    show kaori_basic_neutral at right with dissolve

    "Ruka, Airi, Kaori... todas vestidas con ropa elegante pero juvenil, observándome con curiosidad."

    mutou "Buenas noches a todas. Lamento la demora."

    "Empiezo a hablar con ellas. Respondo a sus preguntas sobre la planificación de los ensayos, los presupuestos aprobados y las futuras sesiones de grabación."
    "Mi voz suena serena, profesional, impecable... pero por dentro mi mente está completamente disociada."
    "Mientras Airi habla sobre sus rutinas de baile, la imagen del cuerpo del señor Sato en un departamento frío se cruza por mi pensamiento."
    "Mientras Ruka responde formalmente sobre sus lecciones de canto, pienso en Saori Sato... la chica que se quitó la vida hace seis años tras ser exprimida por este mismo sistema."
    "Y entonces... el recuerdo inevitable golpea mi cabeza."

    play sound "audio/sfx/echo.wav"

    "El día en que murió {i}Minami{/i}."
    "La idol más grande de DokiWave. La cima de la industria. La chica que lo tenía todo según los medios, hasta que la encontraron sin vida en aquella noche de lluvia."
    "Un asco profundo, viscoso y amargo me llena el pecho."
    "El verdadero rostro de esta empresa sigue siendo el mismo. Una maquinaria que tritura personas y luego limpia la escena con una sonrisa."

    # ------------------------------------------------------------------------------------------------------
    # --- ESCENA 4: Fin del Prólogo ---
    # ------------------------------------------------------------------------------------------------------

    "La cena concluye entre risas breves, copas de vino y platos caros devorados a medias."
    "Los ejecutivos se despiden cordialmente y casi todos comienzan a abordar las camionetas privadas que los llevarán a sus casas."
    "Me pongo de pie tranquilamente."

    show yamada_basic_happy with dissolve

    yamada "¿Te vas ya, Mutou? Podemos compartir el transporte."

    mutou "No gracias, Yamada. Voy a salir a tomar un poco de aire primero."

    hide yamada_basic_happy
    show yamada_basic_confused with Pause(0.3)

    # Falta el fondooo
    # scene calle_noche with fade
    scene exterior with fade

    "Salgo del restaurante hacia la calle fría y despejada."
    "El aire nocturno de la ciudad me golpea el rostro, disipando un poco el sofoco del comedor."
    "Saco una cajetilla de mi bolsillo, extraigo un cigarrillo y me lo llevo a los labios."
    "Hago chasquear el encendedor."
    "La pequeña llama naranja ilumina la penumbra por un instante antes de encender el tabaco."
    "Doy una calada profunda, dejando que el humo amargo llene mis pulmones."
    "Miro hacia la nada en medio de la noche iluminada por los letreros de neón de la ciudad."

    scene black with fade
    
    # Marcamos el logro como completado de forma permanente
    $ persistent.prologue_completed = True

    # Notificación flotante en pantalla
    $ renpy.notify("Logro desbloqueado: Prologo Completado")
    
    "Capítulo 5 terminado."

    # ------------------------------------------------------------------------------------------------------
    # --- PANTALLA DE LA CITA ---
    # ------------------------------------------------------------------------------------------------------

    with Pause(1.5)
    window hide

    # Cita sobre la verdad, el silencio y la tragedia
    show text "{i}\"Lo preocupante no es la perversidad de los malvados, sino el silencio de los buenos.\"{/i}\n\n-- Martin Luther King Jr." at truecenter with dissolve
    $ renpy.pause()

    hide text with dissolve
    with Pause(1.0)
    window auto
    
    # Salto hacia el siguiente acto, el de Airi (provisional)
    jump a1c1_airi
