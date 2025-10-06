# Idea Alquímica: Tejiendo el Futuro con Prompt Engineering

1. Descripción breve

Este proyecto explora cómo aplicar técnicas de Fast Prompting para generar textos e imágenes de calidad utilizando IA, reduciendo costos y mejorando consistencia. Se implementa en Jupyter Notebook con un caso de uso concreto: la tienda virtual Art-Synt.

2. Estructura

notebooks/: Notebook con pruebas baseline vs fast prompting.

prompts/: Plantillas de prompts YAML.

src/: Código auxiliar (simulación + cálculo de costos).

outputs/: Resultados de ejecución (texto + imágenes).

3. Instalación
git clone (https://github.com/lu-developer476/Inteligencia-Artificial/tree/main/PF-IA-Prompts).git
cd PF-IA-Prompts
pip install -r requirements.txt

4. Ejecución
jupyter notebook notebooks/fast_prompting_poc.ipynb

(Funciona en modo simulación sin claves API. Se puede usar OpenAI API real, configurando el OPENAI_API_KEY)

5. Resultados

5 prompts de texto → slogans cyberpunk

5 prompts de imagen → afiches estilo Art-Synt

Comparativa baseline vs fast prompting (mejor calidad + menor costo)

6. Tecnologías

Python 3.10+

Jupyter Notebook

OpenAI API (texto)

Stable Diffusion / Leonardo.AI / NightCafe (imágenes)

7. Licencia

(Opcional, MIT recomendado)

# Resultados de Generación de Imágenes – Proyecto "Idea Alquímica"

Autor: **Lucas Leonel Montenegro Burgos**  
Fecha: **2025-10-06**

Este directorio contiene las **imágenes generadas mediante IA** a partir de los prompts diseñados
en `prompts/templates.yaml`, dentro del marco del proyecto *Idea Alquímica: Tejiendo el Futuro con Prompt Engineering*.

---

## 📁 Contenido del directorio

| Archivo | Prompt utilizado | Herramienta | Descripción |
|----------|------------------|--------------|--------------|
| `artsynt_poster_01.jpg` | *Afiche publicitario estilo cyberpunk para 'Art-Synt'...* | NightCafe | Cartel promocional con luces de neón y estética urbana lluviosa. |
| `artsynt_poster_02.jpg` | *Afiche publicitario estilo cyberpunk para 'Art-Synt'...* | Leonardo.AI | Variante alternativa con colores fríos y tipografía futurista. |
| `concept_art_01.jpg` | *Ilustración conceptual estilo cyberpunk...* | Stable Diffusion | Escena nocturna con rascacielos, drones y ambiente distópico. |
| `logo_artsynt.png` | *Diseño de logo minimalista estilo cyberpunk para 'Art-Synt'...* | Leonardo.AI | Logo experimental con neón magenta y símbolo tecnológico. |

---

## 🧩 Detalles técnicos

- **Resolución promedio:** 1024x1024 px  
- **Formato:** `.jpg` o `.png`  
- **Estilo visual:** Cyberpunk / Futurista / Neón / Lluvia / Urbano  
- **Paleta principal:** Azul, violeta, magenta, negro  
- **Uso previsto:** Material visual demostrativo para la entrega final del Proyecto de IA (Coderhouse).

---

## 📜 Notas

- Las imágenes fueron generadas con herramientas gratuitas de IA (NightCafe, Leonardo.AI, Stable Diffusion).  
- No se aplicaron ediciones manuales.  
- Cada imagen refleja la **coherencia estética** y **conceptual** buscada con los prompts de texto y de imagen.  
- Los resultados son **reproducibles**: basta con copiar el prompt desde `templates.yaml` en la herramienta correspondiente.

---

> 💡 Consejo: Si querés volver a generar estas imágenes, abrí tu cuenta gratuita en las plataformas indicadas y usá los prompts originales sin modificaciones para obtener resultados similares.

# Resultados de Generación de Texto – Proyecto "Idea Alquímica"

Autor: **Lucas Leonel Montenegro Burgos**  
Fecha: **2025-10-06**

Este directorio contiene los resultados textuales del experimento comparativo entre un **prompt baseline** y un **prompt optimizado (Fast Prompting)**, ejecutado en el notebook `fast_prompting_poc.ipynb`.

---

## 📊 Resumen de los resultados

| Tipo de prompt | Slogan generado | Puntaje | Costo (USD) | Observaciones |
|----------------|----------------|----------|--------------|----------------|
| **Baseline** | “Tu estética cyberpunk comienza aquí.” | 2/3 | 0.0165 | Cumple longitud y evita clichés, pero falta fuerza estética. |
| **Fast Prompting** | “Art-Synt: Tecnología con alma futurista.” | 3/3 | 0.036 | Mayor coherencia con la identidad de marca y tono evocador. |

---

## 🧩 Evaluación de calidad

**Criterios analizados:**
1. Longitud ≤ 12 palabras.  
2. Sin clichés (como “innovación”, “futuro”, etc.).  
3. Estilo evocador cyberpunk (palabras como *neón*, *metal*, *digital*, *alma*...).  

El prompt optimizado obtuvo mejor desempeño global, demostrando:
- Mayor **consistencia estética** con el universo *Art-Synt*.  
- Menor necesidad de iteraciones.  
- **Optimización de costos**, al generar resultados satisfactorios en una sola llamada (“One-Call + Self-Check”).

---

## 🧠 Conclusión

El enfoque de **Fast Prompting** mejora la calidad de salida sin incrementar significativamente el costo de procesamiento, confirmando la hipótesis del proyecto:  
> *“La estructura de un prompt influye directamente en la eficiencia y la calidad del contenido generado por IA.”*

---

📂 Archivos incluidos:
