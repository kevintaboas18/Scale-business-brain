# Finera — mapa completo de clientes

**Todos los clientes, escritos hoy, con su fase y su condición de disparo.**

Esto es lo que pediste: el mapa completo, no una lista recortada. Cada cliente lleva qué le duele,
qué paga, en qué fase entra, **qué tiene que ser verdad antes de perseguirlo**, y qué te exige
servirlo. El foco actual está marcado con 🎯.

**Esto no es asesoría legal ni financiera.** Las filas marcadas ⚖️ requieren confirmación de tu
abogado de valores antes de construirse.

---

## Lado A — Emisores · *el que firma el cheque*

Paga: tarifa de estructuración (día 1) + % anual sobre AUM (recurrente).

| ID | Quién es exactamente | Qué le duele | Fase | Condición de disparo | Qué te exige |
|---|---|---|---|---|---|
| 🎯 **E1** | **Sponsor de real estate de PR. $2–10M por deal, de su propia lista de LPs, 2–6 veces al año** | Ronda de 14 semanas, cap table en Excel, suscripciones en papel, nada que ofrecer al LP que quiere salir antes del año 7 | **1** | **Ninguna. Es hoy** | Abogado de valores + transfer agent. Nada más |
| **E2** | Sponsor de **private credit** de PR, mismo perfil de tamaño y frecuencia | Igual que E1, más servicing de pagos | **1** | Ninguna — **es el mismo avatar con otro activo** | Lo mismo que E1 |
| **E3** | **Gestor emergente** de PR levantando su fondo 1 o 2 | Estructura institucional sin presupuesto institucional | **1** | Ninguna — **ya está dentro de E1**: estructura institucional, decisión de emprendedor | Lo mismo que E1 |
| ⚠️ **E4** | Sponsor haciendo **su primera emisión** | No tiene LPs, no tiene abogado, no tiene activo cerrado | **Evitar** | — | Consumiría soporte sin límite y no puede cerrar. **No es cliente, es un proyecto** |
| **E5** | Sponsor de real estate de **EE.UU. continental** | Igual que E1, mercado 50× más grande y 50× más competido | **2** | 10 emisiones cerradas en PR + 3 sponsors referenciables | Multi-estado: análisis de registro por jurisdicción ⚖️ |
| **E6** | **Emisor de deuda privada** (PYME que levanta deuda de inversionistas privados) | Papeleo de emisión sin banca | **2–3** | E1 estabilizado + estructura de deuda validada ⚖️ | Producto distinto: servicing de intereses y amortización |
| **E7** | **Institución**: fondo grande, banco, aseguradora, cooperativa | Administración legada, costosa, pero **funciona "suficientemente bien"** | **3** | **Las cuatro de A6 en [AUDITORIA-CANVAS.md](./AUDITORIA-CANVAS.md):** ≥10 emisiones, ≥$X AUM, auditoría externa, 3 referencias por nombre | Procurement, certificaciones, seguros, SLA, equipo de soporte. **Es otra empresa** |
| **E8** | Sponsor de **LATAM** | Acceso a capital en USD con estructura reconocible | **4** | E5 funcionando + estructura transfronteriza ⚖️ | Cumplimiento multi-jurisdicción. Lo más caro de la lista |

**Por qué E1, E2 y E3 están todos en fase 1:** no son tres segmentos. **Son el mismo avatar**
—mismo dolor, mismo tamaño, mismo canal, misma oferta— visto con tres etiquetas distintas. Puedes
escribirlos como uno solo sin perder nada.

---

## Lado B — Capital · *el LP*

No paga en fase 1 (ver [`CLIENTE-LP.md`](./CLIENTE-LP.md) §4). Entra **gratis, río abajo de E1.**

| ID | Quién es | Qué le duele | Fase | Qué paga | Condición de disparo |
|---|---|---|---|---|---|
| **C1** | LP acreditado de un deal Finera | PDF trimestral tarde, sin detalle | **2** | Suscripción de administración | Que exista el deal #1 |
| ⭐ **C2** | **LP multi-sponsor** — está en 5 deals y solo 2 usan Finera | Cinco portales, cinco formatos, cinco K-1 que persigue | **2** | **Consolidación.** El más valioso de todo el mapa | ~50+ LPs en 3+ deals |
| **C3** | **Family office** local | Sin vista consolidada de sus privados | **2** | Administración + pre-verificación | C1 funcionando |
| **C4** | **Relocalizado Act 60** | Nuevo en el mercado, sin red local, quiere deals locales | **2** | Administración | C1 funcionando |
| **C5** | **LP vendedor en secundario** | Capital amarrado 7 años y necesita salir | **2–3** | **Tarifa plana por transferencia**, de los proceeds | 🔴 **Los documentos del deal #1 deben permitir transferencias** (`CLIENTE-LP.md` §26) + 300 LPs para densidad ⚖️ |
| **C6** | LP que quiere **estar listo** | Pierde deals sobre-suscritos por tardar días en el papeleo | **1–2** | Cuota baja de pre-verificación | Que exista el deal #1 ⚖️ |

