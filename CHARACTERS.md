# Ficha de Personajes

Este documento contiene las fichas técnicas, personalidades, variables y sistemas de control de los personajes del proyecto.

---

## Protagonista

### **Mutou** (Mánager)
* **Rol:** Mánager Sénior del proyecto *DokiIdols*, actualmente mánager a cargo del proyecto *Angels*.
* **Personalidad:** Perspicaz, cínico, analítico, protector y atormentado por su pasado.
* **Trasfondo:** Regresa a DokiWave tras 5 años de ausencia luego de un trauma del que se siente responsable (el caso de *Minami*), dispuesto a hacer las cosas diferentes o al menos intentarlo.
* **Tono:** Serio, monólogos internos fríos y directos, diálogo profesional pero distante.

---

## Angels

### 1. **Airi Shirayuki**
* **Variable de Afecto:** `aff_airi`
* **Rol:** Idol / Integrante de Angels.
* **Personalidad:** A primera vista es el estereotipo de la persona perfecta: responsable, cariñosa y amante de la cocina, tratando con especial afecto a todas las personas y a sus fans.
* **Conflicto / Trastorno:** Presenta bipolaridad y episodios disociativos graves en los que pierde la noción de su propia identidad.
* **Dinámica con Mutou:** Trata a Mutou con un cariño y afecto especial, producto de su personaje como idol perfecta. Si bien su relación es meramente profesional, su comportamiento es similar al de una persona enamorada buscando la aprobación de su pareja.

### 2. **Ruka Kurogane**
* **Variable de Afecto:** `aff_ruka`
* **Rol:** Streamer de videojuegos / Integrante de Angels.
* **Personalidad:** En persona, tiene una personalidad muy antipática y directa, pero tras la pantalla posee un carácter muy fuerte y es muy conocida por pelear con sus fans en el chat del stream. A pesar de esa coraza, en el fondo es una persona profundamente agradecida.
* **Conflicto:** Vive aterrorizada con la idea de ser reemplazada por alguien más. Debido a este miedo, se sobreexige y se esfuerza mucho más allá de sus límites en secreto, lo que le provoca serios problemas de salud.
* **Dinámica con Mutou:** Al ser el mánager de Angels, trata a Mutou con confianza y afecto, aunque su personalidad tan antipática hace que parezca todo lo contrario.

### 3. **Kaori Sumizome**
* **Variable de Afecto:** `aff_kaori`
* **Rol:** Compositora / Integrante de Angels.
* **Personalidad:** Silenciosa y reservada. No es tímida, sino completamente indiferente a la fama y al dinero. Posee un oído prodigioso y talento para tocar casi cualquier instrumento. Se unió a DokiWave Entertainment únicamente porque le garantizan techo y comida a cambio de hacer música, su actividad favorita.
* **Conflicto / Salud:** Padece severos trastornos de sueño y alimentación por ensayar y componer sin parar. Estar alejada de la música le genera una ansiedad devastadora, la cual intenta calmar fumando o autolesionándose físicamente a escondidas.
* **Dinámica con Mutou:** A pesar de ser su mánager, Mutou es la única persona con la que Kaori parece sentirse cómoda, ya que comparten una complicidad silenciosa desde su primer encuentro informal en el callejón.

---

## Personajes Secundarios

### **Yamada**
* **Rol:** Asistente / Asistente de producción de DokiWave Entertainment.
* **Personalidad:** Hiperactiva, alegre, perfeccionista, con una serenidad corporativa casi inquietante cuando surgen problemas graves.
* **Función en la trama:** Representa la cara "amigable" del sistema corporativo de DokiWave Entertainment que oculta los trapos sucios.

### **Kenjiro Sato**
* **Rol:** Padre de Saori Sato (Ex-idol de DokiIdols en DokiWave Entertainment).
* **Función en la trama:** Su trágico final le revela a Mutou hasta dónde es capaz de llegar la empresa para proteger su imagen.

---

## Reglas Generales de Escritura

1. **Tono de la VN:** Psicológico, dramático, oscuro y misterioso con momentos breves de comedia/interacción cotidiana.
2. **Estilo de Mutou:** Nunca habla de más. Siempre nota detalles que otros ignoran. Monólogos internos directos y perspicaces.
3. **Manejo de Dilemas:** Las decisiones tomadas por el mánager deben equilibrar la salud mental de las chicas, sus niveles de estrés y la reputación de la agencia.

---

## Sistema de Variables del Juego

El flujo narrativo, las rutas individuales y los eventos se gestionan a través de las siguientes variables globales en `script.rpy`:
### 1. Variables de Afecto y Progreso
* `aff_[nombre]` (`aff_airi`, `aff_ruka`, `aff_kaori`): Puntos de afecto/relación acumulables que determinan la cercanía con Mutou y la apertura de rutas individuales.
* `init_aff_[nombre]` (`init_aff_airi`, `init_aff_ruka`, `init_aff_kaori`): Bonos iniciales de afecto que se aplican al comenzar el Acto 1 según decisiones previas.
* `pts_[nombre]` (`pts_airi`, `pts_ruka`, `pts_kaori`): Puntos acumulados (+1 por capítulo completado en cada ruta) utilizados para desbloquear logros y medir el progreso.
### 2. Estado Físico y Psicológico
* `mental_[nombre]` (`mental_airi`, `mental_ruka`, `mental_kaori`): Salud mental de cada chica en una escala de 0 a 100 (`0 = Colapso / 100 = Estable`). Influye en la detonación de crisis psicológicas y episodios disociativos.
* `stress_[nombre]` (`stress_airi`, `stress_ruka`, `stress_kaori`): Nivel de estrés y presión laboral en una escala de 0 a 100 (`0 = Relajada / 100 = Límite`). Afecta el rendimiento y desencadena colapsos de salud física o laboral.
### 3. Métricas de Fama e Impacto
* `fans_[nombre]` (`fans_airi`, `fans_ruka`, `fans_kaori`): Cantidad de seguidores individuales por integrante. Condiciona el impacto mediático y popularidad.
* `agency_fame`: Reputación y nivel general de la agencia/proyecto *Angels*. Determina las oportunidades corporativas y la atención de la directiva de DokiWave Entertainment.
### 4. Flags de Eventos Clave (`Booleans`)
* `know_airi_secret`: Registra si Mutou ha descubierto el secreto y trastorno disociativo de Airi.
* `reveal_ruka_fear`: Registra si Ruka ha revelado a Mutou su miedo irracional a ser reemplazada.
* `made_promise_kaori`: Registra si Mutou ha realizado una promesa personal significativa con Kaori.