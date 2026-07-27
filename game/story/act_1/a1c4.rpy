label a1c4:

    # ------------------------------------------------------------------------------------------------------
    # --- ESCENA 1: La furia de Yamada ---
    # ------------------------------------------------------------------------------------------------------

    scene oficina with fade

    "El ambiente en la oficina de DokiWave es tenso."
    "El constante tecleo furioso de Yamada rompe el silencio del lugar."
    "Tiene la mirada fija en el monitor, con los puños apretados."

    show yamada_basic_angry with dissolve

    yamada "¡No puede ser! ¡Otra vez este sujeto!"
    yamada "¡Es insoportable! ¿Es que no tiene nada mejor que hacer con su vida que arruinar nuestro trabajo?"

    "Me acerco a su escritorio, cruzándome de brazos."

    mutou "¿Qué pasa, Yamada? Pareces a punto de romper el teclado."

    hide yamada_basic_angry
    show yamada_basic_confused

    yamada "Ah, Mutou..."
    yamada "Es que... ese hombre de nuevo, no deja de publicar difamaciones sobre DokiWave en redes sociales."
    yamada "Está intentando tirar los foros oficiales del proyecto Angels."
    yamada "Dice que la empresa explota a las chicas, que destruimos vidas... ¡Puras mentiras para arruinar la imagen de la marca!"

    mutou "...¿Un saboteador?"

    yamada "Sí. Lleva meses en esto. Los chicos de sistemas borran sus publicaciones, pero siempre vuelve con cuentas nuevas."
    yamada "¡Incluso ha venido a pararse afuera del edificio a gritar cosas! Es un hombre problemático. La seguridad ya lo tiene identificado."

    "Miro la pantalla. Decenas de mensajes bloqueados y hilos eliminados. La desesperación en las palabras de ese sujeto es casi palpable a través del texto."

    mutou "Yamada, llevas horas frente a esa pantalla. Te va a explotar la cabeza."
    mutou "Déjalo. Los de sistemas se encargarán. Ve a tomarte un descanso, ve por un café o algo."

    hide yamada_basic_confused
    show yamada_basic_smile

    yamada "Pero... el reporte para la directiva..."

    mutou "Yo me quedo aquí un momento. Ve."

    yamada "Está bien... Tienes razón. Necesito un respiro. Gracias, Mutou."

    hide yamada_basic_smile with easeoutleft

    "Los pasos de Yamada se alejan."
    "Me quedo solo frente a la pantalla. Leo uno de los comentarios antes de que el filtro automático lo borre:"
    "'¡Devuélvanme a mi hija, asesinos! ¡DokiWave oculta la verdad!'"

    mutou "Su hija..."

    "El aire en la oficina se siente sofocante. Necesito salir de aquí un momento antes de que la cabeza empiece a dolerme otra vez."

    # ------------------------------------------------------------------------------------------------------
    # --- ESCENA 2: El estacionamiento ---
    # ------------------------------------------------------------------------------------------------------

    scene estacionamiento_cerca with fade

    "Salgo por la puerta trasera hacia la acera del estacionamiento."
    "El cielo está nublado y el viento frío de la tarde me golpea la cara."
    "Camino despacio con las manos en los bolsillos, buscando un poco de aire limpio."
    "De repente, el sonido de unas pisadas apresuradas sobre el asfalto me pone en alerta."

    # Kenjiro Sato (Padre de Saori)

    #show kenjiro_basic_angry

    "Un hombre maduro, de ropas desgastadas y mirada desencajada, sale de entre los autos estacionados y corta mi paso bruscamente."

    unknown "¡Tú! ¡Tú eres el nuevo mánager del proyecto Angels!"

    "Instintivamente doy un paso atrás, dando un perfil defensivo y apretando los puños dentro de mis bolsillos."

    mutou "Aléjate. Si das un paso más, llamaré a la seguridad del edificio."

    unknown "¡No me voy a ir!"
    unknown "¡Escúchame, maldita sea!"

    "El hombre levanta las manos, pero no para golpear. Le tiemblan descontroladamente."
    "Su rostro está demacrado, con ojeras profundas que delatan años sin dormir bien."

    unknown "No quiero hacerte daño... Solo... solo escúchame. Por favor."

    "Su voz se quiebra. La hostilidad inicial se desmorona, dejando ver solo una desesperación aplastante."

    mutou "...¿Quién eres?"

    sato "Mi nombre es Kenjiro Sato..."
    sato "Mi hija... mi hija se llamaba Saori... Saori Sato"

    # Latidos
    play sound "audio/sfx/heart_echo.wav"
    
    "Sa... ¿Saori?"
    "Ese nombre retumba en mi memoria como un eco distante."
    "Saori. Una de las idols más populares de DokiWave hace unos seis años."
    "Famosa por su sonrisa genuina, su amabilidad con el personal y su carisma arrollador."
    "Sucedió un año antes del incidente de... ella."
    "La mayor estrella."
    "Cuando Saori murió, la noticia apenas duró dos días en los medios..."
    "DokiWave lanzó un comunicado frío atribuyéndolo a 'complicaciones de salud preexistentes' y sofocó cualquier rumor."

    sato "Ella no estaba enferma..."
    sato "Mi pequeña Saori... me llamaba llorando por las noches desde su dormitorio."
    sato "Me contaba cómo la hacían trabajar 18 horas seguidas, cómo la amenazaban con multas millonarias si no sonreía, cómo la aplastaban por dentro..."
    sato "¡DokiWave la mató!"
    sato "¡Se quitó la vida porque ya no podía más!"

    "Sato se pasa la mano temblorosa por el rostro, ahogando un sollozo."

    sato "La empresa compró el silencio de los periódicos. Hicieron parecer que mi hija no importaba..."
    sato "Pero para mí..."
    sato "Para mí..."
    sato "Lo era todo."
    sato "Y ahora... ahora veo los carteles del proyecto 'Angels'. Veo a esas chicas nuevas en las pantallas..."
    sato "Sé quién eres tú, Mutou. Sé que fuiste el mánager estrella de esta mierda de empresa."

    "Sato me mira directamente a los ojos..."
    "Su mirada rota me atraviesa el pecho."

    sato "Te lo suplico... Como padre, te lo suplico en nombre de Saori."
    sato "No dejes que se los vuelvan a hacer."
    sato "No dejes que esas chicas terminen en una bolsa de plástico como mi hija o como... esa otra pobre muchacha."
    sato "Haz algo... Por favor... Haz algo..."
    sato "Por favor..."

    "El hombre da media vuelta, arrastrando los pies hacia la salida del estacionamiento, dejándome completamente solo en la penumbra."

    # ------------------------------------------------------------------------------------------------------
    # --- ESCENA 3: Colapso ---
    # ------------------------------------------------------------------------------------------------------

    "Un mareo violento me hace perder el equilibrio. Me apoyo torpemente contra la carrocería de un auto cercano."
    "La bilis me sube a la garganta."
    "Siento una náusea profunda, un asco visceral que me revuelve el estómago."

    mutou "Saori..."

    # Chillido
    play sound "audio/sfx/echo.wav"

    "Un dolor punzante me atraviesa las sienes, como un clavo ardiente introduciéndose en mi cerebro."
    "Apenas puedo respirar."
    "Sacando las llaves del bolsillo a duras penas, me subo a mi auto en el asiento del conductor y cierro la puerta de golpe."

    scene black with fade

    "Me desmorono sobre el volante."

    # Latidos
    play sound "audio/sfx/heart_echo.wav"

    "El sonido de mi propia respiración agitada retumba en el habitáculo cerrado."
    "Cierro los ojos, pero las imágenes se agolpan: el rostro del señor Sato, las sonrisas de Airi, Ruka y Uta en sus expedientes..."
    "Y la silueta en el suelo de aquella noche de lluvia."
    "Pasan los minutos."
    "O tal vez horas."
    "Poco a poco, el dolor de cabeza se convierte en un latido sordo y distante. Obligo a mi cuerpo a recomponerse."

    # ------------------------------------------------------------------------------------------------------
    # --- ESCENA 4: Chocolate caliente ---
    # ------------------------------------------------------------------------------------------------------

    scene oficina with fade

    "Cuando regreso al edificio, las luces principales ya están apagadas."
    "Yamada sigue en su escritorio, pero su postura es mucho más relajada. Sostiene una taza humeante entre sus manos."

    show yamada_basic_happy with dissolve

    yamada "¡Ah, Mutou! ¡Volviste!"
    yamada "Te busqué por todas partes."

    mutou "Estaba... despejándome la cabeza."

    hide yamada_basic_happy
    show yamada_basic_smile

    yamada "Te ves exhausto."
    yamada "Sabes, no hay nada mejor para el estrés de la tarde que un buen chocolate caliente."
    yamada "Comprare dos en la cafetería del primer piso. Ven, tómate un momento conmigo."

    # Aun no tengo fondo de una caferia
    scene zona_descanso with dissolve

    "Nos sentamos en una de las mesas de la cafetería de la empresa."
    "El vapor del chocolate caliente sube lentamente entre los dos."
    "Doy un pequeño sorbo; el dulzor resulta casi empalagoso, pero ayuda a asentarme el estómago."

    show yamada_basic_happy

    yamada "Mmm... ¡delicioso! Justo lo que necesitaba después de la rabieta de esta tarde."

    mutou "Oye, Yamada..."
    mutou "Sobre el sujeto de los comentarios de hoy..."

    hide yamada_basic_happy
    show yamada_basic_smile

    "El rostro de Yamada cambia sutilmente."
    "Ignora mi mención con una agilidad casi ensayada, tomando otro sorbo de su taza."

    yamada "¡Ay, no hablemos de cosas feas a estas horas!"
    yamada "Todo eso ya está bajo control."
    yamada "Lo que realmente importa es lo de mañana. ¡Mañana es el gran día!"

    mutou "¿Mañana?"

    yamada "¡El convivio de bienvenida!"
    yamada "En el vestíbulo del edificio principal."
    yamada "Las chicas de Angels estarán ahí regalando autografos y saludando a los fans para las cámaras de prensa."
    yamada "Será su primer contacto oficial como grupo."

    mutou "Entiendo..."

    yamada "Y lo mejor viene después. Al terminar el evento, la agencia reservó un comedor privado para cenar todos juntos."
    yamada "Airi, Ruka, Kaori, bueno todas. Finalmente podrán hablar contigo en persona, cara a cara, como su nuevo mánager."
    yamada "Ahora si, formal y nada de presentaciones apresuradas, lo prometo."
    yamada "Así que descansa bien esta noche, Mutou. Mañana vas a tener que causar una buena impresión."

    "Miro a Yamada mientras ella continúa hablando sobre los preparativos, la logística y los horarios del evento."
    "Domina la conversación por completo, desviando cualquier intento de volver al tema del señor Sato o Saori."
    "Bajo la mirada a mi taza de chocolate."
    "Mañana será. Mañana empieza oficialmente el juego."

    scene black with fade



    # Marcamos el logro como completado de forma permanente
    $ persistent.act1_completed = True

    # Notificación flotante en pantalla
    $ renpy.notify("Logro desbloqueado: Acto 1 Completado")



    "Día 3 terminado."

    # ------------------------------------------------------------------------------------------------------
    # --- PANTALLA DE LA CITA ---
    # ------------------------------------------------------------------------------------------------------

    with Pause(1.5)
    window hide

    # Cita sobre la culpa, la responsabilidad colectiva y los secretos
    show text "{i}\"El monstruo no se crea en la oscuridad; se alimenta del silencio de quienes ven la luz y deciden mirar hacia otro lado.\"{/i}\n\n-- Arthur Miller, {i}Las brujas de Salem{/i} (1953)." at truecenter with dissolve
    $ renpy.pause()

    hide text with dissolve
    with Pause(1.0)
    window auto
    
    # Salto hacia el siguiente acto, el de Airi (provisional)
    jump a2c1_airi
