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