**C2 es la fila que más vale del mapa entero.** Es el único cliente que **te paga y además recluta
a tus clientes del Lado A**: paga por una vista incompleta, y completarla requiere que los otros
sponsors entren. Está desarrollado en [`CLIENTE-LP.md`](./CLIENTE-LP.md) §14.

---

## Lado C — Infraestructura · *white-label y API*

**La categoría que no habías nombrado, y que convierte un nodo en cliente que paga.**

| ID | Quién es | Qué compra | Fase | Por qué importa |
|---|---|---|---|---|
| **I1** | **Despacho** que ofrece tokenización **bajo su propia marca** | Tu infraestructura, facturada a él; él le cobra a su cliente | **2–3** | ⚖️ **Posible respuesta al problema de honorarios.** Un despacho generalmente no puede compartir honorarios con un no-abogado, pero comprarte infraestructura como proveedor es una relación distinta. **Confírmalo con tu abogado — no lo tomes de mí** |
| **I2** | **Administrador de fondos** existente | Tu capa de tokenización bajo su servicio | **3** | Te da volumen sin vender deal por deal |
| **I3** | Otra plataforma vía **API** | Emisión y registro como servicio | **3** | Requiere producto maduro y documentado |
| **I4** | **Transfer agent** que quiere tu software | Licencia | **3** | Invierte la relación: tu socio pasa a ser tu cliente |

---

## Lado D — Nodos · *no son clientes, van escritos*

**No firman cheque.** Te traen a los del Lado A. Van en **casilla 3 (Canales)** y **casilla 8
(Socios)** — no en casilla 1.

| ID | Quién | Qué te da | Puede volverse |
|---|---|---|---|
| **N1** | Despachos de valores y real estate | Issuers con el problema ya identificado | **I1** (cliente que paga) |
| **N2** | CPAs con cartera de sponsors | Issuers en el momento de estructurar | **I1** |
| **N3** | Asesores Act 20/22/60 | Relocalizados con capital y sponsors | — |
| **N4** | Brokers comerciales | Deals en estructuración | — |

Playbook completo en [`COLABORACIONES.md`](./COLABORACIONES.md).

---

## El grafo de desbloqueo — *la parte que hace útil al mapa*

Un mapa completo no vale por la lista. Vale por **el orden**: qué cliente abre la puerta de cuál.

```
                        🎯 E1  (sponsor #1)
                            │
        ┌───────────────────┼───────────────────┬──────────────────┐
        │                   │                   │                  │
        ▼                   ▼                   ▼                  ▼
   C1 · C6             E1 repetido          N1 · N2            10 deals
  (sus LPs             (su deal #2)        (nodos, al          + auditoría
  entran con           = motor ① + ②b      ver que           + 3 referencias
  CAC = $0)                                 funciona)              │
        │                                        │                 ▼
        ▼                                        ▼                E7
   50+ LPs ──► C2 ──► C3 · C4                   I1          (instituciones)
   en 3 deals   (consolidación)           (white-label)
        │         │
        ▼         └──► recluta más E1 ──┐
   300+ LPs                              │
        │                                │
        ▼                                ▼
   C5 (secundario) ──► vía de liquidez ──► hace a E1 más fácil de vender
                                                      │
   track record PR ───────────────────────────────────┴──► E5 ──► E8
```

### Lo que prueba el grafo

**Todas las flechas salen de E1.** Hay exactamente **una puerta de entrada** a este negocio, y es
un sponsor diciendo sí. Los otros 17 clientes de este mapa son río abajo de ese sí:

| Lado | Clientes | ¿Alcanzables sin E1? |
|---|---|---|
| A — Emisores | E2, E3 | Sí (mismo avatar) |
| A — Emisores | E5, E6, E7, E8 | **No.** Requieren historial que solo E1 produce |
| B — Capital | C1–C6 | **No.** El LP entra *por el deal* |
| C — Infraestructura | I1–I4 | **No.** Nadie licencia infraestructura sin pruebas |
| D — Nodos | N1–N4 | Contactables sí; **productivos no** |

**El mapa completo es el argumento más fuerte para el foco.** No porque tengas pocos clientes:
porque tienes 18 y **17 están detrás de la misma puerta.**

---

## Cómo esto va en el business model canvas

