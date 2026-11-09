# Finera — auditoría de las casillas 1, 3 y 4 (clientes, canales, relaciones)

**Procedencia de las citas.** Se obtuvieron con un buscador por grep sobre `corpus/segments/`
(2,039 segmentos locales), porque el runtime `ask-hormozi`/`qmd` no está instalado en este
contenedor. Los enlaces salen del campo `timestamp_url` del front-matter de cada segmento —
no se generan. **Son subtítulos automáticos:** el sentido es fiel, la transcripción literal
puede tener errores. Verifica en el vídeo antes de citar en un documento formal.

**Límite de esta auditoría.** Tengo registrado que tu canvas lleva **4 segmentos, 6 canales
y 6 relaciones**, y los nombres de los segmentos. **No tengo el texto literal de tus 6 canales
ni de tus 6 relaciones** (la imagen no se conservó). La crítica de abajo es estructural y se
sostiene con cualquier redacción; si alguna entrada concreta se salva, corrígeme.

**Esto no es asesoría legal ni financiera.**

---

## El error común a las tres casillas

Las tres están llenas de **opciones**, no de **decisiones**. 4 + 6 + 6 = **16 elementos y 0 clientes.**

> *"Cada negocio tiene solo una restricción. Pero la realidad es que la mayoría de los dueños de
> negocio no están trabajando en esa restricción. Están trabajando en algo que creen que es la
> restricción. O más común todavía, están trabajando todo el día sin ni siquiera pensar en la
> restricción, esperando que el negocio crezca."*
> — [*You Need to Find Your Constraint* — 00:00](https://www.youtube.com/watch?v=NucUq-K-YdU&t=0s)

Un canvas con 16 entradas y 0 clientes es exactamente eso: trabajo que se siente como progreso
sobre algo que no es la restricción.

---

## Casilla 1 — Clientes: **mal, y el error no es el que te dije antes**

Antes te dije que el problema era tener 4 segmentos cuando solo 1 pasa los tres filtros
(dolor / capacidad de pago / alcanzabilidad). Eso sigue siendo verdad, pero hay algo peor
que se me pasó:

### Dos de tus cuatro "segmentos" no son clientes

| Lo que escribiste | Qué es en realidad | Casilla correcta |
|---|---|---|
| **Sponsors** | Cliente. Tiene el dolor, paga, es localizable | **1 — Clientes** ✅ |
| **Instituciones** | Cliente posible, ciclo de 18 meses | **1 — Clientes**, año 3+ |
| **Distribuidores** (despachos, CPAs) | **No te pagan. Te traen clientes.** | **3 — Canales** + **8 — Socios** |
| **Inversores / LPs** | ⚠️ **Corregido** — ver nota abajo | **6 — Recursos** hoy; **1 — Clientes** en fase 2 |

> ### ⚠️ Corrección (2026-11-09)
>
> La versión original de esta tabla decía que los LPs **"no te pagan"**, en absoluto. **Eso era
> incorrecto y la corrijo.** El LP sí puede ser un cliente que paga — hay al menos una vía fuerte
> (liquidez secundaria) y dos plausibles (custodia y acceso) — y el propio corpus es explícito en
> que en un marketplace se le puede cobrar a los dos lados. Lo que sostengo, con la secuencia
> fundamentada, es más estrecho: **el LP no es tu *primer* cliente y en el año 1 no paga.**
>
> El análisis completo está en **[`CLIENTE-LP.md`](./CLIENTE-LP.md)**: las cuatro vías de
> monetización ordenadas por viabilidad, el criterio de "quién es permanente" que en realidad
> favorece al LP, la secuencia SaaS→marketplace, y las preguntas regulatorias que decide tu
> abogado y no yo.

Poner un canal en la casilla de clientes no es un detalle de clasificación. **Hace que el canvas
te mienta sobre el tamaño de tu mercado.** Esto aplica de lleno a **Distribuidores**: crees que
tienes cuatro mercados y en el año 1 tienes uno. Y como están en la casilla 1, les estás diseñando
propuestas de valor como si fueran a pagar — esfuerzo gastado en una cuenta que no va a facturar.

> Prueba de una línea para la casilla 1: **¿esta persona firma el cheque, en el modelo de este
> año?** Si no, no va aquí todavía. Si te trae a quien firma, va a canales. Si te deja operar
> legalmente, va a socios. Un cliente de fase 2 va a la casilla 1 de un **canvas de expansión
> fechado**, no al canvas primario.

### Por qué estrechar no es un sacrificio en tu caso: arregla tu palanca más débil

Esto es lo que casi nadie ve. Ya establecimos que en la ecuación de valor tu punto débil es la
**probabilidad percibida** (cero historial, cero emisiones). Estrechar el avatar no es solo foco —
**sube ese número directamente:**

> *"Cuando reduces el avatar con precios basados en nicho, puedes multiplicar tu precio por 5...
> Cuando vas estrecho, la ventaja que tienes es precio premium porque es mucho más específico en
> cuanto al entregable que tienes para ese avatar específico. Así que tienen una probabilidad
> percibida mucho más alta de lograr el resultado, y probablemente de forma muy real tienen una
> probabilidad más alta de lograrlo, porque ya sabes que este tipo de persona, si hace estas
> cosas, obtiene este resultado."*
> — [*Niche Down and 5x Your Price* — 00:00](https://www.youtube.com/watch?v=kVoFflryxDI&t=0s)

Traducido a Finera: **con cero track record, lo único que puedes hacer para que te crean es ser
tan específico que el cliente piense "este tipo solo hace esto".** "Infraestructura de tokenización
de RWA" suena a que no has hecho ninguna. "Hago emisiones Reg D para sponsors de real estate en
Puerto Rico que levantan $2–10M" suena a que has hecho veinte, aunque hayas hecho cero.

Y el encuadre competitivo:

> *"No vas a ganarle a Tony Robbins en desarrollo personal. Así que intenta ganarle a Tony Robbins
> en hombres menores de 25 que están superando trastornos alimenticios... quieres ser más específico
> porque quieres estrechar el campo de juego en el que estás compitiendo. Con el tiempo puedes ir
> cada vez más amplio."*
> — [*You Can't Beat Tony Robbins (But You Can Beat This)* — 00:00](https://www.youtube.com/watch?v=qViyhoDLhks&t=0s)

No le vas a ganar a Securitize ni a Tokeny en "tokenización de RWA". Le puedes ganar en
**sponsors de real estate de Puerto Rico que levantan $2–10M de su propia lista de LPs.** Ahí tú
eres el grande y ellos no están.

### Y la regla de secuencia

> *"Elegir al cliente es lo primero y más importante que puedes hacer en un negocio. Y luego tu
> oferta sale del cliente... El único arrepentimiento que tengo con el libro de ofertas es que le
> habría añadido tu primer cliente como el primer capítulo."*
> — [*You're Going After the Wrong Customers* — 04:30](https://www.youtube.com/watch?v=-5itZz1TgJI&t=270s)

Tus propuestas de valor describen tu arquitectura porque **salieron de tu tecnología, no de un
cliente.** No es un problema de redacción. Es que todavía no hay un cliente de quien pudieran salir.

---

## Casilla 3 — Canales: **mal, pero por una razón distinta a la que crees**

### La regla

> *"Mi regla de un producto, un avatar, un canal."* — *"Puedes tener más de uno, claro.
> Recomiendo que la gente empiece con uno, porque dices 'OK, voy a tener dos de estos canales'.
> Mi pregunta después de eso sería: ¿por qué? Porque no eres tan bueno en uno. No eres ni
> suficientemente bueno para hacer 100,000 al mes con uno. ¿Por qué harías un segundo?"*
> — [*AI Won't Change Business the Way You Think* — 00:00](https://www.youtube.com/watch?v=qiloFrBdbq4&t=0s)

> *"Un avatar, un producto, un canal hasta que llegues a un millón de dólares al año."*
> — [*How Local Businesses Can Make More Money* — 00:00](https://www.youtube.com/watch?v=gKzy9QGyKn8&t=0s)

### Lo importante: la excepción existe, y hay que mirarla de verdad

En esa misma cita nombra **una sola excepción: negocios locales en mercados pequeños.** Si hay
menos de ~50,000 personas en un radio de 10 millas, necesitas más de un canal porque un canal no
alcanza a suficiente gente.

Puerto Rico es un mercado pequeño. ¿Te aplica la excepción? **Mi lectura: no — y de hecho eres
el caso más fuerte de la regla, no la excepción.**

La condición de la excepción es que *un canal no alcanza a todo el mercado*. En tu caso:

| | Negocio local que es la excepción | Finera |
|---|---|---|
| Tamaño del mercado | 10,000 personas | ~50–200 sponsors que hacen Form D en PR |
| ¿Están nombrados? | No. Son anónimos | **Sí. Form D es público. Puedes imprimir la lista** |
| ¿Un canal los alcanza todos? | **No** — por eso necesita varios | **Sí** — venta directa del fundador llega al 100% |

Tu lista es **finita y nombrable**. La venta directa no se "satura": se *agota*, y cuando se agota
ya hablaste con todo tu mercado. Eso es el escenario ideal para un canal, no para seis.

### Y el problema aritmético

**6 canales × 0 clientes = 0 canales.** Un canal no es un canal hasta que produjo un cliente que
pagó. Antes de eso es una hipótesis. Hoy tienes seis hipótesis y cero canales — y el coste de las
seis no es dinero, es que ninguna recibe suficiente atención para llegar a funcionar.

**Casilla 3 correcta hoy:** `Venta directa del fundador sobre la lista de Form D.` Una entrada.
Las otras cinco van a un documento aparte titulado *"canales que probaré después de 10 clientes"*.

---

## Casilla 4 — Relaciones: **mal, y es el error más sutil de los tres**

Ya vimos que mezclas motor ① (retención del emisor) con motor ② (activación de nodos), que son
actividades distintas con métricas distintas. Pero hay algo más abajo:

> *"Retención... es realmente lo único que me importa. Porque en un horizonte de tiempo
> suficientemente largo, cualquier cosa que retenga clientes se vuelve enorme... Y mis dos centavos
> para cualquiera que esté escuchando: **no intentes resolver el churn. Intenta encontrar productos
> de los que la gente ya no se va.** Pasé una parte enorme de mi carrera dándome con la cabeza en
> la pared intentando hacer que algo de lo que la gente inherentemente se va, como una membresía de
> gym, fuera pegajoso... ¿cuántos de ustedes se han ido de su internet últimamente? ¿De su factura
> de celular? ¿De su seguro?"*
> — [*Why Creators Burn Out (and How to Fix It)* — 03:00](https://www.youtube.com/watch?v=81lZi32cE-o&t=180s)

**Aquí está la buena noticia que no estás usando.** Tú ya elegiste, sin darte cuenta, un producto
del que la gente no se va:

- El vehículo vive 5–10 años. El sponsor **no puede migrar a mitad del deal** sin re-papelear con
  todos los LPs, repetir KYC y coordinar un transfer agent nuevo.
- El LP **no puede irse** aunque quiera: su capital está comprometido.

Eso es estructuralmente del nivel "factura de celular". **No tienes un problema de churn.**
Llenar la casilla 4 con seis tácticas de relación es trabajar en un problema que no tienes.

### Dónde está tu churn de verdad: en el borde, no dentro

Tu riesgo no está *durante* el deal. Está en **el momento en que el sponsor estructura el deal #2**,
porque ahí la decisión se vuelve a abrir desde cero y tu ventaja de costo de cambio vale 0.

Eso le da a la casilla 4 **un solo trabajo**: estar presente cuando el sponsor está armando el
siguiente deal. No un newsletter, no un portal, no "soporte dedicado". Una pregunta en el calendario.

**Casilla 4 correcta: dos entradas, no seis.**

| | Entrada | Qué es en concreto | Métrica |
|---|---|---|---|
| **a** | Retención en el borde del deal | Pregunta agendada al cierre: *"¿cuál es tu próximo activo y cuándo?"* + contacto al mes 6 | ¿El sponsor del deal #1 trajo el #2? Sí/No |
| **b** | Activación de nodos | El guion del momento de la distribución a los LPs y el ciclo con despachos | % de deals nuevos vía nodo |

---

## Cómo empezar: el ejercicio de una frase

Esta es la herramienta concreta, y es la respuesta a *"¿cómo deberíamos empezar?"*

> *"Bueno, yo lo haría, pero no puedo porque ___. Y lo que sea ese 'porque', eso debería ser lo
> que se lleve toda tu atención en términos de recursos para ir a resolverlo... la mayor parte del
> tiempo estás pasando los días trabajando en cosas que no son la restricción del negocio."*
> — [*Why Aren't You Spending More on Ads?* — 03:00](https://www.youtube.com/watch?v=S2gLcKxG_8Q&t=180s)

Completa esta frase en voz alta, hoy:

### **"Yo cerraría mi primer sponsor esta semana, pero no puedo porque ______."**

Cada respuesta posible tiene una primera acción distinta — y **solo una de ellas es verdad para ti
ahora mismo**:

| Si tu respuesta es... | La restricción es | Primera acción | ¿Cuánto tarda? |
|---|---|---|---|
| "no tengo el software / la plataforma" | ❌ **Falsa.** El deal #1 se puede ejecutar con abogado + transfer agent + hoja de cálculo | Deja de construir. Ve a la fila que sí aplica | — |
| "no tengo abogado de valores" | ✅ Legal. **Es un prerrequisito, no un paso** | 3 llamadas a despachos de valores en PR esta semana | 2–4 semanas |
| "no sé a quién llamar" | ✅ Lista | Saca los Form D de PR de los últimos 24 meses. Es una tarde | 1 día |
| "no sé qué decirle" | ✅ Oferta | Ya la tienes escrita en el canvas de una página. Úsala | 0 |
| "no me va a creer" | ✅ Probabilidad percibida | Credibilidad prestada: el nombre del transfer agent y del custodio en tu material | 2–6 semanas |
| "no tengo tiempo / estoy solo" | ✅ Capacidad | Entonces 1 segmento y 1 canal no es consejo, es la única opción física | — |

**Yo no sé cuál de las seis es la tuya**, porque las preguntas de intake siguen sin responder.
Por eso no te puedo dar *la* primera acción — te doy el árbol para que la saques tú en 10 minutos.
Las dos primeras filas son las que más veces son la verdadera, y son opuestas: una te dice que
pares de construir, la otra que empieces a llamar.

---

## El cambio de cliente que vale la pena conocer

Esta historia es relevante porque describe el error de segmento que tú podrías estar a punto de
cometer, y cómo se sale de él:

> *"Al principio intentaba vender servicios de nurture de leads a negocios de ladrillo, PYMEs.
> El problema con el nurture de leads cuando tienes una PYME es que tienen flujo de leads
> inconsistente. Y entonces en cuanto dicen 'esto es genial, pero ¿cómo conseguimos leads?',
> yo pensaba 'oh no, esto es otro problema completo, este es otro negocio'. Y entonces tuvimos
> la idea inteligente de: bueno, ¿qué negocios ya tienen leads? Y la respuesta era: los negocios
> que ya trabajan con agencias. Y entonces dije: ah, quizá las agencias son nuestro cliente."*
> — [*How to Reduce Churn* — 00:00](https://www.youtube.com/watch?v=vgqlDIu5-I0&t=0s)

El patrón: **no vendas a quien le falta el insumo que tu producto necesita.** Si tu producto
necesita un activo listo, LPs listos y un abogado ya contratado, el cliente correcto es el que
**ya tiene las tres cosas** — el sponsor que levanta 2 a 6 veces al año — no el que va a hacer su
primera emisión nunca. Si te encuentras explicándole a un prospecto cómo conseguir LPs,
**ese no es tu cliente**, es el cliente de alguien más.

---

## Resumen: tus tres casillas

| Casilla | Tienes | Debería tener | El error |
|---|---|---|---|
| **1 — Clientes** | 4 segmentos | **1** (+1 en anexo año 3) | Dos de los cuatro no son clientes: son un canal y un recurso. El canvas te está mintiendo sobre el tamaño de tu mercado |
| **3 — Canales** | 6 canales | **1** | 6 × 0 clientes = 0 canales. Tu lista es finita y nombrable: eres el caso más fuerte de un solo canal, no la excepción |
| **4 — Relaciones** | 6 relaciones | **2** | Trabajas un churn que estructuralmente no tienes. Tu churn está en el borde del deal, no dentro |

**Lo que las tres comparten:** están llenas con lo que *podrías* hacer. El canvas solo empieza a
servir cuando cada casilla dice lo que *vas* a hacer y, por lo tanto, a qué le estás diciendo no.

---
---

# Anexo — "¿Entonces mis clientes son los sponsors y las instituciones?"

**El sponsor sí. Las instituciones todavía no** — y la razón es más dura que "son lentas".

---

## A1. Primero, "sponsor" ya trae un filtro adentro

No es *sponsors* en general. Es el perfil que ya definimos, y los tres criterios importan:

> El sponsor de real estate o private credit de Puerto Rico que levanta **$2–10M por deal**, de
> **su propia lista de LPs**, entre **2 y 6 veces al año**.

Un sponsor haciendo su primera emisión es un cliente distinto: no tiene LPs, no tiene relación con
un abogado, y consume soporte sin límite. Si te encuentras explicándole cómo conseguir
inversionistas, ese no es tu cliente (§"El cambio de cliente que vale la pena conocer").

---

## A2. Las instituciones fallan uno de los tres filtros — y la regla era los tres

| Criterio | Instituciones |
|---|---|
| Dolor urgente y específico | ❌ No urgente. Ya tienen un administrador y funciona "suficientemente bien" |
| Capacidad de pago | ✅ Sí |
| Alcanzabilidad eficiente | ❌ Ciclo de ~18 meses |

Dos de tres no es aprobar. Pero el conteo no es el argumento fuerte — los dos siguientes sí.

---

## A3. El reencuadre: el ciclo largo no es el problema, es un hecho

Este caso es casi idéntico al tuyo, pero el fundador ya factura $4M al año:

> *"Vendo software de experiencia de cliente a bancos, retailers y dependencias de gobierno...
> mi problema más grande ahora son los ciclos de venta muy largos, y por eso el CAC alto."*
> — *"**¿Cuál es el problema?** ... Sigue. **El hecho de que tome mucho tiempo no es un problema,
> es simplemente un hecho.**"* — *"El problema... la restricción del negocio es el capital."*
> — [*Helping a $4M SaaS Survive Long Sales Cycles* — 00:00](https://www.youtube.com/watch?v=xv2TOH_5F6A&t=0s)

**El ciclo de 18 meses no es el problema. El problema es que no tienes 18 meses de capital.**

La diferencia entre esas dos frases es enorme. La primera suena a que la paciencia lo resuelve.
La segunda es una restricción dura: o tienes con qué esperar, o no entras.

### Y fíjate en cómo ese fundador llegó ahí

> *"Cuando empezamos la plataforma hace 3 años era un producto simple, ciclo de venta más corto,
> menor valor, comprador más chico. Al hacer mucho I+D, el ROI que generamos es mucho más alto,
> comprador más grande, **pero ahora ciclo de venta más largo**... no quiero caer en jaque mate."*

Fue **de ciclo corto a ciclo largo** persiguiendo un comprador mejor, y eso lo metió en una trampa
de capital **teniendo ya $4M de ingreso recurrente.** Tú estarías empezando *dentro* de esa trampa,
desde $0.

---

## A4. La razón más dura: tu única herramienta contra el cero historial no funciona ahí

Lo que sí puedes hacer sin track record:

> *"La prueba por encima de todo. **Tienes que compensar el hecho de que no tienes historial
> ganando donde puedas.** Vas a ganar en servicio. Vas a decir: 'mira, aquí está mi celular, yo soy
> el dueño, voy a hacer todo lo que pueda para asegurarme'. Y segundo, tienes un incentivo
> claramente alineado: 'necesito testimonios, hermano, necesito prueba'. Así que voy a hacer todo
> lo posible para que ganes."*
> — [*How to Get Your First Clients With Zero Proof* — 00:00](https://www.youtube.com/watch?v=QgvX_5km_Yo&t=0s)

**Eso funciona sobre un humano que puede decidir solo.** Un sponsor es exactamente eso: una
persona, con un deal, que puede decir sí el jueves.

**Una institución quitó a ese humano de la decisión.** Entre tú y el sí hay procurement, revisión
de riesgo de proveedor, requisitos de certificación y auditoría, seguros, y referencias de otros
clientes institucionales. **Lo que una institución exige con más fuerza es precisamente lo único
que no tienes — y no se puede compensar con esfuerzo, servicio ni celular personal.**

| | Sponsor | Institución |
|---|---|---|
| ¿Quién decide? | **Una persona** | Un comité y un proceso |
| ¿Acepta "aquí está mi celular"? | **Sí** | No existe esa casilla en su formulario |
| ¿Acepta ser el primero? | **Sí, a cambio de precio y servicio** | **No.** Pide referencias que no tienes |
| ¿Se puede compensar el cero historial? | **Sí** | **No** |

> **Las instituciones no son un cliente lento. Son un cliente para el que todavía no calificas.**
> La puerta no está lejos: está cerrada con llave, y la llave son referencias y operación
> auditada. Eso no lo acelera la insistencia.

Y la regla general:

> *"Para los simples mortales, la mayor parte del tiempo hay que tener la prueba antes del pudín...
> Tenemos que mostrar que podemos hacerlo. Y tan pronto lo haces..."*
> — [*The Real Problem You Don't Want to Face* — 01:30](https://www.youtube.com/watch?v=wH3VBdJ1jbE&t=90s)

---

## A5. El costo real de dejarlas en la casilla 1

No es el tiempo. Es que **las instituciones son la forma más atractiva de no vender.**

Reuniones grandes, números grandes, gente seria, *"muy interesante, hablemos el próximo
trimestre"*. **Se siente como progreso y no produce nada.** Un trimestre de conversaciones
institucionales puede dejarte con cero ingreso y la sensación de haber trabajado mucho — mientras
los sponsors de la lista de Form D siguen sin recibir tu llamada.

Vale la pena nombrarlo porque es el riesgo específico del patrón que has mostrado en todo este
proceso: **preferencia por el alcance máximo.** 14 clases de activo, 10 tipos de cliente, 9 fuentes
de ingreso, 6 canales. Las instituciones son la versión más seductora de ese mismo impulso.

---

## A6. Conviértelas de segmento en hito

Igual que hicimos con los LPs en [`CLIENTE-LP.md`](./CLIENTE-LP.md) §25. En vez de dejarlas en la
casilla 1, escríbelas como **condición de disparo** en el canvas de expansión:

> **Las instituciones se vuelven alcanzables cuando tengamos:**
> - ≥ 10 emisiones ejecutadas y cerradas
> - ≥ $X administrados bajo plataforma
> - Auditoría externa completada
> - **3 sponsors dispuestos a servir de referencia por nombre**

Eso convierte una distracción en una meta, y te dice exactamente qué construir para abrir esa
puerta. Mientras no se cumplan las cuatro, perseguirlas es gastar el recurso más escaso que tienes.

---

## A7. Y lo que puede que ya tengas sin verlo

Existe un cliente "institucional" **alcanzable hoy** — y ya está dentro de tu definición de sponsor.

El **gestor emergente** que levanta $2–10M por deal con su propia lista de LPs es institucional
*en estructura* (tiene vehículo, LPs, administración, obligaciones de reporte) pero decide
*como emprendedor*: rápido, una persona, sin procurement, y **acepta ser el primero** a cambio de
precio y servicio.

Las "instituciones" que estás imaginando —fondos grandes, bancos, aseguradoras— son las de la
puerta cerrada de A4.

**No abras un segmento nuevo. Reconoce que el institucional que sí puedes atender ya está contado
en la casilla 1.** Es la misma persona, vista desde otro ángulo.

---

## A8. Respuesta

| | |
|---|---|
| *"Mis clientes son los sponsors..."* | ✅ **Sí** — con el filtro de A1: $2–10M, lista propia de LPs, 2–6 veces al año |
| *"...e instituciones"* | ❌ **Todavía no.** No por lentas, sino porque **tu única herramienta contra el cero historial no funciona sobre un comité** |
| ¿Dónde van entonces? | Canvas de expansión, con las cuatro condiciones de disparo de A6 |
| ¿Hay un institucional alcanzable? | **Sí, y ya lo tienes:** el gestor emergente. Está dentro de la definición del sponsor |

**Tu casilla 1 tiene un renglón.** No cuatro, no dos. Uno — y es el único que puede decirte sí
esta semana.
