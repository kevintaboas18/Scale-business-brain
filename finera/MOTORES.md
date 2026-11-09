# Finera — los dos motores y el bucle de los LPs

> **Base conceptual:** *"Solo hay dos formas de tener un negocio: una es que la gente nunca deje de comprarte. La otra es que tengas gente que nunca deje de venderte."*
> — Alex Hormozi, [*The Irresistible Referral Offer* — 04:30](https://www.youtube.com/watch?v=3Cyh6y9qjGc&t=270s)
>
> *Nota de procedencia: esta cita se verificó contra el corpus local en una sesión anterior. El runtime de búsqueda (`ask-hormozi` + `qmd`) no está instalado en este contenedor, así que el resto de este documento es análisis aplicado a Finera, no material citado. Donde no hay cita, es mi razonamiento, y lo digo.*

**Esto no es asesoría legal ni financiera.** Nada aquí sustituye a tu abogado de valores.

---

## 0. La asimetría que decide tu secuencia

Los dos motores no se construyen a la vez y no se construyen igual.

| | Motor ① — nunca dejan de comprar | Motor ② — nunca dejan de vender por ti |
|---|---|---|
| **Qué es en Finera** | Servicing fee recurrente sobre AUM del vehículo | Despachos, CPAs, el sponsor repetidor y los LPs que te traen deals |
| **¿Se puede construir?** | Sí. Es diseño: fee sobre AUM, vehículo de 5–10 años, costo de cambio brutal | No. Se gana y después se cosecha |
| **¿Cuándo existe?** | El día que firmas el deal #1 | Meses después del deal #1, **si salió bien** |
| **Signo** | Positivo o cero | **Positivo, cero o negativo** |
| **Qué lo mata** | Que se venda el activo y no haya deal siguiente | Un solo deal mal ejecutado |

### Las dos consecuencias prácticas

**(a) El orden está forzado.** No puedes lanzar un programa de referidos antes de tener algo digno de referir. El error universal es invertirlo: programa de afiliados primero, cero resultado, conclusión equivocada ("en mi industria no funciona"). La secuencia real:

```
1 deal impecable
      ↓
ese sponsor + esos LPs = motor ②
      ↓
motor ② trae deals 2, 3, 4...
      ↓
esos deals = motor ① (fee recurrente)
      ↓
① compone sin vender nada nuevo
```

**(b) El motor ② tiene signo, y tu mercado es pequeño.** En Puerto Rico los sponsors de real estate, los despachos de valores y los CPAs que les sirven se conocen entre ellos. Un nodo que te recomendó y se quemó no vuelve a neutral: se va a −1 y lo comenta. Por eso **un deal perfecto vale más que tres adecuados** — no por orgullo, por aritmética de red.

### El matiz del motor ① que ya habíamos visto

El fee sobre AUM termina cuando se vende el activo. Un vehículo de 7 años es una **anualidad de 7 años, no una perpetuidad**. Lo que lo convierte en perpetuidad es **el siguiente deal del mismo sponsor**. Es decir: el sponsor repetidor es motor ① y motor ② al mismo tiempo, y es la pieza más valiosa de toda la estructura.

---

## 1. El motor que nadie en tu sector trabaja: los LPs

### Por qué está libre

En un private placement, el LP es el único grupo que cumple las cuatro condiciones a la vez:

1. **Vio tu trabajo desde adentro.** Recibió los reportes, las distribuciones, los documentos de impuestos. No está evaluando tu pitch, está evaluando tu ejecución.
2. **Está invertido con otros sponsors simultáneamente.** El LP típico de deals privados está en 2–5 vehículos de distintos sponsors.
3. **No tiene conflicto en recomendarte.** No compite contigo. No le quitas nada.
4. **Nadie se lo pide.** La industria entera trata al LP como capital, no como distribución. Es un canal de alta credibilidad que está sobre la mesa sin tocar.

### La inversión que casi nadie hace

El reflejo es: *LP → más LPs.* Eso vale poco, porque el LP no te paga a ti.

La dirección valiosa es **LP → sponsor**, porque el sponsor **es tu cliente que paga.** Y el LP es la puerta más caliente que existe hacia un sponsor, porque **el LP es el cliente del sponsor.** Cuando el cliente de alguien te recomienda, no estás vendiendo: estás siendo validado por la persona a la que ese sponsor tiene que rendir cuentas.

```
LP del deal #1  ──invertido también con──>  Sponsor B, Sponsor C, Sponsor D
       │
       └── "¿por qué tú no lo haces como lo hizo Finera?"
                        ↓
            demanda entrante del lado del capital
            tirando del lado del activo
```

### La matemática gruesa de un solo deal

| Supuesto | Valor |
|---|---|
| LPs en el deal #1 | 20 |
| Deals privados promedio por LP (aparte del tuyo) | 3 |
| Relaciones con sponsors alcanzables | **60** |
| Intros cálidas que piden 20 conversaciones | 20 |
| Conversión a issuer al 5% | **3 issuers** |

Tres issuers desde un solo deal, con costo de adquisición ≈ 0. Esos son los supuestos que tienes que **verificar en tu primer deal**, no creerme: cuenta los LPs reales y pregúntales en cuántos deals más están. Si el promedio es 1, este motor es mucho más débil de lo que parece y lo quiero saber temprano.

---

## 2. Cómo se construye el bucle (4 piezas)

### Pieza 1 — Haz de la experiencia del LP el producto, no un anexo

**Qué recibe hoy un LP de un sponsor típico en PR:** un PDF una vez por trimestre, tarde, sin detalle, imposible de mostrarle a su contador sin explicarlo.

**Qué quiere:** saber qué tiene, cuánto vale, cuándo le pagan, y poder enseñárselo a su esposa o a su CPA sin traducir nada.

Tu infraestructura de tokenización **ya produce exactamente eso**: posición en vivo, historial de transacciones limpio, documento fiscal descargable. Eso no es un feature. **Es el disparador del referido.** Si el LP no puede sentir la diferencia, el motor ② no arranca, no importa cuánto le preguntes.

> Prueba de fuego: ¿podría un LP mostrarle su posición a otro LP de otro deal en 30 segundos, en el teléfono, y que el otro sienta envidia? Si no, vuelve a la pieza 1.

### Pieza 2 — Nombra el momento

El referido no ocurre al azar, ocurre en un momento específico: **el día de la primera distribución**, cuando el dinero entra a su cuenta. Es el pico emocional del ciclo entero. Ahí va la pregunta, y **solo ahí**.

No en el onboarding (no ha pasado nada todavía). No en un email trimestral genérico. El día que le pagas.

### Pieza 3 — La pregunta correcta

❌ *"¿Conoces a alguien que quiera invertir?"* — inútil. No produce nombres, produce "déjame pensar".

✅ La secuencia que sí produce nombres:

1. **"¿En qué otros deals privados estás metido?"**
   → Respuesta = lista de sponsors por nombre. Información que no tenías.

2. **"¿Cómo te reportan allá? ¿Con qué frecuencia y en qué formato?"**
   → Respuesta = la comparación, hecha por él, en voz alta, a tu favor. Tú no dijiste nada.

3. **"¿Te molestaría si le menciono a [sponsor] que tú me conoces?"**
   → Pide permiso, no pide el favor. Costo psicológico cercano a cero.

4. *(si dice sí)* **"¿Prefieres que yo le escriba o te es más fácil mandarle dos líneas tú?"**
   → Le das la salida fácil y te quedas con la intro escrita por ti. (El patrón completo de "no pidas la intro, escríbela" está en [`COLABORACIONES.md` §3](./COLABORACIONES.md).)

La pregunta 2 es la que hace el trabajo. **El LP construye tu argumento de venta por ti**, y después no puede desdecirse.

### Pieza 4 — La pieza estructural: haz la relación portátil

Esta es la que convierte un programa de referidos en un efecto de red.

Si el LP tiene en Finera: **KYC verificado + historial de posiciones + documentos fiscales en un solo lugar**, entonces cuando invierte en el deal de un sponsor *nuevo*, el camino más barato para él es que ese sponsor use Finera también. No tiene que repetir KYC, no fragmenta sus documentos, no aprende otro portal.

Ahí el LP tiene una **razón egoísta** para empujarte, no solo una razón generosa. Las razones generosas se agotan. Las egoístas, no.

> Esto hay que validarlo con tu abogado de valores: la portabilidad de KYC/AML entre emisiones y entre emisores distintos tiene reglas propias, y "reusar el KYC" puede o no estar permitido según cómo esté estructurado el vehículo y quién sea el responsable del cumplimiento. **No lo asumas por lo que lee bien aquí.**

---

## 3. Las tres capas del motor ②, en orden de dificultad

| Capa | Quién | Qué te trae | Dificultad | Dónde está desarrollada |
|---|---|---|---|---|
| **(a) Nodos profesionales** | Despachos, CPAs, asesores Act 60 | Issuers con el problema ya identificado | Media — requieren confianza previa y tienen reglas de honorarios | [`COLABORACIONES.md`](./COLABORACIONES.md) |
| **(b) Sponsor repetidor** | El issuer del deal #1 en su deal #2 | Ingreso nuevo con CAC = 0 | **Baja** — ya te conoce, solo hay que ejecutar bien | Este doc, §0 |
| **(c) Bucle de LPs** | Los inversionistas del deal #1 | Intros cálidas hacia *otros sponsors* | Baja en esfuerzo, alta en diseño | Este doc, §1–2 |

**La capa (b) es la más fácil y la que más se descuida.** Un sponsor que hizo un deal contigo y quedó contento es el lead más barato que vas a tener en la vida, y la única razón por la que se pierde es que nadie le preguntó cuándo viene el siguiente. Pon en tu calendario, el día que cierra el deal #1: *"¿Cuál es el próximo activo que estás pensando levantar, y cuándo?"*

---

## 4. La casilla 8 del canvas (Socios clave), ordenada

Tu canvas tiene la casilla 8 vacía. El error típico es llenarla por *tipo de empresa*. Llénala por **qué te da cada uno**.

### ⚠️ Primero, el filtro que elimina la mitad

**A quien le pagas no es un socio, es un costo.** Si la relación es "yo te pago, tú me prestas un servicio", eso va a la **casilla 9 (Estructura de costos)**, no a la 8. Mucha gente pone a su abogado en la casilla 8 y siente que tiene socios. No los tiene, tiene facturas.

Un socio legítimo de la casilla 8 hace **al menos una** de tres cosas:
1. Te **reduce un costo** que de otro modo pagarías completo
2. Te **reduce un riesgo** que no puedes eliminar solo
3. Te **trae demanda**

### Casilla 8 — Socios clave (Finera, fase Puerto Rico)

**Grupo 1 — Habilitadores regulatorios** *(reducen riesgo; también aparecen en casilla 9 porque los pagas)*
- **Abogado de valores (PR + federal)** — no es un paso, es un prerrequisito. Sin esto no hay empresa.
- **Transfer agent** — registro de tenedores. Define si tu producto es operable.
- **Custodio calificado** — dónde viven los activos/fondos.
- **Auditor** — su nombre es parte de tu credibilidad, no solo un cumplimiento.
- **Broker-dealer** *(si tu estructura lo requiere — pregunta #1 para tu abogado)*

**Grupo 2 — Nodos de distribución** *(traen demanda; son el motor ②a)*
- Despachos de valores / real estate que hacen private placements
- CPAs con cartera de sponsors
- Asesores de Act 20/22/60
- Brokers comerciales con deals en estructuración

**Grupo 3 — Prestamistas de credibilidad** *(reducen el riesgo percibido por el cliente)*
- El **primer sponsor reconocido** que diga sí. Su nombre es el que abre los siguientes.
- El custodio y el auditor — su marca viaja contigo en cada pitch.

**Grupo 4 — Lado del capital** *(el motor ②c)*
- Family offices locales
- Redes de inversionistas acreditados en PR
- Relocalizados por Act 60 buscando dónde poner capital local

### Lo que esto significa para las otras casillas

| Casilla | Qué añadir, derivado de los dos motores |
|---|---|
| **4 — Relación con clientes** | Sepáralo en dos renglones: *retención del issuer* (motor ①) y *activación de nodos* (motor ②). No es la misma actividad ni la mide lo mismo. |
| **6 — Recursos clave** | Añade dos activos que no son software: **"base acumulada de LPs verificados"** y **"cartera de nodos activos"**. Son los recursos que hacen que el deal #10 cueste menos que el deal #1. |
| **7 — Actividades clave** | Añade **"ejecución del momento de distribución"**. Suena menor. Es el único momento del año en que se enciende el motor ②. |
| **9 — Costos** | Aquí van los del Grupo 1. Y el que nadie presupuesta: **el costo de hacer el deal #1 impecable** (sobre-servicio deliberado). Trátalo como gasto de marketing, porque lo es. |

---

## 5. Las métricas que distinguen un motor de un deseo

**La prueba de una pregunta (motor ①):**
> *"Si el mes que viene no vendo nada, ¿crecen mis ingresos?"*
> Sí → tienes motor ①. No → tienes un negocio de proyectos disfrazado de plataforma.

**La prueba de una pregunta (motor ②):**
> *"¿Qué % de mis deals nuevos llegó por alguien que no está en mi nómina?"*
> Cuando pasa de **50%**, el motor ② está encendido. Antes de eso tienes referidos ocasionales, no un motor.

**Las tres que vale la pena medir desde el deal #1:**

| Métrica | Por qué | Cuándo se mide |
|---|---|---|
| # de LPs que respondieron "¿en qué otros deals estás?" | Es el tamaño real de tu capa (c). Valida o destruye la matemática de §1. | A los 30 días de la primera distribución |
| % de deals nuevos vía nodo | Único indicador de si el motor ② existe | Mensual, desde el deal #2 |
| ¿El sponsor del deal #1 trajo el deal #2? | Sí/No. Binario. Es la capa (b), la más fácil y la más reveladora. | Al cierre del deal #1 + 6 meses |

---

## 6. El riesgo compartido

Los dos motores corren sobre el mismo sustrato: **la ejecución de los deals**. Un solo deal mal ejecutado no te cuesta ese ingreso — te apaga los dos motores a la vez:

- El issuer no renueva ni trae el siguiente → **① se detiene**
- El despacho que lo refirió deja de referir, y el LP quemado habla → **② se vuelve negativo**

En un mercado grande esto se absorbe. En Puerto Rico, no. Es la razón estructural —no filosófica— por la que la estrategia correcta en tu etapa es **un wedge, un tipo de activo, un deal, perfecto**, y no catorce clases de activo en el canvas.

---

## 7. Qué hacer esta semana

1. **Escribe en una página cómo se ve el deal #1 impecable.** No el producto: la experiencia. Qué recibe el issuer, qué recibe el LP, en qué días, en qué formato. Ese documento es tu especificación de producto y tu plan de marketing al mismo tiempo.
2. **Decide el momento de distribución como un evento con guion**, no como una transferencia bancaria. Quién escribe, qué dice, qué pregunta.
3. **Agenda la pregunta al sponsor** para el día del cierre: *"¿cuál es tu próximo activo?"*
4. **Llena la casilla 8** con los cuatro grupos de §4, y mueve a la casilla 9 todo lo que sea una factura.
5. **Pregúntale a tu abogado de valores** la pregunta de la pieza 4: ¿hasta dónde es portátil el KYC/AML de un LP entre emisiones y entre emisores?
