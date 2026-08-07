label a1c1_airi:

    # ------------------------------------------------------------------------------------------------------
    # --- ESCENA 1: Sombras bajo la sonrisa ---
    # ------------------------------------------------------------------------------------------------------

    scene exterior with fade

    "El frío de la noche me cala los huesos mientras sostengo el cigarrillo entre los dedos."
    "Las luces de neón del distrito comercial parpadean a lo lejos, reflejándose en los charcos del asfalto como manchas de tinta brillante."
    "Doy una calada profunda, dejando que el humo amargo llene mis pulmones para anestesiar el dolor de cabeza que me dejó la reunión."
    "A mis espaldas, la puerta de cristal del restaurante de lujo se abre, dejando escapar amortiguadas las risas y el sonido de copas chocando de los ejecutivos que se quedaron a celebrar."
    "El sonido tarareado de una melodía alegre y juvenil se aproxima a paso rápido."

    show airi_basic_happy with dissolve

    "Airi sale dando pequeños brincos sobre los escalones de piedra, acomodándose el cabello apresuradamente como si estuviera escapando de una jaula."
    "Su cabello plateado resalta demasiado contra la sobriedad del edificio corporativo."
    "Al verme apoyado en la barandilla metálica, sus ojos brillan con un entusiasmo infantil, casi desesperado."

    airi "¡Mánager~! ¡Sabía que estabas aquí afuera atrapando el aire helado!"

    mutou "Hola, Airi."
    mutou "¿La cena estuvo buena? Te saliste muy rápido."

    hide airi_basic_happy
    show airi_basic_smile

    airi "¡Súper rica! Aunque los señores de la junta directiva hablan horriblemente aburrido..."
    airi "Todo el tiempo hablando de 'proyecciones trimestrales', 'retención de usuarios' y 'conversión de audiencias'."
    airi "¡Ni que fuéramos máquinas de escribir o robots!"
    airi "Me dolía la cabeza de tanto sonreír a la nada..."

    "Airi se apoya a mi lado en la barandilla de metal, soltando un largo suspiro de alivio."
    "Observa el humo gris de mi cigarrillo elevarse y disiparse hacia el cielo nocturno."
    "El viento helado de la medianoche sopla despacio, haciendo flamear las luces de neón sobre las facciones de su rostro."
    "Por un momento, el silencio entre los dos se alarga."
    "La energía desbordante y casi ruidosa de Airi empieza a disiparse de forma gradual, como si la batería que la mantiene encendida se estuviera agotando."

    hide airi_basic_smile
    show airi_basic_surprised

    "Su mirada, antes chispeante y llena de vida, pierde el foco por completo. Se vuelve extrañamente distante, perdida en la inmensidad vacía de la ciudad."
    "Sus hombros caen un par de centímetros."

    airi "Oye, Mánager..."

    mutou "¿Qué pasa, Airi?"

    airi "..."
    airi "¿Alguna vez has sentido... que no eres tú quien realmente vive tu vida?"

    "La pregunta me toma completamente desprevenido."
    "Sostengo el cigarrillo a medio camino de mi boca y giro la cabeza para mirarla con atención."

    mutou "¿A qué te refieres exactamente?"

    hide airi_basic_surprised
    show airi_basic_smile

    "Airi contempla sus propias manos apoyadas en el metal frío, abriendo y cerrando los dedos despacio, como si los estuviera descubriendo por primera vez."

    airi "A veces... me miro al espejo antes de salir al escenario o escucho mi propia voz hablando con los ejecutivos..."
    airi "Y siento como si otra persona estuviera usando mi cuerpo para moverse."
    airi "Como si la verdadera Airi estuviera atrapada al fondo de una habitación oscura y cerrada, viendo a través de una pantalla cómo alguien más maneja mis sonrisas, mis gestos y mis palabras."

    play sound "audio/sfx/echo.wav"

    "Un escalofrío helado, más frío que el viento nocturno, me recorre la columna vertebral."
    "El contraste entre la Airi eufórica que brincaba en las escaleras hace dos minutos y esta frialdad es aplastante."

    airi "Hay días en los que siento una chispa gigante en el pecho, unas ganas enormes de cantar hasta romper la noche... y al segundo siguiente..."
    airi "Puff. Todo se apaga."
    airi "Miro a la chica sonriente que estaba cantando hace un instante y siento que es una extraña total."
    airi "Es como si..."
    airi "...alguien a quien no conozco."
    airi "¿Es raro sentir que vives con el fantasma de otra persona adentro tuyo, Mánager?"

    "Miro la profundidad vacía en sus ojos."
    "No hay rastro de broma ni de actuación en su postura."
    "Es real."

    menu:
        "Reconfortarla.":
            play sound "audio/UI/Retro5.wav"
            mutou "Es el agotamiento, Airi. La presión de la empresa hace que la mente cree mecanismos de defensa."
            mutou "No eres un fantasma. Solo estás exhausta."
            
        "Ofrecerle un momento de calma.":
            play sound "audio/UI/Retro5.wav"
            $ aff_airi += 1
            mutou "Airi... no sé qué responderte a eso..."
            mutou "Pero no eres un fantasma."
            mutou "Estás viva."

    hide airi_basic_smile
    show airi_basic_happy

    "Como si alguien hubiera accionado un interruptor interno en su cerebro, la mirada distante de Airi desaparece en una fracción de segundo."
    "La frialdad en sus ojos se evapora y su amplia y radiante sonrisa regresa como si nada hubiera pasado."

    airi "¡Jeje~! ¡Ay, Mánager! ¡No me hagas caso!"
    airi "¡A veces digo cosas super raras cuando me da el viento helado directo en la cabeza!"
    airi "¡Seguramente fue por el postre tan dulce que sirvieron en la cena! ¡Olvídalo, olvídalo!"
    airi "¡Airi está genial y lista para ser la número uno!"

    "Se ríe alegremente, una risa aguda que suena ensayada."
    "Sin embargo, alcanzo a notar un leve temblor en la comisura de sus labios y el tono blanco de sus nudillos apretando la barandilla."

    mutou "Airi..."

    hide airi_basic_happy
    show airi_basic_smile

    "Airi se queda congelada por un instante imperceptible al escuchar la gravedad en mi voz."

    # ------------------------------------------------------------------------------------------------------
    # --- ESCENA 2: Despedida y Trayecto ---
    # ------------------------------------------------------------------------------------------------------

    "Un auto blanco de lujo con cristales polarizados se detiene suavemente junto a la banqueta, haciendo sonar dos pitidos breves de la bocina."

    show airi_basic_happy with dissolve

    airi "¡Oh vaya! ¡Llegó el transporte del dormitorio!"
    airi "¡Nos vemos mañana temprano en la agencia, Mánager! ¡Descansa mucho y no fumes tanto!"

    "Airi baja los escalones corriendo, recuperando su andar ligero."
    "Sube al auto y me saluda efusivamente con la mano desde la ventana mientras el vehículo se incorpora al tráfico de la ciudad."

    mutou "Tú también cuídate, Airi..."

    hide airi_basic_happy with dissolve

    "Me quedo solo en la acera."
    "Termino el cigarrillo con una última calada amarga y lo apago en el cenicero de pie junto a la entrada."

    scene estacionamiento with fade

    "Camino a paso lento hacia el estacionamiento subterráneo del restaurante."
    "El eco de mis pisadas sobre el concreto húmedo resuena con monotonía."
    "Las palabras de Airi rebotan en mi mente con la fuerza de un martillazo."
    "'¿Alguna vez has sentido que no eres tú quien realmente vive tu vida...?'"
    "Llego a mi vehículo, quito el seguro con un chasquido metálico y me dejo caer en el asiento del conductor."
    "Giro la llave, el motor cobra vida y salgo hacia las avenidas principales conduciendo en un silencio sepulcral."

    scene black with fade
    with Pause(1.0)

    # ------------------------------------------------------------------------------------------------------
    # --- ESCENA 3: Registro en la Libreta ---
    # ------------------------------------------------------------------------------------------------------

    scene oficina with fade

    "Llego a mi pequeño y austero departamento pasada la medianoche."
    "El lugar huele a café frío y humo viejo. Lanzo las llaves sobre la mesa de la entrada y me quito el saco."
    "Saco mi libreta de notas personal —la que no pasa por la revisión de Yamada ni de los directivos— y me siento a escribir."

    "Escribo con trazos firmes en el apartado reservado para Airi:"

    "{i}'Airi. Su hiperactividad y alegría desbordante son una máscara de supervivencia extremadamente frágil.'{/i}"
    "{i}'Muestra signos claros de disociación y fragmentación emocional. La persona sonriente que interactúa con los fans es una fachada que su mente creó para protegerse.'{/i}"
    "{i}'Si la empresa la presiona demasiado con el ritmo del algoritmo y las exigencias de la industria, la fachada colapsará por completo.'{/i}"

    "Dejo el bolígrafo sobre el papel y cierro la libreta de golpe."

    # ------------------------------------------------------------------------------------------------------
    # --- ESCENA 4: El Expediente de Airi ---
    # ------------------------------------------------------------------------------------------------------

    "Me quito la corbata, apago las luces del departamento y me acuesto en la cama."
    "Me quedo mirando la oscuridad del techo mientras el murmullo lejano de la ciudad se apaga."
    "Trato de cerrar los ojos para conciliar el sueño, pero la mente se niega a descansar."
    "En la penumbra de la habitación, las imágenes del expediente clasificado de Airi —aquel que revisé en la oficina de DokiWave antes del evento— empiezan a proyectarse en mi memoria con nitidez dolorosa."

    play sound "audio/sfx/echo.wav"

    "Recuerdo la carpeta negra con el sello rojo de la directiva:"

    "{i}======================================================{/i}"
    "{i}EXPEDIENTE DE EVALUACIÓN TÉCNICA - PROYECTO ANGELS{/i}"
    "{i}INTEGRANTE 01: Airi Hoshino (18 años){/i}"
    "{i}======================================================{/i}"

    "{i}'[PERFIL COMERCIAL]: Alta retención de audiencia juvenil. Excelente capacidad de improvisación y carisma escénico sobresaliente.'{/i}"
    "{i}'[EVALUACIÓN PSICOLÓGICA DE AGENCIA]: Presenta episodios recurrentes de inestabilidad afectiva y desconexión de identidad tras jornadas prolongadas.'{/i}"
    "{i}'[RECOMENDACIÓN DEL DEPARTAMENTO MÉDICO]: Se sugiere acompañamiento psicológico y reducción de horas de exposición.'{/i}"
    "{i}'[DIRECCIÓN EXECUTIVA - NOTA FINAL]: RECHAZADO. No se aprobarán terapias ni reducciones de horario. Su rasgo volátil la hace altamente moldeable y adictiva para los fans. Explotar su imagen al máximo para el lanzamiento.'{/i}"

    "Abro los ojos de golpe en medio de la penumbra."
    "Un nudo de rabia amarga se aprieta en mi garganta."

    mutou "Hijos de puta..."

    "La directiva lo sabe. Yamada lo sabe. Todos en esa maldita agencia saben que Airi se está rompiendo por dentro."
    "Y no solo no les importa, sino que diseñaron su estrategia de marketing alrededor de su inestabilidad."
    "Para DokiWave, una chica rota es más fácil de controlar, más frágil y más rentable."
    "Es exactamente el mismo patrón..."
    "El mismo juego despiadado que destruyó la vida de Saori Sato... y el que llevó al abismo a Minami."

    "Aprieto las sábanas con la mano en la oscuridad."
    "Esta vez soy yo quien está a cargo."
    "No soy el mismo mánager ingenuo de hace cinco años. Conozco las entrañas sucias de esta empresa y sé cómo juegan."
    "Si Airi se está fracturando, no dejaré que DokiWave termine de romperla."

    "Con la cabeza pesada y esa determinación amarga grabada a fuego en el pecho, finalmente cierro los ojos y me dejo llevar por el sueño."

    "Capítulo 1 Acto 1 terminado."

    # ------------------------------------------------------------------------------------------------------
    # --- PANTALLA DE LA CITA ---
    # ------------------------------------------------------------------------------------------------------

    with Pause(1.5)
    window hide

    show text "{i}\"La mente humana a veces fractura su propia realidad para sobrevivir al dolor de existir.\"{/i}" at truecenter with dissolve
    $ renpy.pause()

    hide text with dissolve
    with Pause(1.0)
    window auto

    return