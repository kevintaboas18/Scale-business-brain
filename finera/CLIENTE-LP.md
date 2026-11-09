# ¿Puede el inversionista (LP) ser cliente de Finera?

**Respuesta corta: sí.** La afirmación anterior de que "los LPs no te pagan" era demasiado
absoluta y está corregida. Lo que sí se sostiene es más estrecho y es una cuestión de **secuencia**,
no de categoría: **el LP no es tu primer cliente, y en el año 1 no paga — pero es tu segundo
negocio, y es el que vuelve a Finera difícil de copiar.**

**Procedencia.** Citas obtenidas con `skills/ask-hormozi/csearch-fallback.py` sobre
`corpus/segments/`; los enlaces salen del front-matter. Son subtítulos automáticos: fieles en
sentido, posiblemente imprecisos en la literalidad. **Nada aquí es asesoría legal ni financiera** —
y en esta pregunta en particular, parte de la respuesta no es mía, es de tu abogado de valores.

---

## 1. El corpus es explícito: a un marketplace se le cobra a los dos lados

El caso es un negocio de tutorías que cobraba solo a los estudiantes:

> *"¿Estás cobrándole algo a los tutores o no?"* — *"Bueno, los clientes pagan."* — *"¿Qué paga
> el tutor? Nada, correcto. Ese es mi punto. **Así que también podrías cobrar — es un marketplace
> de dos lados. Puedes cobrarle a las dos personas.** Les podrías cobrar una cuota de membresía
> para tener la oportunidad de recibir a esta gente de tu parte. Y esas probablemente van a ser
> muy pegajosas."*
> — [*Helping a $200K Service Business Double Revenue* — 03:00](https://www.youtube.com/watch?v=o0hFkaUX2gA&t=180s)

Así que la pregunta "¿puede pagarme el otro lado?" tiene respuesta afirmativa de entrada.
Tu intuición era correcta y mi tabla estaba mal.

---

## 2. El criterio que importa no es "quién paga" — y favorece al LP

Lo interesante de ese mismo caso es el criterio con el que decide **quién es el cliente de verdad**:

> *"La idea es que tienes que cambiar tu perspectiva: **los tutores son tus clientes. Porque ellos
> son los permanentes. Los estudiantes entran y salen.**"*
> — [*Helping a $200K Service Business Double Revenue* — 03:00](https://www.youtube.com/watch?v=o0hFkaUX2gA&t=180s)

La prueba no es quién firma el cheque hoy. Es **quién permanece y quién pasa.** Aplicada a Finera
honestamente, el resultado no es el que yo dije:

| | Sponsor (emisor) | LP (inversionista) |
|---|---|---|
| Vida de la relación | **Deal por deal.** Entre deals, desaparece | Invierte en privados por **décadas** |
| ¿Te puede dejar? | Sí — en cada deal nuevo la decisión se reabre desde cero | Estructuralmente no, mientras dura el deal |
| ¿Se acumula? | No. Tienes los sponsors que te ganaste, uno por uno | **Sí. Cada deal te deja ~20 LPs más, gratis** |
| ¿Es copiable? | Sí. Otro proveedor puede ganárselo | **No. Nadie más tiene tu base de LPs** |
| ¿Paga hoy? | **Sí** | No |

**Conclusión honesta: el sponsor es quien te paga primero; el LP es quien se acumula.**
Los dos son clientes reales en una Finera madura. **El LP es el que hace que el negocio no se
pueda copiar** — y eso es exactamente lo que ya habíamos puesto en la casilla 6 como
*"base acumulada de LPs verificados"*. Ese renglón estaba bien; lo que estaba mal era negarle
la posibilidad de facturar.

---

## 3. Las cuatro vías de monetización del LP, ordenadas por viabilidad

### ① Liquidez secundaria — la fuerte

El LP que quiere salirse antes del año 7 paga una comisión por la transacción.

**Por qué es la mejor candidata:**
- Es **el dolor exacto que tú mismo identificaste** cuando escribimos tu oferta: *"no tiene nada
  que ofrecerle al LP que quiere salirse antes del año 7"*.
- Es urgente y con fecha: el LP que necesita liquidez la necesita **ahora**, no en abstracto.
- El dinero está en la mesa: le estás entregando efectivo en el momento de cobrar.
- Es la única pieza que **tu infraestructura de tokenización habilita y el Excel del sponsor no.**
  Aquí sí hay una razón técnica real para que exista Finera.

⚠️ **Es también la de mayor carga regulatoria, con diferencia.** Operar un mercado donde se
transan valores es actividad regulada. Ver §6.

### ② Custodia / puntos base sobre la tenencia — la estándar

Comisión anual sobre el valor de la posición, cobrada al inversionista. Es un modelo corriente en
la industria. Menos emocionante, más predecible, y **recurrente del lado que se acumula.**

⚠️ Custodiar activos de terceros tiene reglas propias. Ver §6.

### ③ Acceso / membresía — la del corpus

Exactamente la cuota de membresía de la cita: el inversionista acreditado paga una cuota anual
por acceso a deals verificados de Puerto Rico. Funciona si tu curaduría vale algo — es decir,
**después de tener historial, no antes.**

⚠️ Cobrar por acceso a ofertas de valores toca reglas de intermediación. Ver §6.

### ④ Las débiles — nómbralas para descartarlas

| Vía | Por qué no |
|---|---|
| Suscripción por el dashboard / reporting | Nadie paga por ver su propia posición. Es higiene, no producto |
| Cuota de KYC por inversionista | Oferta terrible: le cobras por el privilegio de ser verificado. Eso lo paga el emisor |
| Comisión sobre la distribución | Le cobras por recibir su propio dinero. Destruye el motor ②c completo |

---

## 4. Por qué no es el primero: la dirección de adquisición

Esta es la parte que sostengo, y no es sobre dolor ni sobre dinero. Es logística:

**No puedes adquirir un LP antes de adquirir un sponsor.** El LP entra a tu sistema *a través de
un deal*. No hay puerta de entrada que no pase por el emisor.

```
sponsor paga  →  deal  →  ~20 LPs entran con CAC = $0  →  repetir
                                      ↓
                    400 LPs en 15 deals  =  mercado secundario real
                                      ↓
                    AHORA el LP puede pagarte (①, ② o ③)
```

El costo de adquisición del LP es **$0 mientras vaya río abajo del sponsor.** Si intentas
adquirir LPs de frente, estás compitiendo con todas las casas de bolsa del mundo, sin un solo
deal que mostrar, con un presupuesto de marketing de cero. Es la peor pelea disponible.

### Y la trampa específica del marketplace

> *"Si miras la cantidad de gente que ha intentado construir marketplaces, **casi todos fracasan.**
> Y es mi opinión que **los mejores marketplaces corren un SaaS primero, y una vez que llegan a
> escala, pueden empujar más hacia el marketplace**, como Shopify por ejemplo... porque saben que
> para la gran mayoría **ganan más cobrando $29 al mes que llevándose 4% de cero.**"*
> — [*Helping a $4.3M Creator Platform Business Scale to $100M* — 01:30](https://www.youtube.com/watch?v=1Grge4LqDlM&t=90s)

**"4% de cero" es literalmente tu mercado secundario en el año 1.** Un secundario con 20 LPs de un
solo deal no es un mercado: no hay suficientes vendedores ni suficientes compradores para que un
precio exista. La comisión por transacción de la vía ① **no vale nada hasta que hay densidad**,
y la densidad la produce el lado del sponsor.

Por eso la secuencia correcta es la del Shopify:

| Fase | A quién le cobras | Qué cobras | Condición para pasar de fase |
|---|---|---|---|
| **1 — SaaS** | Sponsor | Estructuración + % anual sobre AUM | 10–15 deals, ~300–400 LPs verificados |
| **2 — Marketplace** | Sponsor **y LP** | + liquidez secundaria, custodia | Que haya dos lados con volumen real |

---

## 5. Lo que cambia el día que el LP te paga (y hay que decidirlo, no dejarlo pasar)

Este es el costo del segundo lado, y es real:

> *"Tienes que mantener los dos lados, ¿cierto? Porque si empiezas a mandarles deals malos...
> simplemente no van a querer recibir más intros de tu parte."*
> — [*Helping a $15K-Per-Deal Connector Build His Back End* — 01:30](https://www.youtube.com/watch?v=Ghi3cpRrK2A&t=90s)

Hoy Finera es **infraestructura neutral**: el sponsor elige el activo, tú ejecutas. Si el deal sale
mal, salió mal el deal del sponsor.

El día que le cobras al LP, el LP es tu cliente — **y entonces la calidad de los deals es tuya.**
Dejas de ser infraestructura y te vuelves **seleccionador**. Eso trae:

- Obligación de due diligence sobre el activo, no solo sobre el papeleo
- Un perfil de responsabilidad distinto frente al inversionista
- Un conflicto estructural: **el sponsor te paga por emitir, el LP te paga por filtrar.** Cuando un
  sponsor que paga trae un deal flojo, los dos lados de tu negocio quieren cosas opuestas.

**No es una razón para no hacerlo.** Es una razón para hacerlo **a propósito y con fecha**, no por
deriva. La mayoría de las plataformas de este tipo cruzan esa línea sin darse cuenta y descubren
el conflicto cuando ya tienen los dos lados cobrando.

---

## 6. La parte que no es decisión tuya ni mía

En casi cualquier negocio, "¿a quién le cobro?" es una decisión libre del fundador. **En el tuyo
no lo es del todo** — y eso es una característica importante de operar infraestructura regulada.
Cada vía de arriba abre una pregunta regulatoria distinta:

| Vía | La pregunta para tu abogado de valores |
|---|---|
| ① Liquidez secundaria | ¿Qué registro requiere operar un mercado secundario de estos valores? ¿Intermediario registrado? ¿Sistema alternativo de negociación? |
| ② Custodia | ¿Quién puede custodiar activos de terceros y bajo qué régimen? ¿Necesito un custodio calificado de por medio? |
| ③ Acceso / membresía | ¿Cobrar por acceso a ofertas exentas me convierte en intermediario? ¿Hay implicación de asesoría de inversión? |
| **Todas** | **¿Cobrarle una comisión al inversionista afecta la exención bajo la que se hizo la emisión?** |

La última es la que más gente pasa por alto y la que puede invalidar una emisión entera.
**Yo no te puedo responder ninguna de las cuatro, y no debes tomarlas de mí.** Lo que sí puedo
hacer es que llegues a esa reunión con las cuatro preguntas escritas, lo cual ahorra horas
facturadas.

---

## 7. La posición corregida, en una frase

| | |
|---|---|
| ❌ Lo que dije | *"El LP no es tu cliente; no te paga."* — demasiado absoluto, incorrecto |
| ✅ Lo correcto | *"El LP no es tu **primer** cliente y en el año 1 no paga. Es tu **segundo negocio**, llega gratis río abajo del sponsor, y es el lado que hace a Finera no copiable — sujeto a lo que diga tu abogado sobre cómo se le puede cobrar."* |

**Para el canvas:** LPs se queda en la **casilla 6 (Recursos)** del canvas primario, y aparece en
la **casilla 1 de un canvas de expansión fase 2**, con el disparador escrito: *"cuando haya ~300
LPs verificados en 10+ deals"*. Así no pierdes la visión y tampoco diluyes el año 1.

Lo que **sí** debes hacer ya, aunque el LP no pague todavía: el trabajo del motor ②c en
[`MOTORES.md`](./MOTORES.md) §2. Toda la base de LPs que acumules ahora es el inventario del
negocio de fase 2 — y la estás construyendo gratis mientras el sponsor paga la cuenta.

---
---

# Parte II — La membresía: por qué "acceso prioritario" falla y qué sí funciona

*(Añadido tras tu objeción: el LP no es cliente por acceso, pero sí podría serlo por membresía
con prioridad. Tienes razón en la primera mitad. La segunda hay que rediseñarla.)*

## 8. Lo que tienes bien, y es la distinción importante

**Peaje ≠ upgrade.**

| | Qué es | Efecto |
|---|---|---|
| **Cobrar por acceso** | Quitas algo que era gratis y lo vendes de vuelta | Reduce el embudo. Mata al ticket chico |
| **Cobrar por prioridad** | Añades algo que nadie tenía | No reduce nada. Solo añade |

Y tu razón es exacta: **"nadie quiere empezar a pagar para invertir poco."** Si alguien invierte
$25,000 y le cobras $500 al año, le quitaste 2% antes de que el activo rinda nada. La cuenta no
cierra para él, así que no entra — y el que no entra tampoco se convierte en el LP acumulado que
necesitas para la fase 2. El peaje te cuesta dos veces.

Eso está bien pensado. El problema está en la otra mitad.

---

## 9. La prueba que tiene que pasar cualquier membresía

> *"Para que un negocio de ingreso recurrente sea de verdad recurrente — uno de los errores
> grandes es que la gente toma algo que es **inherentemente valioso** e intenta facturarlo
> **como si fuera consumible.** La educación tiene un valor único altísimo. El día antes de que
> sepas anunciar, anunciar es increíblemente valioso. El día después de que sabes anunciar, ¿por
> qué pagaría por algo que ya sé hacer? **Va de enorme a cero.** ... La continuidad es muy difícil
> de construir si tu propuesta de valor principal es educación. En cualquier negocio de ingreso
> recurrente **necesitas crear, o al menos demostrar, valor consumible.**"*
> — [*Helping an Online Coach Get to $1M/Month* — 01:30](https://www.youtube.com/watch?v=-54qGpM3q0M&t=90s)

**La prueba: ¿el miembro consume esto todos los meses, o lo usa una vez y ya?**

Aplícala a *"acceso prioritario a activos y oportunidades"*:

1. El LP paga la membresía
2. Le llega el deal con prioridad
3. Invierte $100,000
4. **Su capital queda comprometido 7 años**
5. ¿Para qué sigue pagando la membresía? **No puede volver a invertir.**

El valor va de enorme a cero **en el primer uso**, igual que en la cita. Diseñaste un producto de
valor único y lo estás facturando como suscripción. Es el error exacto que describe.

### Y peor: la anti-selección

Mira quién se queda pagando:

| LP | ¿Sigue pagando? | ¿Te genera ingreso del lado del sponsor? |
|---|---|---|
| El que invirtió | **No.** Ya usó la membresía y está ilíquido | **Sí** — tú cobras el AUM de su deal |
| El que nunca invierte | **Sí.** Sigue esperando "el bueno" | **No** |

**Tu ingreso de membresía vendría de la gente que no transa, y lo perderías justo cuando alguien
sí transa.** Está invertido. El cliente ideal de esa membresía es el que nunca te hace ganar dinero.

---

## 10. Y hay un problema anterior al regulatorio: la prioridad no es tuya para venderla

Esto no necesita abogado para verse.

**En una emisión Reg D, quien decide la asignación es el emisor, no la plataforma.** El sponsor
mira su lista de LPs, decide a quién le da cuánto, y cierra. Tú ejecutas.

Si le vendes "prioridad" a un miembro:
- El sponsor llena el deal con su propia lista → **tu miembro no recibió nada**
- Tienes un cliente que pagó por una promesa que **no estaba en tu poder cumplir**
- Y para cumplirla tendrías que pedirle al sponsor —tu cliente que paga— que le dé preferencia a
  alguien de tu lista por encima de los suyos. **Le estás pidiendo un favor a quien te factura.**

Estarías vendiendo un producto cuyo cumplimiento depende de un tercero con incentivos opuestos.
Eso no es un riesgo legal, es un producto roto.

---

## 11. Lo regulatorio, que además es serio

Cada pieza de "acceso prioritario a oportunidades" abre una pregunta distinta. **No son mías de
responder; son de tu abogado de valores, y esta lista es para que llegues con ellas escritas:**

| Pieza del diseño | La pregunta |
|---|---|
| Cobrar por recibir ofertas | ¿Cobrar por acceso a ofertas de valores me convierte en intermediario registrable? |
| Una lista de pago que recibe deals | En 506(b) no hay solicitación general. ¿Una membresía pagada **crea** la relación previa y sustantiva, o la contamina? **Puede cortar en los dos sentidos** |
| Prioridad en la asignación | ¿Preferir a quien me paga crea deberes frente a los demás inversionistas? |
| Cualquier cobro al inversionista | ¿Afecta la exención bajo la que se hizo la emisión? |

La segunda es la que hace que esto no sea un detalle: **el mecanismo que quieres usar para vender
la membresía es el mismo mecanismo que determina si la emisión del sponsor es válida.** Un error
ahí no te cuesta la membresía, le cuesta la emisión a tu cliente.

---

## 12. La versión limpia: prioridad en **estar listo**, no en **acceso**

Esto te da casi todo lo que querías, sin nada de lo anterior.

**Todos ven el deal en el mismo momento. El miembro puede *actuar* en minutos y el no-miembro en
días.**

| | No miembro | Miembro |
|---|---|---|
| ¿Cuándo ve el deal? | **Al mismo tiempo** | Al mismo tiempo |
| KYC / AML | Lo empieza ahora: 2–5 días | **Ya hecho** |
| Acreditación documentada | La junta ahora | **Ya en expediente** |
| Firma de suscripción | Lee y firma de cero | **Pre-cargada, firma en minutos** |
| Fondeo | Coordina transferencia | **Instrucciones ya validadas** |

**Por qué esto funciona y lo otro no:**

- **No prometes asignación.** No prometes nada que no controles. Solo vendes preparación, que es
  100% tuya.
- **Pero en un deal sobre-suscrito, la velocidad *es* la asignación.** El miembro gana de facto,
  sin que tú hayas preferido a nadie. Obtienes el efecto de la prioridad sin venderla.
- **No hay divulgación selectiva.** Todos reciben lo mismo a la misma hora.
- **Te cuesta cero entregarlo.** Ese KYC lo ibas a hacer igual; solo lo haces antes.
- **Y es honesto:** *"pagas por estar listo, no por tener ventaja."* Se puede decir en voz alta
  delante del sponsor y delante de los otros LPs, que es la prueba real de un diseño limpio.

⚠️ Sigue siendo tema de abogado si una cuota por pre-verificación tiene implicaciones, pero es
una pregunta mucho más chica que las cuatro de §11.

---

## 13. Lo que de verdad es consumible: la membresía correcta

Vuelve a la prueba de §9: **¿qué usa el LP todos los meses durante 7 años?**

No es acceso a deals nuevos — está ilíquido, no puede comprar. Es **todo lo relativo al dinero que
ya tiene adentro.** Y eso lo consume continuamente, exactamente durante el período en que la otra
membresía valdría cero:

| Pieza | ¿Consumible? | Por qué paga |
|---|---|---|
| Posición en vivo y valuación | ✅ Mensual | Hoy recibe un PDF trimestral tarde |
| Documentos fiscales consolidados | ✅ Anual, crítico | Hoy persigue K-1s de 5 sponsors distintos |
| Historial de distribuciones | ✅ Continuo | Hoy lo lleva en su propio Excel |
| **Consolidación multi-sponsor** | ✅ **Mensual** | **Ver sus 5 deals en una pantalla. Nadie se lo da hoy** |
| Solicitud de liquidez | ✅ Cuando la necesita | La vía ① de §3, para el activo que ya tiene |
| Datos de términos comparables en PR | ✅ Por deal | Hoy negocia sin ningún referente |

**La inversión del diseño, en una línea:**

| | Tu versión | La versión que pasa la prueba |
|---|---|---|
| Qué vende | Acceso a lo que **todavía no tiene** | Control de lo que **ya tiene** |
| Cuándo vale | **Antes** de invertir | **Después**, durante 7 años |
| Valor tras el primer uso | **Cero** | **Crece** (más posiciones, más historial) |
| ¿Quién paga? | El que no transa | **El que sí invirtió** |
| ¿Resuelve tu objeción del ticket chico? | No — el costo va antes del beneficio | **Sí** — se paga de las distribuciones ya recibidas |
| ¿Prometes algo de un tercero? | **Sí** | No |

Y fíjate que tu propia objeción se resuelve sola: el LP que no ha invertido no paga $20. **El LP
con $100,000 adentro recibiendo distribuciones paga $200 al año sin pestañear**, porque el costo
sale de un flujo que ya existe.

---

## 14. La pieza que vuelve esto un motor, no una cuota

De la tabla de §13, una fila es distinta a todas: **la consolidación multi-sponsor.**

Si tu miembro está en 5 deals privados y solo 2 usan Finera, su pantalla muestra 2 de 5.
**Está pagando por una vista incompleta, y completarla requiere que los otros 3 sponsors entren.**

```
LP paga membresía
      ↓
ve 2 de sus 5 deals
      ↓
quiere los otros 3 adentro
      ↓
"¿por qué tú no lo haces como Finera?"  →  a 3 sponsors, por su cuenta
      ↓
sponsors nuevos = tu cliente que PAGA el AUM
```

Eso es un **cliente que paga y que además recluta a tus clientes principales.** Es el motor ②c de
[`MOTORES.md`](./MOTORES.md) §1, pero con un mecanismo de dinero adentro y con una razón egoísta
en vez de generosa. De todo lo discutido, **esto es lo que yo construiría.**

---

## 15. La estructura de precio

> *"Los $12,000 van a compensar el CAC. Puedes quedar a la par en los $12,000 si sabes que esa
> persona entra a una membresía de $3,000 al año, que es prácticamente todo margen y no se va.
> Eso te permite gastar muchísimo más que tu competencia, porque ellos necesitan ganar en los 12 y
> tú puedes quedar a la par. Y entonces tienes esta **pila de facturas de $3,000 que se van
> acumulando**, con muy poco esfuerzo de mantener."*
> — [*Helping a Real Estate Education Business Scale to $3M* — 03:00](https://www.youtube.com/watch?v=sGiObaoef10&t=180s)

Traducido a tu caso — y es exactamente tu intuición del peaje, formalizada:

| Capa | Precio | Quién | Propósito |
|---|---|---|---|
| **Acceso a los deals** | **$0. Siempre** | Cualquier inversionista acreditado | Es tu front end del lado LP. **No le pongas peaje nunca** |
| Pre-verificación ("estar listo") | Cuota baja o incluida | El LP que quiere actuar rápido | Elimina fricción en el momento de suscribir |
| **Membresía de administración** | Recurrente, modesta | **El LP que ya invirtió** | La pila que se acumula. Todo margen |
| Liquidez secundaria | Por transacción | El LP que sale | Fase 2, cuando haya densidad |

**El acceso gratis no es generosidad, es el embudo.** Cada LP que entra gratis es inventario de la
fase 2, y lo acumulas mientras el sponsor paga la cuenta.

---

## 16. Resumen de la Parte II

| Tu planteamiento | Veredicto |
|---|---|
| "El LP no es cliente por acceso; cobrar acceso es peligroso" | ✅ **Correcto, y por la razón correcta.** El peaje en la demanda cuesta doble |
| "Nadie paga para invertir poco" | ✅ **Correcto.** El costo no puede ir antes del beneficio |
| "Membresía con prioridad de acceso a activos y oportunidades" | ❌ **Rediseñar.** Valor único facturado como recurrente, anti-selecciona a quien no transa, y promete una asignación que decide el sponsor, no tú |
| "Prioridad, entre muchas cosas más" | ✅ **La intuición es buena.** La forma limpia es **prioridad en estar listo**, no en acceso |

**Lo que mantengo de antes:** el LP paga en fase 2, no en fase 1, porque no puedes adquirirlo río
arriba del sponsor. **Lo que cambia con tu objeción:** cuando pague, no paga por entrar — **paga
por administrar lo que ya tiene adentro.** Eso es consumible, se cobra de un flujo existente, y la
pieza de consolidación multi-sponsor lo convierte en el único cliente que te trae más clientes.

---
---

# Parte III — "¿Solo pueden ser clientes si les cobro comisión?"

*(Pregunta: ¿es la comisión la única vía? Aclaración: una comisión por cada transacción que el
inversionista realiza.)*

**No. Hay cuatro estructuras de cobro distintas, y la comisión por transacción es la peor de las
cuatro para Finera en el año 1 — por tres razones independientes.**

---

## 17. Lo primero: "comisión por transacción" es la frase que activa el registro

De todo lo discutido en este documento, esta es **la única estructura que tiene nombre propio.**

La compensación basada en transacciones por facilitar operaciones con valores — es decir, cobrar
un porcentaje cada vez que alguien compra o vende un valor — es el factor central del análisis de
si alguien está actuando como intermediario registrable. No es un borde gris: es el centro del
análisis.

**Esto no te lo puedo responder yo, y es importante que no lo tomes de mí.** Lo que sí te puedo
decir con claridad:

| | |
|---|---|
| Suscripción por software de administración | Pregunta chica. Es software |
| Cuota pagada por el emisor | Pregunta chica. Estructura corriente en la industria |
| Puntos base por custodia | Pregunta mediana. Régimen de custodia |
| **Comisión por transacción** | **Pregunta grande, con nombre.** Es el factor central del análisis de intermediación |

Si vas a explorarla, la conversación con tu abogado de valores va **antes** de construirla, no
después. Es la diferencia entre un producto que hay que ajustar y una actividad que hay que
registrar.

---

## 18. Antes del abogado, la aritmética: ¿cuántas veces transa un LP?

Esta objeción no necesita a nadie más, y por sí sola descarta la comisión como motor del año 1.

| Evento | ¿Es transacción del LP? | Frecuencia |
|---|---|---|
| Suscribirse a un deal | Sí | **1 vez cada 1–3 años** |
| Recibir una distribución | No. No la inicia él | Trimestral, pero no es su transacción |
| Vender en secundario | Sí | **Tal vez 1 vez en 7 años, o nunca** |
| Ver su posición, bajar su K-1 | No | Continuo |

**El LP casi nunca transa.** Su característica definitoria es que *inmoviliza* capital durante años.

| Estructura | Eventos de cobro en 7 años |
|---|---|
| Suscripción mensual modesta | **~84** |
| Comisión por transacción | **1, tal vez 2** |

Una comisión sobre un evento que ocurre una vez cada varios años no es una fuente de ingreso: es
un billete de lotería. Y es el mismo problema de *"4% de cero"* de §4, agravado — aquí es **4% de
casi nunca.**

---

## 19. Y tu propia objeción la descarta

Tú escribiste, correctamente:

> *"eso es quitarle el acceso y eso sería peligroso, porque nadie quiere empezar a pagar para
> invertir poco."*

**Una comisión por transacción es exactamente eso.** Si cobras 1% sobre una suscripción de $25,000,
son $250 **en el momento exacto en que está decidiendo si invierte.** El peaje que rechazaste con
razón no desapareció: se movió del portón a la caja.

| | Cuota de acceso | Comisión por transacción |
|---|---|---|
| ¿Cuándo paga? | Antes de ver el deal | **En el momento de invertir** |
| ¿Ya rindió algo el activo? | No | **No** |
| ¿Castiga al ticket chico? | Sí | **Sí — proporcionalmente igual** |
| ¿Es el peaje que rechazaste? | Sí | **Sí** |

Tu intuición ya había resuelto esto. La comisión por transacción contradice tu propio criterio.

---

## 20. Y te pone del lado equivocado de tu propio motor

Cada LP que entra a un deal tuyo es, al mismo tiempo:

1. Inventario de la fase 2 (§4)
2. Un nodo del motor ②c que puede traerte sponsors (`MOTORES.md` §1)
3. Un futuro miembro de la membresía de administración (§13)

Las tres cosas requieren **que entre el mayor número posible, con la menor fricción posible.**

Una comisión en el momento de suscribir es **fricción en el torniquete de la cosa que más te
interesa llenar.** Estarías cobrando peaje en la entrada del activo que quieres acumular.

---

## 21. Las cuatro estructuras, ordenadas para ti

| # | Estructura | Quién paga | Predecible | Carga regulatoria | ¿Castiga el ticket chico? | Veredicto año 1 |
|---|---|---|---|---|---|---|
| **1** | **Cuota por la capa del inversionista** | **El emisor** | ✅ Sí | 🟢 Baja | **No — el LP paga $0** | ⭐ **Mejor** |
| **2** | Suscripción de administración | El LP ya invertido | ✅ Sí | 🟢 Baja | No — sale de distribuciones | ✅ Buena, fase 1 tardía |
| **3** | Puntos base por custodia | El LP | 🟡 Semi | 🟡 Media | Algo | 🕐 Fase 2 |
| **4** | **Comisión por transacción** | El LP | ❌ No | 🔴 **Alta, con nombre** | **Sí** | ❌ **No en año 1** |

### La que no habías considerado: **que el emisor pague la capa del inversionista**

Es la que disuelve el problema entero.

Finera le cobra al **sponsor** por la experiencia del inversionista — el portal, el reporting, los
documentos fiscales de sus LPs. **El LP no paga nada, recibe todo.** Y tú monetizas el lado del
inversionista igual, solo que facturado a quien ya te paga.

Por qué funciona:
- **Es estructura corriente.** Los agentes de transferencia y administradores de fondos cobran al
  emisor por inversionista o por posición desde siempre. No estás inventando nada raro.
- **El sponsor lo quiere.** Sus LPs son su capital repetido; una buena experiencia del LP es su
  interés directo, no un favor que le pides.
- **Cero pregunta nueva de intermediación.** El dinero viene del emisor, que ya es tu cliente.
- **Y resuelve tu objeción sin rodeos:** nadie paga para invertir poco, porque **nadie paga.**

⚠️ **La trampa, y es importante:** si lo cobras **por inversionista**, le creas al sponsor el
incentivo de traer *menos* LPs para pagarte menos — justo contra tu estrategia de acumulación.
Cóbralo **plano por deal**, o métele la capa del inversionista dentro del % de AUM que ya cobras.
Nunca por cabeza.

---

## 22. La conclusión que incomoda

Poniendo juntas §4, §20 y §21: **puede que lo correcto en el año 1 sea no monetizar al LP en
absoluto, a propósito.**

La base de LPs vale más como **inventario** que como ingreso por cuotas:

| Como ingreso de cuotas, año 1 | Como inventario, fase 2 |
|---|---|
| 20 LPs × $200 = **$4,000/año** | 400 LPs = el mercado secundario existe, la consolidación multi-sponsor funciona, el motor ②c trae sponsors |

Los $4,000 no mueven nada y te cuestan fricción en el torniquete. **Trata la capa del inversionista
como gasto de marketing de la fase 2**, igual que el sobre-servicio deliberado del deal #1
(`MOTORES.md` §4). Es la misma lógica:

> *"Si quedo a la par, en el peor de los casos, en la primera transacción, pero igual vuelven cada
> año y compran otra propiedad, sigue siendo un activo que compone."*
> — [*Helping a Tax Firm Get More Leads* — 03:00](https://www.youtube.com/watch?v=6NSu1htqWa8&t=180s)

---

## 23. El argumento honesto a favor del porcentaje

Para no dejarlo manco — el porcentaje tiene **una** ventaja real, y el corpus la nombra:

> *"Tu ROI tampoco es claro, porque tienes una tarifa plana para todos... Si tuvieras un porcentaje
> podrías ver clarísimo: cada marca hace seis deals en promedio, me llevo este porcentaje, el deal
> promedio es de tanto, y entonces tienes matemática alrededor. Pero por ahora estás en tarifa
> plana y está bien. No me ofende."*
> — [*Helping a $2M Coaching Biz Hit $20M* — 06:00](https://www.youtube.com/watch?v=MwU7mXoLfRM&t=360s)

El porcentaje te da visibilidad de economía unitaria. Es cierto. Pero fíjate en el veredicto:
*"está bien, no me ofende"* — la tarifa plana no es un error, es una decisión con un costo de
información.

Y el contraejemplo pesa más, porque es del mismo negocio que el tuyo:

> *"Cobramos una tarifa plana por el servicio de $22,000, la mitad por adelantado y la mitad al
> cerrar."* — *"¿Independiente del tamaño del deal?"* — *"Sí. Puede ser un deal de 800k o la compra
> de una casa de 1.5 millones."*
> — [*Our CAC Is $6,700 and We Don't Know What's Working* — 00:00](https://www.youtube.com/watch?v=15CxTygzVio&t=0s)

**$15 millones de ingreso al 27% de margen, en asesoría inmobiliaria, con tarifa plana
independiente del tamaño del deal.** Su línea basada en porcentaje es el 10% del ingreso. En un
negocio de deals, plano no es la opción pobre.

---

## 24. Dónde sí tiene lugar la comisión

No la descartes para siempre. Descártala **para el año 1**:

| Condición | Por qué |
|---|---|
| Fase 2, con ~300–400 LPs en 10+ deals | Antes de eso es 4% de casi nunca |
| Solo en **liquidez secundaria**, no en suscripción primaria | En el secundario el LP está *recibiendo* efectivo: el costo sale del flujo, no del bolsillo. Ahí sí pasa tu propio filtro |
| Después de que tu abogado te diga qué registro requiere | §17. Esta conversación va antes de construir |

**La diferencia es de qué lado del dinero está el cobro.** Comisión al suscribir = le cobras por
entregar dinero. Comisión al vender en secundario = le cobras por recibirlo. La segunda es la que
tu propio criterio aprueba.

---

## 25. Respuesta en una tabla

| Tu pregunta | Respuesta |
|---|---|
| *"¿La única manera es cobrarle comisión?"* | **No.** Hay cuatro estructuras, y la comisión es la cuarta de cuatro para el año 1 |
| *"¿Una comisión por cada transacción que realizan?"* | Es la de mayor carga regulatoria (§17), la de menos eventos de cobro (§18), **y es el mismo peaje que tú ya habías rechazado** (§19) |
| ¿Entonces qué? | **Que el emisor pague la capa del inversionista.** El LP paga $0, tú monetizas igual, cero pregunta nueva. Plano por deal, **nunca por cabeza** |
| ¿Y la comisión? | Fase 2, solo en liquidez secundaria, y después de tu abogado — no antes |
