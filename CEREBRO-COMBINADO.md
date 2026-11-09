# Scale Business Brain — el cerebro combinado

Este repositorio ya no es un solo agente. Son **17 skills** que se cargan
automáticamente en Claude Code y se reparten el trabajo de un asesor de negocio.

```bash
git clone https://github.com/kevintaboas18/Scale-business-brain.git
cd Scale-business-brain
./setup.sh          # instala el CLI y el índice QMD de ask-hormozi
```

Al abrir el repo en Claude Code, `.claude/skills/` expone las 17 skills.
`ask-hormozi` además necesita `setup.sh` porque tiene un corpus indexado.

---

## 1. Las dos mitades

| | **ask-hormozi** | **founder-playbook** |
|---|---|---|
| Origen | 2.039 vídeos de YouTube (@MoreMozi) | 15 libros de negocio destilados |
| Formato | 9.330 segmentos de 90 s, BM25 local | 16 skills en Markdown con árboles de decisión |
| Autor | 1 (Alex Hormozi) | 15 autores |
| Ventana | sep-2025 → jul-2026 | Atemporal (1990s–2020s) |
| Qué devuelve | **Lo que se dijo**, con enlace al minuto | **Cómo decidir**, con marco y plantilla |
| Verificable | ✅ Cita clicable a YouTube | ❌ Síntesis sin cita puntual |
| Peso | 82 MB | 5,3 MB |

**La complementariedad no es casual, es estructural:**

- `ask-hormozi` responde *"¿qué ha dicho Hormozi sobre X?"* — evidencia, citada.
- `founder-playbook` responde *"¿qué marco aplico a mi situación?"* — método.

Uno es el **archivo**. El otro es el **procedimiento**.

---

## 2. El hueco que se cierra

El corpus de `ask-hormozi` cubre el canal MoreMozi de sep-2025 a jul-2026.
**No incluye los libros de Hormozi.** Era su límite más señalado.

`founder-playbook` trae exactamente eso:

- `100m-offers` — *$100M Offers* (diseño de oferta, ecuación de valor)
- `100m-leads` — *$100M Leads* (Core Four, lead magnets, LTGP:CAC)
- `money-models` — *$100M Money Models* (secuencia de ofertas, payback 30 días)

Es decir: **el mismo autor, la capa que faltaba.** Los vídeos son Hormozi
improvisando sobre casos concretos; los libros son Hormozi sistematizado.
Ahora tienes las dos.

---

## 3. La mente del agente combinado

Hay una skill que cambia la naturaleza del conjunto: **`diagnose`**.

Es un meta-skill enrutador. Su premisa:

> *"El momento peligroso es cuando aplicas el marco correcto al problema
> equivocado."*

Clasifica todo problema de startup en **cinco modos de fallo**, y su aporte
real es nombrar el error de diagnóstico típico de cada uno:

| Fallo | Cómo se ve | Diagnóstico equivocado habitual |
|---|---|---|
| **Producto** | Lo prueban y lo dejan | "Necesitamos mejor marketing" |
| **Mercado** | Nadie paga | "Necesitamos más features" |
| **Mensaje** | Buen producto, no lo entienden | "El producto está mal" |
| **Distribución** | Lo comprarían, pero no se enteran | "Necesitamos mejor web" |
| **Precio** | Lo quieren, no pagan eso | "Hay que añadir valor" |

Y su observación central: **el fundador casi siempre se equivoca por una capa.**

Con `diagnose` delante, el conjunto deja de ser una biblioteca y pasa a ser un
**flujo**:

```
Pregunta vaga  →  diagnose  →  identifica el modo de fallo
                                  ↓
                        skill del marco correcto
                        (mom-test, traction, 100m-offers…)
                                  ↓
                        ask-hormozi
                        ¿qué dijo Hormozi de esto, en concreto?
                                  ↓
                        Respuesta: marco + evidencia citada
```

---

## 4. En qué se especializa el conjunto

**Ir de cero a los primeros clientes de pago, y de ahí a escalar** — con
sesgo hacia negocios de servicios, agencias, SaaS B2B y PYMEs.

| Etapa | Skills que trabajan |
|---|---|
| No sé qué me pasa | `diagnose` |
| Validar el problema | `mom-test`, `four-steps`, `lean-startup` |
| Posicionar y nombrar | `obviously-awesome`, `blue-ocean-strategy` |
| Redactar el mensaje | `storybrand`, `made-to-stick` |
| Diseñar oferta y precio | `100m-offers`, `monetizing-innovation`, `money-models` |
| Conseguir clientes | `traction`, `100m-leads` |
| Cerrar ventas B2B | `spin-selling`, `influence` |
| Escalar más allá | `crossing-the-chasm` |
| **Contrastar con la realidad** | **`ask-hormozi`** |

---

## 5. Qué gana cada uno

**`ask-hormozi` gana estructura.** Solo tenía dos modos: buscar y citar. Ahora
alguien decide *qué* buscar y *por qué*. La búsqueda BM25 mejora mucho cuando
la consulta viene de un marco ("coste de adquisición", "oferta de atracción")
en lugar de una pregunta en lenguaje natural.

**`founder-playbook` gana verificabilidad.** Es síntesis sin cita puntual: no
puedes comprobar de dónde sale cada afirmación. `ask-hormozi` sí puede, con
enlace al segundo exacto. Un marco respaldado por un vídeo concreto pesa más
que un marco solo.

**Y aparece algo que ninguno tiene por separado: contraste temporal.**
Los libros son de 2021–2025. Los vídeos llegan a jul-2026. Puedes preguntar
si Hormozi sigue diciendo hoy lo que escribió, y verificarlo con timestamp.

---

## 6. Límites honestos

- **Sesgo de autor.** 3 de 16 skills son de Hormozi, más un corpus entero suyo.
  El conjunto piensa como él: negocios de servicios, alto margen, cash-flow
  rápido, poco capital. Para hardware, deep tech o marketplaces está flojo.
- **`founder-playbook` no cita.** Es interpretación de terceros de los libros,
  no los libros. Compra los libros.
- **`ask-hormozi` usa subtítulos automáticos.** Hay erratas. Verifica.
- **Nada cubre regulación, licencias ni cumplimiento.** Para fintech, salud o
  cualquier sector regulado, estos 17 skills no sustituyen a un abogado.
- **BM25 no es semántica.** Vocabulario distinto al del vídeo = no lo encuentra.

---

## 7. Licencias

| Componente | Licencia |
|---|---|
| Código de `ask_hormozi/` | MIT |
| `corpus/` | **No MIT.** Redistribuido con permiso; derechos del titular. Ver `corpus/NOTICE.md` |
| `founder-playbook/` | MIT |

Proyecto no afiliado ni respaldado por Alex Hormozi, Acquisition.com, MoreMozi,
YouTube, ni por ninguno de los autores de los libros destilados.