| Documento | Qué lleva |
|---|---|
| **Canvas primario** | Casilla 1 = **E1** (con E2 y E3 escritos como el mismo avatar). Las nueve casillas completas sobre ese cliente |
| **Canvas de expansión — fase 2** | C1, C2, C3, C4, C6 · E5 · I1 — cada uno con su condición de disparo |
| **Canvas de expansión — fase 3** | E6, E7 · I2, I3, I4 |
| **Canvas de expansión — fase 4** | E8 |
| **Casilla 3 y 8 del primario** | N1–N4 |
| **Anexo del plan** | Este mapa completo, con el grafo |

Un inversionista que vea este mapa con fases y condiciones de disparo lee **visión con criterio**.
El mismo mapa sin fases lee **falta de foco**. Es el mismo contenido; lo que cambia es que las
condiciones de disparo demuestran que sabes cuál es el orden.

---

## Las condiciones de disparo, juntas

Para pegar donde las veas:

| Desbloquea | Cuando sea verdad que... |
|---|---|
| **C1, C6** | Hay un deal cerrado |
| **C2** | 50+ LPs verificados en 3+ deals |
| **C3, C4** | C1 funciona y hay reporting que se puede mostrar |
| **C5** | 🔴 Los documentos del deal #1 permiten transferencias **+** 300+ LPs **+** respuesta del abogado sobre registro |
| **I1** | 3+ deals cerrados **+** respuesta del abogado sobre la estructura de proveedor |
| **E5** | 10 emisiones cerradas en PR **+** 3 sponsors referenciables |
| **E6** | E1 estabilizado **+** estructura de deuda validada |
| **E7** | ≥10 emisiones **+** ≥$X AUM **+** auditoría externa **+** 3 referencias por nombre |
| **E8** | E5 funcionando **+** estructura transfronteriza resuelta |
| **I2, I3, I4** | Producto documentado **+** historial de operación sin incidentes |

**La única fila sin condición es E1.** Esa es la que te toca esta semana.

---

## Los tres ejes — *no "sponsor o institución"*

**Pregunta: ¿todos los clientes son sponsor o institución? Falso.** De los 17 clientes del mapa
(los 18 menos E4, marcado a evitar; N1–N4 no son clientes), **11 no son ninguno de los dos.**

| Grupo | IDs | Cuántos | ¿Sponsor o institución? |
|---|---|---|---|
| Sponsors | E1 · E2 · E3 · E5 · E8 | 5 | ✅ Sponsor |
| Instituciones | E7 | 1 | ✅ Institución |
| **PYME emisora de deuda** | E6 | 1 | ❌ Ni uno ni otro |
| **Inversionistas (LPs)** | C1 · C2 · C3 · C4 · C5 · C6 | 6 | ❌ Son el capital, no el emisor |
| **Compradores de infraestructura** | I1 · I2 · I3 · I4 | 4 | ❌ Son proveedores que te compran a ti |
| | | **17** | **6 sí · 11 no** |

**Verdadero solo para la fase 1** — y ahí es todavía más estrecho: en fase 1 tu cliente es el
sponsor, **y tampoco la institución** (E7 es fase 3).

### El eje correcto: posición en la vida del activo

Lo que une a los 17 no es el tipo de empresa. Es **dónde está cada uno respecto del activo
tokenizado:**

| Eje | Quién | IDs | Qué hace con el activo |
|---|---|---|---|
| **1 · Lo crea** | Emisores | E1–E8 | Estructura y emite |
| **2 · Lo tiene** | Capital | C1–C6 | Lo posee, lo reporta, lo vende |
| **3 · Lo administra para otro** | Infraestructura | I1–I4 | Opera el ciclo bajo su propia marca |

Esto explica tres cosas que la clasificación por tipo de empresa no explica:

1. **Por qué todos salen de E1.** El activo tiene que existir antes de que haya quien lo tenga o
   quien lo administre. El grafo de desbloqueo es una consecuencia del eje, no una regla aparte.
2. **Por qué las fases caen donde caen.** Cada cliente aparece en un punto distinto de la vida del
   activo, y la vida del activo tiene un orden.
3. **Por qué I1 no es un nodo.** Un despacho que te *refiere* está en el eje de distribución; un
   despacho que te *compra la infraestructura* está en el eje 3. Misma empresa, posición distinta.

### Y una nota sobre tu tercera propuesta de valor

Tu frase original —*«Del activo al inversionista: todo el ciclo de vida en una sola
plataforma»*— la critiqué como descripción de arquitectura, y como **mensaje de venta** sigue
siendo mala: a ningún sponsor le duele no tener un ciclo de vida completo.

Pero como **modelo interno para organizar a tus clientes, es exactamente el eje correcto.** Es la
distinción entre un buen modelo mental y un buen pitch: el mismo contenido sirve para pensar y no
para vender. Guárdala para el canvas y para explicar la empresa a un inversionista; no la uses
para abrir una conversación con un sponsor.
